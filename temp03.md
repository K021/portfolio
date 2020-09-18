


<h1 class='header'><span>temp.03</span></h1>



##### 할일
1. 장고 테스트 문서 만들기
2. 테스트 코드 작성하기
3. 성구 검색 디비 완성하기
4. 형을 위한 크롤러 주석 및 정리해서 보내주기
5. 블로그 파기
6. 장고 번역문서 커밋하기

##### 휴식
1. 은경이 프론트 강의 듣기





# Python


## Interning

> 자료: [길롯 블로그 - python string interning](http://guilload.com/python-string-interning/)

### 1. 파이썬에선 변수가 담고 있는 값이 같으면 변수의 주소도 같다?

파이썬은 효율성을 위해 간단한 문자열 또는 숫자를 미리 저장해둔다. 이를 `interning`이라고 한다. 

> - `intern`: 전쟁 또는 정치적인 이유로, 범죄사실의 증명이 없음에도 사람을 가두어 두다. 
> - `interning`은 파이썬에 국한되지 않고, 현대 객체 지향 언어에서 두루 사용되는 방식이다. ( Python, PHP(5.4이상), Lua, Ruby, Java etc.)


### 2. interning 사례

> - `interning`을 확인하기 위해선, 변수의 주소값을 확인해야 한다. 서로 다른 변수가 같은 두 값을 가지고 있을 때, 각 변수의 주소값이 일치하는 것으로써 `interning`을 확인할 수 있다.  
> - python 에서 객체의 주소를 확인할 수 있는 함수는 `id()`이다. (이 함수는 c 타입의 주소, 곧 진짜 메모리 주소를 반환한다.)
> - 명시적인 주소값의 확인 없이도, 연산자 `is`를 통해 주소값의 일치를 확인할 수 있다. 

```python
# 간단한 문자열의 일치
a = 'asdf'
b = 'asdf'

hex(id(a))
>>> '0x10ecbb420'
hex(id(b))
>>> '0x10ecbb420'

a is b
>>> True

# 간단한 숫자의 일치
a = 123
b = 123

hex(id(a))
>>> '0x10b6e14e0'
hex(id(b))
>>> '0x10b6e14e0'

a is b
>>> True
```


### 3. interning 예외 사례

```python
a = 'asdf!'
b = 'asdf!'
a is b
>>> False

a = 1.23
b = 1.23
a is b
>>> False
```


### 4. 강제 interning

```python
import sys
a = sys.intern('asdf!')
b = sys.intern('asdf!')

a is b
>>>True
```


### 5. interning 의 장점

- 메모리 절약
- 비교 연산 효율성 증가 (`O(n)`->`O(1)`)  
	문자열을 비교할 때, 바이트 단위로 비교할 필요 없이, 포인터만 비교하면 된다.  
 

### 6. native interning 의 조건

##### 공통
`immutable value` 즉, 불변값이어야 한다.

##### 숫자
: `[-5, 256]` 의 정수

##### 문자열
1. 길이가 `0` 또는 `1` 인 모든 문자열
2. `NAME_CHARS` 이외의 문자를 포함한 경우 제외
	
	```python
	NAME_CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
	
	'foo' is 'foo'  # True
	'foo!' is 'foo!'  # False
	```
3. 컴파일이 아닌 실행시 선언되는 변수 제외
	
	```python
	'foo' is ''.join(['f', 'o', 'o'])  # False
	'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'  # True
	
	# 연산 후 문자열 길이가 20이 넘어가면 제외된다.
	'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'  # False
	
	# 그냥 문자열 길이가 20이 넘는 것은 괜찮다.
	'foooooooooooooooooooooooooooooo' is 'foooooooooooooooooooooooooooooo'
	```






# Django Source Code

## `QuerySet._for_write`

> facebook django group 에 질문했던 내용




# Django Migration

- [Rollback emulation](https://docs.djangoproject.com/en/2.0/topics/testing/overview/)

<hr class='clear'>

- google 'django difference between TestCase and TransactionTestCase'
- [django doc - TransactionTestCase](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#transactiontestcase), [django doc - TestCase](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#testcase)
- [django tutorial - Part5: testing](https://docs.djangoproject.com/en/2.0/intro/tutorial05/)

<hr class='clear'>

- facebook answer: google 'django initial data'
- [providing initial data for models](https://docs.djangoproject.com/en/2.0/howto/initial-data/) 의 [providing initial data with migrations](https://docs.djangoproject.com/en/2.0/howto/initial-data/#providing-initial-data-with-migrations)
- [data migration](https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations)
	- [RunPython](https://docs.djangoproject.com/en/2.0/ref/migration-operations/#runpython) 
		- [SchemaEditor](https://docs.djangoproject.com/en/2.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor)

<hr class='clear'> 



# Django


## model 과 migration

##### 1. 처음 마이그레이션엔 기본값이 필요없다
처음 migration 에는 default 값이 필요가 없다. 그 다음 마이그레이션부터는 기본값이 필요하다. 데이터베이스의 생성여부는 중요하지 않다. 

##### 2. 데이터베이스를 지우면 다시 마이그레이트 해주어야 한다.
중간에 오류가 생기면 데이터베이스를 지우고 다시 생성하는 일이 빈번한데, migrate 를 잊으면 테이블이 없다는 말이 뜬다. 


## 오류: 테이블이 없습니다 / 칼럼이 없습니다

```bash
OperationalError: no such table: scripture_verse  
OperationalError: no such column: scripture_verse.book_name
```
변경된 사항이 잘 마이그레이션 되었는지 확인하자. 그리고 `shell_plus`를 다시 실행하는 것도 잊지 말자. 데이터베이스를 밀어버린 경우에도 다시 마이그레이션 해주어야 한다. 



# Nginx Error

## Ubuntu-Nginx, 13 Permission Denied

##### Error Message:  
```
PermissionError at /admin/post/image/3/change/  
[Errno 13] Permission denied: '/srv/pdxen-homepage-pj/pdxenhomepage/media'
```

##### 원인 및 문제 해결
`nginx user`인 `deploy`가 `media` 폴더에 접근 또는 변경 권한이 없기 때문이다. `media` 폴더가 없으면 만들어주고, 디렉토리 유저를 recursive하게 변경하자.

```bash
sudo chown -R deploy:deploy /srv/pdxen-homepage-pj/pdxenhomepage/media
```

> ububtu nginx user 확인하기: `sudo vi /etc/nginx/nginx.conf`


## attempt to write a readonly database  ## Error Message:
```
OperationalError at /todo/add/
attempt to write a readonly database
```
`db.sqlite` 의 user 가 ubuntu 이고, 유저만 쓰거나 변경할 수 있도록 설정되어 있기 때문이다. (`-rw-r--r--`) 다음과 같이 db.sqlite 의 유저를 uwsgi 유저인 `deploy` 로 변경해주면 된다.

```bash
sudo chown deploy:deploy /srv/todo-management/todo/db.sqlite3
```
이것을 마쳐도 아래의 에러가 날 것이므로, `db.sqlite`의 상위 폴더의 유저도 변경해주자. 

```bash
sudo chown deploy:deploy /srv/todo-management/todo/
```

## unable to open database file
```
OperationalError at /todos/add/
unable to open database file
```
위 에러를 해결하면 발생하는 오류로, `db.sqlite` 의 상위 폴더의 접근권한이 없는 경우이다. 이 경우, 해당 상위 폴더의 유저를 변경해준다. 

```bash
sudo chown deploy:deploy /srv/todo-management/todo/
```


# HTML


## background

##### HTML 문법 유효성 검사
- 작성된 html 문서가 웹표준에 맞는지 검사해준다.
- 검사 도구 (Validator): [validator.w3.org](https://validator.w3.org/)

##### entitycode: 
HTML 이나 XML 과 같은 마크업 문서에서, 일련의 특수한 문자를 나타내는 문자 조합으로, Character Reference 라고 불린다. 이것은 다음의 두 가지로 나뉜다:

1. numeric character reference: 숫자로 기호를 나타내는 것 (`<`=`&#60;`)
2. character entity reference: 문자로 기호를 나타내는 것 (`<`=`&lt;`)

> entity code table: [entitycode.com](http://entitycode.com/)


## tag

##### 이미지
- `img`: 이미지 태그
	- `src`: 이미지 주소
	- `alt`: 이미지가 없을 때 대체하는 텍스트. 시각장애인에게 제공되는 정보이기도 하다. 
- `figure`: 도표, 차트, 이미지, 표 등을 감쌀 때 사용되는 요소
- `figcaption`: 해당 피규어의 정보를 담고 있는 태그




# Database


## Transaction


##### Transaction 이란

transaction 이란, 데이터베이스를 변경하는 작업의 단위이다. transaction 은 다음 네 가지 질의어(sql) 요청으로 구성되어 있다:

1. select
2. insert
3. update
4. delete


##### Transaction 의 특성

transaction 은 다음 네 가지 특성을 지닌다:

1. 비분리성 (Atomicity): 데이터베이스는 transaction 단위로 변경된다. transaction 을 구성하는 일부 쿼리만 반영되는 경우는 없다. transaction 전체가 반영되거나 반영되지 않거나이다. 
2. 일관성 (Consistency): transaction 이 대상으로 하는 데이터베이스는 일관적이어야 한다. transaction 중 데이터베이스에 변경이 있어도, 그 변경사항이 반영되지 않는다.
3. 독립성 (Isolation): 한 transaction 이 다른 transaction 의 연산에 끼어들 수 없다.
4. 영구성 (Durability): 한번 반영된 transaction 은 영구히 반영된다. 

각각의 첫 글자를 모아, 이 성질을 ACID 라고 부르기도 한다. 이론적으로 데이터베이스 시스템은 각각의 transaction 에 대해 상기 성질들을 보장하지만, 실제로는 성능을 위해 종종 무시되기도 한다. transaction 을 지원하는 데이터베이스를 transactional database 라고 한다. 대부분 관계형데이터베이스가 해당된다.  


##### transaction 의 실행과정

- Begin the transaction
- Execute several queries: 쿼리를 실행하고 변경된 데이터를 만든다. 그러나 데이터베이스에 적용하지는 않는다.
- Commit the transaction: 변경된 데이터를 데이터베이스에 적용한다. 


##### Commit 과 Rollback

transaction 이 완료되면 commit, 중간에 취소되거나 오류가 발생하여 처음으로 되돌리는 경우에는 Rollback.

- commit: transaction 의 쿼리가 성공하면, 변경된 데이터를 데이터베이스에 적용하는 연산. 
- rollback: transaction 이 비정상적으로 종료된 경우, transaction 을 처음부터 다시 시작하거나, 진행된 transaction 을 취소하는 연산. 이것은 DBMS 설정에 따라 다르다. 사용자가 원하는 경우, transaction 은 commit 전에 언제든지 rollback 을 진행할 수 있다.  

> DBMS: Database Management System 의 약자로, 데이터베이스를 수정하고 저장, 관리할 수 있는 소프트웨어이다. Mysql, Postgresql 등이 있다.


##### Transaction 의 상태

- Active
- Failed: 오류가 나서 실패
- Aborted: 중지되어 rollback 연산 실행
- Partially committed: transaction 이 완료되었으나 commit 되지 않은 상태
- Committed: 완료후 데이터베이스에 적용까지 된 상태

— <cite>[wikipedia](https://ko.wikipedia.org/wiki/데이터베이스_트랜잭션), [개발자 홀로 서기](http://mommoo.tistory.com/62), [limkydev](http://limkydev.tistory.com/100)</cite>

## B tree




# ETC

## Big-O notation

> Big-O notation: refers to the complexity of a given algorithm. In computer science, big O notation is used to classify algorithms according to how their running time or space requirements grow as the input size grows.

인풋 아웃풋의 기울기를 말한다고 보면 된다. 