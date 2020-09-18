


<h1 class="header"><span>Djangogirls Project 기본 설정</span></h1> 


## 목차

**장고 기본 설정**  
[요약](#장고_요약)  
[개발 환경 설정](#장고_개발_환경_설정)  
[장고 프로젝트 기본 설정](#장고_프로젝트_기본_설정)  

**장고 관리**  
[관리자 페이지 관리](#관리자_페이지_관리)  
[사용자 페이지 관리](#사용자_페이지_관리)  
[기타 설정 변경](#기타_설정_변경)  
[ORM](#ORM)  
[내장함수](#내장함수)  
[Template 언어](#template_언어)  

**기타**  
[Dajango Basic](#django_basic)  
[공부할 것](#공부할_것)  
[질문](#질문)  


<a name='장고_요약'></a>
# Django 기본 설정 요약

### 1. Django 개발환경 설정

* 프로젝트 폴더 생성
* pyenv 가상환경 생성 & 적용
* git 환경설정
* pycharm interpreter 설정
* django 설치 

### 2. Django Project 설정

* 프로젝트 패키지 생성
* 설정 모듈명 변경
* pycharm 루트 폴더 지정
* DB 관리 툴 설치
* 애플리케이션 패키지 만들기
* settings.py에 애플리케이션 패키지 인식시키기
* 모델 만들기
* makemigration
* migrate
* 관리자 페이지에 모듈 등록
* 관리자 계정 생성
* django extensions 



<a name='장고_개발_환경_설정'></a>
# Django 개발 환경 설정 

#### 프로젝트 디렉토리 생성: 
`python/django/prj_djgirls`  

#### pyenv 가상환경 생성: 
`pyenv virtualenv 3.6.2 fc-djgirls`  

#### pyenv 가상환경 적용: 
`pyenv local fc-djgirls`  

#### git 환경설정: 
`git init`, `vim .gitignore`, Github 저장소 연결  

> `git remote -v`: 저장소의 단축 이름과 url을 볼 수 있다.  
`git remote add <저장소단축이름> <url>`: 디렉토리에 리모트 저장소 추가 

#### django 설치 (pyenv상):  
`pip install django`  
`pip freeze > requirements.txt`: 현재 설치 패키지 정보를 저장  
`pip install -r requirements.txt`: 저장된 패키지를 해당 버전으로 설치  
`python 3.6.2`: 파이썬 버전 정보는 README.md 파일에 작성해준다  

#### pycharm interpreter 설정: 
- 프로젝트 폴더 열어서 intrpreter 설정  
- `preferences` &rarr; `project` &rarr; `project interpreter` &rarr; `설정 버튼 add` &rarr; `/usr/local/var/pyenv/versions/pyenv가상환경이름/bin/python` 설정  

#### Django start project
- `django-admin startproject djgirls`: djgirls 폴더 두 개를 djgirls/djgirls의 형태로 생성한다. 상위 폴더는 애플리케이션 폴더로, manage.py를 갖고 있다. 하위 폴더는 세 가지의 설정모듈을 가는 package 폴더이다.  
- 혼란을 방지하기 위해 설정모듈 패키지(하위 django 폴더)의 이름을 config로 변경하자. 이때,하위 설정 모듈에서 해당 패키지명을 사용중이므로, pycharm을 사용해 바꾸자. `pycharm/패키지폴더우클릭/Refactor(두 옵션 모두 선택)`으로 한 번에 바꿔버리자. 이때, comments, string 모두 변경하도록 옵션을 클릭해줘야 한다. 하위 설정 파일 모듈명을 모두 string으로 작성해두었기 때문이다. (자세한 파일구조 하단 참조)
- **pycharm 소스 루트 설정**: pycharm은 열려있는 가장 상위 폴더인 프로젝트 폴더를 루트 폴더라고 인식한다. 따라서 애플리케이션 폴더는 패키지로 인식하게 되는데, 이를 막기 위해 루트폴더 지정이 필요하다. `djgirls(App.folder)우클릭/Mark Directory as/Sources Root`

[refactoring 되는 부분 이미지보기](img/django-basic/config-dir-refactoring.png)

#### Django Support 켜기: 
- `설정` &rarr; `Languages & Framworks` &rarr; `Django` &rarr; `Enable Djnago Suport` 선택
- Django project root: 프로젝트 최상위 폴더
- Settings: 설정 파일 (위 설정을 하고 진행해야 오류가 안 난다)
- Manage script: manage.py 파일



<a name='장고_프로젝트_기본_설정'></a>
# Django Project 기본 설정

## Django project 생성

#### django project 생성

`django-admin startproject djgirls`: djgirls 폴더 두 개를 djgirls/djgirls의 형태로 생성한다. 상위 폴더는 애플리케이션 폴더로, manage.py를 갖고 있다. 하위 폴더는 세 가지의 설정모듈을 가는 package 폴더이다.  

#### djgirls 설정 모듈 패키지명 변경

혼란을 방지하기 위해 설정모듈 패키지(하위 django 폴더)의 이름을 config로 변경하자. 이때,하위 설정 모듈에서 해당 패키지명을 사용중이므로, pycharm을 사용해 바꾸자. `pycharm/패키지폴더우클릭/Refactor(두 옵션 모두 선택)`으로 한 번에 바꿔버리자. 이때, comments, string 모두 변경하도록 옵션을 클릭해줘야 한다. 하위 설정 파일 모듈명을 모두 string으로 작성해두었기 때문이다.  

```python
prj_djgirls # Django project folder
	djgirls # Django application folder
		manage.py 
		djgirls # Django settings folder (package)(이걸 config로 설정)
			__init__
			settings.py
			urls.py
			wsgi.py
```

#### pycharm 소스 루트 설정

pycharm은 열려있는 가장 상위 폴더인 프로젝트 폴더를 루트 폴더라고 인식한다. 따라서 애플리케이션 폴더는 패키지로 인식하게 되는데, 이를 막기 위해 루트폴더 지정이 필요하다. `djgirls(App.folder)우클릭/Mark Directory as/Sources Root`

## DB 관리 툴

#### 데이터베이스 설정하기 (sqlite)

장고에는 sqlite가 내장되어 있다. (settings.py 안의 DATABASE 설정에서 확인할 수 있다)
`./manage.py migrate`: DB 테이블을 만들어준다  
`brew cask install sqlitebrowser`: sqlite browser 설치. 웹 상에서 설치파일을 찾아 설치할 수도 있다.   

## 장고 App 생성

#### 장고 애플리케이션 패키지 만들기
`python manage.py startapp blog` `blog`라는 이름의 `application package`가 `application folder` 안에 생성된다.  

#### 생성한 애플리케이션 패키지 장고에 인식시키기

`settings.py/INSTALLED_APPS에 'blog'입력`  

## 로컬에서 서버 돌리기
`python manage.py runserver``runserver`:장고 내장 서버 이름  


## Model

#### 모델 만들기
 `models.Model`을 상속받아야 한다. 이 상속을 위해서는 `django.db.models`를 import. 이것이 해당 클래스가 장고 모델임을 의미한다.  

- `models.CharField` - 글 제목처럼 글자 수가 제한된 텍스트를 정의할 때 
- `models.TextField` - 글자 수에 제한이 없는 긴 텍스트를 위한 속성
- `models.DateTimeField` - 날짜와 시간을 다루는 경우  
- `models.ForeignKey` - 다른 모델에 대한 링크  

#### 생성된 모델 데이터베이스에 적용

`./manage.py makemigrations blog`: DB 변경 사항 기록. 실제 DB를 변화시키는 것이 아니다. 앞으로 -식으로 변경될 수 있다. -이러한 모델이 생성되었다더라 정도의 느낌이다.

```bash
$ ./manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```
위 알림에 나와있는 `blog/migrations/0001_initial.py`에 가보면 다음과 같은 정보가 입력되어 있다. 어떤 모델이 입력되었는지 저장하되, 그 모델을 DB에 기록하지는 않는 것. 그것이 `makemigrations`이다. 

```python
    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
```
`./manage.py migrate blog`: 변경 사항을 DB에 적용한다. 이제 DB 테이블에서 blog_post 모델을 확인할 수 있다. 모델이 변경될 때마다 `migrate`를 해주어야 변경사항이 적용된다.  

## 관리자 페이지

**관리자 페이지 생성하기**  
`blog/admin.py`: 관리자 페이지를 관리하는 모듈. 이 모듈 안에 다음을 작성해준다.  

```python
# .models는 admin.py와 같은 폴더 안의 models.py를 가리킨다.
# blog.models로 임포트할 수도 있지만, App. package 이름이 변경될 수도 있으므로 상대경로를 추천한다.
from .models import Post 

# 관리자 페이지에 Post 모듈 등록
admin.site.register(Post)
```
**관리자 계정 생성**  
이제 `localhost:8000/admin`으로 접속하면 관리자 페이지 접속 창이 뜬다. 관리자 계정이기 때문에 회원가입 버튼이 없다. `./manage.py createsuperuser`로 관리자 계정을 생성해준다. `sqlite`툴의 `데이터보기/auth_user테이블`을 선택하면 생성된 계정을 볼 수 있다.  

## 터미널에서 장고 관리하기
**django_extensions**  
`pip install ipython django_extensions`: 장고 확장기능 설치. 이것도 장고 애플리케이션이므로 `settings.py/INSTALLED_APPS`에 `django_extensions`를 설치한다. 이때, 반드시 끝에 `,`를 잊지 말고 붙여주자. 이제 `./manage.py shell`로 장고 프로젝트가 포함된 상태로 ipython 쉘이 열린다. 원하는 모듈에서 원하는 것을 불러올 수 있다. 하지만 매번 임포트하는 것도 고된 일이다. `./manage.py shell_plus`로 모든 모듈 및 다양한 것을 불러올 수 있다.  
`pip freeze > requirements.txt`: env 환경이 바뀌었으므로  requirements 재설정



<a name='관리자_페이지_관리'></a>
# Django 관리자 페이지 관리

### Post의 제목이 뜨지 않고 'Post Object'뜨는 문제 해결

**원인**: Post 객체가 표시될 str를 정해주지 않았기 때문  
**해결**: 

```python
# models.py

class Post(models.Model):
	...
	
	def __str__(self):
		return self.title
```  




<a name='사용자_페이지_관리'></a>
# Django 사용자 페이지 관리

**사용자 페이지 구상**: 첫 페이지에 블로그 포스트 리스트를 보여주자

### 1. 데이터를 가공할 view_controller 생성
`view controller`는 url을 받아 정보를 처리한 후, Template을 호출해 그 정보와 함께 rendering한다.

```python
<blog.views.py>

# request는 urlresolver가 보내는 인자를 받는다.
def post_list(request):
    posts = Post.objects.all()
    context = {
        # 현 value인 posts는 QuerySet이다
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context)
```
```python
def post_list(request):
	# url 요청에 대한 응답을 http 형식으로 보내는 것
	return HttpResponse('Post List')
```

## 2. URL 관리  

`urls.py/urlpatterns`에 특정 url 요청과 view_controller를 연결해준다. 이 `urls.py`가 `urlresolver`의 역할을 한다. 

```python
from django.conf.urls import url
from django.contrib import admin
from blog.views import post_list  # alt+enter로 import해주자

urlpatterns = [
    # 정규표현식
    # 메인주소/ 뒷 부분만 받는다. 
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list)
]
```
**정규표현식으로 url에서 인자 받기**  

```python
<urls.py>
# post/ 뒤에 오는 하나 이상의 수를 이름이 pk인 키워드 인자로 받아서 post_detail에 넘겨준다.
# 그룹 이름이 없으면 위치 인자로 넘겨준다.
url(r'post/(?P<pk>\d+)/', post_detail)  

<views.py>
# post_detail 함수의 인자로 pk를 설정해주어야 한다. 
def post_detail(request, pk)
```
> `pk`: 관계형 데이터베이스의 기본 키(Primary Key)로, 한 레코드(특정 클래스의 한 객체)의 식별자로 사용된다. 장고의 경우, 인스턴스를 구별하는 키로는 `id`와 `pk` 모두 사용가능하다.  
> `관계형 데이터베이스`: 관계형 데이터베이스란, 데이터를 키와 값들의 관계를 간단한 테이블로 정리한 데이터베이스이다. 데이터를 column과 row를 이루는 하나 이상의 테이블로 정리하며, 고유 키(Primary key)가 각 로우를 식별한다. 이 로우는 레코드 또는 튜플로 부른다. 일반적으로 각 테이블은 하나의 클래스(고객이나 제품과 같은)를 대표한다. 로우는 그 클래스의 인스턴스를 가리키며 컬럼은 그 인스턴스의 속성에 해당한다. 

## 3. Template 관리  

**Template 폴더 생성**  
`html`파일만 관리하는 Templates 폴더를 만든다. `djgirls_prj/Templates/blog/Post_list.html`

**Template directory 생성**  
뷰컨트롤러에서 Template html 파일을 참조하는 경우가 많다. 그때마다 상대경로를 입력하는 것도 번거롭고, 나중에 위치를 변경하면 더 골치 아파진다. 그래서 아예 Template이 있는 디렉토리를 설정해 둘 수 있다.   
저장된 Template Directory 정보는 settings.py가 호출될 때 인식된다. (manage.py를 호출하거나 runserver를 명령하면 settings.py가 호출된다.)  

```python
<settings.py>

# 상위폴더로 갈 때: os.path.dirname(path)
# 하위폴더로 갈 때: os.path.join(BASE_DIR, <바로 하위 폴더>)

# __file__이 setting.py를 의미하고, os.path.abspath(__file__)은 그 경로를 의미한다. 
# 따라서 아래 명령어는 현재 파일에서 두 번 올라가면 BASE_DIR 라는 의미
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 템플릿 파일을 저장할 'template' 폴더
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```
이 상태 만으로는 `TEMPLATE_DIR`과 `BASE_DIR`은 파일 경로를 담고 있는 문자열 변수일 뿐이다. 설정파일의 템플릿 설정에 해당 경로를 저장해주어야 한다.  
<a name=01></a>

```python
<settings.py>

# 템플릿에 관련된 옵션을 다루는 곳
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 디렉토리 루트를 불러오는 곳이다. 
        'DIRS': [
            # 파이썬에서는 항목을 세로로 나열할 때 컴마를 찍는 것을 권장한다. 
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
이제 `views.py`에서 Template file을 `TEMPLATE_DIR` 기준으로 쉽게 참조할 수 있다.  

```python
<settings.py>

return render(request, 'blog/post_list.html', context)
```



## 4. Static 파일 관리

**Static directory 생성**  
서버에서 파일은 크게 두 가지로 나뉜다. 유저가 업로드한 파일과, 사이트 자체에서 이용하는 파일이다. 후자는 변할 이유가 없기 때문에 정적 파일이라고 부른다. 이 정적 파일은 `Application folder`아래 `Static` 폴더에 저장해준다. css 파일은 정적파일로 분리된다. 

**Static directory 경로 입력**  
Django 프로젝트에서 Static 폴더를 인식할 수 있도록 `settings.py`에 경로를 입력해준다.

```python
# 새로만든 static 디렉토리를 가리키도록 os.path를 사용해 변수 할당
# 정적 파일을 저장할 'static'폴더
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 장고에서 정적파일을 검색하고 가져올 폴더 목록
# STATICFILES_DIRS는 지정된 변수임으로 명칭을 틀려서는 안 된다.  
STATICFILES_DIRS = [
    STATIC_DIR,
]
```

**Template에서 Static file 참조하기**  

```html
# static은 기본 태그가 아니므로 로드해야 한다.
{% load static %}

# static (template)tag를 이용한다.
<link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.css' %}">
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

<a name='기타_설정_변경'></a>
# 기타 설정 변경

```python
# 관리자 페이지 언어를 변경한다. 미국 영어의 경우는 'en-us'
LANGUAGE_CODE = 'ko-kr'

# 기본적으로 장고는 모든 시간을 UTC 기준으로 저장한다. 기본 설정은 'UTC'
TIME_ZONE = 'Asia/Seoul'
```

<br>

<a name='ORM'></a>
# ORM

**ORM**: DB 안의 데이터를 마치 파이썬의 객체처럼 접근하게 해주는 도구. SQL문이 사용하기 어려워서 사용하는 것. 아래의 명령어들이 전부 예시이다.   
**QuerySet**: DB에 보낸 질의(Query)에 대한 응답 셋. iterable하다.  
`Post.objects.all()` 모든 Post 객체를 쿼리셋으로 불러온다.  
`Post.objects.create()` 인자를 키워드로 전달하며 객체를 생성할 수 있다. DB에 Save까지 해준다.  
`User.objects.create(username='')` 으로 유저 객체를 생성할 수 있다.  
`P.delete()` 로 객체를 지울 수 있다. 이 메서드는 해당하는 클래스의 객체가 몇개 지워졌는지 반환한다.    

```python
p = Post.objects.create(
	title=request.POST['title'],
	content=request.POST.get('content'),
	author=User.objects.get(username='elohimawmar')
)
# 이 상태에서 print(p.query)로 SQL문의 query를 볼 수 있다. 
# SELECT * FROM "blog_post" == Post.objects.all()
```
`Post.objects.last()`, `Post.objects.first()`  
`Post.objects.get(pk=3)`: 조건에 해당되는 객체를 '하나' 받아온다. 없으면 오류. (`Post.`필수)
> `Post.objects.get()`에 실패했을 때 발생하는 예외 = `Post.DoesNotExist`  
> 이런 예외가 발생하는 경우, `HttpResponse(status=404)`로 상태를 전달할 수 있다. 

`Post.objects.filter(published_date__isnull=False)`  
: 필터에 해당되는 객체를 쿼리셋으로 받아온다.  
`Post.objects.filter(title__contains='text')`  
: Post의 속성 title이 문자열 'text'을 포함하고 있는가  
`Post.objects.order_by('created_date')`  
: 해당 속성을 기준으로 오름차순 정렬. 내림차순을 원한다면 `'-created_date'`을 사용하면 된다.  

> QuerySet들은 하나로 연결할 수 있다.  
> `Post.objects.filter(published_date__lte=timezone.now()`  


<a name='내장함수'></a>
# Django 내장함수
**현재 시간 호출**: `self.published_date = timezone.now()`  
**DB에 객체 저장**: `p.save()` 


<br>

<a name='template_언어'></a>
# Django Template 언어

##### 변수: `{{ post }}``{{ post.title }}`  
##### 구문:  

```python
# 여기서 for와 같은 것을 Template 태그라고 부른다.
{% for post in posts %}
	# linebreaksbr은 html에서 무시하는 줄바꿈을 표시해준다. truncatewords보다 앞에 와야 한다.  
	# truncatewords는 보이는 단어 수를 제한해준다. char 는 이제 문자 수를 제한한다. 
	<div>{{ content|linebreaksbr|truncatewords:50 }}<div>
{% endfor %}

# 조건문
{% if delete %}
    {% include 'blog/post_form2.html' %}
{% endif %}
```

##### 1. Template extending (템플릿 확장)  

```
# 메인 템플릿: content라는 이름의 block 구역 설정
{% block content %}
{% endblock %}

# 상속 템플릿: base.html을 받아옴
{% extend 'base.html' %}
# 설정된 block 안에 내용을 넣음
{% block content %}
{% endblock %}
```

##### 2. Template에 url 넣기  
Template 변수 이용하기: `href="post/{{ post.pk }}"`  
url tag와 url name 이용하기: `href="{% url 'url_name' pk=post.pk %}"`

##### 3. post 요청에서 csrf 검증하기
> **CSRF: 사이트간 요청 위조 (Cross-site request forgery)**  
> 서버가 쿠키 대조 만으로 브라우저를 인증하는 것을 이용하여 사용자인 척 악의적인 요청을 보내는 것. 사용자가 해당 사이트에 로그인 하면 로그인 쿠키가 남게 된다. 이때 사용자를 해커의 공격 페이지에 접근하게 한다. 이미지  태그 혹은 버튼에 악의적인 요청을 숨겨둠으로서 사용자는 자신도 모르는 사이에 잘못된 요청을 하게 된다.   
> **CSRF 토큰**  
> csrf를 방지하는 여러 방법 가운데 하나이다. 다음의 과정을 거친다.  
> > 1. 서버가 클라이언크에 토큰을 전달한다.  
> > 2. 클라이언트는 form과 함께 토큰을 전달한다.  
> > 3. 서버는 토큰이 일치할 때만 요청을 수락한다.

```html
# csrf_token 태그를 form 태그 바로 아래에 넣어준다
<form class="form-horizontal" method="post">
    {% csrf_token %}
    
# csrf_token은 parsed html에서 다음과 같은 형태로 바뀐다.
<input type="hidden" name="csrfmidlewaretoken" value="토큰" />
```  



<a name='django_basic'></a>
# Django Basic

**manage.py**: 장고에서 제공하는 다양한 기능으로 사이트 관리를 도와주는 모듈  
**settings.py**: 사이트 설정 관리  
**url.py**: url 요청 정보를 어디로 보낼 것인가. urlresolver가 사용하는 패턴 목록을 관리  
 
##### MVC pattern
Model-View-Controller (장고에서는 MTV. 아래 괄호 안은 장고 이름)  
`model`: Database  
`view`(Template): 사용자에게 제공되는 화면 또는 기능 (html 파일)  
`controller`(view): 그 사이에서 데이터를 가공, view 생성 (urlresolver에 연결) (장고에서는 view 라고 불리며, python 함수이다.)  


##### Request에서 Response까지의 과정
사용자의 요청이 서버에 도달  
서버는 해당 요청을 장고에 전달  
장고는 해당 url을 분석해서 controller에 연결  
controller는 요청을 받아 사용자에게 제공할 view를 리턴  
server는 그 리턴을 사용자에게 전달  

##### Terminal  
`pip list`: 현재 설치된 패키지 목록  
`brew install tree`: `tree 경로`로 디렉토리 구조를 보여준다.  
`./manage.py`: `./`는 파일을 실행하라는 의미이다. 기본적으로 zsh은 스크립트 편집기로 해당 파일을 연다. 파일을 열 프로그램을 특정하고 싶다면, 해당 파일의 상단에 다음과 같은 것을 기록할 수 있다. `#!/usr/bin/env python`(python 실행)

##### Pycharm 단축키  
`alt + enter`: 빨간줄에서 실행, 없는 모듈 임포트  
`cmd + click`: 해당 모듈이 있는 파일로 이동

## Pycharm 설정  
##### 1. Debug로 Runserver하기  
`Run/Debug configurations/왼쪽탭/Python/Unnamed`에서  
`Script`에는 `manage.py`의 경로를, `Script parameters`에는 `runserver`를 입력해준다.



<a name='공부할_것'></a>
# 공부할 것.

**django_extensions**  
`l = [[1]*3]*3` 같은 리스트 객체 생성  
`REST아키텍처` 유알엘만 보고 무슨 뜻인지 알게 하는 것을 지향

<a name='질문'></a>
# 질문

shell 자동완성하는 툴   
 
`<setting.py>`의 TEMPLATE = [] 는 옵션인가? 변수인가? 뭐라고 부르는 것이 맞나? [-----](#01)  

`ORM`이 뭔지 다시 한 번만 설명해주세요. SQL문이 사용하기 어려워서 사용하는 도구인가요?  

데이터베이스 상에 표시되는 `blog_post`는 blog 애플리케이션 안의 Post클래스를 의미하는 것인가요? 근데 왜 p가 소문자죠?

---
