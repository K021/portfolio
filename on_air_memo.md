## 17.10.10.화  
**pyenv versions**: 만들어진 pyenv 가상환경 목록  
**terminal**: cp a b = a path를 b path로 복사  
**django coding style**: [장고에서 권장하는 코딩 스타일](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)  
**migaration log**: `./manage.py showmigrations`

## 17.10.13.금

값을 간단하게 보여주고 싶을 때: `Entry.objects.values_list('pk', flat=True)`  
`.query.__str__()`: 해당 쿼리 보여줌  
`git reset HEAD~1`: 커밋 하나 지움  
`git commit --ammend`  

### instagram 기능
사진 업로드  
팔로우  
동영상 업로드  
좋아요  
좋아요 리스트  
검색 (해쉬태그 검색)  
댓글  
DM  
로그인  
회원가입  
프로필페이지  
무한 스크롤  
위치태그  
얼굴인식, 사진필터 // 불가  

애플리케이션  
사용자   	로그인  
	회원가입  
	프로필 페이지  
	팔로우  

포스트  
	사진올리기  
	댓글달기  
	좋아요 누르기  
	
	
숙제  
문서: field type(relationship부분은 필요ㄴㄴ)/ Query set  
인스타그램: 사진업로드, 사진 댓글


## 17.10.19.목

custom User를 admin에 설정할 때는 다음과 같이 한다.

```python
from django.contrib.auth.admin import UserAdmin
from member.models import User

admin.site.register(User, UserAdmin)
```

## 17.10.23.월

**Templaten Language**  
class tag 안에 `{% if %}`와 같은 템플릿 언어를 사용할 수 있다. 여지껏  href 태그에 템플릿 언어를 사용해왔던 것을 생각하면 참 당연한 소리.

**Django TDD**  
`./manage.py test`: 장고 프로젝트 폴더에 있는 test로 시작하는 python 파일을 모두 테스트 파일로 인식한다. 그 안에 있는 메서드 중 test로 시작하는 함수를 전부 실행해 결과를 보여준다.  

**Queryset: `get_or_create`**  

```python
# object에는 추출 혹은 생성된 인스턴스가, 
# iscreated에는 생성되었으면 True, 아니면 False 값이 리턴된다. 
object, iscreated = Person.objects.get_or_create(
	# first_name과 last_name을 기준으로 검색하고, 
	# 인스턴스가 없을 경우, defaults의 값을 포함하여 새로운 객체를 생성한다.
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
```

**Python Built-in Function**  
`isinstance(instance, class)`: 인스턴스가 해당 클래스의 인스턴스인가 검사. 불리언 리턴

**Django Field ManyToMany**  

1. 커스텀 중개 모델을 사용하면, add/remove 메서드를 사용할 수 없다.  


> **중개모델을 직접 불러와서 작업하거나**  
> `Relation.objects.filter().delete()`  
> `Relation.objects.create()`  
> 
> **인스턴스에서 연결된 중개모델을 불러온다**  
> `self.myrelations_with_stars.filter().delete()`  
> `self.myrelations_with_stars.create()`  

```python
class User(AbstractUser):
    stars = models.ManyToManyField(
        'User', # 어떤 클래스와 관계를 맺을 것인가. 이 경우 재귀적 호출.
        # 일방적인 관계가 되도록 설정 
        # symmetrical=True일 경우, A 인스턴스에서 B 인스턴스를 참조하면, 
        # 자동적으로 B도 A를 참조한다.
        symmetrical=False, 
        through='Relation',
        related_name='followers'
    )
    
class Relation(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='myrelations_with_stars'
    )
    star = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='myrelations_with_followers'
    )
```

## 17.10.26.목

aws 배포 팁: 배포가 완료된 후부터 코딩을 시작해야 오류가 왜 나는지 알 수 있다. 

## 17.10.27.금

### 1. 찾아볼 것  

uwsgi options:  
`(Local)ec2_deploy_project/.config/uwsgi/mysite.ini`에 적히 옵션들이 무엇이 있는지 알 수 있다.  
what is linux master process for  
리눅스 서비스 파일 (블로그: uWSGI 서비스 설정파일 작성 관련)  
`sudo shutdown -r now` 서버 컴퓨터를 종료하고 재실행한다.  

