## 파일 입출력하기

- `for line in f:`:  `\n`을 포함한 한 줄을 가져온다.  
- 파일 입력하기: `f.(write)`, `wt`로 반복해서 입력하게 되면 파일 맨 끝에서 입력한다.  


## 파일 포인터 다루기 

```python
file.seek(n)  # 파일의 n번째 바이트로 이동
file.seek(n, 1)  # 현재 위치에서 n바이트 이동(n이 양수면 뒤쪽으로, 음수면 앞쪽)
file.seek(n, 2)  # 맨 마지막에서 n바이트 이동(n은 보통 음수)
file.tell()  # 현재의 파일 포인터 위치 돌려줌
```

## 파일 존재 확인하기

```python
# 폴더, 파일, 링크에 상관없이 path의 존재 확인. 
# 플랫폼에 따라서 os.stat(path)을 실행할 수 없는 경우에도 False를 반환 
os.path.exists(path)

# 개별 확인
os.path.isdir(path)
os.path.isfile(path)
os.path.islink(path)
```

## 파일 복사, 삭제하기

##### 파일 복사하기

```python 
import shutil

# 폴더는 그 안에, 파일이름은 새로운 파일로 저장. 
# 폴더가 없으면 에러
# 겹치는 파일이 있으면 덮어쓰기
shutil.copy('파일이름', '폴더/파일이름') 
```


##### 폴더 복사하기

```python 
import shutil

# 겹치는 폴더가 있을 경우 에러
shutil.copytree('폴더이름', '새폴더이름')
```


##### 파일, 폴더 이동하기

이동은 삭제후 복사하기와 같으며, 이름 바꾸기와도 같다.

```python 
# 파일경로에 포함된 폴더가 없으면 에러
# 겹치는 파일이 있으면 덮어쓰기
shutil.move('파일이름', '파일경로')

# 겹치는 폴거가 있으면 에러.
shutil.move('폴더이름', '폴더이름')
```


##### 폴더 삭제하기

```python
shutil.rmtree('폴더이름')
```


##### 파일 삭제하기

파일 삭제는 `shutil`에 없다. 

```python
import os

os.remove('파일이름')
```


##### 정규표현식으로 파일 찾아서 지우기

```python
import os
import fnmatch

for file in os.listdir('./garage/'):  # garage/ 또는 garage 로 해도 무방하다.
	if fnmatch.fnmatcn(file, 'what*'):
		os.remove('garage/' + file)
```


## 정규표현식으로 파일 다루기

`fnmatch`: 정규표현식을 사용해서 파일을 찾을 수 있게 해주는 모듈. 이때 사용되는 표현식은 `re` 모듈에서 사용하는 정규표현식과는 다르다.  

| Pattern  | Meaning                          |
|----------|----------------------------------|
| `*`      | matches everything               |
| `?`      | matches any single character     |
| `[seq]`  | matches any character in seq     |
| `[!seq]` | matches any character not in seq |
| `[?]`    | matches `?`                      |


##### 정규표현식으로 파일 찾아서 지우기

```python
import os
import fnmatch

for file in os.listdir('./garage/'):  # garage/ 또는 garage 로 해도 무방하다.
	if fnmatch.fnmatcn(file, 'what*'):
		os.remove('garage/' + file)
```


##### 정규표현식으로 파일 찾아서 리스트로 받기

```python
# fnmatch.filter(<파일이름리스트>, <문자열>)
print(fnmatch.filter(os.listdir('.'), '*.txt'))

>>> ['alias-deleted.txt', 'copied.txt', 'writetest02.txt']
```


##### 정규표현식으로 파일 찾기 2 (전역적 검색)

```python
import glob

# 현재폴더 기준으로 찾기
glob.glob('./copied.txt', recursive=False)
>>> ['./copied.txt']
glob.glob('*.txt', recursive=False)
>>> ['alias-deleted.txt', 'copied.txt', 'writetest02.txt']

# 절대경로로 찾기
glob.glob('/Users/ElohimAwmar/python/testpython/copied.txt', recursive=False)
>>> ['/Users/ElohimAwmar/python/testpython/copied.txt']

# 상대경로로 찾기
# `../` 하나가 상위폴더 한 단계를 의미. 겹쳐서 사용가능. `.../`는 안됨
glob.glob('../../python/*/copied.txt', recursive=False)
>>> ['../../python/testpython/copied.txt']

# 중간 생략하기
glob.glob('/Users/ElohimAwmar/python/*/copied.txt', recursive=False)
>>> ['/Users/ElohimAwmar/python/testpython/copied.txt']

# 폴더 하위의 모든 파일을 재귀적으로 검사
# recursive=True 하고 ** 사용
glob.glob('../**/copied.txt', recursive=True)  # 현재 폴더 바로 상위 폴더 기준 하위의 모든 파일 검사
>>> ['../copied.txt', '../testpython/copied.txt', '../testpython/garage/copied.txt']
```

