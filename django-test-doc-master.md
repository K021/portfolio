<h1 class='header'><span>Django test</span></h1>


## 관련 문서

##### 장고 공식 문서 (내가 정리한 문서 / 관련 공식 문서)
- [django test tutorial](django-test-tutorial.md) / [Tutorial - Testing](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)
- [django test document master](django-test-doc-master.md) - 현재 문서 / [Testing in Django](https://docs.djangoproject.com/en/2.0/topics/testing/), [Writing and running tests](https://docs.djangoproject.com/en/2.0/topics/testing/overview/)
- [django test document - testing tools](django-test-doc-testing-tools.md) / [Testing tools](https://docs.djangoproject.com/en/2.0/topics/testing/tools/)
- 미정 / [Advanced testing topics](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/)

##### 개인 정리 문서
- [Django initial data](django-initial-data.md)
- [Database Transaction](database-transaction.md)
- [Pytest - Django test third-party package](django-test-pytest.md)






# 장고에서 테스트하기 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/)

> <cite>[Testing in Django](https://docs.djangoproject.com/en/2.0/topics/testing/)</cite>

현대 웹개발자에게, 자동화된 테스트는 대단히 유용한 디버그 도구이다. 다양한 문제를 해결하기 위해 테스트 묶음을—[test suite](https://en.wikipedia.org/wiki/Test_suite)—사용할 수 있다:

> **테스트 묶음(test suite)**: test case 의 묶음으로, 테스트 하려는 프로그램이 특정 작동들(set of behaviour)을 하는 것을 보이기 위해 필요한 테스트 모음이다. 예를 들어, DB 인덱스를 구축할 때 오류가 나지 않는지를 검사하기 위해 A, B, C 세 가지의 test case 가 필요하다면, 그 세가지 test case 의 묶음을 test suite 라고 하는 것.  
> — <cite>[wikipedia](https://en.wikipedia.org/wiki/Test_suite)</cite>

- 새로운 코드를 작성할 때, 코드가 예상한대로 작동하는지 검증할 수 있다.
- 예전 코드를 수정할 때, 수정된 코드가 예상 밖의 문제를 발생시키지는 않는지 검사할 수 있다. 

웹 어플리케이션 테스트는 꽤나 복잡한 작업이다. 어플리케이션에 여러 논리 구조가 겹겹이 쌓여있기 때문이다 - HTTP 수준의 request 처리에서 프로세스 검증, 그리고 템플릿 렌더링 까지. 장고의 테스트 프레임워크와 다양한 유틸리티를 사용하면, request 시뮬레이션과 테스트 데이터 입력, 어플리케이션 출력값 검사를 수행할 수 있고, 일반적 수준에서 코드가 의도대로 동작하는지를 검증할 수 있다. 

가장 좋은 점은, 그런 과정이 매우 간단하다는 것이다. 

장고에서 테스트 코드를 작성할 때, 파이썬 기본 라이브러리에 내장되어 있는 [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) 모듈을 사용하길 추천한다. 이에 관한 자세한 내용은 [테스트 코드 작성하고 실행하기](https://docs.djangoproject.com/en/2.0/topics/testing/overview/)에서 다룬다. 

원한다면 다른 파이썬 테스트 프레임워크를 사용할 수도 있다. 장고는 그런 경우를 위한 도구들과 API를 통합적으로 지원한다. 이에 관한 자세한 내용은 [고급 테스트 주제](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/)의 [별도의 테스트 프레임워크 사용하기](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#other-testing-frameworks) 항목에서 다룬다.

- [테스트 코드 작성하고 실행하기](https://docs.djangoproject.com/en/2.0/topics/testing/overview/)
- [테스트 도구](https://docs.djangoproject.com/en/2.0/topics/testing/tools/)
- [고급 테스트 주제](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/)







# 테스트 코드 작성하고 실행하기 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#module-django.test)

> ##### 참고문서
> - [테스트 튜토리얼](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)
> - [테스트 도구 레퍼런스](https://docs.djangoproject.com/en/2.0/topics/testing/tools/)
> - [고급 테스트 주제](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/)

이 문서는 두개의 기본적인 부분으로 나뉩니다. 첫째, 장고에서 어떻게 테스트 코드를 작성할 것인가를 설명합니다. 그리고 나서, 어떻게 실행할 것인지를 설명합니다. 

## 테스트 작성하기 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#writing-tests)

장고의 유닛 테스트는 파이썬 기본 모듈을 사용합니다: [unittest](https://docs.python.org/3/library/unittest.html#module-unittest). 이 모듈이 테스트를 정의하는 방식은 클래스 기반입니다.

아래의 예는 [django.test.TestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)를 상속하는 하위 클래스입니다. [django.test.TestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)는 독립적으로 돌아가는 transaction 내에서 테스트를 실행하는 [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)의 하위 클래스 입니다. 

> **Transaction**: Transaction processing is information processing in computer science that is divided into individual, indivisible operations called transactions. Each transaction must succeed or fail as a complete unit; it can never be only partially complete.  
> — <cite>[wikipedia](https://en.wikipedia.org/wiki/Transaction_processing)</cite>  
> 
> 참고: [Transaction](database-transaction.md)

```python
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
```

테스트를 [실행하게 되면](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#running-tests), 테스트 유틸리티는 'test'로 시작하는 파일을 모두 검사하여, 그 안에 정의된 모든 test case를 찾아냅니다. ([unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)의 하위 클래스) 그리고 그 test case 안에 있는 test suite 를 빌드하고, 실행합니다. (역자 주: test suite 는 test case class 안에 있는 함수들을 의미하는 것 같다.) 

[unittest](https://docs.python.org/3/library/unittest.html#module-unittest)에 관한 자세한 정보는, 파이썬 문서를 참조하자.

> ##### 테스트 코드를 어디에 둘까?
> 
> 기본 [startapp](https://docs.djangoproject.com/en/2.0/ref/django-admin/#django-admin-startapp) template 은 새 장고 애플리케이션을 생성할 때 `tests.py` 파일을 만든다. 수행할 테스트가 얼마 없을 때는 이것으로 충분하다. 그러나 test suite 가 많아서 체계적으로 관리하고자 한다면, `test_models.py`, `test_views.py`, `test_forms.py`와 같이 하위 모듈로 나누어 테스트를 관리할 수 있다. 어떤 구조로 정리할지는 편한대로 선택하면 된다.
> 
> [Django test runner를 사용해 테스트를 재사용 할 수 있는 애플리케이션 만들기](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#testing-reusable-applications)를 참조하자.

> ##### 경고
> 
> 만일 테스트가 데이터베이스에 접근해야 한다면(모델을 만들거나 쿼리하는 것 처럼), 반드시 [django.test.TestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)를 상속하도록 하자. [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)를 상속한다면 문제가 생길 수 있다.
> 
> [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)를 사용하면, 개별적인 테스트들을 transaction 내에서 실행하고 각각의 데이터베이스를 날려버림으로 초래하는 위험를 피할 수 있다. 그러나 만일 우리의 테스트가 데이터베이스와 상호작용하는 경우, 테스트가 실행되는 순서에 따라 테스트 결과가 영향받을 수 있다. 이 경우, 독립적으로 돌아갈 때는 통과하지만, suite 에서 돌아갈 때는 실패하는 테스트가 발생할 수 있다. 



## 테스트 실행하기 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#running-tests)

테스트를 작성했다면, `manage.py` 유틸리티의 `test` 명령으로 실행할 수 있다:

```bash
(manage.py 파일이 있는 디렉토리에서)
$ ./manage.py test
```

테스트 파일 검색은 unittest 모듈의 [내장 테스트 발견](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) 기능을 기반으로 한다. 기본값은 현재 작업 디렉토리 하위에 있는 모든 파일 중 'test*.py' 파일들을 찾아내는 것이다. 

원한다면 실행하려는 테스트를 지정할 수 있다. 테스트 라벨을 `./manage.py test` 다음에 적어주면 된다. 테스트 라벨은 파이썬 타입의 절대 경로로(full python dotted path), 패키지, 모듈, TestCase 의 하위클래스, 또는 테스트 메서드가 될 수 있다:

```bash
# animals.tests 안에 있는 모든 테스트 실행하기
$ ./manage.py test animals.tests

# animal 패키지 안에 있는 모든 테스트 실행하기
$ ./manage.py test animals

# 하나의 test case 만 실행하기
$ ./manage.py test animals.tests.AnimalTestCase

# 하나의 테스트 메서드만 실행하기
$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak
```

테스트 코드를 검색할 디렉토리를 지정할 수도 있다. 

```bash
$ ./manage.py test animals/
```

테스트 파일 이름 `test*.py` 형태가 아니라면, `-p` 또는 `--pattern` 옵션으로 custom filename pattern 을 지정할 수도 있다. 


```bash
$ ./manage.py test --pattern="tests_*.py"
```

테스트 실행 중 `Ctrl+C`로 중단을 시도한다면, test runner는 현재 실행중인 테스트를 완료한 후에 우아하게 종료된다. 우아한 종료시, test runner 는 테스트 결과를 출력하고(테스트 실패 상세, 실행된 테스트 수, 발생한 에러와 실패 수) 하던대로 데이터베이스를 지운다. 따라서 [--failfast](https://docs.djangoproject.com/en/2.0/ref/django-admin/#cmdoption-test-failfast) 옵션을 잊었을 때에는 `Ctrl+C` 옵션이 매우 유용할 수 있다. (몇몇 테스트는 예상치 못한 실패가 일어나는 경우가 있고, 모든 테스트가 끝나기 전에 상세한 오류 정보를 얻고 싶은 경우가 있다는 것에 주목하자.)

> `--failfast`: 첫번째 오류가 발생하자마자 종료하는 옵션

현재 실행 중인 테스트가 완료되길 기다리고 싶지 않을 경우, `Ctrl+C`를 두 번 입력하면 즉시로 종료되지만, 우아하지는 않을 것이다. 테스트 결과 상세가 출력되지 않고, 생성된 데이터베이스가 삭제되지도 않는다. 

> ##### 경고를 활성화한 채로 테스트 하기 
> 파이썬 경고를 활성화한 채로 테스트를 하는 것도 좋은 생각이다: `python -Wall manage.py test`. `-Wall` 은 파이썬의 Deprecation Warning 을 보여주는 옵션이다. 다른 많은 파이썬 라이브러리와 마찬가지로 장고도 이 경고를 사용해 앞으로 없어질 feature 를 알려준다. 완전 틀린 것은 아니지만 더 나아질 수 있는 코드도 알려준다. 

> **Deprecation**: 여러 분야에서 특정 용어나 특성, 도안, 또는 관행이 앞으로 없어지거나 무효화 될 것이기 때문에 그것을 사용하는 것을 지양하길 바라는 것을 의미한다. (주로 새로운 것으로 대체되는 경우가 많다) Deprecation Warning 은 특정 프로그래밍 코드가 새로운 버전에서 더 이상 사용되지 않을 예정일 때 제공되는 경고이다.  
> — <cite>[wikipedia](https://en.wikipedia.org/wiki/Deprecation), [Janis Lesinskis' Blog](https://www.lesinskis.com/python_deprecation_tutorial.html)</cite>

---

### 1. 테스트 데이터베이스 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#the-test-database)

데이터베이스가 필요한 테스트는 배포에 사용할 진짜 데이터베이스를 사용하지 않는다. 별도의 빈 데이터베이스가 생성된다. 

테스트의 성공 여부와 관계없이 테스트 데이터베이스는 모든 테스트가 실행된 후에 삭제된다. 

테스트 데이터베이스가 없어지지 않기를 바란다면 [`test --keepdb`](https://docs.djangoproject.com/en/2.0/ref/django-admin/#cmdoption-test-keepdb) 옵션을 사용할 수 있다. 이 옵션을 사용하면, 테스트 실행 사이사이에 데이터베이스를 보존한다. 데이터베이스가 없는 경우에는 먼저 생성된다. 최신 정보를 반영하기 위해 모든 migration 이 적용된다. 

테스트 데이터베이스 이름의 기본값은 `settings.py` [DATABASES](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES) 안에 선언된 각각의 [NAME](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME) 값 앞에 `test_`를 덧붙인 것이다. SQLite 을 사용한다면, in-memory 데이터베이스를 기본값으로 사용한다. (즉, 데이터베이스가 파일시스템을 완전히 우외하여 메모리에 생성된다.) [DATABASES](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES) 안에 있는 [TEST](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-TEST) 딕셔너리를 선언하면 테스트 데이터베이스에 필요한 다양한 설정을 제공할 수 있다. 예를 들어, 별도의 테스트 데이터베이스 이름을 설정하고자 한다면, [TEST](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-TEST) 딕셔너리 안의 [NAME](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME) 값을 설정해주면된다. 

PostgreSQL 을 사용하는 경우에는, [USER](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER) 가 내장 postgres 데이터베이스에 읽기 권한이 있어야 한다.

별도의 데이터베이스를 사용하는 경우를 제외하면, test runner는 settings.py 파일에 기록된 데이터베이스 설정을 그대로 사용한다.([ENGINE](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-ENGINE), [USER](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER), [HOST](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-HOST)) 테스트 데이터베이스는 [USER](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER)에 설정된 유저로 생성된다. 그러므로 해당 유저가 새로운 데이터베이스를 생성할 권한이 있는지 확인해야 한다.

테스트 데이터베이스의 문자 인코딩을 설정하려면, TEST의 [CHARSET](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEST_CHARSET) 옵션을 사용하자. MySQL을 사용한다면, 특정한 collation 을 관리하기 위해 [COLLATION](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEST_COLLATION) 옵션을 사용할 수 있다. 이러한 고급 검색을 자세히 알아보려면 [settings 문서](https://docs.djangoproject.com/en/2.0/ref/settings/)를 참고하자.

> **Character Set**: 문자기호와 인코딩 값의 일대일 대응 정보의 집합. (예: A -> 0000, B -> 0001)  
> **Collation**: 문자끼리 비교하는 방법의 집합. (예: 인코딩 값을 비교해 일치 여부를 판단한다, A와 a는 같은 문자로 판단한다)  
> — <cite>[MySQL.com](https://dev.mysql.com/doc/refman/8.0/en/charset-general.html)</cite>

SQLite in-memory database 를 사용한다면, SQLite 3.7.13+ 버전부터 [캐쉬 공유 설정](https://www.sqlite.org/sharedcache.html)이 가능하므로 스레드간 데이터베이스를 공유하는 기능을 테스트할 수 있다. 

> ##### 프로세스
> - 실행 중인 프로그램의 인스턴스.
> - 운영체제로부터 프로페서, 주소 공간, 메모리 등의 자원을 할당받는다. 
> 
> ##### 스레드
> - 한 프로세스 내에서 동작하는 여러 실행의 흐름으로,
> - 프로세스 내의 자원들을 대부분 공유한다. 다른 스레드와도 자원을 공유한다.
> - 기본적으로 하나의 프로세스가 생성되면 하나의 스레드가 같이 생성된다. 이를 메인 스레드라고 부르며, 스레드를 추가로 설정하지 않는 한 모든 프로그램은 메인스레드에서 실행된다. 스레드를 추가하는 경우, 프로세스는 여러 스레드를 가지게 되며, 이를 멀티스레드라고 한다.  
> - 스레드간 통신이 프로세스간 통신보다 훨씬 간단하다. (별도의 자원을 이용하지 않고, 전역 변수 공간을 이용하여 데이터를 주고 받을 수 있다.)
> - 스레드간 메모리를 공유하기 때문에, 충돌이 생길 수 있다.
> 
> — <cite>[강관우의 브런치](https://brunch.co.kr/@kd4/3), [진형아빠이야기](http://ralf79.tistory.com/34)</cite>

> ##### 테스트를 실행 중, 배포용 데이터베이스에서 데이터 가져오기?
> 모듈이 컴파일되는 동안 데이터베이스에 접근하는 코드가 있다면, 테스트 데이터베이스가 준비되기 전이기 때문에 이런 일이 발생한다. 이는 예상치 못한 결과를 가져올 수 있다. 예를 들어, 모듈 단위의 코드에 데이터베이스 쿼리가 존재하고, 진짜 데이터베이스(배포용 데이터베이스)가 존재한다면, 그 데이터가 테스트를 오염시킬 수 있다. 이런 import-time 데이터베이스 쿼리를 사용하는 것은 아주 안 좋은 생각이다. 이런 일이 발생하지 않게 코드를 다시 짜자.
> 
> 이 사례는 커스텀 [ready()](https://docs.djangoproject.com/en/2.0/ref/applications/#django.apps.AppConfig.ready)를 사용하는 경우에도 적용된다.  
>
> `AppConfig.ready()`: [레지스트리](https://docs.djangoproject.com/en/2.0/_modules/django/apps/registry/)가 작성 완료되자마자 실행되는 함수로, 모듈레벨에서 임포트할 수 없는 모델을 이 함수를 통해 임포트 할수 있다. 원하는 기본값으로 ready() 함수를 커스텀해주면 된다.
> 
> ##### 참고
> [고급 다중 데이터베이스 테스트 주제](https://docs.djangoproject.com/en/2.0/topics/testing/advanced/#topics-testing-advanced-multidb) 

---

### 2. 테스트 실행 순서 [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#order-in-which-tests-are-executed)

모든 TestCase 코드가 깨끗한 데이터베이스[^clean]로 실행되는 것을 보장하기 위해서, 장고 test runner 는 다음과 같은 방식으로 테스트 순서를 재배열한다:

- 모든 [TestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase)의 하위클래스가 먼저 실행된다. 
- 그 후에, 장고 베이스의 테스트는 특별히 정해진 순서 없이 실행된다. ([SimpleTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase) 또는 [TransactionTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase)의 하위 클래스)
- 그리고 나서 [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)의 하위 테스트 중, 데이터베이스를 변경할 것으로 보이는 테스트들이 실행된다. (doctests 를 포함해서)

[^clean]: 원문: 'clean database'

> ##### 알아두기
> 
> 테스트 순서 재배열은, test case 순서에 대한 예상치 못한 의존성을 찾아낼 수 있습니다. 예를 들어 TransactionTestCase test 에서 생성된 데이터베이스에 영향을 받는 doctest 가 있는 경우 의존성 문제가 발생할 수 있습니다. 이런 경우는 반드시 독립적으로 실행될 수 있도록 업데이트 되어야합니다.

[test --reverse](https://docs.djangoproject.com/en/2.0/ref/django-admin/#cmdoption-test-reverse) 옵션으로 그룹 내의 실행 순서를 뒤집을 수 있습니다. 이것을 통해 우리의 테스트가 각각 독립적으로 실행되는지 여부를 확인할 수 있습니다. 

<hr class="clear">

> ##### doctest 란?
> `doctest`는 함수의 기능을 설명해두는 docstring 안에 대화형 파이썬 세션처럼 보이는 텍스트가 있는지를 검색한 후, 해당 세션들을 실행하여 텍스트에 써진대로 정확히 동작하는지를 확인한다.
> 
> 다음은 docstring 에 대화형 파이썬 세션 형태의 문자열이 있는 경우이다. 
> 
> ```python
> def square(x):
>     """Return the square of x.
>     
>     >>> square(2)
>     4
>     >>> square(-2)
>     4
>     """
> 
>     return x * x
> ``` 
> 
> 다음의 코드를 실행하면, docstring 내에 작성된 대로 작동하지 않는 경우에는 경고를 해준다.
> 
> ```python
> import doctest
> doctest.testmod()
> ```
> 
> 다음은 doctest 에서 오류가 난 경우이다
> 
> ```python
> In [1]: def square(x):
>    ...:     """Return the square of x.
>    ...:
>    ...:     >>> square(2)
>    ...:     4
>    ...:     >>> square(-2)
>    ...:     4
>    ...:     """
>    ...:
>    ...:     return x
>    ...:
> 
> In [2]: import doctest
> 
> In [3]: doctest.testmod()
> **********************************************************************
> File "__main__", line 4, in __main__.square
> Failed example:
>     square(2)
> Expected:
>     4
> Got:
>     2
> **********************************************************************
> File "__main__", line 6, in __main__.square
> Failed example:
>     square(-2)
> Expected:
>     4
> Got:
>     -2
> **********************************************************************
> 1 items had failures:
>    2 of   2 in __main__.square
> ***Test Failed*** 2 failures.
> Out[3]: TestResults(failed=2, attempted=2)
> ```
> — <cite>[파이썬을 여행하는 히치하이커를 위한 안내서 - 테스트 코드 작성하기](http://python-guide-kr.readthedocs.io/en/latest/writing/tests.html)</cite>

---

### 3. Rollback 기능 구현(emulation) [¶](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#rollback-emulation)

migrations 를 통해 최초로 로드된 데이터는 어떤 것이든지[^initial-data], TestCase test 에서만 사용가능하고, TransactionTestCase test 에서는 사용할 수 없습니다. 그리고 이것은 transaction 이 지원되는 backend 에서만 사용가능합니다. (가장 대표적인 예외가 MySQL 의 MyISAM 스토리지 엔진입니다.)
[LiveServerTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.LiveServerTestCase) 또는 [StaticLiveServerTestCase](https://docs.djangoproject.com/en/2.0/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase)와 같은 TransactionTestCase 하위의 클래스에도 적용됩니다. 

> 참고: [Django initial data](django-initial-data.md), [Transaction](database-transaction.md), [TransactionTestCase 와 TestCase 의 차이](temp.03.md#transactiontestcase-vs-testcase)

[^initial-data]: 원문: 'any initial data loaded in migrations'

장고에선 그 정보를 test case 마다 다시 불러올 수 있다. TestCase 또는 TransactionTestCase 의 body[^body] 안에  `serialized_rollback=True` 옵션을 추가하면 된다. 하지만 이 옵션은 해당 test suit 를 약 3배 정도 느리게 만든다는 점을 기억하자. (TestCase 의 경우에도, non-transactional database 에서 돌아간다면 이런 설정이 필요할 수 있다.)

> ##### serialized_rollback=True 옵션이 하는 일은?
> 이 옵션은 데이터베이스에 기록되어 있는 initial data 를 serialize 하여 문자열로 저장합니다. 나중에 그 문자열을 다시 읽어들여 rollback 기능을 수행합니다. migration 시 기록된 데이터를 사용해야 한다면 반드시 적용해줘야 하는 옵션입니다. ([Rollback 이란?](database-transaction.md))
> 
> ##### serialization 이란?
> 데이터 구조 또는 객체의 상태에 관한 정보를, 저장 또는 전송할 수 있는 특정 형식으로 변환하는 것을 말합니다. 결과물로 생성된 일련의 비트 정보는 serialization format 에 따라 다시 읽혀져 원래 객체와 실질적으로 완전히 일치하는 또 다른 객체를 만드는데 사용됩니다. 쉽게 말하면, 서로 다른 언어를 사용하는 둘 이상의 시스템 사이에 데이터를 교환하기 위해, 모든 시스템이 이해할 수 있는 언어로 데이터를 기록하는 것을 의미합니다.  
> 
> — <cite>[wikipedia](https://en.wikipedia.org/wiki/Serialization) 참조</cite>

[^body]: 옵션을 추가하라는 것은, 해당 테스트의 클래스 변수 `serialized_rollback` 을 `True` 로 선언하라는 것.

Third-party app 을 사용하거나, MyISAM 으로 개발하는 경우에는 이 옵션을 설정해야 한다. 그러나 일반적으로는, transactional database 로 개발하는 것이 좋고, 대부분 테스트에 TestCase 를 사용하는 것이 좋다. 

initial serialization은 대개 매우 빠르게 이루어진다. 그러나 이 과정에서 제외하고 싶은 app 이 있다면, settings 모듈 변수 [TEST\_NON\_SERIALIZED\_APPS](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TEST_NON_SERIALIZED_APPS)에 추가하면 된다. (약간 더 빨라진다)

serialized data 가 두 번 로드되는 것을 방지하기 위해서, serialized_rollback=True 설정은 테스트 데이터베이스를 지울 때, [post\_migrate](https://docs.djangoproject.com/en/2.0/ref/signals/#django.db.models.signals.post_migrate) signal 을 무효화한다. 

---

### 4. 다른 테스트 조건들

장고 설정 파일의 DEBUG 설정과 상관 없이, 장고 테스트는 `DEBUG=False` 로 실행된다. 테스트하려는 코드의 결과가 production 설정에서 보이는 것과 일치하도록 하기 위해서이다. 

데이터베이스와 다르게, 별도의 '테스트 캐쉬'라는 것이 없다. 따라서 production 상태에서 테스트를 실행하면, live system 캐쉬에 데이터가 입력된다. 테스트가 완료되어도 캐쉬들은 사라지지 않는다. 이런 특징은 나중에 [바뀔 수도 있다.](https://code.djangoproject.com/ticket/11505)

---

### 5. 테스트 결과 이해하기

테스트를 실행하게 되면, test runner 가 준비되는 동안 나오는 메세지를 볼 수 있다. 이 메세지가 얼마나 상세하게 나올지를 정할 수 있는데, 커맨드 라인에 `verbosity` 옵션을 사용하면 된다. 

```bash
Creating test database...
Creating table myapp_animal
Creating table myapp_mineral
```

앞에서 설명한 것과 같이 테스트 데이터베이스를 만드는 것을 볼 수 있다. 

테스트 데이터베이스가 만들어지면, 장고는 테스트를 실행한다. 아무런 문제가 발생하지 않았다면, 다름과 같은 것을 보게된다:

```bash
----------------------------------------------------------------------
Ran 22 tests in 0.221s

OK
```

실패한 테스트가 있다면, 테스트 실패에 관한 상세한 정보를 볼 수 있다:

```bash
======================================================================
FAIL: test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/dev/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_poll
    self.assertIs(future_poll.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)
```

이 에러 출력문에 관한 자세한 설명은 이 문서의 범위를 벗어난다. 그러나 상당히 직관적이기 때문에 이해하는 데 어려움이 없을 것이다. 자세한 설명은 파이썬의 [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) 라이브러리 문서를 참조하자. 

오류가 발생했다면, 그 갯수에 상관없이 test runner 의 리턴 값[^return-code]은 항상 `1` 이다. 모든 테스트가 성공한 경우에는 `0` 이 된다. 이 특징은 test runner 를 shell script 내에서 사용하고, 그 레벨에서 테스트 성공여부를 판단하는 경우에 유용하다.  

[^return-code]: 원문: 'return code'

> ##### shell script 란?
> Unix shell, 곧 command-line interface 에서 한 줄 한 줄 실행할 수 있도록, 명령줄을 모아놓은 파일을 말한다. 
> 
> 스크립트가 무엇인지 알면 이해하기가 더 쉬워진다. 스크립트란, 컴파일 없이 인터프리트(interpret)
방식으로 동작하는 프로그램을 의미한다. 쉽게 말해 컴파일을 통해 별도의 실행 파일을 만들 필요 없이, 텍스트 형식으로 저장되는 프로그램으로서, 한 줄씩 순차적으로 읽고 실행하도록 작성된 프로그램이다. 파이썬 스크립트, js 스크립트, 쉘 스크립트 같은 것이 있으며, 쉘 스크립트는 쉘 프로그램으로 읽고 실행하도록 작성된 프로그램 파일이다.  
> 
> — <cite>[wikipedia](https://en.wikipedia.org/wiki/Shell_script), [Tae-ho blog - 쉘 스크립트란 무엇인가](http://blogger.pe.kr/320)</cite>

---

### 6. 테스트 속도 빠르게 하기

##### 여러 테스트를 동시에 실행하기
테스트들이 충분히 독립적이고 하드웨어가 멀티 코어라는 전제 하에, 한 번에 여러 테스트를 실행함으로써 속도를 높일 수 있다. [test --parallel](https://docs.djangoproject.com/en/2.0/ref/django-admin/#cmdoption-test-parallel) 을 참고하자.

> ##### --parallel 옵션과 python exception traceback
> 
> `--parallel` 옵션을 사용하는 경우, 파이썬 traceback 을 정확히 표시하기 위해선, 서드파티 패키지인 `tblib` 를 설치해야 한다. 
> 
> ```bash
> pip install tblib
> ```
> 
> 그렇지 않으면, 장고에서 exception traceback 를 표시하지 못할 수 있다. 이런 경우가 발생하면 해당 테스트를 parallelization 없이 다시 실행하는 것도 방법이다. 
> 
> ##### Python Exception Traceback 이란
> traceback 모듈은 에러 메시지를 만들기 위해 call stack 을 사용한다. (call stack 은 프로그램 코드의 실행 순서를 저장하는 정보라고 생각하면 쉽다.) traceback 은 exception handler 에서 부터 그 exception 을 발생하게 한 call 까지의 과정을 보여준다. (주로 예외 처리에 사용되지만, 일반 스택을 살펴보는데 사용할 수도 있다)  
> 
> 아래는 traceback 표시의 예이다.
> 
> ```bash
> Traceback (most recent call last):
  File "traceback_print_exc.py", line 20, in <module>
    produce_exception()  # 이게 exception 을 발생시킨 call
  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception
    produce_exception(recursion_level-1)
  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 16, in produce_exception
    produce_exception(recursion_level-1)
  File "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/traceback/traceback_example.py", line 18, in produce_exception
    raise RuntimeError()  # 이게 exception handler
RuntimeError
> ```
> 
> — <cite>[Pymotw.com - Traceback](https://pymotw.com/2/traceback/)</cite>

##### 비밀번호 hashing

기본 패스워드 hasher 는 느리게 설계되어 있다. 테스트에서 인증해야 할 유저가 많다면, custom settings file 을 사용하고[^custom-settings-file], [PASSWARD_HASHERS](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD_HASHERS) 설정을 더 빠른 알고리즘으로 바꾸자.

[^custom-settings-file]: 왜 custom settings file 을 사용하라고 했는지 모르겠다. 테스트만을 위한 설정 파일을 만들라는 건가 싶은데, 장고의 어떤 문서에서도 그것을 설명하는 곳은 없어 보인다. TestCase class 내에서 settings 정보를 오버라이드 하거나 변경할 수 있는 메서드는 있지만, 파일에 해당하는 것은 없는 것 같다. 

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
```

만약 fixture 에서 사용하는 hashing algorithm 이 있다면, 빠뜨리지 말고 [PASSWARD_HASHERS](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD_HASHERS) 에 포함하자. (새로운 패스워드를 hashing 하는데 사용되는 hasher 는 PASSWARD_HASHERS 의 첫 번째 hasher 뿐이지만, 이미 존재하는 어떤 패스워드가 특정 hasher 로 변환되었을 경우, 그것을 읽는데 그 hasher 가 필요하다.)

> 참고: [Farhan Ahmad - Using custom settings in django tests](https://thebitguru.com/blog/784-using-custom-settings-in-django-tests)


##### 테스트 데이터베이스 보존하기

`test --keepdb` 옵션을 사용하면 테스트를 진행하는 동안 테스트 데이터베이스를 보존할 수 있다. 생성과 삭제를 생략할 수 있기 때문에 테스트 실행 속도가 빠르다. 










