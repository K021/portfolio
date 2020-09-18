
# 프로젝트 정리

## 규모가 있는 기타 프로젝트

### 하나대투 API Python module

서강대 수학과 교수님이 주식의 실시간 데이터가 필요하다고 하셔서 만든 모듈. 하나대투의 불편한 API를 간단하게 사용할 수 있게 해준다. 

- 저장소: https://github.com/K021/hana
- 작업 시기: 2018년 11월
- 진행 상태: 완료
- 구현된 기능:
	- 실시간 주식, 선물, 옵션의 거래 데이터를 틱 단위로 수신하여 엑셀 또는 텍스트 파일로 저장
	- 실시간 주식, 선물, 옵션 주문
- 사용된 기술: Python

### UWB 기반 실시간 측위 알고리즘

- 자율주행 로봇을 만드는 오딘로보틱스라는 회사에서 일하면서 개발한 알고리즘으로, 1개의 수신기에서 3개의 송신기의 신호를 받아서 삼변측량으로 수신기의 위치를 특정하는 알고리즘입니다.
- UWB 는 Ultra Wide Band 의 약자로, 초광대역 주파수 대역을 말합니다. 이 대역의 신호는 회절성이 좋아 장애물이 많은 곳에서도 거리 측정 오차가 적기 때문에 로봇의 위치를 측정하는 데 사용됩니다. 
- UWB trilateration 관련 논문 여러 개를 뒤져서 찾아낸 3 가지 알고리즘을, OpenGL 을 사용하여 시뮬레이션을 돌려 가장 정확도가 높은 알고리즘을 찾았습니다. 
- 그 결과, 기존 연구실에서 석사 과정 학생이 진행하던 연구 결과는 90% 확률로 90cm 이내의 정확도였지만, 제가 만든 알고리즘은 그 오차를 30cm 이내로 낮추었습니다. 
- 저장소: 없음. (해당 알고리즘은 (주)오딘로보틱스에 소유권이 있기 때문에 공개할 수 없습니다.)
- 작업 시기: 2019년 7-8월
- 진행 상태: 완료
- 사용된 기술: C++


### 한국어 감성 분석 프로젝트

현재 졸업 프로젝트로 진행하는 프로젝트로, 네이버 영화평 데이터인 NSMC 의 분석 정확도를 91% 이상으로 높이는 프로젝트입니다.

- 저장소: https://drive.google.com/drive/folders/1LjOChcyCZQk5s5sk06sqRbpVIKVeB6FT?usp=sharing
- 작업 시기: 2020년 7월 ~ 진행 중
- 현재 성능: Electra base 모델 기반, 3 에폭 모델 기준 91.4% 정확도
- 사용된 기술: Electra, Pytorch, Python


### 마크업 언어, Xenmark

피디젠 홈페이지의 문서를 자유롭게 작성할 수 있도록 도와주는 일종의 마크업 언어인 Xenmark 를 개발하였다.

- 저장소: https://github.com/K021/pdxen-homepage (pdxen homepage 프로젝트에 포함, 현재 private 상태가 볼 수 없습니다.)
- 프로젝트 안내문: 
	- 국문: [Xenmark: 피디젠 홈페이지를 위한 마크업 언어](./xenmark-ko-pub.md)
	- 영문: [Xenmark: a markup language for Pdxen](./xenmark-en-pub.md)


## 규모가 있는 웹앱 프로젝트

### Pdxen Homepage

(주)피디젠에서 근무하며 만든 홈페이지로, 저 혼자 프론트와 백엔드 전부 작업하였습니다. 간단한 웹앱이기 때문에 api 형태가 아닌 장고만으로 프론트 백엔드 모두 작업하였습니다. 

- 저장소: https://github.com/K021/pdxen-homepage (현재 private 상태가 볼 수 없습니다.)
- 프로젝트 안내문: [(주)피디젠 홈페이지](./pdxenhomepage-pub.md)
 	- English version: [Xenmark: a markup language for Pdxen](./xenmark-en-pub.md)
- 개괄: 기업과 그 서비스를 소개하고, 문의하기 기능을 통해 바이어들이 쉽게 연락할 수 있는 회사 홈페이지 
- 작업 시기: 2018년 2월
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

