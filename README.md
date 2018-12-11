
## Project Document in English

- [Xenmark: a markup language for Pdxen](./xenmark-en-pub.md)

## 프로젝트

### Audmix Project

Backend 2명, ios 1명, Android 2명 총 5명이 작업한 프로젝트로, API 형태로 구현되었으며, 저는 Backend 의 유저와 포스트 부분을 맡았습니다. 

- 저장소: https://github.com/K021/Audiomix-project
- 프로젝트 안내문: [Soundhub: 음악 오픈 프로듀싱 플랫폼](./team-project-soundhub-pub.md)
	- English version: [Xenmark: a markup language for Pdxen](./xenmark-en-pub.md)
- 개괄: 음악을 좋아하는 사람들이 음원을 올리고, 악기별 트랙을 쉽게 믹스할 수 있게 해주는 프로젝트. 
- 진행 상태: 완료
- 구현된 기능
	1. 유저 관리
		1. 회원가입, 로그인, 로그아웃 (소셜로그인, 이메일 인증)
		2. 회원정보 수정, 회원 탈퇴
	2. 유저간 상호작용
		1. 팔로우
		2. 메세지
	3. 핵심 서비스
		1. 악기 트랙을 올리는 Post 작성, 수정, 삭제
		2. Post 좋아요 토글
		3. Post 에 어울리는 악기 트랙을 올리는 Comment 작성, 수정, 삭제
		4. 트랙 믹스  
	4. 기타
		1. 메일 보내기 (비동기 처리)
		2. 유저, 포스트 검색
- 사용된 기술
	- django, aws EB, aws S3, nginx, celery, docker, postgresql 등


### Pdxen Homepage

(주)피디젠에서 근무하며 만든 홈페이지로, 저 혼자 프론트와 백엔드 전부 작업하였습니다. 간단한 웹앱이기 때문에 api 형태가 아닌 장고만으로 프론트 백엔드 모두 작업하였습니다. 

- 저장소: https://github.com/K021/pdxen-homepage (현재 private 상태가 볼 수 없습니다.)
- 프로젝트 안내문: [(주)피디젠 홈페이지](./pdxenhomepage-pub.md)
- 개괄: 기업과 그 서비스를 소개하고, 문의하기 기능을 통해 바이어들이 쉽게 연락할 수 있는 회사 홈페이지 
- 진행 상태: 완료
- 구현된 기능
	1. 메인 페이지: 스타트업 느낌의 메인페이지 디자인
	2. about, products, services 페이지를 통해 회사와 회사의 서비스 소개
	3. contacts 페이지를 통한 메일 보내기 기능
	4. signup 및 login 기능
	5. editor 페이지에서 xenmark 를 통한 편집 기능
		- 마케팅 팀이 홈페이지를 관리할 필요가 있어서, 피디젠 홈페이지에 적합한 markup 언어를 만들었다. 
	6. 모바일 반응형 페이지
- 사용된 기술
	- django, aws EC2, nginx, celery, docker, Bootstrap4 등


### Instagram

인스타그램 클론 코딩 프로젝트로, 장고를 연습하기 위해 만든 프로젝트입니다.

- 저장소: https://github.com/K021/instagram
- 프로젝트 안내문: [사진 블로그: Instagram Project](./instagram-pj-pub.md)
- 진행 상태: 완료
- 구현된 기능:
	1. 로그인, 회원가입, 소셜로그인(Facebook)
	2. Post 와 Comment 모델의 연결
		- 사진 업로드
		- 삭제 (Post 작성자만 삭제 가능, DB에서 지우는 것이 아닌 연결을 끊는 것)
		- 댓글 작성 및 삭제
		- post list 페이지와 detail 페이지
	3. 좋아요 기능
	4. 팔로우 기능
	5. 유저 프로필 페이지, 수정 가능

&mdash; <cite>아래 항목 업데이트 예정</cite> 


### Crawler Project

크롤링이 간단하다보니, 필요할 때마다 심심풀이로 만들게되었습니다.

- 저장소: https://github.com/K021/crawler
- 프로젝트 안내문: [크롤러: 웹툰, 유튜브, teachable cite]()
- 진행 상태: 진행중
- 하위 프로젝트
	- Naver Webtoon Crawler
	- Youtube Crawler
	- Teachable Cite Crawler
	- Keepbible Cite Crawler


### Orange: Organized Random Team Generator

교회 청년부에서, 소그룹 팀을 짜기 위해 만들었습니다. 모두가 잘 섞이기 위해 무작위로 선정된 팀이 필요한데, 또 너무 랜덤하면 문제가 생겼습니다. 남자나 여자가 한쪽으로 쏠려도 문제고, 나이가 많고 적은 정도가 쏠려도 문제고, 친한사람들만 있어도, 안 친한 사람들만 있어도 문제입니다. 따라서 특정 조건의 균형을 유지한 채로 랜덤한 조함을 찾을 필요가 생겼습니다. 

