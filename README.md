# Mooluck AI

**KDT 독거 노인을 위한 무럭이 서비스,** <strong>Mooluck</strong>입니다.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1774a899-69f2-4193-9fb2-8f7bea9867a6" width="300" height="300" />
</p>

---

<h2 align="center">💻 프로젝트 팀 소개 💻</h2>

<table align="center">
  <tr height="160px">
    <td align="center" width="150px">
      <a href="https://github.com/cheonghaa">
        <img src="https://avatars.githubusercontent.com/u/148474216?v=4" height="130px" width="130px" />
        <br />
        <strong>이도윤</strong><br />
        <span>팀장(PM), Open AI 연동</span>
      </a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/heodoong">
        <img src="https://avatars.githubusercontent.com/u/170384564?v=4" height="130px" width="130px" />
        <br />
        <strong>서수호</strong><br />
        <span>프론트엔드 설계, 연구 자료 조사</span>
      </a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/kogunwoo">
        <img src="https://avatars.githubusercontent.com/u/113786196?v=4" height="130px" width="130px" />
        <br />
        <strong>고건우</strong><br />
        <span>백엔드 설계, API 통합 연동</span>
      </a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/YooSeokHwan">
        <img src="https://avatars.githubusercontent.com/u/170384539?v=4" height="130px" width="130px" />
        <br />
        <strong>유석환</strong><br />
        <span>DB 설계 및 데이터 시각화, GitHub 관리</span>
      </a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/yeonsoo1010">
        <img src="https://avatars.githubusercontent.com/u/128021464?v=4" height="130px" width="130px" />
        <br />
        <strong>조연수</strong><br />
        <span>UI/UX 디자인, 반응 애니메이션 및 인터랙션</span>
      </a>
    </td>
    <td align="center" width="150px">
      <a href="https://github.com/wpfkf4644">
        <img src="https://avatars.githubusercontent.com/u/170283983?v=4" height="130px" width="130px" />
        <br />
        <strong>안젤라</strong><br />
        <span>인증 및 보안 시스템 개발, 서버 인프라 구축</span>
      </a>
    </td>
  </tr>
</table>

---

<h1 align="center">🛠️ 개발 가이드 🛠️</h1>

---

### 📌 Branch 전략 및 커밋 규칙
프로젝트의 원활한 협업을 위해 아래 규칙을 준수하여 개발합니다.

---

### 🌱 개발, 커밋, 푸쉬
- **커밋 메시지를 명확하게 작성**하고 의미를 전달할 수 있도록 합니다.
- 원격지 브랜치로 **수시로 push**하여, 항상 작업 진행 상황을 동료가 확인할 수 있도록 합니다.

--- 
### ✏️ 커밋 메시지 규칙
커밋 메시지의 명확한 구분을 위해 다음 규칙을 준수합니다.
```
Feat: 새로운 기능 추가
Fix: 버그 수정
Docs: 문서 수정
Style: 코드 포맷팅, 세미콜론 누락 등 코드 변경이 없는 경우
Refactor: 코드 리팩토링
Test: 테스트 코드 추가 또는 리팩토링
Chore: 패키지 매니저 수정, 기타 변경
Design: CSS 등 UI 디자인 변경
Comment: 주석 추가 및 변경
Rename: 파일 또는 폴더 이름 변경
Remove: 파일 삭제
!BreakingChange: 커다란 API 변경
!HotFix: 치명적인 버그 긴급 수정
```
### 🔄 PR (Pull Request) 생성
- **피드백이나 도움이 필요할 때**, 또는 **merge 준비가 완료되었을 때**는 Pull Request를 생성합니다.
  - Pull Request는 코드 리뷰를 위한 시스템으로, 협업의 품질을 높이는 데 필수입니다.
  - **merge 준비 완료 시** `dev` 브랜치로 반영합니다.
  - 최종적으로 `dev`를 `master`에 반영하여 업데이트합니다.
    
### 📥 PR 예시 (Pull Request Example)
- **PR 제목 형식** : `[날짜]-[이름]-[기능] [작업 내용]`
 
 ```
  2024-11-06 유무럭 로그인 기능 추가
  2024-11-06 유무럭 목표 자산 조회 기능 CSS 수정
 ```

### 🚀 배포 방법
- `master`로 **merge가 일어나면 자동으로 배포**가 이루어지도록 설정(CI/CD).
- `master` 브랜치는 항상 최신 상태를 유지해야 합니다.

---

### 📚 참고 자료
[hyunjun.kr](https://hyunjun.kr/21)


