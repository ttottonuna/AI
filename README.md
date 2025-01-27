### Mooluck AI

<br>
<div align="center">
  <h1>[ 무럭이 키우기 ] </h1>
  <p>🌱 TTS / STT 기능을 통한 양방향 소통이 가능한 독거노인을 위한 반려식물 서비스 🌱</p>
</div>



## 🌿 Introduction
반려식물 “무럭이”는 단순한 대화 및 터치만을 통해 독거노인께는 정서적 안정을 지원하고, 독거 노인 돌봄 기관 측에서는 이를 통한 상호작용 데이터를 통해 모니터링이 가능하도록 한 B2G 서비스입니다.
<br>
<br>



## ✍️ 프로젝트 개요

- **프로젝트명:** 무럭이 키우기
- **프로젝트 기간:** 2024.09 ~ 2024.11.21 (고도화 기간 : 2024.12.03 ~ 2025.01.23)
- **프로젝트 형태:** 해커톤 참가 프로젝트
- **목표:**
  - 독거노인의 정서적 안정을 위한 반려식물 서비스 지원
  - 돌봄기관 측에 편리하고 빠르게 노인들을 관리할 수 있는 서비스 제공
- **주요 타겟 사용자:** 독거 노인 돌봄 기관 측에서 도입, 실 사용자는 소외된 독거노인 분들을 실타겟층으로 설정

<br>
<br>


## 💻 프로젝트 팀 소개 💻
<div align="center">
<h3> Team | Spring Retriever </h3>
<p>"봄을 되찾는 사람들"이라는 뜻으로, 독거노인 분들의 더 나은 삶, 새로운 삶을 목표로 저희 팀은 함께 달려왔습니다 ! 💥</p>
<br>
</div>

|▪ 이도윤 ▪|▪ 고건우 ▪|▪ 서수호 ▪|▪ 안젤라 ▪|▪ 유석환 ▪|▪ 조연수 ▪|
|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|<img src="https://avatars.githubusercontent.com/u/148474216?v=4" height="130px" width="130px" />|<img src="https://avatars.githubusercontent.com/u/113786196?v=4" height="130px" width="130px" />|<img src="https://avatars.githubusercontent.com/u/170384564?v=4" height="130px" width="130px" />| <img src="https://avatars.githubusercontent.com/u/170283983?v=4" height="130px" width="130px" />|<img src="https://avatars.githubusercontent.com/u/170384539?v=4" height="130px" width="130px" />|<img src="https://avatars.githubusercontent.com/u/128021464?v=4" height="130px" width="130px" />|
팀장 PM<br> 로그인 기능 <br><a href="https://github.com/cheonghaa">@cheonghaa</a>|상호작용 BE <br> AI(TTS/STT) <br><a href="https://github.com/kogunwoo">@kogunwoo </a>|아이디어 기획 <br> 애니메이션 <br><a href="https://github.com/heodoong">@heodoong</a>|AI(TTS/STT) 관리<br> 인프라 설계 <br><a href="https://github.com/ttottonuna">@ttottonuna</a>|DB 관리 <br>인프라 설계 <br><a href="https://github.com/YooSeokhwan">@YooSeokhwan</a>| 날씨 API<br> 관리자 페이지 <br><a href="https://github.com/yeonsoo1010">@yeonsoo1010</a>|
<br>
<br>


## 💬 About Our Service
<div align="center">
  <img width="500" src="https://github.com/user-attachments/assets/23ef9928-d280-48c6-9ce8-9173cc11d3cd" />
  <br>
  <br>
  <p>노인분들의 편리한 사용을 위하여 직관적인 UI/UX로 사용자가 사용에 어려움을 느끼지 않도록 터치 요소와 기능들을 간소화 및 최소화하였습니다.</p>
  <p>또한 복지 기관 관리자분들의 사용성을 고려하여, 관리하고 계시는 노인분들의 상호작용을 한 눈에 알아볼 수 있도록 하였습니다.</p>
<br>
<br>
</div>

**서비스 특징**


1️⃣ STT/TTS를 통한 무럭이와의 양방향 소통 <br>
2️⃣ 정서적 안정을 위한 물주기 기능과 쓰다듬기 기능 <br>
3️⃣ 위치 기반 서비스를 통한 날씨 알려주기 기능<br>
4️⃣ 사용자 정보를 한 눈에 볼 수 있는 관리자 페이지
<br>
<br>

## 📌 주요 기능
### **0. 회원가입 | 로그인**


#### **로그인**
- 가장 첫 화면은 노인 계정 로그인 화면으로, 오른쪽 아래의 "관리자" 버튼을 누르게 될 경우 관리자 로그인 페이지로 넘어가게 됩니다.
- 로그인을 두 가지 페이지로 나눠두었으며 다음과 같이 이동합니다.
    - 일반 사용자 ⇒ 무럭이 페이지
    - 관리자 ⇒ 관리자 페이지

