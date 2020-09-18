# ETC

- 클래스 디자인 패턴 23개 [gmlwjd9405.github.io: 디자인 패턴 종류](https://gmlwjd9405.github.io/2018/07/06/design-pattern.html)


# Linux

#### 매뉴얼 보기 `man`
- `man` 명령어를 통해 `man chmod` 처럼 매뉴얼을 볼 수 있다. 
- `q` 로 나올 수 있고, `enter` 키를 입력하면 매뉴얼의 다음 줄을 계속해서 볼 수 있다.

 
## chmod
> http://eunguru.tistory.com/93

### 접근 권한의 8진수 표현 
| 8진법 | 2진법 | 파일모드 |
|:---:|:-----:|:-----:|
|  0  |  000  |  ---  |
|  1  |  001  |  --x  |
|  2  |  010  |  -w-  |
|  3  |  011  |  -wx  |
|  4  |  100  |  r--  |
|  5  |  101  |  r-x  |
|  6  |  110  |  rw-  |
|  7  |  111  |  rwx  |

### 주요 옵션
- `-R, --recursive`: 하위 디렉토리와 파일의 권한까지 변경

### r 권한이 빠져도 보인다?


## 실행파일 만들기



## 링크 걸기

> - [wiki: 심볼릭 링크](https://ko.wikipedia.org/wiki/심볼릭_링크)
> - [JaeYeon Baek: 하드링크와 심볼릭링크 개념 잡기](http://jybaek.tistory.com/578)

- 링크를 걸어줄 때는 무조건 절대경로로 잡아주어야 한다. 
- 하드링크는 같은 파일에 두 개의 이름을 지어준다고 생각하면 된다. 원본이 삭제되어도 사용할 수 있는 링크로, 사실상 원본의 개념이 없다. 프로그래밍에서 두 변수에 같은 주소 값이 할당된 것으로 이해하면 좋다.
- 심볼릭 링크는 해당 파일에 별명을 지어주는 것이라 생각하면 좋다. 원본 파일이 사라지면 작동하지 않는다.


# Vim 자동완성

> https://johngrib.github.io/wiki/vim-auto-completion/

놀랍게도 vim 에서 자동완성이 된다고 한다. 서버에서 만질 때 말고는 큰 의미는 없을 것 같기는 하지만, 알아는 두자. 지금은 시간이 없으니 나중에 찾아보자. 



# git

## fork
> http://taewan.kim/post/updating_fork/

> https://nvie.com/posts/a-successful-git-branching-model/
> https://learngitbranching.js.org



# Pandas

## dataframe

- index 가 같은 시리즈를 묶어놓은 것

## dataframe 만들기

## dataframe 에서 정보 가져오기

#### Column 이 기본: df['key']
- 기본적으로 column 을 가져온다. 
- 한 칼럼은 시리즈로, 두 칼럼 이상은 dataframe 객체로 가져온다.
- 날짜 스트링일 때는, 해당 구간의 datetime 인덱스를 가지는 dataframe 을 가져온다. 따라서 인덱스에 날짜를 배정할 생각이면, datetime 클래스로 넣어주는 것이 좋다. 

#### Row 값은: df.iloc[], df.loc[]
- 한 로우는 시리즈로, 두 로우 이상은 dataframe 객체로 가져온다. 
- `df.iloc[정수 인덱스]`: `0` 또는 `-1` 과 같이 순서로 값을 불러와야 할 수 있다.
- `df.loc[인덱스]`: 정수가 아닌 인덱스를 기준으로 가져온다. 


# 코인 거래

## 계좌 만들기
- 고팍스에선 현금 입금이 가능