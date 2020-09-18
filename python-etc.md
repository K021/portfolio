pep
언더스코어
맹글링
클래스메서드

- https://mingrammer.com/underscore-in-python/#3-특별한-의미의-네이밍을-하는-경우


## private name mangling

파이썬의 특정 클래스 변수를 외부에서 참조하지 못하게 하려면, `__` 더블스코어를 변수 앞에 붙여주면 된다. 

예를 들어, `Student`클래스에 `__score` 이라는 변수를 선언하면, 외부에서 해당 변수에 접근할 때에는, 내부적으로 변경된 `_Student__score` 라는 이름을 통해서만 접근할 수 있다. 파이썬은 기본적으로 '절대 참조할 수 없는 변수/메서드'는 존재하지 않고, 다만 실수로 접근하지 못하게만 해두었다.

외부적으로 쉽게 참조하거나 변경되면 안 되는 속성은 `__` 더블스코어를 붙여주고, 이를 참조하거나 변경하는 메서드를 따로 지정해주면 좋다. 

```python
In [148]: class Student:
     ...:     def __init__(self, name, score):
     ...:         self.name = name
     ...:         self.__score = score
     ...:
     ...:     def get_score(self):
     ...:         return self.__score
     ...:
     ...:     def set_score(self, score):
     ...:         self.__score = score
     ...:

In [149]: s = Student('john', 57)

In [150]: s._Student__score
Out[150]: 57

In [151]: s.get_score()
Out[151]: 57

In [152]: s.set_score(56)

In [153]: s.get_score()
Out[153]: 56

In [154]: s._Student__score = 58

In [155]: s.get_score()
Out[155]: 58
```


## 클래스 매서드의 종류

#### 1. 인스턴스 메서드
클래스 메서드에 아무 데커레이터도 없으면, 인스턴스를 받아오는 첫번째 인자를 선언해주어야 하는데, 관례적으로 `self` 라는 이름을 사용한다. 

```python
class Student:
	
   def __init__(self, name, score):
       self.name = name
       self.__score = score

   def get_score(self):
       return self.__score

   def set_score(self, score):
       self.__score = score
    
   def study()
```


## 인스턴스 변수와 클래스 변수

```python
class Test:
	cls_attr = 10
	def __init__(self, name):
		self.name = name

a = Test('katie')
a.name  # 인스턴스 변수
>>> katie

a.cls_attr  # 클래스 변수
>>> 10

Test.cls_attr  # 클래스 변수
>>> 10

# 인스턴스에서 클래스 변수를 바꾸려고 시도하면, 
# 클래스 변수가 바뀌는 것이 아니라 같은 이름의 인스턴스 변수가 생성된다.
# 해당 이름의 인스턴스 변수가 없을 때 클래스 변수를 참조하기 때문이다. 
a.cls_attr = 20	# 인스턴스 변수 새로 선언
a.cls_attr		# 인스턴스 변수 우선
>>> 20

# 클래스 변수는 변하지 않았다.
Test.cls_attr
>>> 10

# 인스턴스 변수와 클래스 변수의 이름이 중복될 떼
# 인스턴스에서 클래스 변수를 접근하려면 `__class__` 속성을 사용할 수 있다. 
a.__class__.cls_attr
>>> 10
```

## assert