**processor status**  
`ps -ax | grep uwsgi`  
-a : 다른 사용자들의 프로세서도 보여준다.  
-x : 로그인 상태에 있는 동안 아직 완료되지 않은 프로세서들을 보여준다.  
`
 

**(server) nginx conf 파일 복사**

```
sudo cp -f /srv/ec2_deploy_pj/.config/nginx/mysite.conf /etc/nginx/sites-available/mysite.conf
```

리눅스 심볼릭링크
005cbb

### 2. 새로운 내용  
**쉘스크립트**  
`export` 변수 이름 지정  
`source ~/.zshrc` 파일 안에 담긴 모든 명령어 실행  
`pip install psycopg2` postgresql을 사용하기 위해서는 psycopg2가 필요하다.
`./manage.py collectstatic` 스태틱파일을 한 곳으로 모음

**아마존 데이터베이스 서비스**  
1) psql에서 데이터 서버 불러오기:  

```
psql --host=mydbinstance-joo2theeon.ccdyfkfjc58s.ap-northeast-2.rds.amazonaws.com --user=joo2theeon --port=5432 deploy
```



# 질문

* oh-my-zsh 설치가 왜 웹에 나와있는 것과 다른가요

```
# oh-my-zsh 설치
sudo curl -L http://install.ohmyz.sh | sh
```

* 시크릿 키 생성할 때 왜 소문자로만 한 건가요
* (조교님) nginx user 가 왜 root라고 하셨나요
 
 

## 17.10.30.월

**파이썬 단축키**  
`cmd + delete` 파이참 한 줄 삭제  
`shift + enter` 파이참 바로 밑에 줄 생성

-



# 17.10.31.화

프리티어는 겟과 풋 요청 수가 제한되어 있다. 한 달 기준이다. s3 결재페이지에 들어가면 볼 수 있다.


## CORS
11:33 //  
/서비스/S3/버킷선택/권한/CORS구성/  
s3는 기본적으로 모든 url에 대해 열려있다. 따라서 다른 도메인에 있는 파일을 가져 올 수도 있다. 스크립트 태그 안에서 요청하는 것을 브라우저 단에서 제한하기 위해 있는 것이다. [aws.s3.cors], (검색: cors 메커니즘)  
서버에서 접속하게 하려면 서버 주소를 넣으면 된다.  

```
<!-- Sample policy -->
<CORSConfiguration>
	<CORSRule>
		# 사용 예시
		<AllowedOrigin>http://localhost:8000<AllowedOrigin>
		<AllowedOrigin>http://127.0.0.1:8000<AllowedOrigin>
		
		# * 가 있으면 모든 주소가 용납된다. 
		<AllowedOrigin>*</AllowedOrigin>
		<AllowedMethod>GET</AllowedMethod>
		<MaxAgeSeconds>3000</MaxAgeSeconds>
		<AllowedHeader>Authorization</AllowedHeader>
	</CORSRule>
