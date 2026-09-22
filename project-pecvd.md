---
layout: page
title: PECVD 반도체 증착장비 시뮬레이터
---

<div style="margin-bottom: 1.5rem;">
  <a href="/project" style="display: inline-flex; align-items: center; gap: 0.4rem; text-decoration: none; font-weight: 600; color: var(--link-color); font-size: 0.95rem;">
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="19" y1="12" x2="5" y2="12"></line>
      <polyline points="12 19 5 12 12 5"></polyline>
    </svg>
    Project 목록으로 돌아가기
  </a>
</div>

<div style="max-width: 860px; margin: 0 auto;">

  <h2>⚡ PECVD 반도체 증착장비 시뮬레이터 (System Monitor)</h2>
  <p>
    반도체 핵심 8대 공정 중 박막 증착(Deposition) 단계를 웹 브라우저 상에서 정밀하게 모사하는 <strong>교육 및 분석용 PECVD 장비 제어 대시보드 시뮬레이터</strong>입니다. 
    가상 3D 진공 챔버 및 플라즈마 반응, 공정 레시피 제어, 실시간 두께 및 균일도 트렌드 데이터를 시각화합니다.
  </p>

  <!-- 제작 기술 및 개발 환경 요약 박스 -->
  <div class="project-tech-box" style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 1.2rem 1.5rem; margin: 1.5rem 0 1.8rem 0;">
    <h3 style="margin: 0 0 0.8rem 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; color: var(--text-color);">
      🛠️ 기술 스택 & 핵심 기능 (Tech Stack)
    </h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; border: 1px solid rgba(0, 120, 215, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">⚛️ Three.js (3D 챔버)</span>
      <span style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">📊 Canvas Data Trend</span>
      <span style="background: rgba(230, 81, 0, 0.12); color: #e65100; border: 1px solid rgba(230, 81, 0, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🧪 Recipe Control</span>
      <span style="background: rgba(104, 33, 122, 0.12); color: #ab47bc; border: 1px solid rgba(104, 33, 122, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">💡 Plasma Simulation</span>
      <span style="background: rgba(100, 116, 139, 0.12); color: #475569; border: 1px solid rgba(100, 116, 139, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🖥️ Responsive Dashboard</span>
    </div>
    <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.92rem; opacity: 0.9; line-height: 1.6; color: var(--text-color);">
      <li><strong>3D 인터랙티브 챔버</strong>: Three.js 기반으로 챔버 형상, 서셉터, 가스 샤워헤드 및 플라즈마 방전 상태를 360도 회전(OrbitControls)하며 시각적으로 확인</li>
      <li><strong>공정 레시피 & 파라미터 제어</strong>: Standard SiN, Low-Stress SiN, SiO₂, Amorphous Si 프리셋 제공 및 챔버 압력(Torr), 온도(℃), RF Power(W), 가스 유량(SiH₄, NH₃, N₂) 실시간 조절</li>
      <li><strong>박막 물성 트렌드 실시간 계산</strong>: 공정 조건에 따른 실시간 증착 속도(Dep. Rate), 박막 두께(Thickness Trend) 및 웨이퍼 면내 균일도(Uniformity) 분석 차트 렌더링</li>
    </ul>
  </div>

  <!-- 실행 및 바로가기 바 -->
  <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <a href="https://taesub0204.github.io/PECVD/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.2rem; background: #0078d7; color: #ffffff !important; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 12px rgba(0, 120, 215, 0.3);">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
      새 창에서 전체화면으로 실행하기 (Live Simulator)
    </a>
    <span style="font-size: 0.88rem; opacity: 0.8;">※ 아래 임베드 화면에서 챔버를 마우스로 직접 회전하거나 레시피를 제어해보실 수 있습니다.</span>
  </div>

  <!-- 실시간 라이브 인터랙티브 시뮬레이터 (iframe) -->
  <div style="border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; box-shadow: 0 6px 20px var(--shadow); background: #000; margin-bottom: 2.5rem;">
    <div style="background: var(--box-bg); padding: 0.6rem 1rem; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; font-size: 0.85rem;">
      <span style="display: flex; align-items: center; gap: 0.5rem; font-weight: 600;">
        <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #10b981;"></span>
        PECVD System Simulator Live View
      </span>
      <a href="https://taesub0204.github.io/PECVD/" target="_blank" rel="noopener noreferrer" style="color: var(--link-color); text-decoration: none; font-weight: 600;">전체화면 ↗</a>
    </div>
    <div style="position: relative; width: 100%; height: 720px;">
      <iframe src="https://taesub0204.github.io/PECVD/" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" title="PECVD Simulator"></iframe>
    </div>
  </div>

</div>
