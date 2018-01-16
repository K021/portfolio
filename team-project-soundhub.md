
# Soundhub: 음악 오픈 프로듀싱 플랫폼  

> : Soundhub는 여러 사람들이 모여서 하나의 완성된 음악을 만드는 과정을 수월하게 해주는 서비스입니다. 


#### 우리는 이런 문제에 주목했습니다

음악 대부분은 많은 악기가 어우러져서 만들어집니다. 그러나 한 사람이 여러 악기를 모두 잘 하는 경우는 많지 않습니다. 어떤 사람은 기타를 잘 치기도 하고, 건반을 잘 다루기도 하고, 노래를 잘 부르기도 합니다. 이런 이유로 여러 사람이 모여 밴드를 결성하고는 합니다. 서로가 함께 해야 좋은 음악을 만들 수 있기 때문이죠. 시간도 충분하고, 알고 있는 음악가들도 많다면 이는 별 문제가 되지 않습니다. 시간을 내어 서로가 만나 작곡을 하고, 맞추어 보고, 녹음을 하면 되죠. 

그러나 만일 평범한 회사원이 음악을 하고 싶다면 어떻게 할까요? 시간도 많지 않고, 아는 음악가도 별로 없고, 보컬 또는 악기 하나만 잘하는 사람이 음악을 만들고 싶다면 어떨까요? **멋진 음악가들을 만날 장소**가 있었으면 할 것이고, **그들과 작업할 만한 상황**이 되길 바랄 것입니다. Soundhub는 바로 이런 문제에 주목했습니다.


#### 우리 서비스는 다섯가지 핵심기능을 제공합니다.  

* **Post**: 사용자는 자신이 연주한 트랙을 업로드할 수 있습니다.  
* **Comment**: 사용자는 다른 사람의 Post를 보고 그 트랙에 어울리는 트랙을 녹음해 업로드할 수 있습니다.
* **동시재생**: 사용자는 한 Post Track에 업로드된 많은 Comment Track들 중 몇 개를 골라서 동시에 재생할 수 있습니다.  
* **Mix**: 사용자는 자신이 어울린다고 생각하는 Comment Track들과 Post Track을 믹스할 수 있습니다. 
공유: 그 믹스된 음원을 다른 SNS에 공유할 수 있습니다.
* **메세지**: 사용자는 자신과 잘 맞는다고 생각하는 음악가와 소통할 수 있습니다. 


#### 우리 서비스의 대상은 자신의 음악을 만들고 싶은 일반인입니다. 

누구든지 자신이 잘 다루는 악기가 있고, 음악을 만들고자 하는 열정만 있다면 음악을 만들 수 있습니다. 자신의 악기로 트랙을 작곡해 올리고, 다른 사람이 올린 트랙들을 들어보고, 어울리는 트랙을 녹음해 업로드하고, 마음에 드는 조합이 있다면 믹스할 수 있습니다. 그리고, 그 트랙들을 만든 음악가들과 연락할 수 있습니다.


# 구현된 기능 개괄

* 유저 관리
	* 회원가입
	* 로그인
	* 로그아웃
	* 회원정보 수정
	* 회원탈퇴
* 유저간 기능
	* 팔로우
	* 메세지
* 프로젝트 기능
	* Post 작성, 수정, 삭제
	* Post 좋아요 토글
	* Comment 작성, 수정, 삭제
	* 트랙 믹스
* 기타
	* 메일 보내기
	* 검색



# 기술적으로 도전적이었던 부분과 해결방법

## 목차

