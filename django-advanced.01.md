
# Settings


## 장고에서 정적파일 다루기
> Static files, Media Files 다루기: 정적파일은 기본적으로 잘 변하지 않는 정보다.


### Django의 정적파일은 두 종류가 있다.

- Static files: javascript, css, image 파일 등의 고정 정보
- Media files: 이용자가 업로드하는 파일. 정적이지만 언제 추가될지 알 수 없다. 


### Settings.py의 Static file 관련 상수

`STATICFILES_DIRS`: 정적 파일이 저장된 디렉토리 리스트로, 개발단계에서 사용한다.  

```python
# 대개는 'static'이라는 한 폴더에서 관리한다. 
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
```

`STATIC_URL`: 정적 파일을 가리키는 URL의 최상위 경로이다. 실재 존재하지는 않는다. `STATIC_ROOT`에 지정된 경로를 참조한다.  

```python
# '/static/css/test.css/'와 같은 URL은 전부 Static file 경로로 해석한다.
# 문자열은 반드시 '/'로 시작해서 '/'로 끝나야 한다. 
STATIC_URL = '/static/'
``` 

`STATIC_ROOT`: Django에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로이다. Django 앱 폴더 안에 있는 `static`이라는 이름의 폴더와, `STATICFILES_DIRS` 경로에 있는 파일을 모은다. 모으는 명령어는 다음과 같다. `./manage.py collectstatic`  

`STATIC_ROOT`는 실서비스를 위한 설정 항목으로, 개발과정에는 필요하지 않다. 따라서 `DEBUG = False`일 때만 유효한 설정이다. (`DEBUG = True`인 경우는 `django.contrib.staticfiles`가 알아서 urlpattern를 변경해준다. 따라서 개발 단계에서는 `STATICFILES_DIRS`와 `STATIC_URL`만 신경쓰면 된다.)

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 장고 앱 폴더 경로
ROOT_DIR = os.path.dirname(BASE_DIR)  # 장고 프로젝트 폴더 경로
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
```


### Static file 을 다루는 명령어

- `./manage.py collectstatic`: static file을 한 곳으로 모아준다. 서비스 론칭 전에 해준다.
- `./manage.py findstatic <filename>`: static file 검색.  


### Settings.py의 Media file 관련 상수

`MEDIA_URL`: 미디어 파일을 가리키는 URL 최상위 경로이다. 실재하지는 않는다.  
`MEDIA_ROOT`: 미디어 파일이 저장되는 경로를 가리킨다.  

```python 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

`MEDIA_URL`은 urlpatterns를 따로 변경해주어야 한다. 

```python
(config.urls.py)
urlpatterns += static(
    settings.MEDIA_URL,  # media url 표시자를 인식하고,
    document_root=settings.MEDIA_ROOT,  # 이 경로에 저장하는 듯하다.
)
```



## Template

### 1. Post요청

**Post & get 정보는 QueryDic 형태**  
form 태그를 이용해 전송한 정보는 key:value `QueryDic`의 형태로 전송된다. 이때의 `key`는 `input` 태그의 `name`이, `value`는 기본값 혹은 `input` 태그의 `value` 속성이 전송된다.  

**Action 속성 기본값**  
form 태그의 action 기본값은, 현재 페이지이다.  

**Post / QuerySet 삭제: delete() 메서드**  
`ModelObject.delete()`: `Post.objects.get(pk=pk).delete()`  
`QuerySet.delete()`: `Post.objects.all().delete()`

<br><br>


## Views

1. **redirect**  
`redirect('/')`: 메인 페이지로 리다이렉트. `HttpReponseRedirect`의 단축형이다.
`redirect('post_detail', pk=post.pk)`: `view name`과 인자로 `view`를 바로 호출할 수도 있다.  

<br><br>


## et cetra
1. **REST Architecture (Representational State Transfer)**  
url 작성 구조로, url이 그 페이지의 기능을 효과적으로 나타내는 것을 목적으로 한다.
2. **Pillow**: 파이썬 이미지 라이브러리로, 장고가 이 패키지를 이용해 이미지 필드를 만든다.  
_ 설치: `pip install pillow`  
_ 사용(파이썬): `from PIL import Image`  

```python
# Pillow Usage Example
myimage = Image.open('filename')
print(myimage.format, myimage.size, myimage.mode)
>>> ('PNG', (512, 512), 'RGB')
```


<br><br>

---
# Models
-

### 1. Basic info  
**makemigrations**: ORM을 SQL로 바꿔준다.  
**migrate**: 그 SQL을 실행한다.  
**table name**: default=`ApplicationName_ModelName`, 변경가능  
**primary_key**:`id field` 자동생성, `primary_key=True` 옵션으로 내가 원하는 필드에 `primary_key` 배정 가능.  
**SQL type**: `setting.py/DATABASES/'default'/'ENGINE'`에 데이터베이스 관리 툴 정보가 저장되어 있다. 이 툴에 맞춰서 `ORM`을 변환한다.  

### 2. Using Models
**INSTALLED_APPS에 모듈입력**  
`model`을 사용하기 위해서는, 그 모델의 `models.py`가 포함되어 있는 `module`(applicaion folder) 이름을 `settings.py/INSTALLED_APPS`에 입력해줘야 한다.  

### 3. Fields
**field name**: model ORM에서 사용하는 메서드인 clean, save, delete 같은 것은 포함하지 않도록 한다.  
**field type**: 모든 field는 적절한 field class의 인스턴스여야 하는데, 이때 결정되는 field class의 type이 `data type`/`HTML widget`/`vailidation` 등을 결정하게 된다.  
**field classes**: `model field reference`에서 어떤 필드 클래스가 있는지 확인할 수 있고, 원하는 경우 커스텀을 만들 수 있다.  
**custom field**: 내부적으로는 CharField로 동작하지만, 입력할 때에는 전화번호/이메일 형식으로 입력하게 하는 필드를 만들 수 있다. 이런 필드 한 개짜리 오픈소스도 많다.  

### 4. Field Options
**field-specific arguments**: 각 필드는 특정한 인자를 받는데, 이는 [model field reference][mfr-fs]에 나와있다.  
**field-common arguments**: 필드에 관계없이 사용할 수 있는 인자도 있다. [model field reference][mfr-fc]

`null=True`: null 값이 들어갈 수 있음  
`blank=True`: 빈 문자열이 들어갈 수 있음 / admin에서 입력 비필수 필드 설정 (form validation 검사)  

`choice=<tuple_name>`: CharField를 체크박스로 바꾼다.

```python
class Person(models.Model):
	# tuple의 앞 부분은 DB에 입력되는 값, 뒷 부분은 form widget에 표시되는 값이다. 
	# 뒷 부분의 경우, get_<field_name>_dispaly()로 가져올 수도 있다. 
	# 앞부분의 경우, 대문자로 쓰는 것이 권장된다.
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
```python
>>> p = Person(name="Fred Flintstone", shirt_size="L")
>>> p.save()
>>> p.shirt_size
'L'
>>> p.get_shirt_size_display()
'Large'
```

<br><br>

## Relationship

recursive relationship: 재귀관계. 자신이 자신을 호출하는 것  
lazy relationship: 객체를 호출할 때, 객체 자체를 호출하는 것이 아니라 이름을 저장해두었다가 필요할 때 검색한다.

### 1. many-to-many field

`RelatedManager`를 통해 `added`, `removed`, or `created` 될 수 있다.

**attributes**  