</CORSConfiguration>
```

11:44 //  
환경변수 위키  
`export`: 환경변수를 지정하는 명령어

```
export abc=lhy
echo abc
```
환경변수는 당고와 파이썬에서도 가져다쓸 수 있다. manage.py를 까보면 볼 수 있따.  os.environ.setdefault

init에 settings 미리 정의 

-

2:32 //  
apt 우분투 파일 패키기 관리자




# 17.11.02.목


### 백그라운드에서 실행 중인 docker 접속하기  

* `docker ps`: 실행 중인 docker  
* `docker exec -it b40f /bin/zsh`: b40f container에서 /bin/zsh을 terminal 형식으로 실행하라

(12:23 nginx.conf)  
supervisor로 프로그램을 관리하려면 그 프로그램이 터미널로 실행되어야 한다. 

서비스를 호스팅 받아소 쓸 때으 ㅣ종류가 갈린다.   
on-premises  
http://programmerchoo.tistory.com/64  
ecs


### Elastic Beanstalk 명령줄 인터페이스(EB CLI)

설치: `pip install awsebcli`
유저 생성: Access key ID와 Secret access key를 `vim ~/.aws/credentials`에 넣어주자.
eb init --profile eb

서버 엔진엣그 서버안에 80 요청잉 노다.  서버 안에 도커가 돌아감 80 엔진엓스 도터  도커 안의 엔진엑스 우리가 설정한 엔진엑스는 도커 엔진엑스  도케 엔진엑스가 80포트 사용. 이 포트가 외부 엔진엑스롸 연결 expose 80포트 

deploy하면 Dockerfile을 자동으로 빌드해준다. 


17.11.03
단일 컨테이너 도커 구성 http://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create_deploy_docker_image.html

엘라스트 빈스토근 보안 그룹이 두 개다. 이엘비랑 이씨투  
request - EB - ELB - EC2 - RDS  
RDS에서 EC2를 허가해준다.  

http://k021-eb.ap-northeast-2.elasticbeanstalk.com/

스케치, 액츄어


# 17.11.06.월

> EB로 디플로이를 하면 도커파일이 올라간다. EC2 안에 AmazonLinux 위에 우분투(도커)가 돌아간다. 


# 17.11.07

파이썬 ㅁ = a and b or c



# 17.11.09.목

**질문시간**  
cbv generics viewsets 

**실행확인**  
런서버 키고 포스트맨 작성  

`./manage.py test test-file-path`

**질문**  
ReadOnlyField가 뭐하는 놈인가


# 17.11.13.월

**Authentication**  

TokenAuthentication  
install, migrate 디비 테이블을 사용하기 때문에 
토큰은 유저 비밀 정보를 대체해서 쓰인다. 토큰이 있으면 이미 인증된 것 처럼 작동한다. 
로그인할 때 토큰을 생성해서 보내준다. 클라이언크는 그 토큰을 받아서 헤더에 보낸다. 

* Response는 왜 rest_framework를 ㅆ는가 

create_user는 set_password 내부 메서드가 실행, 그냥 생 암호가 아니라 해쉬한 값이 들어간다. 
ReadOnlyField  

facebook login api  
redirection URI 정보를 developers.facebook.com 애플리케이션에 등록  

custom backends  


# 17.11.14.화

**질문**  

`debug_token_info` 는 왜 안 쓰는가. 토큰이 올바른지를 확인하는 과정을 거쳐야 하지 않는가. 우리가 저번 프로젝트 할 때는 생략한 것인가??   
`UserInfo` 클래스에 왜 `name`이 없는가  
프론트 측에서 전달하는 `data`에 사진이나 이메일, 그리고 이름도 전달해야 하지 않는가.  
`debug token`은 프론트 말고 서버에서 한 번만 하면 되지 않는가?  

django internationalization and translation  


# 17.11.16.목

cors 문제 해결 

```python
CORS_ORIGIN_WHITELIST = (
    'localhost:3001',
)
```
branch 이름이 다르면 upstream 명령어  

**`pip install awsebcli`**  
**`Dockerfile`**  
**`eb init`**: Elastic Beanstalk 애플리케이션을 하나 생성한다. 애플리케이션은 EB 환경을 구축할 수 있는 최소단위다.  
**`eb create`**: EB 컴퓨터 안에 EC2 생성.  
**`eb deploy`**:   
**`eb open`**: 배포된 eb 열기  


**docker 명령어**  
`docker build -t instagram .`: 현재 폴더를 기준으로 `Dockerfile`을 돌려서 `instagram` 태그로 이미지 생성  
`docker images`: 만들어진 도커 이미지  
`docker run --rm -it base /bin/zsh`: `base` 이미지의 `/bin/zsh`을 터미널로(`-it`) 실행, 실행 후 도커 이미지 닫기(`--rm`)  
`docker run --rm -it -p 8013:80 instagram`: 인스타그램 이미지를 8013:80 포트로 실행. (8013은 도커가 돌아가는 컴퓨터에서 외부 요청을 받아들이는 포트. 80은 도커에서 외부 요청을 받아들이는 포트. 외부에서 컴퓨터에 8013포트로 요청이 오면 컴퓨터는 해당 요청을 도커의 80번 포트로 연결해준다.)  
`docker ps`: 현재 실행중인 도커 이미지   `docker exec -it 34d0 /bin/zsh`: 실행중인 도커 이미지 `34d0`의 `/bin/zsh`을 터미널로 실행  
`docker stop 6413`: 실행중인 도커 중지

**기타**  
`./manage.py runserver 0:8001`: 8001번 포트로 런서버. 모든 아이피에서 들어올 수 있음(0의 의미)  
`python -m http.server 3001`: 실행되는 폴더를 기준으로 서버를 열고, 안에 index.html이 있으면 그 파일을 열어준다. 없으면 폴더 파일 전체를 보여준다.  

eb extension

## 질문

`docker exec -it 34d0 /bin/zsh`: 실행중인 도커 이미지의 `/bin/zsh` 실행  
- zsh 말고 다른 것도 실행할 수 있겠네?  
- supervisor


# 17.11.17.금요일

메시지 브로커 솔루션을 통해 메세지를 셀러리에게 보낸다. 메세지는 작업 명령이다. 셀러리는 한 큐에 쌓인 메세지를 불러와서 실행한다.  
여기서는 브로커로 Rabbitmq를 사용한다. 


http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
셀러리 인스턴스, 앱 또는 응용프로그램 생성. 모든 샐러리 작업의 시작점으로 사용됨

[aws.s3.cors]:https://s3.console.aws.amazon.com/s3/buckets/fc-6th-test-joo2theeon/?region=ap-northeast-2&tab=permissions
 
 
# 17.11.20.월요일

HTTP요청을 하는 경우, axios(HTTP library)를 사용해보자. jquery는 많이 무거워서 많이 않쓴다.

# 17.11.21.화요일

api 작성  
로그 관리  
CI(Continuous Integration)   
pagenation  

로그 파이썬 모듈이 있다. python 의 loggin.logger 가 로그 기록  
https://docs.djangoproject.com/en/1.8/topics/logging/  

`ps -ax | grep runserver`: 현재 런서버 잡기  
`kill -9 17331 48557`: 런서버 죽이기  


# 17.11.13.목요일

## CI (Continuous Integration)

예전 소프트웨어 개발은 배포가 제대로 이루어지지 않았다. 한 번에 많이 짜서 합치는 식. 지금은 작은 단위로 쪼개서 관리한다. 이때 사용하는 것이 CI 툴이다.   

`Trevis CI`: 가장 유명한 툴. 깃헙에만 연결되어 있다. Github 코드를 테스트하는 등 다양한 기능을 가지고 있다고.  
`.travis.yml` 파일 작성. `mysite` 와 같은 위치  

```yml
language: python

