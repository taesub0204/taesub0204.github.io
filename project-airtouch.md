---
layout: page
title: 에어터치 (AirTouch) 시연 영상
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

<div style="max-width: 740px; margin: 0 auto;">

  <h2>🎬 에어터치 (AirTouch) - 안드로이드 공간 제스처 컨트롤러</h2>
  <p>
    한국폴리텍대학 하이테크 과정 <strong>프로젝트 실습</strong>으로 제작 중인 
    <strong>AI 기반 스마트폰 비접촉 공간 제스처 제어(에어마우스) 앱</strong> 구동 시연 영상입니다. 
    영상의 재생(▶) 버튼을 누르면 브라우저에서 바로 시청하실 수 있습니다.
  </p>

  <!-- 제작 기술 및 개발 환경 요약 박스 -->
  <div class="project-tech-box" style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 1.2rem 1.5rem; margin: 1.5rem 0 2rem 0;">
    <h3 style="margin: 0 0 0.8rem 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; color: var(--text-color);">
      🛠️ 제작 기술 및 개발 환경 (Tech Stack)
    </h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
      <span style="background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🎬 프로젝트 실습</span>
      <span style="background: rgba(245, 158, 11, 0.12); color: #d97706; border: 1px solid rgba(245, 158, 11, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🚧 현재 APP 개발 진행 중</span>
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; border: 1px solid rgba(0, 120, 215, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">📱 Android (Kotlin)</span>
      <span style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">👁️ Google MediaPipe Hands</span>
      <span style="background: rgba(112, 80, 229, 0.12); color: #7050e5; border: 1px solid rgba(112, 80, 229, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">📷 CameraX</span>
      <span style="background: rgba(104, 33, 122, 0.12); color: #ab47bc; border: 1px solid rgba(104, 33, 122, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">♿ AccessibilityService</span>
      <span style="background: rgba(100, 116, 139, 0.12); color: #475569; border: 1px solid rgba(100, 116, 139, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🪟 Overlay Window</span>
    </div>
    <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.92rem; opacity: 0.9; line-height: 1.6; color: var(--text-color);">
      <li><strong>온디바이스 비전 AI</strong>: 스마트폰 전면 카메라 영상을 초당 30프레임으로 분석하여 손의 21개 3D 랜드마크를 실시간 추적</li>
      <li><strong>비접촉 에어마우스 인터페이스</strong>: 화면을 물리적으로 터치하지 않고도 허공에서 커서 이동, 단일 탭 클릭, 더블 탭, 연속 스크롤 구현</li>
      <li><strong>안드로이드 시스템 통합</strong>: 안드로이드 접근성 서비스(AccessibilityService)와 오버레이 윈도우를 연동하여 기기 전체 앱 및 홈/최근앱/뒤로가기 시스템 내비게이션 완벽 지원</li>
      <li><strong>APP 개발 진행 중</strong>: 오터치 방어 알고리즘(안전 영역 클램핑, 해부학적 오른손/왼손 판정, 편안한 휴식 손 자세 오인식 차단 등) 고도화 및 최적화 진행 중</li>
    </ul>
  </div>

  <div class="video-showcase-container">

    <!-- 16:9 가로 동영상 카드 -->
    <div class="video-card-landscape">
      <div class="video-iframe-wrap ratio-16-9">
        <iframe 
          src="https://www.youtube.com/embed/iKYv35nSBq4" 
          title="에어터치 / AirTouch - 프로젝트 실습" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen>
        </iframe>
      </div>
      <div class="video-details">
        <span class="video-badge blue">📱 에어터치 (AirTouch) 구동 시연</span>
        <h3>비접촉 공간 제스처 에어마우스 (AirTouch)</h3>
        <p>
          스마트폰 화면을 터치하지 않고도 카메라 앞 손동작만으로 포인터 이동, 핀치 클릭, 상하 스크롤 및 앱 조작을 매끄럽게 수행하는 시연 영상입니다.
        </p>
        <a href="https://www.youtube.com/watch?v=iKYv35nSBq4" target="_blank" rel="noopener noreferrer" class="video-link-btn">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.02.257-.012.108c-.052.56-.13 1.103-.24 1.503a2.01 2.01 0 0 1 1.416-1.42c1.123-.302 5.288-.332 6.11-.335zM6.4 5.209v5.582l4.8-2.791L6.4 5.209z"/>
          </svg>
          YouTube에서 크게 보기
        </a>
      </div>
    </div>

  </div>

  <hr style="margin: 3rem 0 2rem 0; border: none; border-top: 1px solid var(--border-color);">

  <!-- 프로젝트 상세 설명 및 개발 코멘트 -->
  <h2>💡 프로젝트 상세 소개 및 개발 코멘트</h2>

  <div style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.5rem 1.8rem; margin-top: 1.2rem; box-shadow: 0 4px 15px var(--shadow);">

    <div style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.8rem; flex-wrap: wrap;">
      <span style="font-weight: 700; font-size: 1.05rem; color: var(--text-color);">📌 개발 상태</span>
      <span style="background: rgba(239, 68, 68, 0.12); color: #ef4444; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 6px; font-size: 0.9rem;">프로젝트 실습</span>
      <span style="background: rgba(245, 158, 11, 0.12); color: #d97706; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 6px; font-size: 0.9rem;">현재 APP 개발 진행 중</span>
    </div>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: var(--text-color);">
      1. 프로젝트 배경 및 기획 의도
    </h3>
    <p style="margin: 0 0 1.2rem 0; font-size: 0.95rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      요리 중 손에 물이나 기름이 묻었을 때, 장갑을 착용하고 작업할 때, 또는 침대에 스마트폰을 거치해 두고 손을 뻗기 어려울 때 <strong>화면을 직접 만지지 않고 허공에서 손동작만으로 스마트폰을 완전히 제어</strong>할 수 있도록 기획한 애플리케이션입니다. 온디바이스 AI 비전 모델을 탑재하여 별도의 외부 센서나 하드웨어 없이 스마트폰 전면 카메라만으로 동작합니다.
    </p>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: #0078d7;">
      2. 핵심 구현 기능 (Key Features)
    </h3>
    <ul style="margin: 0 0 1.2rem 0; padding-left: 1.4rem; font-size: 0.93rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      <li><strong>적응형 스무스 커서 (Air Mouse)</strong>: 검지와 엄지 중심 좌표를 화면 해상도로 실시간 변환하며, 미세 손떨림은 감쇠하고 빠른 이동 시 지연 없이 반응하는 동적 EMA 필터를 적용했습니다.</li>
      <li><strong>마이크로 핀치(Pinch) 클릭 판정</strong>: 엄지와 검지 끝의 거리와 손가락 마디 접촉을 정밀하게 계산하여, 가벼운 핀치로 원하는 버튼/링크를 오차 없이 단일 탭 클릭합니다.</li>
      <li><strong>무중단 연속 드래그 & 스크롤</strong>: 핀치를 유지한 상태로 손을 위아래/좌우로 움직여 뉴스 피드 스크롤, 웹서핑, 유튜브 숏츠 넘기기 등을 자연스럽게 조작합니다.</li>
      <li><strong>시스템 내비게이션 바 연동</strong>: 화면 하단 영역에서 제스처를 취해 홈 화면 이동, 최근 앱(멀티뷰) 열기, 뒤로가기 액션을 즉시 트리거합니다.</li>
    </ul>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: #e65100;">
      3. 오작동 방어 알고리즘 및 트러블슈팅
    </h3>
    <p style="margin: 0 0 0.8rem 0; font-size: 0.95rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      실제 사용 환경에서 발생할 수 있는 다양한 오작동(False Positive)을 원천 차단하기 위해 다중 교차 검증 필터를 구축했습니다:
    </p>
    <ul style="margin: 0; padding-left: 1.4rem; font-size: 0.93rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      <li><strong>해부학적 오른손/왼손 판별</strong>: 전면 카메라 거울상 반전 환경에서 3D 손바닥 법선 벡터(Palm Normal Z)와 카이랄성(Chirality)을 분석하여 의도하지 않은 손의 간섭을 차단합니다.</li>
      <li><strong>편안한 손 자세(Relaxed Hand) 가짜 핀치 방어</strong>: 핀치 의도 없이 손가락을 자연스럽게 웅크리고 손을 내릴 때 발생하는 원근 착시를 걸러내어 불필요한 클릭이나 드래그를 방지합니다.</li>
      <li><strong>시스템바 안전영역 및 체류 시간(Dwell Time) 보장</strong>: 아래 방향으로 빠르게 스와이프할 때 시스템 버튼이 실수로 눌리지 않도록 가속도 소프트 클램프와 정지 핀치 시간을 검증합니다.</li>
    </ul>

  </div>

</div>
