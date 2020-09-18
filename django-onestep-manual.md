<h1 class="header"><span>Django Onestep Manual</span></h1> 



# Django 개발 환경 설정 

##### 프로젝트 디렉토리 생성: 
`python/django/prj_djgirls`  

##### pyenv 가상환경 생성: 
`pyenv virtualenv 3.6.2 fc-djgirls`  

##### pyenv 가상환경 적용: 
`pyenv local fc-djgirls`  

##### git 환경설정: 
`git init`, `vim .gitignore`, Github 저장소 연결  

> `git remote -v`: 저장소의 단축 이름과 url을 볼 수 있다.  
`git remote add <저장소단축이름> <url>`: 디렉토리에 리모트 저장소 추가 

##### django 설치 (pyenv상):  
`pip install django`  
`pip freeze > requirements.txt`: 현재 설치 패키지 정보를 저장  
`pip install -r requirements.txt`: 저장된 패키지를 해당 버전으로 설치  
`python 3.6.2`: 파이썬 버전 정보는 README.md 파일에 작성해준다  

##### pycharm interpreter 설정: 
- 프로젝트 폴더 열어서 intrpreter 설정  
- `preferences` &rarr; `project` &rarr; `project interpreter` &rarr; `설정 버튼 add` &rarr; `/usr/local/var/pyenv/versions/pyenv가상환경이름/bin/python` 설정  

##### Django start project
- `django-admin startproject djgirls`: djgirls 폴더 두 개를 djgirls/djgirls의 형태로 생성한다. 상위 폴더는 애플리케이션 폴더로, manage.py를 갖고 있다. 하위 폴더는 세 가지의 설정모듈을 가는 package 폴더이다.  
- 혼란을 방지하기 위해 설정모듈 패키지(하위 django 폴더)의 이름을 config로 변경하자. 이때,하위 설정 모듈에서 해당 패키지명을 사용중이므로, pycharm을 사용해 바꾸자. `pycharm/패키지폴더우클릭/Refactor(두 옵션 모두 선택)`으로 한 번에 바꿔버리자. 이때, comments, string 모두 변경하도록 옵션을 클릭해줘야 한다. 하위 설정 파일 모듈명을 모두 string으로 작성해두었기 때문이다. (자세한 파일구조 하단 참조)
- **pycharm 소스 루트 설정**: pycharm은 열려있는 가장 상위 폴더인 프로젝트 폴더를 루트 폴더라고 인식한다. 따라서 애플리케이션 폴더는 패키지로 인식하게 되는데, 이를 막기 위해 루트폴더 지정이 필요하다. `djgirls(App.folder)우클릭/Mark Directory as/Sources Root`

##### Django Support 켜기: 
- `설정` &rarr; `Languages & Framworks` &rarr; `Django` &rarr; `Enable Djnago Suport` 선택
- Django project root: 프로젝트 최상위 폴더
- Settings: 설정 파일 (위 설정을 하고 진행해야 오류가 안 난다)
- Manage script: manage.py 파일

##### 터미널 장고 관리 환경
`pip install ipython django_extensions`  
`settings.py/INSTALLED_APPS에 django_extensions를 설치`: 이때, 반드시 끝에 ,를 잊지 말고 붙여주자. `./manage.py shell`로 장고 모듈을 불러온 ipython 사용  
`pip freeze > requirements.txt`  


# 장고 앱 제작

##### 애플리케이션 폴더 생성
`django-admin startproject djgirls`: 프로젝트 폴더 위치에서 명령

##### config 모듈 패키지명 변경
`pycharm/패키지폴더우클릭/Refactor(두 옵션 모두 선택)`: Pycharm 의 refactor 기능을 사용해 변경해야 문자열도 변경된다. 

##### pycharm 소스 루트 설정
`애플리케이션 폴더 우클릭/Mark Directory as/Sources Root`

##### django 애플리케이션 패키지 생성
`./manage.py startapp todo`  
`settings.py/INSTALLED_APPS에 'todo'입력`  

##### model 선언

```python
from django.db import models

class Todo(models.Model):
	...
```
  
`models.CharField` - 글 제목처럼 글자 수가 제한된 텍스트를 정의할 때 
`models.TextField` - 글자 수에 제한이 없는 긴 텍스트를 위한 속성
`models.DateTimeField` - 날짜와 시간을 다루는 경우  
`models.ForeignKey` - 다른 모델에 대한 링크  

##### 모델 마이그레이션
`./manage.py makemigrations [앱이름]`: 앱이름을 생략하면 모든 앱을 대상으로 한다.  
`./manage.py migrate [앱이름]`

##### 관리자 페이지 생성
```python
from .models import Post 

admin.site.register(Post)
```