### Audmix Project

Backend 2명, ios 1명, Android 2명 총 5명이 작업한 프로젝트로, API 형태로 구현되었으며, 저는 Backend 의 유저와 포스트 부분을 맡았습니다. 

- 저장소: https://github.com/K021/Audiomix-project
- 프로젝트 안내문: [Soundhub: 음악 오픈 프로듀싱 플랫폼](./team-project-soundhub-pub.md)
- 개괄: 음악을 좋아하는 사람들이 음원을 올리고, 악기별 트랙을 쉽게 믹스할 수 있게 해주는 프로젝트. 
- 작업 시기: 2017년 12월
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


## 성구 검색 프로그램

### Search Bible 2.0

제가 필요해서 만든, 콘솔 입출력으로 작동하는 성구 검색 프로그램입니다. 

- 저장소: https://github.com/K021/search_bible
- 사용된 기술: python
- 작업 시기: 2017년 9월 
- 진행 상태: 완료
- 구현된 기능: 
	1. 한글 성경 검색, 영어 성경 검색
	2. `+` 검색과 `-` 검색이 가능
	3. 한글 성경과 영어 성경을 구절 별로 함께 출력 가능

### Search Bible Online

Django 를 활용해, 성구 검색 프로그램을 웹 프로그램으로 만들어서 어디서든지 고급 검색이 가능하게 하려는 프로젝트

- 저장소: https://github.com/K021/SearchBibleOnline
- 사용된 기술: python, Django
- 작업 시기: 2018 년 6월
- 진행 상태: 일시 중지
- 구현된 기능: 
	1. 원래 텍스트 파일에서 읽어오던 성경 구절을 권, 장, 절 단위로 데이터베이스화
	2. and, or, not 검색

## 공부용 웹앱 프로젝트

### Instagram

인스타그램 클론 코딩 프로젝트로, 장고를 연습하기 위해 만든 프로젝트입니다.

- 저장소: https://github.com/K021/instagram
- 프로젝트 안내문: [사진 블로그: Instagram Project](./instagram-pj-pub.md)
- 작업 시기: 2017년 11월 경
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
- 사용된 기술
	- django, aws EB, aws S3, nginx, celery, docker, postgresql 등

### Todo-management 웹앱

할일을 작성하고, 우선순위에 따라 나열하고, 완료 처리를 할 수 있는 기본적인 앱을 웹으로 구현해보았습니다.

