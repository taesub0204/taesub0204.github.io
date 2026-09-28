---
layout: post
title: "[SQLD 2024] 07. 제2과목 관리 구문 - DML, TCL, DDL, DCL 완벽 마스터"
date: 2026-10-02
categories: [SQLD]
tags: [SQLD, 제2과목, DML, TCL, DDL, DCL, MERGE, COMMIT, ROLLBACK, 제약조건, GRANT]
---
> **출제 비중**: 제2과목 40문항 중 약 6~8문항 출제 (오라클 vs SQL Server 트랜잭션 차이 및 DDL 명령어 단골!)  
> **핵심 키워드**: DML (INSERT/UPDATE/DELETE/MERGE), TCL (COMMIT/ROLLBACK/SAVEPOINT), DDL (CREATE/ALTER/DROP/TRUNCATE), 제약조건 5가지, DCL 권한 옵션 비교

---

## 1. DML (데이터 조작어, Data Manipulation Language)

사용자가 데이터의 실질적인 값(튜플)을 삽입, 수정, 삭제, 조회할 때 사용하는 명령어입니다.

### 1) INSERT (데이터 삽입)
```sql
-- 특정 컬럼만 지정 삽입 (명시되지 않은 컬럼은 NULL 또는 DEFAULT 값 입력)
INSERT INTO EMP (EMPNO, ENAME, SAL) VALUES (7999, 'KIM', 3000);

-- 대량 데이터 삽입 (CTAS 스타일의 서브쿼리 INSERT)
INSERT INTO EMP_BACKUP SELECT * FROM EMP WHERE DEPTNO = 10;
```

### 2) UPDATE (데이터 수정)
```sql
UPDATE EMP
SET SAL = SAL * 1.1, COMM = 500
WHERE DEPTNO = 20;  -- ⚠️ WHERE 절 생략 시 테이블 전체 행의 데이터가 변경됨!
```

### 3) DELETE (데이터 삭제)
```sql
DELETE FROM EMP
WHERE EMPNO = 7999;  -- ⚠️ WHERE 절 생략 시 테이블의 모든 데이터가 삭제됨! (롤백 가능)
```

### 4) MERGE (데이터 병합 / UPSERT)
데이터가 테이블에 이미 존재하면 `UPDATE`를 수행하고, 없으면 신규로 `INSERT`를 수행합니다.
```sql
MERGE INTO EMP T
USING EMP_NEW S ON (T.EMPNO = S.EMPNO)
WHEN MATCHED THEN
    UPDATE SET T.SAL = S.SAL, T.COMM = S.COMM
WHEN NOT MATCHED THEN
    INSERT (EMPNO, ENAME, SAL) VALUES (S.EMPNO, S.ENAME, S.SAL);
```

---

## 2. TCL (트랜잭션 제어어, Transaction Control Language)

### 📌 핵심 명령어
- **`COMMIT`**: 데이터 조작 작업이 정상 완료되었음을 최종 확정하고 디스크에 영구 반영하며, 행 잠금(Lock)을 해제합니다.
- **`ROLLBACK`**: 직전 `COMMIT` 시점 또는 특정 `SAVEPOINT` 시점으로 작업을 취소하고 원래 상태로 되돌립니다.
- **`SAVEPOINT 저장점명`**: 트랜잭션 도중 특정 지점으로 롤백할 수 있는 체크포인트를 설정합니다.
```sql
SAVEPOINT SP1;
UPDATE EMP SET SAL = 1000 WHERE EMPNO = 7788;
ROLLBACK TO SP1;  -- SP1 이후의 작업만 취소됨
```

