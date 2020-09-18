## 연습문제 링크
#### 기본
- [위키독스: 파이썬 300제 #클래스](https://wikidocs.net/7035)
- [위키독스: 파이썬 300제 #리스트](https://wikidocs.net/7023)

#### 심화
- [programmers: 코딩테스트 연습할 수 있는 곳](https://programmers.co.kr/learn/challenges)



# 리스트

### 선언
리스트의 선언은 두 가지 형태가 있다.

```python
l = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = [0, 1, 2, 3] 
```
빈 리스트를 선언할 때에는 빈 대괄호로 선언하는 것보다 클래스로 선언하는 것이 관례적으로 더 추천된다. 

```python
l = list()
l = []  # 써도 상관은 없음
```

# 리스트
- 선언 형태 두 가지
- 특징: 갯수 지정 필요 없음, 
서로 다른 타입의 원소 가능
- 리스트 comprehension, 원소 곱하기로 복사
- 메서드, 구문
  - len, 
  - index, 슬라이싱
  - del, pop, append, extend, 
  - sort, sorted,
  - in 으로 원소 확인
  - join
  - sum, max, min 등의 함수를 사용할 때 통째로 보내면 됨
  - unpacking 두 가지
  - map, filter
- 주의할 점
  - 레퍼런스 저장, 파라미터로 보낼 때, 리스트 복사하기
  - 곱하기로 복사할 때 이중 리스트


# 딕셔너리
- 선언형태 두 가지
- 특징: 키로 데이터 추출, 
키는 리스트 같은 거 빼고 되지만 주로 문자열, 
값에는 다 들어갈 수 있음.
- 메서드, 구문
  - len
  - 그냥 추가, 언패킹 추가



# 클래스

## 기본

#### 클래스 명은 카멜케이스
- 클래스 명은 카멜케이스, `NamedTuple`
- 함수 및 변수는 스네이크, `get_gross_number`
- 상수는 전부 대문자: `TIME_TABLE`


## 상속

### 클래스 선언과 상속
클래스의 기본 선언 형태는 다음과 같다.

```python
class ClassName(SuperClassName1, SuperClassName2):
	pass
```
`class` 문에 클래스 이름과 함께 괄호를 열고 상속하고자 하는 클래스 명을 적는다. 상속할 것이 없을 경우에는 함수와 다르게 괄호를 생략할 수 있다:

```python
class TestClass:
	pass
```
모든 클래스는 `object` 클래스를 상속하므로, 위 선언문은 다음과 정확히 일치한다.

```python
class TestClass(object):
	pass
```

### 상속시 초기화자 오버라이드
클래스를 상속할 때는 초기화자에 무언가 추가해야 하는 경우가 허다하다. 이런 경우 부모 클래스의 초기화자가 오버라이드 될 수 있으므로, 부모 클래스의 초기화를 같이 실행해주어야 한다. 

부모의 초기화는 `super().__init__(초기화 인자)`로 실행할 수 있다.

> `super(ParentClass, self).__init__(args)` 는 옛날 문법이니 사용하지 않는다.

```python
class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Man(Human):
	def __init__(self, name, age):
		super().__init__(name, age)
		self.sex = 'MALE'

# 인자를 키워드로 보낼 때는 등호 주변에 공백을 없애는 것이 관례다.
m = Man(name='Daniel', age=23) 
print(f'm: {m.name}, {m.age}, {m.sex}')
>>> m: Daniel, 23, MALE
```

부모 클래스의 초기화자가 어떤 인자를 받는지 정확히 알고 있다면 위와 같은 코드를 짤 수 있으나, 그렇지 않는 경우가 많다. 그리고 부모 크래스가 변할 수 있다는 점을 고려하면 다음과 같은 코드가 더 낫다:

```python
class Man(Human):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.sex = 'MALE'
```

### 다중 상속
> 상속은 보통 하나만 하는 경우가 많다.

```python
class Human:
	def __init__(self):
		self.place = 'Earth'
	@staticmethod
	def speed():
		return 100

class Korean:
	def __init__(self):
		self.place = 'Korea, Earth'
	@staticmethod
	def speed():
		return 200

class KoreanStudent(Korean, Human):
	def __init__(self, school='highschool'):
		Korean.__init__(self)  # super() 는 self 를 알아서 전달해준다.
		Human.__init__(self)  # 그냥 클래스를 사용할 때는 직접 전달해주어야 한다.
		self.school = school
		
	def __str__(self):
		return f'place: {self.place}, school: {self.school}'
```
상속하는 두 상위 클래스의 메서드 또는 속성 이름이 겹칠 때는, 먼저 상속한 (여기서는 `Korean`) 클래스의 메서드를 참조한다.

```python
student = KoreanStudent()
student.speed()
>>> 200
```

이런 참조 순서는 클래스의 `mro()` 메서드를 통해 확인할 수 있다. 

> mro: Method Resolution Order

```python
// 둘다 같은 것
KoreanStudent.mro()
student.__class__.mro()
>>> [__main__.KoreanStudent, __main__.Korean, __main__.Human, object]
```

하지만 `place` 속성은 순서가 뒤바뀌어 있다:

```python
student.place
>>> 'Earth'
```
이는 클래스의 초기화자에서 `Korean` 클래스가 먼저 초기화되기 때문에 `Human`에 의해 오버라이딩 된 것이다. 이 점을 고려하여 초기화해야 한다.



## 속성과 메서드

### 메서드의 종류
1. 인스턴스 메서드
	- 아무런 데커레이터도 없는 일반 메서드로, 첫번째 인자로 인스턴스를 받아야 한다. 
	- 첫번째 인자는 관레적으로 `self` 라는 이름을 사용한다.
2. 스태틱 메서드
	- 인스턴스 객체가 필요없을 때 사용하는 메서드로, `@staticmethod` 데코레이터를 붙여줘야 한다.
3. 클래스 메서드
	- 클래스 객체가 필요할 때 사용하는 메서드.
	- 첫번째 인자로 클래스 객체를 가져와야 한다. 관례적으로 `cls` 라고 한다.
	- `@classmethod` 데커레이터를 붙여야 한다.


```python 
class Human(object):
    created_count = 0

    def __init__(self, name, age, sex='Male'):
        self.name = name
        self.sex = sex
        self._age = age
        self.create_count()

    def get_age(self):
        return self._age

    def increase_age(self, years=1):
        self._age += years

    @staticmethod
    def cry():
        print('응애응애')

    @staticmethod
    def speak(word):
        print(f'{word}')

    @classmethod
    def create_count(cls):
        cls.created_count += 1

    @classmethod
    def get_num_of_humans(cls):
        return cls.created_count
```

### 클래스 속성과 인스턴스 속성
- 클래스는 인스턴스를 대량 생산하기 위한 틀과 같은 것이고, 인스턴스는 그 틀에 맞게 생산된 객체이다. 
- 클래스 속성은 모든 인스턴스들이 공유하고,
- 인스턴스 속성은 해당 인스턴스에서만 접근할 수 있다.
- 인스턴스 속성와 클래스 속성의 이름이 겹칠 때, 인스턴스 속성이 우선된다. 
	- 이 경우 인스턴스에서 클래스 속성에 접근하기 위해서는 `instance.__class__.class_prop` 과 같이 접근할 수 있다. 

	
```python
class Test:
    cls_attr = 10
    def __init__(self, name):
        self.name = name

a = Test('Katie')
a.name  # 인스턴스 변수
>>> Katie

a.cls_attr  # 클래스 변수
>>> 10

Test.cls_attr  # 클래스 변수
>>> 10

# 클래스 속성은 모든 인스턴스에서 공유한다.
a2 = Test('jason')
a2.cls_attr
>>> 10

# 인스턴스에서 클래스 변수를 바꾸려고 시도하면, 
# 클래스 변수가 바뀌는 것이 아니라 같은 이름의 인스턴스 변수가 생성된다.
# 해당 이름의 인스턴스 변수가 없을 때 클래스 변수를 참조하기 때문이다. 
a.cls_attr = 20 # 인스턴스 변수 새로 선언
a.cls_attr      # 인스턴스 변수 우선
>>> 20

# 클래스 변수는 변하지 않았다.
Test.cls_attr
>>> 10

# 인스턴스 변수와 클래스 변수의 이름이 중복될 떼
# 인스턴스에서 클래스 변수를 접근하려면 `__class__` 속성을 사용할 수 있다. 
a.__class__.cls_attr
>>> 10

a.__class__.cls_attr = 30  # 클래스 변수 변경

# a 의 인스턴스 변수는 변하지 않고,
# 클래스 변수가 변했고,
# 클래스 변수는 모든 인스턴스가 공유한다.
a.cls_attr, Test.cls_attr, a2.cls_attr
>>> 20, 30, 30
```


### 프라이빗 맹글링

파이썬에는 기본적으로 접근 불가능한 속성 또는 메서드가 없다. 그러나 실수를 방지하기 위해 접근이 까다롭게 만들어 놓은 것이 있다.

1. `_` 하나를 앞에 붙인 변수 (컨벤션)
	- 모듈 임포트시 로드되지 않는다.
	- 객체 속성 메서드 참조시 검색이 안 된다.
	- 보통 이런 속성은 직접 불러오거나 변경하지 않고, `getter`, `setter` 함수를 만든다.
2. `__` 언더스코어 두 개를 앞에 붙인 변수 (맹글링)
	- 파이썬 인터프리터가 해당 변수 이름 앞에 `_ClassName` 을 붙여 변수 명을 바꾼다.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

s = Student('john', 57)

s._Student__score
>>> 57

s.get_score()
>>> 57

s.set_score(56)

s.get_score()
>>> 56

s._Student__score = 58

s.get_score()
>>> 58
```

### 매직 메서드

언더스코어 두개로 감싸진 메서드를 매직 메서드라고 부른다. 클래스 내에서 특별한 기능을 담당한다. 대표적으로 다음 메서드가 있다

- `__init__(self)`: 인스턴스가 생성될 때 호출되는 초기화자 메서드 
- `__eq__(비교대상)`: 동등 연산자 연산 결과를 반환하는 메서드
- `__str__()`: 해당 클래스의 인스턴스를 문자열로 변환한 결과를 반환하는 메서드

> 이 외에도 다양한 매직 메서드들이 있다. 다음을 참조하자  
> 
> - <cite>[school of web: 파이썬 - OOP Part 6. 매직 메소드](http://schoolofweb.net/blog/posts/파이썬-oop-part-6-매직-메소드-magic-method/)</cite>
> - <cite>[코리카츄의 개발블로그: 파이썬 더블 언더스코어: Magic Method](https://corikachu.github.io/articles/python/python-magic-method)</cite>


## 네임드 튜플

튜플을 사용하고 싶은데, 인덱스가 아닌 속성으로 참조하고 싶고, 클래스를 만들자니 크기가 너무 작은 것들을 관리할 수 있다. 

```python
from typing import NamedTuple

class Human(NamedTuple):
	name: str  # 자료형 설정은 설정도, 사용도 의무가 아니다. 참조일 뿐.
	age: int = 3  # 기본값 설정

h = Human(name='Daniel', age=34)
h.name, h.age
>>> ('Daniel', 34)
```


# 언더스코어

#### 1. 인터프리터(Interpreter)에서 마지막 값을 저장하고 있음
```python
>>> 3
3
>>> _
3
```

#### 2. 무시하고 싶은 값
```python
for _ in range(10):
	print('hello')

x, y, *_ = [1, 2, 3, 4, 5]
x, y, _
>>> (1, 2, [3, 4, 5])
```

#### 3. 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할때
- private 속성, 메서드
- 예약어와 겹칠 때
	- 특정 변수의 이름을 `map_` 이라고 할 수 있는데, 이것은 예약어인 `map` 함수와 충돌을 방지하기 위한 것이고, 종종 사용된다. 
- 매직 메서드

#### 4. 숫자 리터럴 값의 자릿수 구분
```python
1_000_000
>>> 1000000
```