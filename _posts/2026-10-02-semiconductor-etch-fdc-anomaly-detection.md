---
layout: post
title: "[반도체 장비 데이터 실무] 04. 식각(Etch) 공정 FDC 센서 이상탐지 및 고장 유형 분류 (Random Forest)"
date: 2026-10-02
categories: [반도체장비]
tags: [반도체, FDC, 이상탐지, 머신러닝, RandomForest, FeatureEngineering, ConfusionMatrix]
math: true
---

# [반도체 장비 데이터 실무] 4주차 · 식각 장비(Etch FDC) 센서 이상탐지 및 고장 유형 분류

> **Key Summary**
> - **목표**: 식각(Dry Etch) 공정 FDC 센서 시계열 데이터를 웨이퍼 단위 피처(33개)로 엔지니어링하고, 머신러닝(Random Forest)을 통해 웨이퍼 이상 유무(이진 분류) 및 구체적 고장 유형(4분류)을 판별합니다.
> - **주요 인사이트**:
>   1. **정밀도 1.00의 함정**: 이상으로 예측한 웨이퍼는 100% 맞혔으나(정밀도 1.00), 실제 이상 25장 중 6장을 놓쳤습니다(재현율 0.76).
>   2. **놓친 웨이퍼 6장의 실체**: 놓친 웨이퍼는 100% **`GAS_LEAK`** 유형(평가 데이터 내 GAS_LEAK 10장 중 6장, 즉 60%를 미검출). 센서 신호가 정상(NORMAL)과 유사하게 겹치는 미묘한 이상임을 규명했습니다.
>   3. **도메인 피처의 위력**: 직접 생성한 파생 변수인 `pressure_slope`(MainEtch 구간 압력 시계열 선형회귀 기울기)가 전체 33개 특징 중 **Feature Importance 1위**를 차지했습니다.

---

