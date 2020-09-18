<h1 class="header"><span>iterator</span></h1>

파이썬에서 이터레이터는 참 매력적인 기능을 갖고 있다. 이 문서에서는 이터레이터를 효과적으로 사용하는 방법에 대해 알아보자.

> ##### 참고자료
> - [Python 의 yield 키워드 알아보기 &mdash; tech.ssut](https://tech.ssut.me/2017/03/24/what-does-the-yield-keyword-do-in-python/)
> - [Python Itertools &mdash; Real Python](https://realpython.com/python-itertools/)



# 함수에서 generator 출력하기

generator 는 iterator 이지만, 다른 iterator 와 다르게 모든 값을 메모리에 담고 있지 않고 그때 그때 값을 생성한다. generator 를 만드는 방식은 두 가지로, 컴프리헨션과 함수 선언이 있다.

한 번만 순회할 거대한 이터레이터가 필요하다면, 제너레이터를 사용하는 것이 좋다. 


## comprehension 사용하기

```python
In [13]: gen = (x for x in range(10))

In [14]: print(gen)
<generator object <genexpr> at 0x110b01ba0>

In [15]: for i in gen:
    ...:     print(i)
    ...:
0
1
2
3
4
5
6
7
8
9
```


## `yield` 로 출력하는 함수

제너레이터를 출력하는 함수는, 함수를 호출해도 내부 코드가 실행되지 않고, 반복문을 통해 순회할 때에만 실행된다.  

```python
In [1]: def test(n):
   ...:     for i in range(n):
   ...:         yield i+1
   ...:

In [2]: test(19)
Out[2]: <generator object test at 0x110a26db0>

In [3]: for i in test(20):
   ...:     print(i)
   ...:
1
2
3
.
.
.
19
20
```


# itertools 사용하기

> [Python Itertools &mdash; Real Python](https://realpython.com/python-itertools/): 이거 좀 대박이다. 읽어보자.


## itertools 를 사용한 더 나은 grouper

### naive grouper

```python
def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]
```

```python
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> naive_grouper(nums, 2)
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
```

### better grouper

> 5배 정도 더 빠르다

```python
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n  # 같은 iterator 객체를 사용함으로써, 순차적인 출력이 가능해 중복이 없어진다.
    return zip(*iters)
```

```python
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(better_grouper(nums, 2))
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
```