> 참조 &mdash; <cite>[statkclee: 방어적 프로그래밍](http://statkclee.github.io/xwmooc-sc/novice/python/05-defensive.html)</cite>

방어적 프로그래밍(defensive programming)이란, 프로그램의 특정 함수의 인자 입력에 실수가 일어난다는 가정하에 이를 방지하는 코드를 짜는 것이다. 가장 일반적인 방식은 가정 설정문(assertions)으로, 이것은 프로그램의 특정 지점에서 항상 참이어야 하는 조건을 검사한다. 파이썬이 가정 설정문을 만나면, 가정 설정문의 조건이 참인지 확인한다. 참이면 아무것도 하지 않고, 거짓이면 즉시 프로그램을 정지시키고 미리 설정된 오류 메시지를 출력한다. 

> 파이어 폭스 웹브라우져 같은 프로그램은 가정 설정문(assertion)으로 가득차 있다. 코드의 10-20%는 다른 80-90%의 코드가 올바르게 동작하는지 확인하기 위해서 존재한다고 보면 된다.

###### 가정 설정문은 다음의 3가지 경우로 나눌 수 있다:
- **사전 조건**(precondition): 올바르게 동작하기 위해서 함수의 시작점에서 참이여 되는 것.
- **사후 조건**(postcondition): 함수가 끝날 때 참을 보증하는 것.
- 기타 **불변식**(invariant): 그 외에 코드 내부 특정한 지점에서 항상 참이어야 하는 것.

###### 가정 설정문의 문법은 다음과 같다:
```python
# assert 조건, 에러 메세지
def test(n):
	assert n >= 0, 'Data must not be smaller than 0'
	return n ** 0.5
```
```python
In [291]: test(4)
Out[291]: 2.0

In [292]: test(-4)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-292-d2bb95962d49> in <module>()
----> 1 test(-4)

<ipython-input-290-78f3e5ae1231> in test(n)
      1 def test(n):
----> 2     assert n >= 0, 'Data must not be smaller than 0'
      3     return n ** 0.5

AssertionError: Data must not be smaller than 0
```

###### 다음은 파이썬의 내장 모듈인 datetime 에 정의된 함수이다:
```python
# /usr/local/var/pyenv/versions/3.6.3/lib/python3.6/datetime.py
def _days_before_month(year, month):
    "year, month -> number of days in year preceding first day of month."
    assert 1 <= month <= 12, 'month must be in 1..12'
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))
``` 


## Python Source Code 파헤치기

> 참조: &mdash; <cite>[Python Documentation: Inspect Module](https://docs.python.org/2/library/inspect.html#retrieving-source-code)</cite>


### math.py 의 메서드는 왜 전부 pass? 

Pycharm 의 `navigate declaration`[^navigate] 기능을 사용해서 math 모듈을 검사하면, math.py 라는 것이 나오나, 메서드 안의 로직이 전부 `pass`로 채워져 있다. 이 math 모듈은 사실 파이썬의 구조를 이해할 수 있도록 Pycharm 에서 생성해준 가짜 파일이다. 진짜 모듈은 c 언어로 작성되어 있고, 이미 컴파일된 상태로 저장되어 있기 때문에 파이참에서 보여주기가 애매해서 그런 듯하다.

[^navigate]: `cmd + B` 또는 `cmd + click` 또는 포스터치를 통해, 특정 객체가 정의된 곳을 참조할 수 있는 기능. 


### math module 을 한번 찾아보자:

첫번째로, 모듈의 `__file__` 속성을 이용할 수 있다. 이 속성은 모듈의 file path 를 저장하고 있다. 모듈이 built-in 모듈일 경우에는 에러가 난다. 

```python
In [16]: import math

In [17]: math.__file__
Out[17]: '/usr/local/var/pyenv/versions/3.6.3/lib/python3.6/lib-dynload/math.cpython-36m-darwin.so'
```
`python3.6/lib-dynload/` 아래 있다는 것을 알 수 있다. 

```python
In [18]: inspect.getmodule(sys)
Out[18]: <module 'sys' (built-in)>

In [19]: sys.__file__
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-19-8e158a6bd20a> in <module>()
----> 1 sys.__file__

AttributeError: module 'sys' has no attribute '__file__'
```

두 번째로, [inspect](https://docs.python.org/2/library/inspect.html#retrieving-source-code) 모듈을 사용할 수 있다. 

```python
In [45]: inspect.getfile(math)
Out[45]: '/usr/local/var/pyenv/versions/3.6.3/lib/python3.6/lib-dynload/math.cpython-36m-darwin.so'

In [46]: inspect.getfile(celery.Celery)
Out[46]: '/usr/local/var/pyenv/versions/3.6.3/envs/testpython/lib/python3.6/site-packages/celery/app/base.py'
```


### builtin 모듈은 어디에 있는가?

python 의 built-in 모듈은 인터프리터에 내장되어있다. `sys.builtin_module_names` 로 built-in module 에는 무엇이 있는지 알 수 있다. 

```python
In [19]: import sys

In [20]: sys.builtin_module_names
Out[20]:
('_ast',
 '_codecs',
 '_collections',
 '_functools',
 '_imp',
 '_io',
 '_locale',
 '_operator',
 '_signal',
 '_sre',
 '_stat',
 '_string',
 '_symtable',
 '_thread',
 '_tracemalloc',
 '_warnings',
 '_weakref',
 'atexit',
 'builtins',
 'errno',
 'faulthandler',
 'gc',
 'itertools',
 'marshal',
 'posix',
 'pwd',
 'sys',
 'time',
 'xxsubtype',
 'zipimport')
```

### 추가적으로 조사할 링크
- [구글 검색: where is python math module](https://www.google.com/search?newwindow=1&client=safari&rls=en&ei=_X38W9-rI8PrvASXuLOwAw&q=where+is+python+math+module&oq=where+is+python+math+mo&gs_l=psy-ab.3.0.0i203.983437.986438..987321...4.0..1.213.1847.0j9j2......0....1..gws-wiz.......35i39j0i30j0i10i30j0i8i30j33i21j0i19.tkRw1l57LMY)
- [stackoverflow: Where can I inspect Python's math functions?
](https://stackoverflow.com/questions/5476189/where-can-i-inspect-pythons-math-functions)
- [stackoverflow: Where are math.py and sys.py?](https://stackoverflow.com/questions/18857355/where-are-math-py-and-sys-py)
- [python 2.7 document](https://docs.python.org/2/library/python.html)
- [stackoverflow: Finding the source code for built-in Python functions?
](https://stackoverflow.com/questions/8608587/finding-the-source-code-for-built-in-python-functions/8608609#8608609)
- [구글 검색: what is .so file?](https://www.google.com/search?client=safari&rls=en&q=what+is+.so+file&ie=UTF-8&oe=UTF-8)