## 목차
1. [배경 및 실습 목표](#1-배경-및-실습-목표)
2. [미션 1 · FDC 센서 시계열 특징 추출 파이프라인 (Feature Engineering)](#2-미션-1--fdc-센서-시계열-특징-추출-파이프라인-feature-engineering)
3. [미션 2 · 데이터셋 분할 및 불균형 분석 (Stratified Split)](#3-미션-2--데이터셋-분할-및-불균형-분석-stratified-split)
4. [미션 3 · 이진 분류(정상 vs 이상) 모델 학습 및 성능 평가](#4-미션-3--이진-분류정상-vs-이상-모델-학습-및-성능-평가)
5. [미션 4 · 오분류 분석: 놓친 웨이퍼는 어떤 것이었나?](#5-미션-4--오분류-분석-놓친-웨이퍼는-어떤-것이었나)
6. [미션 5 · 다중 분류(4분류: FDC 고장 원인 판별) 모델링](#6-미션-5--다중-분류4분류-fdc-고장-원인-판별-모델링)
7. [미션 6 · 혼동행렬(Confusion Matrix) 시각화 및 에러 패턴 분석](#7-미션-6--혼동행렬confusion-matrix-시각화-및-에러-패턴-분석)
8. [미션 7 · 모델의 판단 근거: Feature Importance 분석](#8-미션-7--모델의-판단-근거-feature-importance-분석)
9. [미션 8 · 공정 엔지니어 관점의 심층 고찰 및 실무 Q&A](#9-미션-8--공정-엔지니어-관점의-심층-고찰-및-실무-qa)
10. [총평 및 향후 개선 방향](#10-총평-및-향후-개선-방향)

---

## 1. 배경 및 실습 목표

반도체 플라즈마 식각(Dry Etch) 공정에서는 챔버 압력, RF 전력, 가스 유량, 온도 등 수많은 센서가 실시간으로 수집됩니다. 이러한 데이터를 **FDC(Fault Detection and Classification)** 시스템에 연결하여, 공정 중 발생하는 이상 웨이퍼를 신속히 걸러내고 장비의 고장 원인을 정확히 규명하는 것이 수율(Yield) 관리의 핵심입니다.

- **데이터셋 구성**:
  - `traces.csv`: 웨이퍼별, 공정 스텝별 8대 센서의 실시간 시계열 데이터
  - `wafer_info.csv`: 웨이퍼 ID, 공정 일시, 챔버, 레시피, 고장 레이블(`label`, `fault_type`)
- **실습 파이프라인**:
  - Step 1: 시계열 센서 트레이스로부터 통계적·물리적 요약 피처 생성
  - Step 2: 정상(0) vs 이상(1) 이진 분류 (Binary Classification)
  - Step 3: 미검출(False Negative) 웨이퍼의 고장 유형 추적 및 원인 분석
  - Step 4: 4분류(NORMAL, RF_UNSTABLE, PRESSURE_DRIFT, GAS_LEAK) 다중 분류 모델 구축
  - Step 5: 특징 중요도(Feature Importance) 분석을 통한 핵심 물리 인자 발굴

```python
# 기본 환경 설정 및 라이브러리 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (confusion_matrix, classification_report,
                             accuracy_score, precision_score, recall_score)

SEED = 42  # 재현성을 위한 난수 시드 고정
```

---

## 2. 미션 1 · FDC 센서 시계열 특징 추출 파이프라인 (Feature Engineering)

실제 현업에서는 웨이퍼 1장당 수십~수백 초에 걸쳐 센서 트레이스가 기록됩니다. 공정 특성상 플라즈마 반응이 본격적으로 일어나는 **`MainEtch`** 구간에 집중하고, 해당 구간의 8대 센서 신호를 웨이퍼당 한 줄의 요약 특징으로 변환합니다.

### 8대 주요 센서
1. `rf_forward_W` (RF 인가 전력)
2. `rf_reflected_W` (RF 반사 전력)
3. `chamber_pressure_mTorr` (챔버 압력)
4. `ar_flow_sccm` (Ar 가스 유량)
5. `cf4_flow_sccm` (CF4 식각 가스 유량)
6. `esc_temp_C` (ESC 척 온도)
7. `he_backside_Torr` (웨이퍼 냉각 He 후면 압력)
8. `endpoint_intensity` (종말점 검출 광학 강도)

### 특징 추출 함수 구현
- 8대 센서 $\times$ 4가지 기술통계량(`mean`, `std`, `min`, `max`) = 32개 특징
- 시간에 따른 압력 변화 추세를 나타내는 1차 다항식 회귀 계수 `pressure_slope` = 1개 특징
- **총 33개 파생 특징** 생성

```python
# 1-1. 데이터 로드
tr = pd.read_csv('traces.csv')
wi = pd.read_csv('wafer_info.csv', parse_dates=['timestamp'])

SENSORS = ['rf_forward_W', 'rf_reflected_W', 'chamber_pressure_mTorr', 'ar_flow_sccm',
           'cf4_flow_sccm', 'esc_temp_C', 'he_backside_Torr', 'endpoint_intensity']

# 1-2. 특징 추출 함수 정의
def make_features(tr):
    """트레이스에서 웨이퍼당 한 줄짜리 특징(33개)을 생성하는 파이프라인"""
    # 1) MainEtch 구간만 필터링
    main = tr[tr['step'] == 'MainEtch']
    
    # 2) wafer_id 기준 8개 센서 통계량 집계 (32개)
    feat = main.groupby('wafer_id')[SENSORS].agg(['mean', 'std', 'min', 'max'])
    
    # 3) 멀티인덱스 컬럼 평탄화 (예: rf_forward_W_mean)
    feat.columns = ['_'.join(column) for column in feat.columns]
    
    # 4) 시계열 동적 변화를 반영하는 압력 기울기(pressure_slope) 계산 (33번째 특징)
    feat['pressure_slope'] = main.groupby('wafer_id')['chamber_pressure_mTorr'].apply(
        lambda x: np.polyfit(x.index, x.values, 1)[0]
    )
    
    # 5) wafer_id를 인덱스에서 컬럼으로 변환
    feat = feat.reset_index()
    return feat

# 1-3. 특징 데이터셋과 웨이퍼 메타데이터 결합
data = make_features(tr).merge(wi, on='wafer_id', how='left')
print(f"최종 병합 데이터 Shape: {data.shape}")  # (400, 39)
```

---

## 3. 미션 2 · 데이터셋 분할 및 불균형 분석 (Stratified Split)

머신러닝 입력으로 사용할 33개 피처(`X`)와 정상/이상 타깃(`y = label`)을 분리하고, 학습(Train)과 평가(Test) 데이터를 7:3 비율로 분할합니다.

> **층화 분할(Stratified Split) 적용 이유**
> - 반도체 제조 공정 데이터는 정상이 대다수이고 이상이 소수인 **클래스 불균형(Class Imbalance)** 특성을 지닙니다.
> - `stratify=y` 옵션을 주어 Train셋과 Test셋 모두에서 이상의 비율(약 21%)이 동일하게 유지되도록 분할합니다.

```python
# 2-1. X, y 정의
drop_cols = ['wafer_id', 'timestamp', 'chamber', 'recipe', 'fault_type', 'label']
FEATURES = data.drop(drop_cols, axis=1)

X = FEATURES
y = data['label']

# 2-2. 층화 분할 (Train: 280장, Test: 120장)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=SEED
)

# 2-3. 클래스 비율 확인
print("Train셋 비율:\n", y_train.value_counts(normalize=True) * 100)
print("Test셋 비율:\n", y_test.value_counts(normalize=True) * 100)
```

**분할 결과:**
- **학습용 (Train, 280장)**: 정상 221장(78.9%), 이상 59장(21.1%)
- **평가용 (Test, 120장)**: 정상 95장(79.2%), 이상 25장(20.8%)

---

## 4. 미션 3 · 이진 분류(정상 vs 이상) 모델 학습 및 성능 평가

앙상블 기반 결정 트리 모델인 `RandomForestClassifier`를 사용하여 정상(0)과 이상(1)을 분류합니다.

```python
# 3-1. 모델 학습
rf = RandomForestClassifier(n_estimators=200, random_state=SEED)
rf.fit(X_train, y_train)

# 3-2. 평가셋 예측
pred = rf.predict(X_test)

# 3-3. 혼동행렬 및 지표 계산
tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()

print("혼동행렬 (Confusion Matrix):")
print(f"[[TN={tn}, FP={fp}]\n [FN={fn}, TP={tp}]]\n")

print(f"정확도 (Accuracy) : {accuracy_score(y_test, pred):.4f}")
print(f"정밀도 (Precision): {precision_score(y_test, pred):.4f}")
print(f"재현율 (Recall)   : {recall_score(y_test, pred):.4f}")
```

### 실행 결과 및 핵심 지표 분석

| 지표 (Metric) | 수치 | 의미 해석 |
| :--- | :---: | :--- |
| **정확도 (Accuracy)** | **95.0%** (114/120) | 전체 120장 중 114장을 정확히 분류함 |
| **정밀도 (Precision)** | **1.0000** (19/19) | 모델이 **이상**이라고 예측한 19장은 100% 실제 이상이었음 (오경보 FP=0) |
| **재현율 (Recall)** | **0.7600** (19/25) | 실제 이상 웨이퍼 25장 중 19장만 탐지하고 **6장을 정상으로 놓침 (미검출 FN=6)** |

> **Insight: 정밀도 1.00의 함정**
> - 얼핏 정밀도가 1.00이라 모델이 완벽해 보이지만, 반도체 팹(FAB)에서는 **이상을 정상으로 오판하여 불량 웨이퍼가 후속 공정으로 유입되는 미검출(FN) 비용이 치명적**입니다.
> - 따라서 재현율(0.76)이 정밀도에 비해 크게 떨어지는 원인을 파악해야 합니다.

---

## 5. 미션 4 · 오분류 분석: 놓친 웨이퍼는 어떤 것이었나?

모델이 놓친 이상 웨이퍼(실제는 이상(1)인데 정상(0)으로 예측한 False Negative) 6장의 정체를 파악하기 위해 `fault_type`을 매핑하여 분석합니다.

```python
# 4-1. 놓친 웨이퍼 마스크 추출 (FN: y_test == 1 & pred == 0)
missed = (y_test.values == 1) & (pred == 0)

# 4-2. 놓친 웨이퍼의 fault_type 집계
missed_types = data.loc[X_test.index[missed], 'fault_type'].value_counts()
test_types = data.loc[X_test.index, 'fault_type'].value_counts()

# 4-3. 유형별 놓침 비율 정리
summary = pd.DataFrame({
    '평가 전체': test_types,
    '놓침 (FN)': missed_types
}).fillna(0)

summary['놓침 비율'] = (summary['놓침 (FN)'] / summary['평가 전체']).map(lambda x: f'{x:.1%}')
display(summary)
```

### 오분류 분석 요약 테이블

| 고장 유형 (`fault_type`) | 평가 전체 (장) | 놓침 건수 (FN) | 놓침 비율 (%) | 비고 |
| :--- | :---: | :---: | :---: | :--- |
| **`GAS_LEAK`** | **10** | **6** | **60.0%** | **놓친 6건 전부 GAS_LEAK에 집중됨!** |
| `NORMAL` | 95 | 0 | 0.0% | 정상 웨이퍼는 오경보 없음 |
| `PRESSURE_DRIFT` | 9 | 0 | 0.0% | 100% 완벽 탐지 |
| `RF_UNSTABLE` | 6 | 0 | 0.0% | 100% 완벽 탐지 |

> **분석 결론:**
> - `RF_UNSTABLE`과 `PRESSURE_DRIFT`는 모델이 단 1건도 놓치지 않고 100% 잡아냈습니다.
> - 반면, **`GAS_LEAK`은 평가 대상 10장 중 무려 6장(60%)을 정상으로 오판**했습니다.
> - 이는 가스 누출(GAS LEAK) 현상의 센서 변동 폭이 미세하여 정상(NORMAL) 공정 신호의 통계적 분포와 크게 중첩(Overlap)되기 때문입니다.

---

## 6. 미션 5 · 다중 분류(4분류: FDC 고장 원인 판별) 모델링

공정 엔지니어에게 단순히 "이상입니다"라고 알려주는 것보다, **"RF 전력 불안정입니다"** 또는 **"압력 드리프트가 발생했습니다"**라고 원인을 명시해 주어야 장비 정지(Down Time)를 최소화하고 즉각적인 PM 조치를 취할 수 있습니다.

타깃을 세부 고장 유형인 `fault_type`으로 변경하여 4개 클래스 다중 분류를 수행합니다.

```python
# 5-1. 목표 변수를 fault_type 으로 변경하여 층화 분할
ym = data['fault_type']
Xm_train, Xm_test, ym_train, ym_test = train_test_split(
    X, ym, test_size=0.3, stratify=ym, random_state=SEED
)

# 5-2. 4분류 랜덤포레스트 모델 학습
rf4 = RandomForestClassifier(n_estimators=200, random_state=SEED)
rf4.fit(Xm_train, ym_train)
pred4 = rf4.predict(Xm_test)

# 5-3. Classification Report 출력
print(classification_report(ym_test, pred4, zero_division=0))
```

### 다중 분류 평가 결과 (`classification_report`)

```text
                precision    recall  f1-score   support

      GAS_LEAK       0.60      0.43      0.50         7
        NORMAL       0.96      0.98      0.97        95
PRESSURE_DRIFT       1.00      1.00      1.00         9
   RF_UNSTABLE       1.00      1.00      1.00         9

      accuracy                           0.95       120
     macro avg       0.89      0.85      0.87       120
  weighted avg       0.94      0.95      0.95       120
```

- **`RF_UNSTABLE` / `PRESSURE_DRIFT`**: Precision 1.00, Recall 1.00, F1-score 1.00의 무결점 성능.
- **`GAS_LEAK`**: Precision 0.60, Recall 0.43, F1-score 0.50으로 상대적으로 매우 저조.

---

## 7. 미션 6 · 혼동행렬(Confusion Matrix) 시각화 및 에러 패턴 분석

어떤 고장 유형이 어떤 유형으로 잘못 분류되었는지 직관적으로 확인하기 위해 혼동행렬을 시각화합니다.

```python
# 6-1. 혼동행렬 계산 (레이블 순서 명시)
LABELS = ['NORMAL', 'RF_UNSTABLE', 'PRESSURE_DRIFT', 'GAS_LEAK']
cm = confusion_matrix(ym_test, pred4, labels=LABELS)

# 6-2. Heatmap 시각화 및 데이터 표기
fig, ax = plt.subplots(figsize=(7, 6))
cax = ax.imshow(cm, cmap='Blues')
fig.colorbar(cax)

ax.set_xticks(range(len(LABELS)))
ax.set_yticks(range(len(LABELS)))
ax.set_xticklabels(LABELS, rotation=45, ha='right', fontsize=11)
ax.set_yticklabels(LABELS, fontsize=11)
ax.set_xlabel('Predicted Label', fontsize=12, fontweight='bold')
ax.set_ylabel('Actual Label', fontsize=12, fontweight='bold')
ax.set_title('Confusion Matrix (4-Class FDC Model)', fontsize=14, fontweight='bold', pad=15)

for i in range(len(LABELS)):
    for j in range(len(LABELS)):
        ax.text(j, i, cm[i, j], ha='center', va='center',
                color='white' if cm[i, j] > cm.max()/2 else 'black',
                fontsize=13, fontweight='bold')

plt.tight_layout()
plt.show()
```

![혼동행렬 시각화]({{ '/images/images_반도체장비데이터실무_week04/confusion_matrix.png' | relative_url }})

### 혼동행렬 해석
- **행(Row)**: 실제 고장 유형 (Actual)
- **열(Column)**: 모델의 예측 (Predicted)
- 대각선 성분이 올바르게 예측한 경우입니다.
- `RF_UNSTABLE`(9건)과 `PRESSURE_DRIFT`(9건)는 100% 대각선에 위치하여 오분류가 전혀 없습니다.
- **오분류의 대부분은 `GAS_LEAK`이 `NORMAL`로 잘못 분류된 것**입니다.

---

## 8. 미션 7 · 모델의 판단 근거: Feature Importance 분석

랜덤포레스트 모델이 어떤 특징을 근거로 이상과 정상, 고장 유형을 판단했는지 **특징 중요도(Feature Importance)**를 추출하여 상위 10개를 시각화합니다.

```python
# 7-1. 특징 중요도 Series 생성 및 정렬
importance = pd.Series(rf4.feature_importances_, index=Xm_train.columns)
top10 = importance.sort_values(ascending=False).head(10)

# 7-2. 가로 막대그래프 시각화
plt.figure(figsize=(9, 6))
bars = plt.barh(top10.index[::-1], top10.values[::-1], color='royalblue')
plt.title("Top 10 Feature Importances", fontsize=14, fontweight='bold', pad=12)
plt.xlabel("Importance", fontsize=12)
plt.ylabel("Features", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 7-3. 도메인 특징 pressure_slope 의 순위 확인
rank = importance.sort_values(ascending=False).index.get_loc('pressure_slope') + 1
print(f"pressure_slope 특징의 중요도 순위: {rank} 위")
```

![특징 중요도 Top 10]({{ '/images/images_반도체장비데이터실무_week04/feature_importance.png' | relative_url }})

### Feature Importance 주요 해석

1. **`pressure_slope`의 압도적 1위 기록**:
   - 원본 센서의 단순 정적 통계량(평균, 최댓값 등)이 아니라, 엔지니어가 물리적 도메인 지식을 바탕으로 직접 파생시킨 **압력의 시간당 변화율(기울기, `pressure_slope`)이 전체 33개 변수 중 가장 높은 중요도(1위)**를 나타냈습니다.
   - 이는 식각 공정 중 압력 드리프트나 미세 가스 누출, 배기 밸브의 제어 응답 지연 등이 일어날 때 **기울기 변화**가 가장 민감한 이상 신호(Early Indicator)로 작동함을 방증합니다.
2. **RF 전력 및 챔버 압력 관련 피처의 강세**:
   - `rf_reflected_W`(반사 전력), `chamber_pressure_mTorr` 관련 통계량들이 상위권에 포진하여 플라즈마 임피던스 매칭 및 압력 안정성이 장비 상태 판별의 핵심 변수임을 확인했습니다.

---

## 9. 미션 8 · 공정 엔지니어 관점의 심층 고찰 및 실무 Q&A

### Q1. 이진 분류 결과를 한 문장으로 요약한다면?
> **답변:** 이진 분류 모델의 정밀도는 **1.00**, 재현율은 **0.76**으로, 모델이 이상이라고 판단한 웨이퍼는 100% 실제 이상이었으나, 실제 이상 웨이퍼 **25장 중 6장(24%)을 정상으로 오판하여 놓쳤습니다.**

### Q2. 왜 유독 `GAS_LEAK` 유형만 모델이 잘 잡지 못하는가?
> **답변:** 놓친 이상 웨이퍼 6장이 전부 `GAS_LEAK`이었으며, 평가 데이터셋 내 `GAS_LEAK` **10장 중 6장(60.0%)**을 정상으로 오분류했습니다.  
> 지난주 박스플롯 분포 분석에서 확인했듯이, `GAS_LEAK`은 RF 방전 불안정이나 급격한 압력 드리프트와 달리 센서 변동 폭이 매우 미세하여 **정상(NORMAL) 센서 분포와 상당 구간 겹치기 때문**에 단순 통계량 기반 분리 경계로는 오분류되기 쉽습니다.

### Q3. 정밀도 1.00은 과연 마냥 좋은 신호인가?
> **답변:** 정밀도 1.00은 이상이라고 경고한 알람에 거짓 경보(False Alarm, 오경보)가 없어 설비 엔지니어의 피로도를 낮춘다는 점에서는 긍정적입니다.  
> 그러나 재현율이 0.76에 불과하여 **실제 불량 웨이퍼의 24%가 이상 징후를 감지받지 못하고 후속 공정으로 유출**되었으며, 특히 `GAS_LEAK`은 60%를 놓쳤습니다. 반도체 수율 관리 관점에서 미검출 비용은 막대하므로, 정밀도만 보고 우수한 모델이라고 단정할 수 없습니다.

### Q4. 현업에 납품한다면 '이진 분류'와 '4분류' 중 무엇을 선택하겠는가?
> **답변:** 현장 공정/설비 엔지니어에게는 **4분류 모델**을 납품해야 합니다.  
> 이진 분류는 단순히 "이상 발생" 여부만 알려주어 엔지니어가 챔버 전체를 점검해야 하므로 원인 규명 및 설비 정지 시간이 길어집니다. 반면 4분류 모델은 `RF_UNSTABLE`, `PRESSURE_DRIFT`, `GAS_LEAK` 등 원인 부위를 즉시 특정해주어 **MTTR(Mean Time To Repair, 평균 복구 시간)을 획기적으로 단축**시킬 수 있습니다. 단, `GAS_LEAK`의 낮은 재현율에 대한 보완책이 함께 제공되어야 합니다.

### Q5. 파생 변수 `pressure_slope`가 중요도 1위에 오른 물리적 이유는?
> **답변:** `pressure_slope`는 `MainEtch` 반응 구간 동안 챔버 내부 압력이 시간에 따라 변화하는 속도와 방향(추세)을 나타냅니다.  
> 가스 유입 불량, 배기 라인(APC 밸브/터보 펌프)의 성능 저하, 미세 누출이 발생하면 순간적인 압력 절댓값(평균/최댓값)은 정상 스펙 범위 내에 있더라도 **시간 경과에 따른 압력 추세선(기울기)이 뚜렷하게 왜곡**됩니다. 따라서 정적 요약 통계량보다 시계열의 동적 변화율을 담은 기울기 피처가 고장 판별에 결정적인 기여를 했습니다.

### Q6. 미검출이 심한 `GAS_LEAK`의 재현율을 개선하기 위한 엔지니어링 방안은?
> **답변:** 모델 알고리즘 교체 외에도 다음과 같은 실무적 접근이 가능합니다.
> 1. **도메인 기반 추가 특징 엔지니어링**:
>    - 단순히 압력 기울기뿐만 아니라, 가스 공급 유량(`cf4_flow_sccm`, `ar_flow_sccm`)과 압력 간의 상관계수, 구간별 미분값, 가스 밸브 응답 지연 시간 등 미세 누출을 포착할 수 있는 다변량 시계열 피처를 추가 생성합니다.
> 2. **데이터 수집 및 증강(Data Augmentation)**:
>    - 상대적으로 샘플 수가 적고 정상과 유사한 경계 영역의 `GAS_LEAK` 웨이퍼 데이터를 추가 수집하거나, SMOTE/시계열 데이터 증강 기법을 통해 학습 데이터셋의 표현력을 강화합니다.
> 3. **분류 임계값(Threshold) 조정 및 비용 민감 학습(Cost-sensitive Learning)**:
>    - `rf.predict_proba()`를 활용하여 `GAS_LEAK` 또는 이상 클래스에 대한 판정 확률 임계값을 0.5에서 0.3~0.4 수준으로 낮춥니다. 약간의 정밀도 하락(오경보 증가)을 감수하더라도 미검출 웨이퍼를 대폭 줄여 공정 리스크를 방어합니다.

---

## 10. 총평 및 향후 개선 방향

이번 실습을 통해 반도체 식각 공정의 FDC 센서 데이터를 바탕으로 이상탐지 및 고장 유형 분류 파이프라인을 구축해 보았습니다.

- **핵심 배운 점**:
  - 도메인 지식 기반의 **Feature Engineering(`pressure_slope`)**이 모델 성능에 지대한 영향을 미친다는 점을 확인했습니다.
  - 단순 정확도(Accuracy)나 정밀도(Precision)에 현혹되지 않고, **재현율(Recall)과 오분류 세부 유형(GAS_LEAK)**을 파고드는 **에러 분석(Error Analysis)**의 중요성을 체득했습니다.
- **Next Step**:
  - 미세 이상(`GAS_LEAK`) 탐지율 제고를 위한 센서 간 상관관계 피처 개발
  - Isolation Forest, AutoEncoder 등 비지도 학습 기반 이상탐지 알고리즘과의 하이브리드 결합
  - 모델의 실시간 추론 지연 시간(Inference Latency) 최적화

---
*Posted by 반도체 장비 데이터 실무 분석팀*