- 저장소: https://github.com/K021/todo-management
- 프로젝트 안내문: [할일 정리 웹앱 안내문](https://github.com/K021/todo-management/blob/master/README.md)
- 작업 시기: 2018년 11월 경
- 진행 상태: 완료
- 구현된 기능: 
	1. 할일 작성, post
	2. 작성한 할일 detale page
	3. 할일 변경
	4. 할일 삭제
	5. 할일 우선 순위에 따라 정렬
	6. 할일 우선 순위 변경
	7. 할일의 기한이 다가오면 1시간 단위로 알림 메일 발성

### React 로 만든 위자드 앱 Frontend Demo 프로그램

위자드 앱의 데모 프로그램을 제작하려는 스타트업에게, 이런 식으로 제작할 수 있음을 보여주기 위한 영상입니다.

- 저장소: https://github.com/K021/aml-frontend-react
- 사용 기술: javascript, react, bootstrap4
- 시연 영상: https://youtu.be/mHyLJKtt4zM
- 작업 시기: 2018년 12월
- 진행 상태: 완료

### Orange: Organized Random Team Generator

교회 청년부에서, 소그룹 팀을 짜기 위해 만들었습니다. 모두가 잘 섞이기 위해 무작위로 선정된 팀이 필요한데, 또 너무 랜덤하면 문제가 생겼습니다. 남자나 여자가 한쪽으로 쏠려도 문제고, 나이가 많고 적은 정도가 쏠려도 문제고, 친한사람들만 있어도, 안 친한 사람들만 있어도 문제입니다. 이러한 문제를 해결하기 위해, 특정 조건의 균형을 유지한 채로 랜덤한 조함을 찾는 프로젝트입니다.

- 저장소: https://github.com/K021/Orange/tree/master/orange
- 진행 상태: 진행중


## Crawler Project

크롤링이 간단하다보니, 필요할 때마다 심심풀이로 만들게되었습니다.

- 저장소: https://github.com/K021/crawler
- 사용된 기술: python
- 작업 시기: 2017 ~ 2018년
- 진행 상태: 완료
- 하위 프로젝트
	- Naver Webtoon Crawler
	- Youtube Crawler
	- Teachable Cite Crawler: 인터넷 강의 사이트를 쉽게 만들어주는 Teachable 을 기반으로 한 사이트들의 영상을 크롤
	- Keepbible Cite Crawler: 성구 검색 프로그램 제작을 위해 성경 전체 크롤링


## HTML, CSS, SCSS 공부용 프로젝트

### Photoblog
- 저장소: https://github.com/K021/sample_photo_blog
- 설명: 하나의 단일 html 페이지로 이루어져 있으며, SCSS 로 CSS 를 짰습니다.
- 작업 시기: 2017년 9월 경

### Dabang
- 저장소: https://github.com/K021/dabang
- 설명: 그 당시 다방의 홈페이지와 똑같이 기능하도록 만든 한 페이지 html 프로젝트입니다. 하나의 단일 html 페이지로 이루어져 있으며, SCSS 로 CSS 를 짰습니다.
- 작업 시기: 2017년 9월 경



# 사용할 수 있는 기술 스택

##### 사용 수준 분류
- 관심 (&#9733;&#9734;&#9734;&#9734;): 코드를 읽을 수 있으며, 책을 참고하여 약간의 수정작업 또는 작은 변경사항 추가를 할 수 있음
- 활용 (&#9733;&#9733;&#9734;&#9734;): 시스템 동작 방식을 알고 있으며, 기본적인 기능을 구현할 수 있음
- 능숙 (&#9733;&#9733;&#9733;&#9734;): 시스템에 대한 이해가 깊고, 고급 기능을 사용할 수 있음.
- 전문 (&#9733;&#9733;&#9733;&#9733;): 주요 이슈 트러블 슈팅을 할 수 있을 정도로 내부 구조에 대해 이해하고 있으며, 오픈소스의 경우 커밋을 할수 있을 정도의 수준

##### 사용가능한 기술 스택과 그 수준
- `HTML`&#9733;&#9733;&#9733;&#9734;, `CSS`&#9733;&#9733;&#9734;&#9734;, `Sass`&#9733;&#9733;&#9734;&#9734;
- `Git`&#9733;&#9733;&#9733;&#9734;, `Gitbook`&#9733;&#9733;&#9733;&#9734;
- `C`&#9733;&#9733;&#9733;&#9734;, `C++`&#9733;&#9733;&#9733;&#9734;, `javascript`&#9733;&#9734;&#9734;&#9734;, `Python`&#9733;&#9733;&#9733;&#9734;
- `Django`&#9733;&#9733;&#9733;&#9734;
- `Celery`&#9733;&#9733;&#9734;&#9734;
- `AWS EC2`&#9733;&#9733;&#9734;&#9734;, `AWS ElasticBeanstalk`&#9733;&#9733;&#9734;&#9734;, `AWS RDS`&#9733;&#9733;&#9734;&#9734;, `AWS S2`&#9733;&#9733;&#9734;&#9734;
- `Postgresql`&#9733;&#9733;&#9734;&#9734;, `Sqlite`&#9733;&#9733;&#9734;&#9734;
- `Docker`&#9733;&#9733;&#9733;&#9734;
- `Sentry`&#9733;&#9733;&#9734;&#9734;
- `Travice CI`&#9733;&#9733;&#9734;&#9734;

##### 사용가능 스택의 수준별 분류
- 관심 (&#9733;&#9734;&#9734;&#9734;):
	- `Pytorch`
- 활용 (&#9733;&#9733;&#9734;&#9734;):
	- `CSS`, `Sass`
	- `javascript`
	- `AWS EC2, EB, S3, RDS`
	- `Postgresql`, `Sqlite`
	- `Docker`
	- `Celery`, `Sentry`, `Travice CI`
- 능숙 (&#9733;&#9733;&#9733;&#9734;):
	- `HTML`
	- `git`, `Gitbook`
	- `Python`, `C`, `C++`
	- `Django`
- 전문 (&#9733;&#9733;&#9733;&#9733;):

# 주제별 공부한 내용 정리

## AWS
- [AWS 배포하기](./aws-deploy-pub.md)
- [AWS EC2 로 배포하기](aws-deploy-ec2-pub.md)

## Bootstrap
- [bootstrap4](bootstrap4-pub.md)

## Django
- [Django 기초](django-basic.md)
- [Django 빠른 개발 매뉴얼](django-onestep-manual.md)
- [Django 심화](django-advanced.01.md)
- [Django DateTime](python-datetime-with-django.md)
- [Django REST framwork](django-rest-framwork.md)
- [Django Migration 초기값에 관하여](django-initial-data.md)
- [Django Test 공식 문서 번역](django-test-doc-master.md)
- [Django Test Tools 공식 문서 번역](django-test-doc-testing-tools.md)
- [Pytest 로 Django 테스트하기](django-test-pytest.md)
- [Celery 를 통한 비동기 처리](celery.md)

## Python
- [Python 기초](python-basic.md)
- [Python 심화](python-etc.md)
- [Python 파일 처리](python-file.md)
- [Python 으로 크롤링하기](crawler.md)
- [Python 으로 Youtube 크롤링 하기](python-youtube.md)
- [Python iterator](python-iter.md)
- [Pythonic 한 코드란 무엇인가](python-pythonic-code.md)
- [노마드코더 영상 크롤링](crawling-nomad.md)
- [Python 강의 준비 자료](lecture-python.md)
- [Pyenv, pip 명령어 정리](pyenv-pip-python-commands.md)

## R
- [R 기초](r.md)

## Docker
- [도커 사용하기](docker.md)

## Database
- [Database Transaction](database-transaction.md)

## javascript
- [javascript 핵심 정리](js.md)
- [javascript 개발 환경 설정](js-dev-env-setting.md)
- [javascript 중요 모듈 설명](js-module.md)
- [Node.js 로 Instagram 클론하기 - 노마드코더 강의 정리](nomadcoders-instaclone-with-nodejs.md)

## React
- [Instragram 클론 강의 - React - 노마드코더 강의 정리](react-nomad-insta.md)
- [노마드 코더 리액트 강의](react-nomad.md)
- [빠른 개발을 위한 리액트 매뉴얼](react-routine.md)

## Git
- [git](./git-pub.md)
- [remote-repository-stale-branch-delete](remote-repository-stale-branch-delete.md)

## 기타
- [깃헙 페이지로 디벨로그 만들기](develog-with-github-pages.md)
- [on_air_memo](on_air_memo.md)
- [HTML & CSS](./html-css-pub.md)
- [SASS](sass.md)
- [소켓통신이란](socket.md)
- [Hana 증권 API 를 이용해 실시간 증권 데이터 가져오기](stock-data-on-air.md)
- [다양한 문제 해결 1](temp02.md)- [다양한 문제 해결 2](temp03.md)
- [다양한 문제 해결 3](temp04.md)- [다양한 문제 해결 4](temp05.md)



# 기타

## 알고리즘 대회

- [2019 KAKAO BLIND RECRUITMENT 2차 시험 진출](https://programmers.co.kr/competitions/79/2019-2nd-kakao-blind-recruitment)
- [이데일리 Coding Challenge 2018 본선 진출](https://coding.edaily.co.kr/schedule/schedule.php)
- [2018 Winter Coding - 겨울 스타트업 인턴 프로그램](https://programmers.co.kr/competitions/86/2018%20Winter%20Coding%20겨울%20스타트업%20인턴%20프로그램)

## 알고리즘 공부 내용

&mdash; <cite>업데이트 예정</cite> 


## 추가적으로 정리 할 것들
- audmix [gitbook](https://nachwon.gitbooks.io/soundhub/content/) 올리기