- 저장소: https://github.com/K021/Orange/tree/master/orange
- 프로젝트 안내문: [Organized Random Team Generator]()
- 진행 상태: 진행중


### Search Bible Online

개인적으로 성경 구절을 검색할 일이 많은데, 버전간 비교 검색이나, 고급 검색을 지원하는 웹페이지가 존재하지 않습니다. 그래서 만들었습니다. 언제 어디서나 성경을 '고급 검색'할 수 있는 프로그램.

- 저장소: https://github.com/K021/SearchBibleOnline 
- 프로젝트 안내문: [Search Bible Online]()
- 진행 상태: 진행중


### 하나대투 API Python module

서강대 수학과 교수님이 주식의 실시간 데이터가 필요하다고 하셔서 만드는 모듈. 하나대투의 불편한 API를 간단하게 사용할 수 있게 해준다.

- 저장소: 아직 없음
- 프로젝트 안내문: [하나대투 api 파이썬 모듈]()
- 진행 상태: 진행중


## 사용할 수 있는 기술 스택

##### 사용 수준 분류
- 관심 (&#9733;&#9734;&#9734;&#9734;): 코드를 읽을 수 있으며, 책을 참고하여 약간의 수정작업 또는 작은 변경사항 추가를 할 수 있음
- 활용 (&#9733;&#9733;&#9734;&#9734;): 시스템 동작 방식을 알고 있으며, 기본적인 기능을 구현할 수 있음
- 능숙 (&#9733;&#9733;&#9733;&#9734;): 시스템에 대한 이해가 깊고, 고급 기능을 사용할 수 있음.
- 전문 (&#9733;&#9733;&#9733;&#9733;): 주요 이슈 트러블 슈팅을 할 수 있을 정도로 내부 구조에 대해 이해하고 있으며, 오픈소스의 경우 커밋을 할수 있을 정도의 수준

##### 사용가능한 기술 스택과 그 수준
- `HTML`&#9733;&#9733;&#9733;&#9734;, `CSS`&#9733;&#9733;&#9734;&#9734;, `Sass`&#9733;&#9733;&#9734;&#9734;
- `Git`&#9733;&#9733;&#9733;&#9734;, `Gitbook`&#9733;&#9733;&#9733;&#9734;
- `C`&#9733;&#9733;&#9734;&#9734;, `Python`&#9733;&#9733;&#9733;&#9734;
- `Django`&#9733;&#9733;&#9733;&#9734;
- `Celery`&#9733;&#9733;&#9734;&#9734;
- `AWS EC2`&#9733;&#9733;&#9734;&#9734;, `AWS ElasticBeanstalk`&#9733;&#9733;&#9734;&#9734;, `AWS RDS`&#9733;&#9733;&#9734;&#9734;, `AWS S2`&#9733;&#9733;&#9734;&#9734;
- `Postgresql`&#9733;&#9733;&#9734;&#9734;, `Sqlite`&#9733;&#9733;&#9734;&#9734;
- `Docker`&#9733;&#9733;&#9733;&#9734;
- `Sentry`&#9733;&#9733;&#9734;&#9734;
- `Travice CI`&#9733;&#9733;&#9734;&#9734;

##### 사용가능 스택의 수준별 분류
- 관심 (&#9733;&#9734;&#9734;&#9734;):
- 활용 (&#9733;&#9733;&#9734;&#9734;):
	- `CSS`, `Sass`
	- `C`
	- `AWS EC2, EB, S3, RDS`
	- `Postgresql`, `Sqlite`
	- `Docker`
	- `Celery`, `Sentry`, `Travice CI`
- 능숙 (&#9733;&#9733;&#9733;&#9734;):
	- `HTML`
	- `git`, `Gitbook`
	- `Python`
	- `Django`
- 전문 (&#9733;&#9733;&#9733;&#9733;):

## 주제별 공부한 내용 정리

* [git](./git-pub.md)
* [html&css](./html-css-pub.md)
* [javascript](./javascript-pub.md)
* [django_basic](./django-basic-pub.md)
* [aws_deploy](./aws-deploy-pub.md)
* [docker](docker-pub.md)

## 알고리즘 대회

- [2019 KAKAO BLIND RECRUITMENT 2차 시험 진출](https://programmers.co.kr/competitions/79/2019-2nd-kakao-blind-recruitment)
- [이데일리 Coding Challenge 2018 본선 진출](https://coding.edaily.co.kr/schedule/schedule.php)
- [2018 Winter Coding - 겨울 스타트업 인턴 프로그램](https://programmers.co.kr/competitions/86/2018%20Winter%20Coding%20겨울%20스타트업%20인턴%20프로그램)

## 알고리즘 공부 내용

&mdash; <cite>업데이트 예정</cite> 


## 추가적으로 정리 할 것들
- audmix [gitbook](https://nachwon.gitbooks.io/soundhub/content/) 올리기
