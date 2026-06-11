---
layout: page
title: History
---

# History

<style>
/* 타임라인 왼쪽 선과 검은색 동그라미(노드) 제거 */
.timeline {
  border-left: none !important;
  padding-left: 0 !important;
}
.timeline-item::before {
  display: none !important;
}
</style>

<div class="timeline animated-timeline" style="list-style-type: none;">
  <!-- Item 1 -->
  <div class="timeline-item" style="--delay: 0.1s">
    <span class="timeline-date falling-text">In Progress</span>
    <div class="timeline-content glass-card">
      <h3 class="falling-text">1. 바이브 코딩(Vibe Coding) 및 프로그래밍 기초 역량 강화</h3>
      <ul style="list-style: none; padding-left: 0;">
        <li class="falling-text">프로그래밍 전반에 대한 기초 지식 확립 및 소프트웨어 동작 원리 이해</li>
        <li class="falling-text">생성형 AI 기반의 바이브 코딩 기법을 적용한 신속한 로직 설계 및 구현</li>
        <li class="falling-text">AI 도구를 활용한 효율적인 코드 분석 및 트러블슈팅(문제 해결) 프로세스 경험</li>
        <li class="falling-text">반도체 장비 제어 및 예지보전 관련 실습</li>
      </ul>
    </div>
  </div>

  <!-- Item 2 -->
  <div class="timeline-item" style="--delay: 0.3s">
    <span class="timeline-date falling-text">Past Experience</span>
    <div class="timeline-content glass-card">
      <h3 class="falling-text">2. 소프트웨어 품질 보증 (SQA)</h3>
      <ul style="list-style: none; padding-left: 0;">
        <li class="falling-text">요구사항 분석 기반의 테스트 케이스(Test Case) 설계 및 작성</li>
        <li class="falling-text">QA 프로세스에 따른 테스트 수행 및 결함(Bug) 검증</li>
      </ul>
    </div>
  </div>

  <!-- Item 3 -->
  <div class="timeline-item" style="--delay: 0.5s">
    <span class="timeline-date falling-text">Past Experience</span>
    <div class="timeline-content glass-card">
      <h3 class="falling-text">3. IT 시스템 및 하드웨어 관리</h3>
      <ul style="list-style: none; padding-left: 0;">
        <li class="falling-text">컴퓨터 구조(Architecture)에 대한 이해를 바탕으로 한 시스템 조립 및 초기 세팅</li>
        <li class="falling-text">하드웨어 장애 진단, 부품 교체 등 전반적인 PC 유지보수 지원</li>
      </ul>
    </div>
  </div>
</div>

<style>
/* 한 글자씩 떨어지는 애니메이션을 위한 스타일 */
.char {
  display: inline-block;
  opacity: 0;
  transform: translateY(-20px);
  animation: dropDownChar 0.4s forwards cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes dropDownChar {
  0% {
    opacity: 0;
    transform: translateY(-20px) scale(0.9);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const elements = document.querySelectorAll('.falling-text');
  
  // 빠른 노출을 위해 0초부터 바로 시작
  let currentDelay = 0; 
  
  elements.forEach((el) => {
    const text = el.innerText;
    el.innerHTML = '';
    
    for (let i = 0; i < text.length; i++) {
      const charSpan = document.createElement('span');
      charSpan.className = 'char';
      
      // 띄어쓰기 유지
      if (text[i] === ' ') {
        charSpan.innerHTML = '&nbsp;';
      } else {
        charSpan.innerText = text[i];
      }
      
      // 글자 간격을 0.005초로 확 줄여서 거의 동시에 다다닥 떨어지도록 설정
      charSpan.style.animationDelay = currentDelay + 's';
      currentDelay += 0.005; 
      
      el.appendChild(charSpan);
    }
    
    // 다음 줄 텀도 짧게
    currentDelay += 0.05; 
  });
});
</script>