# 버전은 여러개 집어 넣을 수 있다. 
python:
  - 3.6

# command to install dependencies
install:
  - pip install -r requirements.txt

before_script:
  - cd instagram

script:
  - python manage.py test
```  

**`.gitignore`에 포함되는 파일 Travis로 관리하기**  
> Travis는 프로젝트 코드를 `git` 단위로 관리하기 때문에 `.gitignore`에 있는 파일은 검사에 포함되지 못하기 때문에 Travis에 따로 보내주어야 한다. 파일은 Travis 공개키로 암호화를 시켜 보낸다. 여러개의 파일을 하나씩 암호화 하고 푸는 것은 번잡하기 때문에 하나의 압축파일로 만들어서 암호화 시킨다. 암호화 과정은 Travis cli를 사용한다.  

**파일 압축**: (Terminal) `tar cvf secrets.tar .config_secret` // 생성된 `secrets.tar`는 `.gitignore`에 넣어준다.  
**파일 압축 해제 명령**: `before_intall:`에 `tar xvf secrets.tar`를 입력해준다.  

[Travis - Ecrypting files](https://docs.travis-ci.com/user/encrypting-files/)  
**Travis cli 설치**: `gem install travis`  
**Travis Login**: `travis login` 유저네임은 대소문자를 구별한다.  
**파일 암호화**: `travis encrypt-file <file name> -a -f`  
`-a`: add 옵션. `yml`파일에 파일 decode 명령어를 자동으로 입력해준다. 파일 압축해제 명령어는 따로 추가해주어야 한다.   
`-f`: force 옵션. 기존 파일을 덮어씌울 수 있다.  

.requirements/ 생성, dev.txt에 기존 requirements.txt 파일을 넣어두고, deploy.txt 파일에 필요한 요소만 적어둔다. 이때, 부등호로 조건을 주는 것이 좋다.  

# 17.11.27.월요일

준비 없는 자에게 미래는 없다.  

도커 없이 디플로이 하는 것.  

./manage.py만 치면 커맨드가 나온다  
배포를 하면 수퍼 유저를 만드는 코드를 짜두면 좋다. 17.11.27  
django-admin django document  