<div align="center">
<img width="500" src="https://github.com/user-attachments/assets/6d4c20bd-5563-449d-8b4d-6fe29e54879e" /><img width="500" src="https://github.com/user-attachments/assets/2ed42fe5-76d6-476d-aab3-1ddd84db8f9d" />
  <p>(첫번째 사진 : 고령자 계정 로그인 페이지 | 두번째 사진 : 관리자 계정 로그인 페이지) </p>
</div>
<br>
<br>



#### **신규 관리자 회원가입**
<div align="center">
<img width="600" src="https://github.com/user-attachments/assets/ba03a155-b2d1-45a2-8a5c-9987caa89154" />
</div>

- 회원가입의 경우 관리자만 신규로 회원가입이 가능하며, 노인 계정의 경우 관리자가 직접 추가 / 입력하는 방식으로 구성하여 노인분들이 직접 회원가입을 하거나 하는 상황을 최소화하도록 하였습니다.

<br>
<br>



### **1. 메인 화면**
<div align="center">
    <img width="600" height="350" src="https://github.com/user-attachments/assets/f51b6fdb-e16d-43fd-af5e-8c750d6de988" />
</div>


- 양방향 소통 가능 : 대화 버튼을 누르면 무럭이와 대화가 가능하며, 위는 실제 무럭이와 대화가 진행되고 있는 장면입니다.
- 날씨 정보 제공 : 위치 기반 서비스를 통해 그 지역의 현재 날씨가 배경으로 나오고 있습니다.
- 물 주기 기능 : 정해진 시간에 맞춰서 화면에 알람이 뜨고, 그 시간에 맞춰 무럭이를 터치하게 될 경우 무럭이에게 물을 줄 수 있으며 관리자 측에서 이 소통 결과가 로그로 쌓이게 됩니다.
- 쓰다듬기 기능 : 지정한 물 주기 시간 이외에 터치하게 될 경우 무럭이를 쓰다듬을 수 있으며, 이 결과 또한 관리자 측에서 로그로 확인할 수 있습니다.



### **2. 관리자 페이지**
<div align="center">
    <img width="600" src="https://github.com/user-attachments/assets/003aae21-585a-4f70-8ebd-0cb652ddbaee" />
</div>



- 관리자 측에서 관리하고 있는 노인분들에 대한 데이터와 로그 확인이 가능합니다.
- 상호작용 횟수
  - 0회: 빨간색으로 '위험' 표시
  - 1회: 주황색으로 '경고' 표시
  - 2회 이상: 초록색으로 '양호' 표시	

#### 관리자 페이지 특징
<div align="center">
<img width="1200" src="https://github.com/user-attachments/assets/53f190af-6404-489c-b28c-29ed70973c13" />
</div>
<br>

## ✔ System Architecture
<div align="center">
  <img width="800" src="https://github.com/user-attachments/assets/f931153e-740a-4388-80b0-e862c70385c5" />
</div>
<br>
<br>

## ✔ ER Diagram
<div align="center">
  <img width="800" src="https://github.com/user-attachments/assets/5f04ac74-6bba-48b2-a5df-9743067a496d" />
</div>
<br>
<br>

## 🛠️ Tech Stacks
<div align="center">
  <img src="https://img.shields.io/badge/Illustrator-654520?style=for-the-badge&logo=adobe-illustrator&logoColor=white" alt="Illustrator"/>
  <img src="https://img.shields.io/badge/Git-EB5B00?style=for-the-badge&logo=Git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" alt="Python"/><br/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/Javascript-FEEC37?style=for-the-badge&logo=Javascript&logoColor=white" alt="Javascript"/>
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=white" alt="Vue.js"/>
  <img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=Java&logoColor=white" alt="Java"/><br/>
  <img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white" alt="Spring"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=Amazon%20S3&logoColor=white" alt="Amazon S3"/>
  <img src="https://img.shields.io/badge/Open%20API-181717?style=for-the-badge&logo=Open%20API&logoColor=white" alt="Open API"/>
</div>
<br>
<br>

## 🙆‍♀️ Collaboration Tool
<div align="center">
  <img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white" alt="Github"/>
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white" alt="Slack"/>
  <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white" alt="Notion"/>
  <img src="https://img.shields.io/badge/Figma-C68FE6?style=for-the-badge&logo=Figma&logoColor=white" alt="Figma"/>
</div>

<br>
<br>
<h2>🛠️ 개발 가이드 🛠️</h2>

### 📌 Branch 전략 및 커밋 규칙
프로젝트의 원활한 협업을 위해 아래 규칙을 준수하여 개발합니다.

### 🌱 개발, 커밋, 푸쉬
- **커밋 메시지를 명확하게 작성**하고 의미를 전달할 수 있도록 합니다.
- 원격지 브랜치로 **수시로 push**하여, 항상 작업 진행 상황을 동료가 확인할 수 있도록 합니다.

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


