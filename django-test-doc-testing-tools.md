



## SimpleTestCase [¶](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#simpletestcase)

*class* SimpleTestCase[[source]](https://docs.djangoproject.com/en/2.0/_modules/django/test/testcases/#SimpleTestCase)[¶](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase)

[unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)의 하위클래스로, 다음과 같은 기능을 더했다:

1. 몇가지 유용한 assertion:
2. [설정을 수정해서](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#overriding-settings) 테스트 실행하기
3. [`django.test.Client`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.Client) 를 대신할 [`self.client`](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase.client)

테스트가 데이터베이스에 쿼리를 날려야 한다면, TransactionTestCase 또는 TestCase 를 사용하자.

##### SimpleTestCase.allow_database_queries
SimpleTestCase 는 기본적으로 데이터베이스 쿼리를 허용하지 않는다. SimpleTestCase 가 transaction 내에서 실행되지 않기 때문에, 다른 테스트에 영향을 줄 수 있는 쿼리 실행을 피하기 위해서이다. 그러나 이런 문제가 걱정되지 않는 경우에는 `allow_database_queries=True`로 설정함으로써 무효화할 수 있다. 

> 참고: [Transaction 이란?](database-transaction.md)

##### 경고
SimpleTestCase 와 그 하위 클래스들은, `setUpCall()` 와 `tearDownClass()` 로 클래스 전체의 initialization 을 수행한다. 이 메서드들을 오버라이드할 때에는, `super()` 를 잊지 말자. 

```python
class MyTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ...

    @classmethod
    def tearDownClass(cls):
        ...
        super().tearDownClass()
```

setUpClass() 에서 exception 이 발생하면 파이썬이 어떻게 동작할지 알고 있어야 한다. 그 경우, 클래스에 있는 테스트는 물론이고 tearDownClass() 도 실행되지 않는다. django.test.TestCase 의 경우, super() 에 의해 생성된 transaction 을 누출시킨다(leak). 이것은 segmentation fault 를 포함한 다양한 증상을 발생시킨다. 만일 고의적으로 exception 을 발생시키고 싶다면, super() 함수를 호출하기 전에 하면 이런 문제를 예방할 수 있다. 



## TransactionTestCase [¶](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#transactiontestcase)

TransactionTestCase 는 SimpleTestCase 를 상속하고, 그것에 데이터베이스 관련된 특징을 추가했습니다:

1. 각각의 테스트 시작 전에 데이터베이스를 known state 로 되돌립니다. 이것은 ORM을 사용하는 것과 테스트하는 것을 용이하게 하기 위해서입니다. 
2. 데이터베이스 [fixtures](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures) 
3. [데이터베이스 백엔드에 따라서 테스트 생략하기](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#skipping-tests)
4. 특수한 [assert*](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerysetEqual) 메서드

> ##### database fixture 란?
> 테스트 데이터베이스에 기본 데이터를 로드하는데 사용되는 모듈중 하나이다. 자세한 것은 아래 링크를 참조하자.
> 
> - [Testing tools - Fixture loading](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures)
> - [Providing initial data - Providing data with fixtures](https://docs.djangoproject.com/en/2.0/howto/initial-data/#providing-initial-data-for-models)

TransactionTestCase 를 상속하는 TestCase 클래스가 더 일반적으로 사용된다. TestCase 클래스는 데이터베이스 Transaction을 이용하여, 각각의 테스트가 시작할 때 테스트 데이터베이스를 known state 로 되돌리는 작업의 속도를 높인다. 그러나 부수적인 결과로, 테스트할 수 없는 데이터베이스 behavior 가 존재한다. 예를 들어, 특정 코드가 transaction 안에서 실행되고 있는지 여부를 테스트할 수 없다. ([select
\_for\_update()](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.select_for_update)를 사용할 때 이런 테스트가 필요하다.) 이런 경우, TransactionTestCase를 사용해야 한다.

> 참고: [Transaction 이란](database-transaction.md)

TransactionTestCast 와 TestCase 는 데이터베이스를 known state 로 돌리는 방법과 commit 과 rollback 의 영향을 테스트 할 수 있는 가의 여부를 제외하면 완전히 일치한다. 

##### TransactionTestCase
- 매 테스트가 끝날 때마다 데이터베이스를 리셋하는데, 이때 모든 테이블을 삭제한다.
- 테스트 결과에 따라 commit 을 할 수도 있고, rollback 을 할 수도 있다. 그리고 그 여부와 그 결과가 데이터베이스에 미치는 영향을 관찰할 수 있다. 

##### TestCase
- 모든 테이블을 삭제하지는 않는다. 대신, 테스트 코드를 데이터베이스 transaction 안에 넣어서 테스트가 끝나면 rollback 시킨다. 테스트가 끝나고 rollback 이 진행되므로, 데이터베이스가 initial state 로 돌아가는 것이 보장된다.   
- 항상 Transaction 안에서 테스트를 실행하기 때문에, 특정 코드가 transaction 안에서 실행되고 있는지, transaction 없이 실행되고 있는지를 검사할 수 없다. 

> ##### 경고
> rollback 이 지원되지 않는 데이터베이스에서 돌아가는 TestCase, 그리고 TransactionTestCase 의 모든 인스턴스는 테스트가 끝나고, rollback 을 수행할 때, 테스트 데이터베이스의 모든 데이터를 지운다.
> 
> 데이터가 다시 로드되지 않는다. initial data reload 기능이 필요하다면, TestCase body 안에 `serialized_rollback = True`를 선언할 수 있다.
> 
> 참고: [Rollback Emulation](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#test-case-serialized-rollback)


## TestCase [¶](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#testcase)

장고 테스트에서 가장 일반적으로 사용되는 클래스이다. [TransactionTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase) 를 상속하고 있다. 테스트 하려는 장고 앱이 데이터베이스를 사용하지 않을 때에는, [SimpleTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase) 를 사용하자.

이 클래스는:

- 테스트를 두 개의 [atomic()]() block 으로 감싼다: 하나는 클래스 전체를 감싸고, 나머지 하나는 각각의 클래스를 감싼다. 그러므로 특수한 데이터베이스 transaction behavior 를 테스트할 때는 [TransactionTestCase](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TransactionTestCase) 를 사용하자. 
- 각각의 테스트 끝에 deferrable database constraints[^deferrable] 를 확인한다. 

[^deferrable]: 뭔소린지 모르겠다. 

이 클래스는, 추가적인 메서드를 제공한다: 

*classmethod* TestCase.setUpTestData()[[source]](https://docs.djangoproject.com/en/2.0/_modules/django/test/testcases/#TestCase.setUpTestData) [¶](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.TestCase.setUpTestData)

위에서 설명했던, class-level atomic() block 이 클래스 레벨의 initial data 의 생성을 허용한다. 이것은 한번에 TestCase 클래스 전체에 영향을 미친다. 이러한 방식의 테스트는 `setUp()` 을 사용했을 때보다 더 빠르다.  

> 여기서의 `setUp()` 은 `unittest.TestCase.setUp()` 을 가르킨다.

예를 들어:

```python
from django.test import TestCase

class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # TestCase 전체를 위한 데이터 set up
        cls.foo = Foo.objects.create(bar="Test")
        ...

    def test1(self):
        # set up 된 데이터 self.foo 를 이용한 테스트
        ...

    def test2(self):
        # set up 된 데이터 self.foo 를 이용한 또 다른 테스트
        ...
```

테스트가 transaction 이 지원되지 않는 데이터베이스에서 돌아가고 있다면, `setUpTestData()` 는 매 테스트가 실행 되기 전마다 실행된다. 이것은 속도를 느리게 한다는 점을 알아두자. (예를 들어 MyISAM engine 을 사용하는 MySQL 같은 데이터베이스들)

`setUpTestData()` 에서 생성된 객체는 어떤 것도 수정하지 않도록 주의하자. 클래스 레벨에서 셋업된 in-memory 객체를 수정하면, 그 정보가 지속적으로 남아 다른 테스트에도 영향을 주기 때문이다. 꼭 수정해야만 한다면, `setUp()` 메서드에서 [refresh\_from\_db()](https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model.refresh_from_db) 를 사용해 원래 정보를 reload 할 수 있다.








# TransactionTestCase vs TestCase


<a id='transactiontestcase-vs-testcase'></a>

## TransactionTestCase 와 TestCase 의 차이

##### TransactionTestCase
- 매 테스트가 끝날 때마다 데이터베이스를 리셋하는데, 이때 모든 테이블을 삭제한다. 따라서 initial data 는 첫 테스트에 한 번 적용되고 사라진다. 
- 테스트 결과에 따라 commit 을 할 수도 있고, rollback 을 할 수도 있다. 그리고 그 여부와 그 결과가 데이터베이스에 미치는 영향을 관찰할 수 있다. 

##### TestCase
- 모든 테이블을 삭제하지는 않는다. 대신, 테스트 코드를 데이터베이스 transaction 안에 넣어서 테스트가 끝나면 rollback 시킨다. 테스트가 끝나고 rollback 이 진행되므로, 데이터베이스가 initial state 로 돌아가는 것이 보장된다.   
- 항상 Transaction 안에서 테스트를 실행하기 때문에, 특정 코드가 transaction 안에서 실행되고 있는지, transaction 없이 실행되고 있는지를 검사할 수 없다. 







<a id="assertion"></a>

# Assertions



## unittest.TestCase [](https://docs.python.org/3/library/unittest.html#assert-methods)


### 가장 많이 사용되는 메서드

1. `assertEqual(a, b)`: `a == b`
2. `assertNotEqual(a, b)`: `a != b`
3. `assertTrue(x)`: `bool(x) is True`
4. `assertFalse(x)`: `bool(x) is False`
5. `assertIs(a, b)`: `a is b`
6. `assertIsNot(a, b)`: `a is not b`
7. `assertIsNone(x)`: `x is None`
8. `assertIsNotNone(x)`: `x is not None`
9. `assertIn(a, b)`: `a in b`
10. `assertNotIn(a, b)`: `a not in b`
11. `assertIsInstance(a, b)`: `instance(a, b)`
12. `assertIsNotInstance(a, b)`: `not instance(a, b)`


### 경고, 로그 관련 메서드

##### 1. exception 발생 여부 검사
- 메서드: `assertRaises(exc, func, *args, **kwargs)`
- 기능: `func(*args, **kwargs)`의 exception 발생 기능 검사

 
##### 2. 
