### 🚨 DBMS별 트랜잭션 동작 방식 차이 (시험 단골! ⭐⭐⭐⭐⭐)
| 비교 항목 | **Oracle** | **SQL Server** |
| :--- | :--- | :--- |
| **기본 커밋 모드** | **수동 커밋 (Manual Commit)**<br>사용자가 명시적으로 `COMMIT` 입력 필요 | **자동 커밋 (Auto Commit)**<br>DML 문장 하나마다 자동 커밋 |
| **DDL 실행 시 동작** | **묵시적 AUTO COMMIT 자동 발생!**<br>(이전 DML 작업까지 모두 강제 확정됨) | **AUTO COMMIT 되지 않음**<br>(DDL 문장도 롤백 가능!) |

---

## 3. DDL (데이터 정의어): CREATE, ALTER, DROP, TRUNCATE

테이블이나 인덱스 등 데이터베이스 객체(Structure)를 생성, 수정, 삭제하는 명령어입니다.

### 1) 주요 데이터 타입
- `CHAR(n)`: 고정 길이 문자열 (남는 공간은 공백으로 패딩)
- `VARCHAR2(n)`: 가변 길이 문자열 (입력된 데이터 실제 크기만큼만 저장)
- `NUMBER(p, s)`: $p$는 전체 자릿수, $s$는 소수점 자릿수
- `DATE`: 연, 월, 일, 시, 분, 초 저장

### 2) ALTER TABLE (테이블 구조 변경)
```sql
-- 1) 컬럼 추가 (새 컬럼은 항상 테이블 맨 뒤에 추가되며 기본값 NULL)
ALTER TABLE EMP ADD (BIRTHDAY DATE DEFAULT SYSDATE);

-- 2) 컬럼 속성 변경 (크기 확대는 자유로우나, 축소는 기존 데이터 최대 길이보다 커야 함)
ALTER TABLE EMP MODIFY (ENAME VARCHAR2(50) NOT NULL);

-- 3) 컬럼명 변경
ALTER TABLE EMP RENAME COLUMN BIRTHDAY TO B_DATE;

-- 4) 컬럼 삭제
ALTER TABLE EMP DROP COLUMN B_DATE;
```

---

## 4. DELETE vs TRUNCATE vs DROP 완벽 비교표 (초특급 빈출! ⭐⭐⭐⭐⭐)

| 비교 항목 | `DELETE` | `TRUNCATE` | `DROP` |
| :--- | :--- | :--- | :--- |
| **명령어 분류** | **DML** (데이터 조작어) | **DDL** (데이터 정의어) | **DDL** (데이터 정의어) |
| **삭제 대상** | 테이블 내의 **데이터 행(Row)** | 테이블 내의 **전체 데이터** | **테이블 구조 + 데이터 전체** |
| **WHERE 조건절** | **사용 가능** (선택 삭제) | **사용 불가** (무조건 전건 삭제) | 대상 없음 |
| **저장 공간(HWM)** | **유지** (용량 반환 안 됨) | **초기화 및 디스크 반환** | **완전 회수 및 삭제** |
| **ROLLBACK 가능 여부** | **가능 (Undo 로그 기록)** | **불가 (즉시 커밋)** | **불가 (즉시 커밋)** |
| **처리 속도** | 느림 (로그 과다 발생) | **매우 빠름 (시스템 부하 최소)** | 빠름 |

---

## 5. 무결성 제약조건 (Constraints) 5가지

| 제약조건명 | 설명 | 비고 |
| :--- | :--- | :--- |
| **PRIMARY KEY (기본키)** | 행을 유일하게 식별하는 유일키 | **UNIQUE + NOT NULL** (테이블당 1개만 가능) |
| **UNIQUE KEY (고유키)** | 컬럼 값의 중복을 방지 | **NULL 값 허용** (복수의 NULL 저장 가능) |
| **NOT NULL** | 컬럼에 NULL 값이 입력되는 것을 금지 | 컬럼 레벨에서만 정의 가능 |
| **CHECK** | 지정된 조건식의 범위 내 값만 허용 | 예: `CHECK (SAL >= 0 AND SAL <= 10000)` |
| **FOREIGN KEY (외래키)** | 다른 부모 테이블의 기본키를 참조 | 참조 무결성 유지 |

