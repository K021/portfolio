
<h1 class="header"><span>Python</span></h1> 

## 파이썬 코드 컨벤션
- [Python PEP8](https://www.python.org/dev/peps/pep-0008/)

## 기본

```
<pyenv 작동구조>
system
	python2
	pyenv
		versions
			2.7.10
			3.6.2
		envs
			2.7.10 - env1
			3.6.2 - env1
			3.6.3 - env2
```

`id.__doc__` 함수 설명

### 진수(base)

기본적으로 숫자형 데이터는 10진수로 간주되지만, 파이썬에서는 2진수, 8진수, 16진수를 표현할 수 있다.

2진수(binary): 0b또는 0B로 시작  
8진수(octal): 0o또는 0O로 시작  
16진수(hex): 0x또는 0X로 시작

```python
>>> 10
10
>>> 0b10
2
>>> 0o10
8
>>> 0x10
16
```

lux[::-1] 스텝을 가장 많이 사용할 수 있는 지점에서 시작
girlsday.split(',')

### 문자열 포맷

옛 스타일 (%)

`string % data`

**변환타입 설명**  
%s	문자열		
%d	10진수  
%x	16진수  
%o	8진수  
%f	10진 부동소수점수  
%e	지수로 나타낸 부동소수점수   
%g	10진 부동소수점수 혹은 지수로 나타낸 부동소수점수  
%%	리터럴 %  

```
>>> '%s' % 42
'42'
>>> '%d x %d : %d' % (3, 4, 12)
'3 x 4 : 12'
```

```
새 스타일 ({}, format)

{}.format(변수)
# 기본형태
>>> '{} {} {}'.format(d, f, s)
'37 3.14 Fastcampus'

# 각 인자의 순서를 지정
>>> '{1} {2} {0}'.format(d, f, s)
'3.14 Fastcampus 37'

# 각 인자에 이름을 지정
>>> '{d} {f} {s}'.format(d=50, f=1.432, s='WPS')
'50 1.432 WPS'

# 딕셔너리로부터 변수 할당
>>> dict = {'d': d, 'f': f, 's': s}
>>> '{0[d]} {0[f]} {0[s]} {1}'.format(dict, 'WPS')
'37 3.14 Fastcampus WPS'

# 타입 지정자 입력
>>> '{:d} {:f} {:s}'.format(d, f, s)
'37 3.140000 Fastcampus'

# 이름과 타입지정자를 모두 사용
>>> '{digit:d} {float:f} {string:s}'.format(digit=700, float=1.4323, string='Welcome')
'700 1.432300 Welcome'

# 필드길이 10, 우측정렬
>>> '{:10d}'.format(d)
'        37'
>>> '{:>10d}'.format(d)
'        37'

# 필드길이 10, 좌측정렬
>>> '{:<10d}'.format(d)
'37        '

# 필드길이 10, 가운데 정렬
>>> '{:^10d}'.format(d)
'    37    '

# 필드길이 10, 가운데 정렬, 빈 공간은 ~로 채움
>>> '{:~^10d}'.format(d)
'~~~~37~~~~'
```

### 특정 위치 리스트 항목 삭제 (del)

파이썬 구문 del을 사용

del은 리스트 함수가 아닌, 파이썬 구문이므로 del <리스트>[오프셋] 형식을 사용한다.

```
>>> del fruits[0]
값으로 리스트 항목 삭제 (remove)

>>> fruits.remove('mango')
리스트 항목 추출 후 삭제 (pop)

>>> fruits.pop()
>>> fruits.pop(-3)
```

### 정렬하기 (sort, sorted)

sort는 리스트 자체를 정렬
sorted는 리스트의 정렬 복사본을 반환

### 리스트 복사 (copy)

copy함수
list함수
슬라이스 연산[:]

## 제어문

**링크**: [강의자료.Github](https://github.com/Fastcampus-WPS-6th/Python/blob/master/08.%20제어문.md)



## 조건문


**임포트 우선순위**: 임포트 함수 겹치면 밑에 것 (우선)  

```
$ import sys  
$ print(sys(argv))
```  

**클래스명**: 대문자  
**모듈명**: 소문자 언더 스코어.  

**Name Mangling**: `_<클래스명>__<속성명>`:보는 방법:`dir(class 이름)``dir(lotte)`  
`__`:private. 해당 클래스 내부에서만 가능  
`_`:protected. 자식 클래스도 가능  

**ask Django**  
**UDEMY**



# class

## method의 분류

### 1. instance method

1. 표시: 없음 (일반적으로 정의하는 함수는 모두 인스턴스 메서드)
2. 인스턴스를 변수로 받고(`self`) 인스턴스 변수를 변화시킨다. 

### 2. class method

1. 표시: 함수 앞에 `@classmethod`
2. 클래스 자체를 변수로 받기 때문에(`cls`) 클래스 전체에 해당하는 변수를 변화시킨다. 

### *인스턴스 변수가 클래스 변수를 오버라이드 하는 경우 




## 질문

정규표현식: `\d*`이 숫자 검색이 안 된다. *은 '없음'인 ''도 포함하기 때문에, match 혹은 search 메소드의 경우 모든 문자열의 맨 앞에 있는 공백을 반환하고 종료되기 때문에,  

```python
l = re.findall('.',printable)
k = 0
for i,j in zip(printable,l):                  
	k = k +1          
	print('{}: 1{}2,3{}4\n'.format(k,i,j)) 
```
이거 실행 안됨: `\r`이 윗 줄을 아랫 줄이 덮어버리는 식으로 출력된다.  
p214. 리터럴이 뭔가요
***

**정적메소드:** 정적 메소드는 인자로 self나 cls를 받지 않기 때문에 self./cls.으로 속성 혹은 메소드에 접근할 수 없다? 그럼 클래스/인스턴스의 정보를 다루지 못하는 것인가?  

**귀도의 조언:** <쉽게 시작하는 파이썬> p193.중간부분에 이런 말이 있다. 'getter/setter 함수보다 간단한 field가 더 낫다.' 간단한 field는 무엇을 의미하는가?  


		