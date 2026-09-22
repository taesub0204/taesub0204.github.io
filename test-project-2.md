---
layout: page
title: 반도체 장비 제어 시연 영상
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

  <h2>🎬 반도체 장비 제어 및 구동 시연 영상</h2>
  <p>
    한국폴리텍대학 반도체융합캠퍼스 하이테크 과정(반도체장비소프트웨어과) 실습 프로젝트로 제작한 
    <strong>장비 제어 UI 소프트웨어</strong> 및 <strong>실제 장비 실습 환경 구동 영상</strong>입니다. 
    영상의 재생(▶) 버튼을 누르면 브라우저에서 바로 시청하실 수 있습니다.
  </p>

  <!-- 제작 기술 및 개발 환경 요약 박스 -->
  <div class="project-tech-box" style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 10px; padding: 1.2rem 1.5rem; margin: 1.5rem 0 2rem 0;">
    <h3 style="margin: 0 0 0.8rem 0; font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem; color: var(--text-color);">
      🛠️ 제작 기술 및 개발 환경 (Tech Stack)
    </h3>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
      <span style="background: rgba(100, 116, 139, 0.12); color: #475569; border: 1px solid rgba(100, 116, 139, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">⏱️ 개발 기간: 약 4~5일</span>
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; border: 1px solid rgba(0, 120, 215, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">💻 C#</span>
      <span style="background: rgba(81, 43, 212, 0.12); color: #7050e5; border: 1px solid rgba(81, 43, 212, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🖥️ WinForms</span>
      <span style="background: rgba(104, 33, 122, 0.12); color: #ab47bc; border: 1px solid rgba(104, 33, 122, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🧰 Visual Studio</span>
      <span style="background: rgba(230, 81, 0, 0.12); color: #e65100; border: 1px solid rgba(230, 81, 0, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">⚙️ 서보모터 티칭값 제어</span>
      <span style="background: rgba(217, 119, 6, 0.12); color: #d97706; border: 1px solid rgba(217, 119, 6, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🤖 Claude</span>
      <span style="background: rgba(16, 185, 129, 0.12); color: #059669; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.25rem 0.7rem; border-radius: 16px; font-size: 0.85rem; font-weight: 600;">🚀 Anti-Gravity</span>
    </div>
    <ul style="margin: 0; padding-left: 1.2rem; font-size: 0.92rem; opacity: 0.9; line-height: 1.6; color: var(--text-color);">
      <li><strong>단기 집중 개발 (4~5일)</strong>: 4~5일이라는 짧은 기간 내에 신속하게 시스템을 완성하기 위해 <strong>Claude</strong>와 <strong>Anti-Gravity</strong> 등 최신 생성형 AI(LLM) 도구를 페어 프로그래머로 적극 활용</li>
      <li><strong>개발 환경 & UI</strong>: <strong>Visual Studio</strong>에서 <strong>C# WinForms</strong>를 활용하여 장비 모니터링 및 시퀀스 조작 HMI 화면 구현</li>
      <li><strong>모션 제어 기술</strong>: 실제 웨이퍼 이송 로봇의 기구적 충돌 방지와 정밀 위치 결정을 위해 <strong>서보모터 티칭값(Teaching Data) 설정</strong> 및 4대 안전 인터록 로직 설계</li>
    </ul>
  </div>

  <div class="video-showcase-container">

    <!-- 영상 1: 반도체장비제어 UI 시연 (16:9 가로 영상) -->
    <div class="video-card-landscape">
      <div class="video-iframe-wrap ratio-16-9">
        <iframe 
          src="https://www.youtube.com/embed/2sfE_pGKbNo?start=15" 
          title="반도체장비제어 UI 시연" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen>
        </iframe>
      </div>
      <div class="video-details">
        <span class="video-badge blue">🖥️ 16:9 Widescreen UI 시연</span>
        <h3>반도체 장비 제어 UI 시연 (HMI)</h3>
        <p>
          C# WinForms 기반으로 개발한 반도체 장비 제어 화면입니다. 
          장비 상태 머신(State Machine), 센서 압력 모니터링, 안전 인터록 해제 및 모터 축 수동 조작 시퀀스 동작을 확인하실 수 있습니다.
        </p>
        <a href="https://www.youtube.com/watch?v=2sfE_pGKbNo&t=15s" target="_blank" rel="noopener noreferrer" class="video-link-btn">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.02.257-.012.108c-.052.56-.13 1.103-.24 1.503a2.01 2.01 0 0 1 1.416-1.42c1.123-.302 5.288-.332 6.11-.335zM6.4 5.209v5.582l4.8-2.791L6.4 5.209z"/>
          </svg>
          YouTube에서 크게 보기
        </a>
      </div>
    </div>

    <!-- 영상 2: 반도체장비제어 실습환경 (9:16 Shorts) -->
    <div class="video-card-shorts">
      <div class="video-shorts-player-box">
        <div class="video-iframe-wrap ratio-shorts">
          <iframe 
            src="https://www.youtube.com/embed/rYqj2iDmK3o" 
            title="반도체장비제어 실습환경" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            allowfullscreen>
          </iframe>
        </div>
      </div>
      <div class="video-details">
        <span class="video-badge red">📱 YouTube Shorts 실습 현장</span>
        <h3>실제 반도체 장비 구동 환경</h3>
        <p>
          웨이퍼 이송 로봇(TR Robot), 카세트(FOUP) 로드포트 및 챔버 구동 모듈이 연동된 실제 반도체 장비 실습 현장 영상입니다.
        </p>
        <ul style="margin: 0 0 1rem 0; padding-left: 1.2rem; font-size: 0.88rem; opacity: 0.85; line-height: 1.6; color: var(--text-color);">
          <li>서보모터 티칭 위치 정밀 안착 구동</li>
          <li>챔버 도어 및 로봇 블레이드 안전 인터록 동작</li>
          <li>실시간 이송 시퀀스 연동 테스트</li>
        </ul>
        <a href="https://www.youtube.com/shorts/rYqj2iDmK3o" target="_blank" rel="noopener noreferrer" class="video-link-btn">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.02.257-.012.108c-.052.56-.13 1.103-.24 1.503a2.01 2.01 0 0 1 1.416-1.42c1.123-.302 5.288-.332 6.11-.335zM6.4 5.209v5.582l4.8-2.791L6.4 5.209z"/>
          </svg>
          Shorts에서 보기
        </a>
      </div>
    </div>

  </div>

  <hr style="margin: 3rem 0 2rem 0; border: none; border-top: 1px solid var(--border-color);">

  <!-- 엔지니어링 회고 및 트러블슈팅 섹션 -->
  <h2>💡 엔지니어링 회고 및 트러블슈팅 (Retrospective)</h2>

  <div style="background: var(--box-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.5rem 1.8rem; margin-top: 1.2rem; box-shadow: 0 4px 15px var(--shadow);">

    <div style="margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.8rem; flex-wrap: wrap;">
      <span style="font-weight: 700; font-size: 1.05rem; color: var(--text-color);">⏱️ 개발 기간</span>
      <span style="background: rgba(0, 120, 215, 0.12); color: #0078d7; font-weight: 600; padding: 0.25rem 0.75rem; border-radius: 6px; font-size: 0.9rem;">단기 집중 개발 (약 4~5일 소요)</span>
    </div>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: var(--text-color);">
      1. LLM(생성형 AI) 적극 활용을 통한 단기 고속 프로토타이핑
    </h3>
    <p style="margin: 0 0 1.2rem 0; font-size: 0.95rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      약 4~5일이라는 매우 타이트한 일정 속에서 복잡한 HMI 제어 프로그램을 신속하게 구현하기 위해, <strong>Claude</strong>와 <strong>Anti-Gravity</strong> 등 최신 LLM 도구를 페어 프로그래머로 적극 투입했습니다. C# WinForms UI 컴포넌트 배치, 비동기 통신 및 상태 머신(State Machine) 기본 구조를 빠르게 생성하여 초기 개발 기간을 획기적으로 단축했습니다.
    </p>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: #e65100;">
      2. 직면한 문제: 하드웨어 고유 특성과 오버슈팅(Overshooting)의 한계
    </h3>
    <p style="margin: 0 0 0.8rem 0; font-size: 0.95rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      소프트웨어 화면은 빠르게 완성되었지만, <strong>실제 하드웨어 장비와 연동하는 순간 AI의 한계</strong>가 명확히 드러났습니다. LLM은 물리 모터의 질량 관성(Inertia), 기구부 마찰, 이송 시 가감속 지연 등 <strong>장비 특유의 기계적 이상 현상</strong>을 파악하지 못했습니다:
    </p>
    <ul style="margin: 0 0 1.2rem 0; padding-left: 1.4rem; font-size: 0.93rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      <li><strong>X축·Z축 위치 오버슈팅 현상</strong>: AI가 작성해 준 단순 좌표 이동 지령 코드로는 모터가 목표 좌표에 정확히 멈추지 못하고, 물리적 관성으로 인해 목표점을 지나쳐버리는 <strong>오버슈팅(Overshooting) 현상</strong>이 지속적으로 발생했습니다.</li>
      <li><strong>웨이퍼 파손 위험</strong>: 웨이퍼를 핸들링하는 로봇은 1~2mm의 미세한 위치 오차로도 카세트(FOUP) 슬롯이나 챔버 기구부와 충돌하여 웨이퍼가 파손될 수 있는 치명적인 위험이 있었습니다.</li>
    </ul>

    <h3 style="margin: 1.4rem 0 0.5rem 0; font-size: 1.15rem; color: #0078d7;">
      3. 해결 방안: 하드웨어 동작 정위치 검증 및 제어 보정 로직 직접 설계
    </h3>
    <p style="margin: 0 0 0.8rem 0; font-size: 0.95rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      결국 기계 장비 제어의 핵심은 '물리 현상을 제어하는 엔지니어의 로직'에 있음을 깨닫고, <strong>실제 장비가 확실하게 정위치(In-Position)를 잡도록 제어 보정 로직을 소프트웨어에 직접 구현</strong>했습니다:
    </p>
    <ul style="margin: 0; padding-left: 1.4rem; font-size: 0.93rem; line-height: 1.7; opacity: 0.9; color: var(--text-color);">
      <li><strong>인포지션(In-Position) 도달 확인 로직 추가</strong>: 단순히 이동 명령 후 시간을 지연(Sleep)시키는 방식 대신, 서보 드라이브의 실제 엔코더 피드백 위치와 인포지션 신호를 실시간 모니터링하여 목표 위치 오차 범위 내에 완벽히 정지했음을 확인한 뒤에만 다음 동작(웨이퍼 픽업, 도어 닫힘 등)을 수행하도록 인터록을 강화했습니다.</li>
      <li><strong>서보모터 티칭값(Teaching Data) 및 가감속 미세 튜닝</strong>: 물리적 오버슈팅을 상쇄할 수 있도록 감속 시작 위치와 티칭 좌표값을 실측 기반으로 미세 보정했습니다.</li>
      <li><strong>성과 및 결론</strong>: X축과 Z축이 충돌이나 덜컹거림 없이 부드럽고 정확하게 정위치에 안착하도록 완성하였으며, 시연 영상에서 보듯 100% 안정적인 웨이퍼 이송 시퀀스를 구현해 냈습니다. <em>"AI는 코딩 속도를 높여주는 강력한 도구이지만, 최종적으로 현장 물리 장비를 안정화하는 것은 기계적 특성을 이해하고 보정하는 엔지니어의 몫"</em>이라는 값진 실무 교훈을 얻었습니다.</li>
    </ul>

  </div>

</div>