1. [activation key 를 활용한 이메일 인증](#1-activation-key-를-활용한-이메일-인증)
2. [stale user 처리](#2-stale-user-처리)
3. [테스트 코드를 위한 더미 클래스 생성](#3-테스트-코드를-위한-더미-클래스-생성)
4. [메일 발송 비동기 처리(celery)](#4-메일-발송-비동기-처리celery)
5. [소셜로그인 - Facebook Login](#5-소셜로그인---facebook-login)
6. [회원가입-로그인시 발생할 수 있는 모든 문제 해결](#6-회원가입-로그인시-발생할-수-있는-모든-문제-해결)

## 1. activation key 를 활용한 이메일 인증  

### [이메일 인증 로직]

1. 회원가입 요청시, 유저 생성
2. 유저 생성시 activation key 생성 
3. 생성된 activation key 정보를 담은 activation link 가 있는 메일 발송
4. activation link에 접속하면
5. 링크 get parameter 에 담긴 activation key 를 통해 유저 특정
6. 해당 유저 activation

### [특이사항]

##### activation key 를 User 모델 안의 필드로 저장하지 않고 별도의 모델로 설계  
: activation key 는 40 자의 hash code 로 구성되어 있는데, 이 key 의 만료 일자를 저장할 곳도 필요하다. key는 유저와 상관이 있는 값이지만 그 만료일자는 그렇지 않기 때문에 따로 분리하는 것이 좋다고 생각했다. 또한, activation key는 처음 로그인할 때를 제외하면 거의 사용되지 않기 때문에 user model 안에 필드로 저장하는 것은 그리 좋지 않은 생각이라 판단했다.  

##### 유저 activation 여부가 데이터베이스에 기록이 안 되어서 고생  
: 이메일 인증 후에 `user.is_active` 값을 `True`로 변경해주는데, 처음에는 `user.save()` 메서드를 호출하지 않아서 데이터베이스에 저장이 되질 않았다. activation view의 리턴 값이 유저 객체와 그 유저의 active 값이었는데, 이때 사용된 user는 active 값이 True인 상태였으므로 출력 값에는 아무런 이상이 없었다. 다만 저장이 안 되는 것이 문제였을 뿐이다. 테스트 코드 상에서 데이터베이스를 검사해주었으면 금방 발견할 수 있었을 텐데, 아직 테스트 코드를 짜기 전이었어서 문제를 발견하는데 한참이 걸렸다. TDD가 왜 중요한지 알게 되는 시점이었다. 

##### activation key 에 사용되는 hashcode 생성과, 만료기한 날짜 생성을 키 인포 클래스 생성 메서드에 병합
: activation key 를 사용하는 뷰가 Signup view 하나 뿐이었을 때에는, 뷰에서 직접 해쉬값과 만료 기한을 생성해서 `create()` 메서드로 key를 생성했다. 그러나 구글/페이스북 로그인 뷰에서도 key 값이 사용되고, 나중에 패스워드 변경메일에도 사용하면서 key와 만료기한을 한꺼번에 생성할 필요가 생겼다. 이제는 key info 생성시에 알아서 key hash code와 만료기한이 생성되고, 키 또는 만료기한을 새로고침하고 싶은 경우를 위해 `refresh()` 메서드를 만들어두었다.  

### [코드]

##### Activation Key Info Class

```python
class ActivationKeyInfoManager(models.Manager):
    def create(self, user):
        """
        1. stale user 삭제
        2. activation key & expired_at 자동 생성

        :param user: ActivationKeyInfo 와 연결될 유저 객체
        :return: 생성된 ActivationKeyInfo 객체
        """
        ...

        # activation key 생성을 위한 무작위 문자열
        # user 마다 unique 한 값을 가지게 하기 위해 user.email 첨가
        random_string = str(random()) + user.email
        # sha1 함수로 영문소문자 또는 숫자로 이루어진 40자의 해쉬토큰 생성
        activation_key = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
        # activation key 유효기간 2일
        expires_at = timezone.now() + timezone.timedelta(days=2)
        # activation key 생성
        activation_key_info = ActivationKeyInfo(
            user=user,
            key=activation_key,
            expires_at=expires_at,
        )
        activation_key_info.save()

        return activation_key_info

# Email Verification 에 사용되는 Activation key 정보를 담고 있는 클래스
# User class 와 one to one 으로 연결
class ActivationKeyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, blank=True)
    expires_at = models.DateTimeField()  # key 만료 기한

    objects = ActivationKeyInfoManager()

    def __str__(self):
        return f'user:{self.user.nickname}'

    def refresh(self):
        """
        간단하게 ActivationKeyInfo 를 새로고침 하기 위한 함수
        """
        # activation key 생성을 위한 무작위 문자열
        # user 마다 unique 한 값을 가지게 하기 위해 user.email 첨가
        random_string = str(random()) + self.user.email
        # sha1 함수로 영문소문자 또는 숫자로 이루어진 40자의 해쉬토큰 생성
        activation_key = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
        # activation key 유효기간 2일
        expires_at = timezone.now() + timezone.timedelta(days=2)

        self.key = activation_key
        self.expires_at = expires_at
        self.save()

    def refresh_expires_at(self):
        expires_at = timezone.now() + timezone.timedelta(days=2)
        self.expires_at = expires_at
        self.save()

```

##### Signup view 중 이메일 인증 로직

```python
class Signup(APIView):
    def get(self, request):
        ...

    def post(self, request):
        ...

        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            # user 생성, 반환
            user = serializer.save()
            # activation key 생성
            activation_key_info = ActivationKeyInfo.objects.create(user=user)
            # 인증 메일 발송
            send_verification_mail.delay(
                activation_key=activation_key_info.key,
                recipient_list=[user.email],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

##### Send Mail Method

```python
@celery_app.task
def send_verification_mail(activation_key, recipient_list):
    """
    activation key 를 담은 activation_link 를 recipient 에게 보냄

    :param activation_key: activation key 의 기능을 수행하는 40자 문자열
    :param recipient_list: 수신자 이메일 목록 list 객체
    :return: send_mail 함수 반환 값
    """

    scheme = 'https://'
    host = 'soundhub.che1.co.kr'
    activation_link = scheme + host + reverse('user:activate') + f'?activation_key={activation_key}'

    subject = '[Soundhub] Email Verification'
    message = ''
    html_message = f'Verify your email to login Soundhub: <a href="{activation_link}">activation link</a>'
    from_email = 'joo2theeon@gmail.com'
    return send_mail(
        subject=subject,
        message=message,
        html_message=html_message,
        from_email=from_email,
        recipient_list=recipient_list,
    )
```

## 2. stale user 처리

### 1. 문제인식 

이메일 인증 방식에 내재하는 잠재적 문제점은, 회원가입은 해두고 activation은 하지 않는 이른바 `stale user`가 생긴다는 점이다. 이 문제는 activation key info 클래스를 생성할 때마다 `stale user`를 삭제하는 방식으로 해결했다. 비동기 처리의 도입을 생각해보았으나, 서비스 규모가 일정수준 이상으로 커질 때까지는 그리 필요하지 않다고 생각되어서 나중으로 미뤄두었다. 

### 2. 대안 비교 및 문제해결 방법 선정

머릿속에 바로 떠오른 해결책은, celery의 비동기 처리를 통한 스케쥴러였다. 그런데 그 코드를 짜기가 너무 귀찮았다. 설정값도 많이 설정해야 하고, 무엇보다 셀러리 비동기 처리를 한 번 밖에 해보질 않아 머릿속에 바로 그려지지 않았다. 문서 찾으면서 작업하려니 너무 귀찮았다.

**그래서 떠오른 생각이 '이메일 인증 유저가 생성될 때마다 `stale user`를 삭제해주는 것'**이었다. 그러나 얼핏봐도 너무 비효율적이었다. `stale user`가 그렇게 자주 생성되지 않을 텐데, 매번 DB를 전부 도는 것은 바보 같은 해결책이라 생각했다. 그러나 그렇다고 비동기 처리를 하는 것은 여전히 귀찮았다.

**그래서 생각해낸 꼼수: 빈도수 설정하기.** `stale user` 삭제 로직이 5%의 확률로 일어나도록 했다. 이렇게 하면 비효율을 95% 감소 시킬 수 있었다. 나중에 실제 서비스를 구현했을 때, 빈도수는 `stale user`의 많고 적음에 따라 쉽게 변화시킬 수 있다. 따라서 변화에 대한 대응도 간단할 것 같았다.

빈도수를 구현하고 나니, **비동기 처리보다는 이게 훨씬 효율적이라는 사실을 알게 되었다.** 애초에 `stale user`는 이메일 인증 유저가 생성될 때 말고는 생성되지 않는다. 내가 주목했던 Activation Key Info가 생성될 때만 생성 가능성이 있다. 따라서 Activation Key Info 가 생성되지 않는다면 아예 `stale user`는 삭제할 필요가 없다. 비동기 처리는 일정 주기로 DB를 청소해주기 때문에, 새로운 유저 생성이 없어도 계속 작동하겠지만 내 코드는 다르다. 반대로 단기간에 `stale user`가 너무 많이 생성되어도 비동기 처리는 처리주기가 도래할 때까지 할 수 있는 것이 없다. 그러나 이 코드는 다르다. `active user`와 `stale user`의 통계적 비율만 안다면, 유저가 많이 생성될 때 많이 작동하고 유저 생성이 적을 때 적게 작동한다. 꽤나 마음에 든다.

그러나 한 가지 문제가 남아있었다. **DB에 쿼리를 날리는 과정이 오래걸리면, 사용자 회원가입도 오래걸린다는 것이다.** 나중에 이 서비스가 꽤나 커졌을 때, 회원가입하는 사람들의 5%는 불쾌한 속도 저하를 경험해야 할 것이다. 이 문제는 `stale user`를 삭제하는 로직을 별개의 함수로 만들고, celery를 붙여서 비동기 처리로 해결했다.

##### activation key info manager class

```python
class ActivationKeyInfoManager(models.Manager):
    def create(self, user):
        """
        1. stale user 삭제
        2. activation key & expired_at 자동 생성

        :param user: ActivationKeyInfo 와 연결될 유저 객체
        :return: 생성된 ActivationKeyInfo 객체
        """
        # A.K.I manager 를 생성할 때마다 stale user 를 삭제하는 것은 매우 비효율적이다. 
        # 따라서, 5%의 확률로 삭제한다.
        if randint(1, 20) == 1:
            # stale user 삭제 비동기 처리
            delete_staleuser.delay()

        ...

        return activation_key_info
```

##### delete_staleuser fuction

```python
@celery_app.task
def delete_staleuser():
    """
    A.K.I 가 생성된 유저를 조회하면서 stale user 를 삭제하는 메서드
    (stale user: 회원가입 후 이메일 인증을 하지 않은 채 오래 지난 유저)

    :return: None
    """
    # 이 함수가 users.models 에서 쓰이기 때문에, global 선언은 로드될 때 충돌을 야기한다.
    from users.models import ActivationKeyInfo

    for aki in ActivationKeyInfo.objects.all():
        if aki.user.is_active is False and aki.expires_at < timezone.now():
            aki.delete()
```

## 3. 테스트 코드를 위한 더미 클래스 생성

유저 파트를 개발하다 보니, 테스트 코드를 작성할 때 계속 유저를 생성해야 했다. activation key info 객체도 마찬가지다. 특히 유저 객체는 생성할 때마다 많은 정보를 입력해야 하고, `nickname`과 `email`이 모두 Unique해야하기 때문에 여러 유저를 생성하기가 불편했다.

이 문제를 해결하기 위해 더미유저 생성을 위한 정보와 생성 매서드를 포함하고 있는 클래스를 정의했다. 

### [더미 사용법]

##### dummy user 생성

```python
user = DummyUser().create()  # 더미 유저 한 개 생성
user1 = DummyUser(1).create()  # 더미 유저 한 개 생성 후 하나 더 생성
superuser = DummyUser().create_superuser()  # 관리자 권한 유저 생성
user_list = DummyUser().create_massive(10)  # 유저 10개 생성
```


##### dummy activation key info 생성

```python
aki = DummyActivationKeyInfo().create()  # 더미 AKI 생성
aki1 = DummyActivationKeyInfo(1).create()  # 더미 AKI 생성 후 하나 더 생성
aki = DummyActivationKeyInfo(user=user).create()  # 더미 AKI에 유저 할당하며 생성
aki_list = DummyActivationKeyInfo().create_massive(10)# 더미 AKI 10개 생성
```


### [더미 코드]

##### users.dummy module
```python
User = get_user_model()


# Test Code 작성시 필요한 dummy user 를 생성하는 클래스
class DummyUser:
    # 인스턴스 생성시 unique 한 필드를 생성하기 위해 'unique'를 받음
    def __init__(self, unique=''):
        self.EMAIL = f'dummy{unique}@gmail.com'
        self.PASSWORD = 'password'
        self.NICKNAME = f'dummy{unique}'
        self.INSTRUMENT = 'instrument'
	
    # 일반 유저 생성
    def create(self):
        return User.objects.create_user(
            email=self.EMAIL,
            nickname=self.NICKNAME,
            password=self.PASSWORD,
            instrument=self.INSTRUMENT,
        )
    # 관리자 권한 유저 생성
    def create_superuser(self):
        return User.objects.create_superuser(
            email=self.EMAIL,
            nickname=self.NICKNAME,
            password=self.PASSWORD,
            instrument=self.INSTRUMENT,
        )

    # 유저 대량 생산
    @staticmethod
    def create_massive(num):
        """
        생성할 유저 수를(num) 입력받아 유저를 생성하고 그 리스트를 반환한다. 
        num=10 이라면, dummy0 ~ dummy9 의 10개를 생성한다.
        """
        user_list = list()
        for i in range(num):
            user = DummyUser(str(i)).create()
            user_list.append(user)
        return user_list


# Test Code 작성시 필요한 dummy activation key info 를 생성하는 클래스
class DummyActivationKeyInfo:
    def __init__(self, unique='', user=None):
        self.dummy_user = DummyUser(unique)
        self.user = self.dummy_user.create() if not user else user

    def create(self):
        return ActivationKeyInfo.objects.create(
            user=self.user,
        )

    # dummy activation key info 대량 생산
    @staticmethod
    def create_massive(num):
        """
        생성할 AKI 수를(num) 입력받아 AKI를 생성하고 그 리스트를 반환한다. 
        """
        aki_list = list()
        for i in range(num):
            aki = DummyActivationKeyInfo(str(i)).create()
            aki_list.append(aki)
        return aki_list
```

## 4. 메일 발송 비동기 처리(celery)

회원가입시 인증메일을 보내는데, 이 과정이 5초 정도 걸린다. 더 나은 사용자 경험을 위해 비동기 처리가 필요하다고 생각했다. celery를 이용해 간단하게 구현했다. 

##### config.celery: 셀러리 설정

```python
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.deploy')

from django.conf import settings

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
```

셀러리 설정 중, autodiscover_tasks()가 프로젝트 내부에서 `tasks`라는 이름의 모듈을 불러온다. 그래서 만든 셀러리 메서드 패키지

```
tasks
├── __init__.py
├── mail.py
└── staleuser.py
```

##### utils.tasks.mail

```python
from django.core.mail import send_mail
from django.urls import reverse

from config import celery_app


__all__ = (
    'send_verification_mail',
    'send_confirm_readmission_mail',
    'send_verification_mail_after_social_login',
    'send_password_reset_mail',
)


@celery_app.task
def send_verification_mail(activation_key, recipient_list):
    ...
    

@celery_app.task
def send_confirm_readmission_mail(recipient_list):
    ...


@celery_app.task
def send_verification_mail_after_social_login(data, recipient_list):
    ...


@celery_app.task
def send_password_reset_mail(data, recipient_list):
    ...

```

## 5. 소셜로그인 - Facebook Login
  
### 1. 문제인식

**페이스북 사용자는 메일이 없다**: 그런데 우리 서비스에서는 이메일이 `username`을 대신하는 `unique field`이다. 구글 로그인의 경우, 무조건 gmail이 존재하기 때문에 문제가 발생하지 않는다. 구글 토큰에서 gmail 정보를 받고, 그 메일에 해당하는 유저를 찾아서 반환한다. 그러나 페이스북 로그인의 경우, 사용자의 메일 정보가 반드시 들어있는 것이 아니기 때문에 메일로 사용자를 특정할 수가 없다. 

### 2. 대안 비교 및 문제해결

페이스북 사용자를 특정하기 위해선 `facebook_user_id`값을 이용해야만 했다. 이것은 페이스북에서 `username` 대신 사용하는 `unique field`로, 구글의 메일과 같은 기능을 한다. 따라서 이 아이디 값과 유저를 대응시켜논 후, 토큰에서 얻은 아이디 값으로 유저를 찾아서 로그인 시켜주어야 한다. 

제일 먼저 떠오른 생각은 새로운 필드를 만드는 것이었다. 유저 필드에 `facebook_user_id`를 추가하고, 그 필드를 기준으로 유저를 찾는 것. 그러나 깊이 분석하지 않아도 너무 저차원적이고, 더러웠다. 페이스북으로 가입하지 않는 모든 유저에도 그 필드가 blank 또는 None 상태로 들어갈 것을 생각하니 불쾌했다. 그래서 `facebook_user_id` 값을 저장하긴 저장하되, 별도의 모델을 만들기로 했다. 

`FacebookUserInfo`라는 별도의 모델에 `facebook_user_id`를 저장해두고, 이 모델을 `User` 모델과 함께 `One to One`으로 묶어주었다. 또한 `facebook backend`를 따로 설정해서, `facebook_user_id`로  `authentication`이 가능하게 처리했다. 

### 3. 코드

##### Facebook User Info

```python
# 페이스북 유저의 Facebook User ID 를 저장하기 위한 모델
# Facebook Backend 에 사용된다
class FacebookUserInfo(models.Model):
    facebook_user_id = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

##### Facebook Backend

```python
# facebook user id 와 일치하는 유저 반환
class FacebookBackend:
    def authenticate(self, request, facebook_user_id):
        try:
            return FacebookUserInfo.objects.get(facebook_user_id=facebook_user_id).user
        except User.DoesNotExist:
            return None

    # 강사님도 아직까지 왜 이 메서드가 필요한지 모르겠다고 함. 문서에서 하라니 하는 것.
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```
```python
# 기본 인증 백엔드에 Facebook Backend 추가함
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.FacebookBackend',
]
```


## 6. 회원가입-로그인시 발생할 수 있는 모든 문제 해결

### [stale user 재로그인]

#### 1. 문제인식
회원가입을 했지만 이메일 인증은 하지 않은 어떤 유저를 가정하자. 한 일년 정도 지나면 자신이 회원가입을 했다는 것을 기억할리 없다. 데이터베이스에 이메일이 남아있기 때문에 다시 회원가입하는 것이 불가능하다. 이 문제를 해결하고자 했다.

#### 2. 해결방법
회원가입을 시도한 이메일이 존재하지만 활성화되지 않은 경우, activation key 의 만료기한을 새로고침 해준 후 인증메일을 다시 보내준다.  

#### 3. 코드

```python
class Signup(APIView):
    def get(self, request):
        ...

    def post(self, request):
        ...
        # 유저 타입 상수
        soundhub = User.USER_TYPE_SOUNDHUB

        email = request.data['email']
        # 전달된 이메일의 유저가 존재하는 경우
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # 소셜로그인 계정인 경우
            if not user.user_type == soundhub:
                ...
            # Soundhub 계정일 때
            elif user.is_active is True:
                raise RequestDataInvalid('이미 존재하는 유저입니다')
            elif user.is_active is False:
                # Activation key 만료 기한 재설정
                user.activationkeyinfo.refresh_expires_at()
                send_confirm_readmission_mail.delay([user.email])
                raise RequestDataInvalid('이메일 인증 중인 유저입니다. 메일을 확인해주세요.')
        ...
```


### [일반 회원가입 후 소셜 로그인]

어떤 회원이 gmail로 일반 회원가입을 한 뒤에 구글 소셜 로그인을 시도한다고 생각하자. 이미 존재하는 계정이 아니라 새로운 계정으로 접속이 되는 것은 소비자가 원하는 것이 아닐 것이다. 이메일이 하나라면, 계정도 하나여야 한다. 그래서 구글 로그인을 시도했을 때, 이미 존재하는 유저의 경우 기존 유저를 반환한다.

##### 구글 로그인

```python
class GoogleLogin(APIView):
    @staticmethod
    def post(request):
        ...

        # 이미 존재하는 유저일 경우 유저 생성 없이 기존 유저 반환
        if User.objects.filter(email=id_info['email']).exists():
            user = User.objects.get(email=id_info['email'])
            user.is_active = True
            user.save()
            data = {
                'token': user.token,
                'user': UserSerializer(user).data,
            }
            return Response(data, status=status.HTTP_200_OK)

        ...
```

### [소셜로그인 후 일반 회원가입]

반대로 소셜로그인을 시도한 후, 일반 계정으로 회원가입을 시도하는 경우이다. 이런 경우는 많이 없겠지만 굳이 만들지 않을 필요가 없어서 만들어 봤다. 소셜로그인과 일반 회원가입의 유일한 차이는 패스워드 존재 여부이다.

#### 1. 로직

1. 회원가입을 시도한 이메일의 계정이 존재하고 그 계정이 소셜계정이면
2. 회원가입시 입력한 패스워드 및 개인 정보와, 본인 여부를 판단할 hashcode를 암호화한다.
3. 암호화된 개인정보를 담은 '회원가입 완료' 링크를 메일로 보낸다
4. 사용자가 메일에 포함된 링크를 클릭한다
5. get parameter로 받은 암호화된 정보를 복호화한다. 
6. 그 정보를 토대로 원래 계정을 수정한다.

#### 2. 코드

##### 회원정보 암호화 후 메일 발송

```python
class Signup(APIView):
    def get(self, request):
        ...

    def post(self, request):
        ...
        
        # 유저 타입 상수
        soundhub = User.USER_TYPE_SOUNDHUB

        email = request.data['email']
        # 전달된 이메일의 유저가 존재하는 경우
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            # 소셜로그인 계정인 경우
            if not user.user_type == soundhub:
                # password 암호화
                encrypted_password = encrypt(
                    key=ENCRYPTION_KEY,
                    plain_text=request.data['password'],
                )
                # 유저의 activation key 새로 설정
                user.activationkeyinfo.refresh()
                # activation key info 암호화
                encrypted_activation_key = encrypt(
                    key=ENCRYPTION_KEY,
                    plain_text=user.activationkeyinfo.key,
                )
                data = {
                    'activation_key': encrypted_activation_key,
                    'nickname': request.data['nickname'],
                    'password': encrypted_password,  # password 암호화
                    'instrument': request.data['instrument'],
                }
                # 유저 정보를 담은 데이터와 함께 메일 발송
                send_verification_mail_after_social_login.delay(data, [user.email])
        ...
```

##### 회원정보 복호화 후 계정 정보 변경

```python
class Signup(APIView):
    def get(self, request):
        """
        1. 소셜로그인으로 생성된 유저가, Soundhub Signup 을 시도하는 경우 Signup.post() 함수에서 인증메일을 보내준다
        2. 인증 메일에는 Signup view 에 get 요청을 보내는 링크를 포함한다
        3. get parameter 로 전달된 정보를 사용해서
        4. 어떤 방식으로도 로그인할 수 있도록 Soundhub password 추가
        """
        # get parameter 에서 값 추출
        # 암호화된 activation key 와 password 복호화
        activation_key = decrypt(
            key=ENCRYPTION_KEY,
            encrypted_text=request.GET['activation_key'],
        )
        password = decrypt(
            key=ENCRYPTION_KEY,
            encrypted_text=request.GET['password'],
        )
        nickname = request.GET['nickname']
        instrument = request.GET['instrument']

        # activation key 에 해당하는 유저가 존재하는지 검사
        activation_key_info = get_object_or_404(ActivationKeyInfo, key=activation_key)
        # activation key 가 만료된 경우
        if not activation_key_info.expires_at > timezone.now():
            raise RequestDataInvalid('activation_key 의 기한이 만료되었습니다.')

        # 해당 유저 정보를 변경하고 저장
        user = activation_key_info.user
        user.nickname = nickname
        user.set_password(password)
        user.instrument = instrument
        user.save()

        data = {
            'token': user.token,
            'user': UserSerializer(user).data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        ...
```

##### 암호화 복호화 메서드

```python
def encrypt(key, plain_text):
    """
    :param key: 36 byte 길이의 문자열. 나중에 암호를 푸는데 사용된다.
    :param plain_text: 암호화하고 싶은 평문
    :return: 암호화된 byte 타입 데이터
    """
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plain_text))


def decrypt(key, encrypted_text):
    """
    :param key: 암호화에 사용되었던 36 byte 길이의 문자열
    :param encrypted_text: 암호화된 byte 타입 데이터
    :return: 복호화된 평문
    """
    # 암호문이 "b'1234'" 형태의 문자열로 오는 경우
    if type(encrypted_text) is str:
        encrypted_text = encrypted_text[2:][:-1].encode('utf-8')

    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8')
```





