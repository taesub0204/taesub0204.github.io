---
layout: page
title: 레트로 지렁이 게임 (Snake Game)
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

  <h2>🐍 레트로 아케이드 지렁이 게임 (TAESUB GAMES)</h2>
  <p>
    고전 아케이드의 향수를 현대적인 웹 기술로 재해석한 <strong>HTML5 Canvas 기반 스네이크 게임</strong>입니다. 
    CRT 모니터 특유의 스캔라인 셰이더 효과, 모노스페이스 레트로 폰트, 그리고 레트로 NES 컨트롤러 가상 패드를 구현하여 몰입감 있는 플레이 경험을 선사합니다.
  </p>

  <!-- 제작 기술 및 개발 환경 요약 박스 -->
  <div class="project-tech-box" style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 1.2rem 1.5rem; margin: 1.5rem 0 1.8rem 0;">
    <h3 style="margin: 0 0 0.8rem 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; color: var(--text-color);">
      🛠️ 기술 스택 & 게임 특징 (Tech Stack)
    </h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
      <span style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🎨 HTML5 Canvas 2D</span>
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; border: 1px solid rgba(0, 120, 215, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">⚡ JavaScript (ES6+)</span>
      <span style="background: rgba(230, 81, 0, 0.12); color: #e65100; border: 1px solid rgba(230, 81, 0, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">📺 CRT Scanline FX</span>
      <span style="background: rgba(81, 43, 212, 0.12); color: #7050e5; border: 1px solid rgba(81, 43, 212, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🕹️ Virtual NES D-Pad</span>
      <span style="background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🔊 Web Audio FX</span>
    </div>
    <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.92rem; opacity: 0.9; line-height: 1.6; color: var(--text-color);">
      <li><strong>정밀한 그리드 충돌 알고리즘</strong>: 캔버스 그리드 상에서 지렁이의 마디(Segment) 배열을 갱신하고, 벽 및 자기 자신과의 충돌을 실시간 감지</li>
      <li><strong>점진적 난이도 조절</strong>: 먹이를 섭취할 때마다 프레임 갱신 주기를 단축하여 자연스러운 속도 가속화 구현</li>
      <li><strong>멀티 컨트롤 인터페이스</strong>: 키보드 방향키, WASD 키 및 모바일 터치 대응을 위한 화면상 NES D-pad 조작 지원</li>
    </ul>
  </div>

  <!-- 실행 및 바로가기 바 -->
  <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <a href="https://taesub0204.github.io/snake-game/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.2rem; background: #059669; color: #ffffff !important; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
      새 창에서 게임 플레이하기 (Play Fullscreen)
    </a>
    <span style="font-size: 0.88rem; opacity: 0.8;">※ 아래 화면에서 [GAME START] 버튼을 누르면 브라우저에서 바로 플레이할 수 있습니다.</span>
  </div>

  <!-- 실시간 라이브 게임 플레이 (iframe) -->
  <div style="border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; box-shadow: 0 6px 20px var(--shadow); background: #000; margin-bottom: 2.5rem;">
    <div style="background: var(--box-bg); padding: 0.6rem 1rem; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; font-size: 0.85rem;">
      <span style="display: flex; align-items: center; gap: 0.5rem; font-weight: 600;">
        <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #10b981;"></span>
        Snake Game Retro Arcade Live View
      </span>
      <a href="https://taesub0204.github.io/snake-game/" target="_blank" rel="noopener noreferrer" style="color: var(--link-color); text-decoration: none; font-weight: 600;">전체화면 ↗</a>
    </div>
    <div style="position: relative; width: 100%; height: 750px;">
      <iframe src="https://taesub0204.github.io/snake-game/" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" title="Snake Game"></iframe>
    </div>
  </div>

</div>
