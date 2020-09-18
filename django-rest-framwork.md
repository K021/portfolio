# Django REST Framwork


**Django REST Framework** (http://www.django-rest-framework.org)  

* `Django REST Framework`는 파이썬 패키지이다.  
* `Python instance`를 `json` 형식으로 바꿔서 전달해준다. 그 반대도 가능하다.  
* `Front End Framework`를 사용할 때, 정보를 제이슨 방식으로 전달하는데, 그때 사용된다. 
* 이와 같은 역할을 하는 패키지는 웹프레임워크에 따라 다르다. 장고의 경우 REST인 것.   


**CRUD**  (https://blog.remotty.com/blog/2014/01/28/lets-study-rest/)  
CRUD는 GET, PUT, POST, DELETE에 일대일로 매치되는 개념이다. Form 체계는 GET, PUT밖에는 되지 않아서 지금까지는 restful한 url을 사용하지 않았지만, CRUD 정보는 URI에 나타나면 안된다. URL은 같되, 메서드만 다르게 해야한다. 다섯번째 메서드에는 PATCH가 있다. (나중에 다룬다.) 
> **URI**: 통합 자원 식별자(Uniform Resource Identifier)로, 하위 개념에 URL, URN을 포함한다.  
> **URL**: (Uniform Resource Locator)  
> 
> url 자체가 모든 것을 나타낸다 = restful 하다 (https://ko.wikipedia.org/wiki/REST)  



**HTML 상태코드**: 상태코드를 받아서 처리하는 경우, 상태코드는 유용하다.  
200 성공 201 성공후 만들어짐 202 성공, 응답은 지금 주지 않는다 204 삭제되었을 때  
400 실패 401 로그인 안 됐을 때 403 권한이 없을 때. 404 페이지가 없을 때, 405는 잘못된 메서드 요청  
301 URI가 변경되었을 때  
500 서버의 문제가 있을 때.



## Tutorial 1  

> 이 튜토리얼은 syntax highlighter인 `pastebin`을 만드는 방법에 대해서 배운다. gist랑 비슷한 것.  


### 직렬화  
직렬화(直列化) 또는 시리얼라이제이션(serialization)은 데이터 구조나 오브젝트 상태를 동일하게 만들거나, 다른 컴퓨터 환경에 저장하고 불러올 수 있는 포맷으로 변환하는 과정이다.   


### Environment Setting  

> pygments: syntax highlighter package (http://pygments.org)  

* 가상환경: `pyenv virtualenv 3.6.3 fc-drf-pj`  
* 패키지: `pip install django`, `djangorestframework`, `pygments`  
* 설치환경 기록: `pip freeze > requirements.txt`  
* 장고 기본 설정:  
`django-admin.py startproject tutorial`, `./manage.py startapp snippets`  

	```python
INSTALLED_APPS = (
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
)
```


### Creating a Model  

* `pygments` 패키지의 `get_all_lexers`와 `get_all_styles`를 사용해 `Snippet`모델 생성,  
* `makemigrations`, `migrate`  


### Creating a Serializer Class  

**Serializer Class**  

* `Python instance`를 `json`으로, 또는 그 반대로 바꾸는데, 그 과정을 Serialize 또는 Deserialize 라고 한다.  
* 장고의 Form class와 비슷하게 동작한다. 
* `serializers.Serializer`를 상속받는 경우, `serialize`하려는 필드와 `create`와 `update` 메서드를 정의해주면 된다. (`create`과 `update` 메서드는 SerializerClass.save()를 할 때 호출된다. ModelSerializer에는 내장되어 있다. 특정 모델 인스턴스를 생성할 필요 없이 데이터 validation만을 위한 serializer라면 필요없다.) 
  
This works very similer to Django Form class. This includes validation functionality.   
피클을 사용할 때는 그냥 함수만 불러오면 된다. 파이썬만을 위한 파일형식으로 저장하는 것이기 때문이다. Serializer 여기서는 제이슨으로 바꾸는 것이기 때문에 중간 모델이 있어야 한다.

* `snippets` app에 `serializers.py` 생성  
* `rest_framework` 패키지의 `serializers.ModelSerializer`를 상속하는 클래스 생성

	> django `model form`이 그랬던 것 처럼, `ModelSerializer`을 사용하면 많은 것을 생략할 수 있다. 
> 
> * 연결할 모델과 필드를 선언만 하면, 자동으로 생성해준다.  
> * `create` 메서드와 `update` 메서드가 내장되어 있다.

	```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
```

### The Use of Serializer

**Serialization**  

`object` 생성  
`ObjectsoSerializer` 생성  
`s = ObjectSerializer(object)`  
`s.data`: python naive datatypes  
`json = JSONRenderer().render(s.data)`: json data

**Deserialization**  

`stream = BytesIO(json)`: `read()` 메서드가 있는 `stream` 형 객체로 변환  
`data = JSONParser().parse(stream)`  
`s = ObjectSerializer(data=data)`  
`s.is_valid()`: 외부 데이터에서 파이썬 객체를 만드는 경우에는 반드시 `validation`을 거쳐야 `.data`에 값이 저장된다. `validation` 결과가 불리언 값으로 반환된다.  
`s.data`: `validation` 결과에 상관 없이 들어온 데이터 값이 담긴다.  
`s.validated_data`: `validation`을 통과한 데이터.  
`s.save`: 











### Creating a Serializer Class   

제이슨으로 변환된 객체는 바이트형식이다.  
파일과 스트림형 객체는 같은 의미이다.  
바이트형 파일을 인메모리에서 `stream`형 객체로 다루고 싶을 때, `BytesIO`를 사용한다.    
`JSONRenderer()`: 파이썬 객체를 제이슨으로 만들어주는 것,  
`JSONParser()`: 제이슨을 파이썬 객체로 만들어주는 것  


### Postman

Chrome에서 Postman을 설치해준다. 브라우저에서는 POST나 DELETE 요청 같은 것을 보내기가 어렵다. 이걸 도와주는 프로그램이다. 

http://www.django-rest-framework.org/tutorial/2-requests-and-responses/