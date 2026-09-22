---
layout: page
title: 레트로 벽돌깨기 게임 (Brick Breaker)
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

  <h2>🧱 레트로 아케이드 벽돌깨기 게임 (TAESUB GAMES)</h2>
  <p>
    네온 글로우 비주얼과 역동적인 사운드로 클래식 아케이드를 현대적으로 리이매진(Reimagined)한 <strong>HTML5 Canvas 벽돌깨기 게임</strong>입니다. 
    패들 타격 위치에 따른 정교한 각도 굴절 물리 연산과 일반(Normal) / 헬(Hell) 스테이지 모드를 제공합니다.
  </p>

  <!-- 제작 기술 및 개발 환경 요약 박스 -->
  <div class="project-tech-box" style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 1.2rem 1.5rem; margin: 1.5rem 0 1.8rem 0;">
    <h3 style="margin: 0 0 0.8rem 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; color: var(--text-color);">
      🛠️ 기술 스택 & 게임 특징 (Tech Stack)
    </h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; border: 1px solid rgba(0, 120, 215, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🎨 HTML5 Canvas 2D</span>
      <span style="background: rgba(104, 33, 122, 0.12); color: #ab47bc; border: 1px solid rgba(104, 33, 122, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">⚡ JavaScript Physics</span>
      <span style="background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🔥 Normal & Hell Stage</span>
      <span style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">✨ Neon Cyberpunk Glow</span>
      <span style="background: rgba(230, 81, 0, 0.12); color: #e65100; border: 1px solid rgba(230, 81, 0, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🎧 Dynamic SFX</span>
    </div>
    <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.92rem; opacity: 0.9; line-height: 1.6; color: var(--text-color);">
      <li><strong>탄도 물리 충돌 연산</strong>: 공이 패들의 중심에서 얼마나 떨어져 맞았는지에 따라 반사 각도를 동적으로 계산하는 현실적 아케이드 물리 구현</li>
      <li><strong>스테이지 난이도 분기</strong>: 정석적인 레인보우 블록 배열의 'NORMAL STAGE'와 불규칙 패턴 및 강화된 속도의 'HELL STAGE' 모드 지원</li>
      <li><strong>사이버펑크 UI & 오디오 피드백</strong>: 네온 블록 파괴 효과, 점수 및 생명 관리, 배경 음악 및 타격 사운드 연동</li>
    </ul>
  </div>

  <!-- 실행 및 바로가기 바 -->
  <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <a href="https://taesub0204.github.io/brick-breaker/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.2rem; background: #7050e5; color: #ffffff !important; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 12px rgba(112, 80, 229, 0.3);">
      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
      새 창에서 게임 플레이하기 (Play Fullscreen)
    </a>
    <span style="font-size: 0.88rem; opacity: 0.8;">※ 마우스 또는 좌우 방향키로 패들을 조종하고 스페이스바를 눌러 시작하세요.</span>
  </div>

  <!-- 실시간 라이브 게임 플레이 (iframe) -->
  <div style="border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; box-shadow: 0 6px 20px var(--shadow); background: #000; margin-bottom: 2.5rem;">
    <div style="background: var(--box-bg); padding: 0.6rem 1rem; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; justify-content: space-between; font-size: 0.85rem;">
      <span style="display: flex; align-items: center; gap: 0.5rem; font-weight: 600;">
        <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #10b981;"></span>
        Brick Breaker Cyberpunk Arcade Live View
      </span>
      <a href="https://taesub0204.github.io/brick-breaker/" target="_blank" rel="noopener noreferrer" style="color: var(--link-color); text-decoration: none; font-weight: 600;">전체화면 ↗</a>
    </div>
    <div style="position: relative; width: 100%; height: 750px;">
      <iframe src="https://taesub0204.github.io/brick-breaker/" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" title="Brick Breaker"></iframe>
    </div>
  </div>

</div>