### 🔗 FOREIGN KEY 삭제 옵션 (부모 행 삭제 시 자식 행 처리)
- `ON DELETE RESTRICT` (기본값): 자식 행이 참조하고 있으면 **부모 행 삭제 불가 (에러)**
- `ON DELETE CASCADE`: 부모 행 삭제 시 **참조하고 있던 자식 테이블의 관련 행들도 함께 연쇄 삭제**
- `ON DELETE SET NULL`: 부모 행 삭제 시 **자식 테이블의 외래키 컬럼 값을 `NULL`로 변경**

---

## 6. 데이터베이스 기타 객체: 뷰(View), 시퀀스(Sequence)

### 1) 뷰 (View)
- 실제 물리적 데이터를 저장하지 않는 **가상 테이블(Virtual Table)**입니다.
- **장점**:
  - **보안성**: 민감한 컬럼(주민번호, 급여 등)을 숨기고 필요한 정보만 사용자에게 노출
  - **독립성**: 기존 테이블 구조가 일부 변경되어도 뷰 구조는 유지 가능
  - **편의성**: 복잡한 조인 쿼리를 뷰로 단순화하여 재사용 용이
- **주의점**: 독립적인 인덱스를 생성할 수 없으며, 집계/조인 뷰는 데이터의 삽입·수정·삭제(DML)가 제한됨

### 2) 시퀀스 (Sequence)
- 고유한 일련번호를 자동으로 생성해주는 데이터베이스 객체입니다. (인조식별자 생성용)
- `시퀀스명.NEXTVAL`: 다음 번호 생성 및 반환
- `시퀀스명.CURRVAL`: 현재 할당된 번호 반환 (반드시 `NEXTVAL`이 1회 이상 수행된 세션에서만 호출 가능)

---

## 7. DCL (데이터 제어어): 권한과 ROLE

데이터베이스의 접근을 통제하고 보안을 위해 권한을 부여(`GRANT`)하거나 회수(`REVOKE`)합니다.

### 1) 권한의 분류
- **시스템 권한**: DB 전체에 영향을 주는 관리자급 권한 (`CREATE USER`, `CREATE TABLE`, `CREATE SESSION` 등)
- **객체 권한**: 특정 객체(테이블, 뷰 등)를 조작할 수 있는 권한 (`SELECT`, `INSERT`, `UPDATE`, `DELETE` ON 테이블명)

### 2) 권한 재부여 옵션 비교 (시험 필수! ⭐⭐⭐)
| 구분 | `WITH GRANT OPTION` | `WITH ADMIN OPTION` |
| :--- | :--- | :--- |
| **적용 권한** | **객체 권한** 전용 | **시스템 권한 및 ROLE** 전용 |
| **권한 전파** | 권한을 받은 유저가 타인에게 재부여 가능 | 권한을 받은 유저가 타인에게 재부여 가능 |
| **권한 회수 (REVOKE) 시 연쇄 작용** | **연쇄 취소 (Cascading) 발생!**<br>중간 관리자의 권한을 회수하면 하위 유저들의 권한도 **모두 함께 취소됨** | **연쇄 취소 안 됨!**<br>중간 관리자의 권한을 회수해도 하위 유저들의 권한은 **그대로 유지됨** |

### 3) ROLE (롤)
- 다수의 사용자에게 일일이 개별 권한을 부여하는 번거로움을 줄이기 위해, **여러 권한을 하나의 그룹으로 묶어둔 집합체**입니다.
- 유저에게 부여할 수도 있고, 다른 ROLE에 포함시킬 수도 있습니다.
- ⚠️ **주의**: 롤을 통해 부여받은 권한은 특정 권한만 쏙 빼서 직접 회수할 수 없으며, **롤 자체를 회수하거나 롤 내부 구성을 변경**해야 합니다.
