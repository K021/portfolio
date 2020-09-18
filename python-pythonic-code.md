
## 문자열 앞을 0으로 채우기

```python
'3'.zfill(5)
>>> '00003'

'4'.rjust(5, '*')
>>> '****4'

s = 'abc'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```

## 문자열 공백 제거

#### 1. 처음과 끝의 공백문자 제거
```python
'\n\t so what?  '.strip()
>>> 'so what?'
```

#### 2. 모든 스페이스(`' '`) 제거
```python
"  what's up man ".replace(' ', '')
>>> "what'supman"
```

#### 3. 모든 공백문자 제거
```python
''.join(' hello world  \t\n'.split())
>>> 'hello world'
```


## map, filter, reduce

##### map 

이터레이터의 각 원소를 함수에 넣은 이터레이터를 만든다. 

```python
# list(map(함수, 이터레이터))
# relation = [[1,2,3],[4,5,6],[7,8,9]] 일 때,
# cols = [[1,4,7],[2,5,8],[3,6,9]] 가 된다.  
cols = list(map(list, zip(*relation)))
```

##### filter

이터레이터의 각 원소 중 조건식을 통과한 원소의 이터레이터를 만든다.

```python
# list(filter(불리언 반환 함수, 이터레이터))
ft = [8, 7, 4, 2, 1, 7, 4, 3, 6, 8, 9, 11, 3, 12]
list(filter(lambda x: x > 5, ft))
```

##### reduce

```python
# reduce(두 원소를 받는 함수, 이터레이터)
# 결과가 이터레이터로 나오지 않음
a = [1, 2, 3, 4, 5]
reduce(lambda x, y: 2*x - y, a)
= 57
```


## 코드 실행시간 간단하게 검사하기

```python
# The "timeit" module lets you measure the execution
# time of small bits of Python code

>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)

0.3412662749997253

>>> timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)

0.2996307989997149

>>> timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)

0.24581470699922647

>>> import timeit
>>> timeit.timeit('l.index(999_999)', setup='l = list(range(0, 1_000_000))', number=1000)
9.356267921015387
>>> timeit.timeit('l.index(999_999, 999_990, 1_000_000)', setup='l = list(range(0, 1_000_000))', number=1000)
0.0004404920036904514
```




## 딕셔너리 value 로 sort 하기

```python
# How to sort a Python dict by value
# (== get a representation sorted by value)

>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# 다시 딕셔너리로 만들기
In [240]: l = sorted(dic.items(), key=lambda x: x[1])

In [241]: dict(l)
Out[241]: {'a': 4, 'b': 3, 'c': 2, 'd': 1}
```

이 방법은 꼭 딕셔너리가 아니어도 가능하다. 이차원 배열에도 적용할 수 있다. 

```python
l = [[1, 4, 9], [3, 4, 5], [3, 9, 3]]
sorted(ll, key=lambda x: x[2])
>>> [[3, 9, 3], [3, 4, 5], [1, 4, 9]]
```


## 여러 변수의 참거짓 한 번에 검사하기 (multiple flag)

```python
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
```


## 두 딕셔너리 합치기

```python
# How to merge two dictionaries
# in Python 3.5+

>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}
```


## 이차원 배열 뒤집기

```python
mylist = [[1,2,3], [4,5,6], [7,8,9]]
new_list = list(map(list, zip(*mylist)))
```


## 2차원 리스트 복사하기

```python
from copy import deepcopy

l = [[2, 0, 0, 0, 1, 1, 0],
     [0, 0, 1, 0, 1, 2, 0],
     [0, 1, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],]
ll = deepcopy(l)
```
이렇게 복사하지 않으면, 리스트 원소인 리스트는 같은 리스트를 공유하게 된다. 하지만 이것보다 약 100배 빠르면서도 더 간단한 방법이 있다.

```python
ll = [x[:] for x in l]
```
워후! 이렇게 바꾼 결과, 내 백준 14502번 연구소 알고리즘이 3분에서 0.99 초로 단축되었다!

## 2차원 리스트 원소들의 리스트 만들기

```python
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - generator 만들기
def gen(l):
	for row in l:
		for n in row:
			yield n
```

속도는 순서대로 느려진다. 1000번 실행한 결과가 다음과 같다. 여러번 돌려본 경우, 1번과 2번은 거의 차이가 없었다. 2번이 살짝 더 빠른 경우도 간혹 있었다. 

1. `0.0015180110931396484`
2. `0.0018129348754882812`
3. `0.0060880184173583984`

2 차원 배열 내 원소의 갯수를 셀 때에도 그 속도는 유지되었다.

```python
l = [
        [2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]


# 방법 3 - generator 만들기
def cnt(l):
    count = 0
    for row in l:
        for n in row:
            if n == 0:
                count += 1
    return count


s = time()
for i in range(1000):
    sum(l, []).count(0)
print(time() - s)

s = time()
for i in range(1000):
    list(itertools.chain.from_iterable(l)).count(0)
print(time() - s)

s = time()
for i in range(1000):
    cnt(l)
print(time() - s)
```
```python
0.0019147396087646484
0.002129077911376953
0.004229068756103516
```

2 차원 배열 내 원소 갯수 세기는 다음 코드가 제일 빠르다.

```python
def cnt(l):
    count = 0
    for row in l:
        count += row.count(0)

>>> 0.0015637874603271484
```


## 문자열 상수 활용하기 

```python
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```


## 리스트 모든 원소 바꾸기

파이썬의 map을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있습니다.

```python
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```


## 곱집합 구하기

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
```



## 순열과 조합

아래는 순열, 조합은 `combinations`이다.

```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
```


## 리스트 안의 원소 갯수 세기

```python
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
```



## 오름차순 리스트에서 이진탐색하기

```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))e
```