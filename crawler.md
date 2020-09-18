
<h1 class="header"><span>Crawler</span></h1>



## 공부 자료

##### 문서
- 뷰티풀수프(한국어라 좀 맞지 않는 것이 있다): [Documentation - Korean](http://memnoth.github.io/pythondocuments/documents/beautifulsoup4/)  
- Requests: [Documentation](http://docs.python-requests.org/en/master/user/quickstart/)

##### 강의 영상: 
[170919  Crawling 01 BS4 requests.mp4](https://www.youtube.com/watch?v=YgLB5I_sCW0&feature=youtu.be)  

##### 블로그: 
- [creative works for Jason](http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-웹-크롤러like-Google-만들기-1-How-to-build-a-web-crawler)  
- [medium - 파이썬으로 크롤링 하기](https://medium.com/@mjhans83/파이썬으로-크롤링-하기-908e78ee09e0)
- [개발자의 취미생활 - requests 기초와 beautiful soup를 활용한 크롤링](http://rednooby.tistory.com/97)


## 설치

> 강의 영상에는 나와있지 않다. 블로그 보고 안 것

- Rquests 패키지 설치: `pip install requests`
- 뷰티풀 수프 설치: `pip install beautifulsoup4`  

다음과 같이 불러온다:

```python
import requests
from bs4 import BeautifulSoup
``` 


## 확인하기: 목표 템플릿 분석

##### 내가 필터링 하려는 태그가 실제 존재하는지 확인해야 한다. 
html 코드를 뜯어볼 때, `<tbody>` 같은 태그가 실제 html에 있나 확인해보아야 한다. `<tr>`만 있어도 브라우저에서 알아서 태그를 만들어주기 때문이다. 그래서 브라우저를 통해 코드를 살펴본 뒤, 터미널에서 한 줄씩 실행해보는 것이 가장 좋다. 클래스 명이 변경된 경우도 있었다.  



# Requests

`Requests`는 우리가 원하는 페이지의 html을 끌어오는 패키지이다. 다양한 기능들이 있지만, 단순한 크롤러를 위해선 아래의 예시만 잘 숙지하면 된다.  

`requests.get()` 함수는 `url`과 `parameter` 정보를 받아서 `get` 요청을 해준다.  

```python
import requests

KEEPBIBLE_URL = 'http://keepbible.com/html/bible_list.html'
bible_info_dict = {
    'bible_name': 'hkjv',
    'book_id': 1,
    'chap_num': 1,
}
```

```python
request = requests.get(KEEPBIBLE_URL, params=bible_info_dict)
```

`BeautifulSoup`에 넣을 때에는 `request.text`를 사용하면 된다. 

```python
soup = BeautifulSoup(request.text, 'lxml')
```



# Beautifulsoup

## parser 선택하기

> **parser**: 구문 해석 프로그램으로, 여기서는 html response를 그 구조에 맞게 읽어들이는 프로그램을 의미한다. 특별한 이유가 없다면 `lxml` parser를 추천한다.

### 1. 종류

##### Python 의 `html.parser`
1. 사용방식: `BeautifulSoup(markup_text, "html.parser")`
2. 특성:
	1. Python에 내장되어 있다
	2. 상당히 빠르다
	3. 필터가 관대하다.  
		: 분석하려는 html에 닫히지 않은 잘못된 태그가 있으면 그냥 무시한다. `<body>`와 `<html>`이 없어도 신경쓰지 않는다.

##### lxml
1. 사용방식: `BeautifulSoup(markup, "lxml")`
2. 특성:
	1. 따로 설치가 필요하다: `pip install lxml`
	2. 아주 빠르다
	2. 필터가 관대하다. (`html.parser` 만큼은 아니다)  
		: 닫히지 않은 태그는 무시하되, `<body>` 태그와 `<html>` 태그는 신경써서 만들어준다.  


## Requests 로 html 문자열 가져오기

```python
import requests

# 목표 url
KEEPBIBLE_URL = 'http://keepbible.com/html/bible_list.html'
# 목표 url의 파라미터
bible_info_dict = {
    'bible_name': 'hkjv',
    'book_id': 1,
    'chap_num': 1,
}

# 목표 url에 요청 후 응답 받아오기
request = requests.get(KEEPBIBLE_URL, params=bible_info_dict)

# html 문자열을 뷰티풀수프 객체로 변환하기
# request.text 에는 html 문자열이 들어있다
# 여기서의 parser는 `lxml`이다
soup = BeautifulSoup(request.text, 'lxml')
```


## Beautifulsoup 객체 다루기

##### 태그 정보 가져오기

```python
tag_a = soup.a  # 문자열 중 첫번째 a 태그 정보를 가져온다. 

In [1]: tag_a
Out[1]: <a name="nett_head">this is link text</a> 
```

##### 태그 이름
```python
In [1]: tag_a.name  # 태그 이름 반환
Out[1]: 'a'

In [2]: tag_a.name = 'h1'  # 태그 이름 변경
Out[2]: <h1 name="nett_head">this is link text</h1>
```


##### 태그 속성

```python
In [1]: tag_a['name']  # 속성 접근
Out[1]: 'nett_head'

In [2]: tag_a.attrs  # 속성 딕셔너리
Out[2]: {'name': 'nett_head'}

In [3]: tag_a['name'] = 'test'  # 속성 변경
In [4]: tag_a
Out[4]: <a name="test">this is link text</a>
```

##### 태그 속성 - 다중 속성
```python
# 다중 속성은 리스트로 나타낸다.
In [1]: tag_a['name'] = ['nett_head', 'test']
In [2]: tag_a
Out[2]: <a name="nett_head test">this is link text</a>

In [3]: tag_div
Out[3]: <div class="col-sm-3 sidebar hidden-xs" style="min-height: 9594px;"></div>
In [4]: tag_div.attrs
Out[4]: {'class': ['col-sm-3', 'sidebar', 'hidden-xs'], 'style': 'min-height: 9594px;'}

# HTML 표준에 따라 다중 속성이 정의될 수 없는 태그라면 예외다.
id_soup = BeautifulSoup('<p id="my id"></p>')
In [5]: id_soup.p['id']
Out[5]: 'my id'
```

##### 태그 내용
```python
In [1]: tag_a
Out[1]: <a name="nett_head">this is link text</a>

In [2]: tag_a.string
Out[2]: 'this is link text'


# 태그가 여러개이고 문자열도 여러개일 때
In [3]: tag_li
Out[3]: <li>that is right<a name="nett_head">this is link text</a></li>

# 문자열이 여러개이면 string으로 접근이 안된다. 
In [4]: tag_li.string

# 문자열이 여러개일 때, strings generator 로 접근할 수 있다.
In [5]: tag_li.strings
Out[5]: <generator object _all_strings at 0x10ea8f7d8>
In [6]: for s in tag_li.strings:
     ...:     print(s)
     ...:
that is right
this is link text


# 태그가 여러개이고 문자열이 하나일 때
In [7]: tag_li
Out[7]: <li><a name="nett_head">this is link text</a></li>

In [8]: tag_li.string
Out[8]: 'this is link text'


# 줄바꿈 문자열이 포함되어 있을 때
In [9]: tag_ul
Out[9]:
<ul class="list-unstyled list-inline">
<li>
<a class="btn btn-default btn-sm" href="https://github.com/guilload">
<i class="fa fa-github-alt fa-lg"></i>
</a>
</li>
<li>
<a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
<i class="fa fa-twitter fa-lg"></i>
</a>
</li>
<li>
<a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
<i class="fa fa-linkedin fa-lg"></i>
</a>
</li>
</ul>

In [10]: l = []
     ...: for s in tag_ul.strings:
     ...:     l.append(s)
     ...:
In [11]: l
Out[11]:
['\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n',
 '\n']

# stripped_strings 로 줄바꿈을 제거할 수 있다. 
# 공백만 있는 문자열과, 문자열 앞뒤 공백은 제거된다. 
In [12]: l = []
     ...: for s in tag_ul.stripped_strings:
     ...:     l.append(s)
     ...:
In [13]: l
Out[13]: []
```

##### 태그 자식 접근하기
```python
In [1]: tag_ul
Out[1]:
<ul class="list-unstyled list-inline">
<li>
<a class="btn btn-default btn-sm" href="https://github.com/guilload">
<i class="fa fa-github-alt fa-lg"></i>
</a>
</li>
<li>
<a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
<i class="fa fa-twitter fa-lg"></i>
</a>
</li>
<li>
<a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
<i class="fa fa-linkedin fa-lg"></i>
</a>
</li>
</ul>

# 줄바꿈 문자도 자식으로 접근된다는 점을 기억하자.
In [2]: tag_ul.contents
Out[2]:
['\n', <li>
 <a class="btn btn-default btn-sm" href="https://github.com/guilload">
 <i class="fa fa-github-alt fa-lg"></i>
 </a>
 </li>, '\n', <li>
 <a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
 <i class="fa fa-twitter fa-lg"></i>
 </a>
 </li>, '\n', <li>
 <a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
 <i class="fa fa-linkedin fa-lg"></i>
 </a>
 </li>, '\n']
```

##### 태그 부모 접근하기
```python
In [1]: tag_a.parent
Out[1]: <body><a name="nett_head">this is link text</a></body>
# 모든 부모를 generator로 돌려주는 .parents 도 있다. 
```


## Beautifulsoup 함수 다루기


### 1. find_all()
> 1. `find_all()`의 결과로 반환된 리스트 항목은 거의 ` bs4.element.Tag` 타입이다.
> 2. `find_all()` 함수는 뷰티풀수프에서 가장 많이 사용되는 함수이므로, 태그 객체를 함수처럼 다루면, 같은 방식으로 동작한다. 다음 코드 각각의 두 줄은 동등하다.
> 
>     ```python
>     soup.find_all("a")
>     soup("a")
>     
>     soup.title.find_all(text=True)
>     soup.title(text=True)
>     ```

##### 원하는 모든 태그 불러오기
```python
# 모든 a 태그를 찾는다.
In [1]: soup.find_all('a')
Out[1]:
[<a class="navbar-toggle nav-link" href="http://github.com/guilload" type="button">
 <i class="fa fa-github"></i>
 </a>,
 <a class="navbar-toggle nav-link" href="http://twitter.com/guilload" type="button">
 <i class="fa fa-twitter"></i>
 </a>,
 <a class="navbar-brand" href="/">
 <img class="img-circle" src="http://www.gravatar.com/avatar/05737f7353d71ece81912e75bd95cf17?s=35"/>
 				guilload.com
 			</a>,
 <a href="/">
 <img class="img-circle" src="http://www.gravatar.com/avatar/05737f7353d71ece81912e75bd95cf17?s=150"/>
 </a>,
 <a href="/">guilload.com</a>,
 <a class="btn btn-default btn-sm" href="https://github.com/guilload">
 <i class="fa fa-github-alt fa-lg"></i>
 </a>,
 <a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
 <i class="fa fa-twitter fa-lg"></i>
 </a>,
 <a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
 <i class="fa fa-linkedin fa-lg"></i>
 </a>,
 <a class="twitter-share-button" data-lang="en" data-via="guilload" href="https://twitter.com/share">Tweet</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Include/stringobject.h#l35" target="_blank">stringobject.h</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Include/stringobject.h#l88" target="_blank">few lines below</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Objects/stringobject.c#l24" target="_blank">stringobject.c</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Objects/stringobject.c#l4745" target="_blank">line 4745</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Objects/stringobject.c#l4732" target="_blank">line 4732</a>,
 <a href="http://www.nltk.org/" target="_blank">NLTK</a>,
 <a href="http://guppy-pe.sourceforge.net/" target="_blank">Heapy</a>,
 <a href="https://docs.python.org/2/library/dis.html#bytecodes" target="_blank">here</a>,
 <a href="https://hg.python.org/releasing/2.7.9/file/753a8f457ddc/Objects/codeobject.c#l72" target="_blank">codeobject.c</a>,
 <a href="http://late.am/post/2012/03/26/exploring-python-code-objects" target="_blank">Exploring Python Code Objects</a>,
 <a href="http://www.laurentluce.com/posts/python-string-objects-implementation/" target="_blank">Python string objects implementation</a>,
 <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a>,
 <a class="dsq-brlink" href="http://disqus.com">comments powered by <span class="logo-disqus">Disqus</span></a>,
 <a href="/pyisaac" title="Porting ISAAC to Python">← Previous</a>]
 
# 모든 a 태그와 b 태그를 찾는다.
soup.find_all(['a', 'b'])

# 모든 태그를 찾는다.
soup.find_all(True)
```

##### 정규표현식으로 찾기
```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
>>> body
>>> b
```

##### 속성으로 접근하기 (attribute)
```python
# class 속성 참조하기
In [1]: soup.find_all('a', 'btn')
Out[1]:
[<a class="btn btn-default btn-sm" href="https://github.com/guilload">
 <i class="fa fa-github-alt fa-lg"></i>
 </a>, <a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
 <i class="fa fa-twitter fa-lg"></i>
 </a>, <a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
 <i class="fa fa-linkedin fa-lg"></i>
 </a>]
 
# class 속성을 키워드 인자로 전달하려면 class_ 를 써야 한다.
soup.find_all("a", class_="sister")

# class 이외의 속성은 속성명을 명시해줘야 한다.
In [2]: soup.find_all('a', 'https://github.com/guilload')
Out[2]: []
In [3]: soup.find_all('a', href='https://github.com/guilload')
Out[3]:
[<a class="btn btn-default btn-sm" href="https://github.com/guilload">
 <i class="fa fa-github-alt fa-lg"></i>
 </a>]

# id 값이 존재하기만 하면 찾아낸다 
soup.find_all(id=True)

# 당연하게도, 정규표현식을 사용할 수 있다
soup.find_all(href=re.compile("elsie"))

# 딕셔너리를 사용할 수 있다. 다음 두 줄은 같은 표현이다.
soup.find_all(href=re.compile("elsie"), id='link1')
soup.find_all(attrs={'href' : re.compile("elsie"), 'id': 'link1'})
```

##### 문자열 찾아내기
```python
In [1]: soup.find_all(text=re.compile('two diff'))
Out[1]: [' reference two different objects:']

# 두 개의 조건을 리스트로 전달할 수 있다.
# 두 개의 조건 중 하나라도 충족시키는 것을 찾는다.
In [2]: soup.find_all(text=[re.compile('two diff'), re.compile('refer')])
Out[2]:
["     *       'interned' dictionary; in this case the two references",
 '. Line 24 declares a reference to an object where interned strings will be stored:',
 '/* The two references in interned are not counted by refcnt.',
 'As you can see, keys in the interned dictionary are pointers to string objects and values are the same pointers. Furthermore, string subclasses cannot be interned. Let me set aside error checking and reference counting and rewrite this function in pseudo Python code:',
 ' reference two different objects:']
```

##### find_all()에 함수를 인자로 전달하기
<hr class="clear">
> 마음에 드는 필터 기준이 없다면, 나만의 함수를 정의하자. 태그 요소를 유일한 인자로 취해야 한다. 인자가 조건에 부합하면 True를, 그렇지 않으면 False를 반화해야 한다.  
> 다음은 class 속성은 정의되어 있고 id 속성은 없는 태그일 때 True 를 돌려주는 함수이다

```python
# 태그의 속성 존재 여부 검사
def has_class_but_no_id(tag):
    return tag.has_key('class') and not tag.has_key('id')
    
soup.find_all(has_class_but_no_id)
>>> [<p class="title"><b>The Dormouse's story</b></p>,
>>>  <p class="story">Once upon a time there were...</p>,
>>>  <p class="story">...</p>]


# class 길이 검사 (속성이 여러개인 경우, 공백이 포함된다)
def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

soup.find_all(class_=has_six_characters)
>>> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
>>>  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
>>>  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# class 속성 여러개 검사
# css_class 인자는, class 가 있을 경우 str, 없을 경우 NoneType 객체이다.
def class_has_btn(css_class):
	if type(css_class) is str:
		return 'btn' in css_class and 'btn-sm' in css_class
	return False

In [1]: soup.find_all('a', class_=class_has_btn)
Out[1]:
[<a class="btn btn-default btn-sm" href="https://github.com/guilload">
 <i class="fa fa-github-alt fa-lg"></i>
 </a>, <a class="btn btn-default btn-sm" href="https://twitter.com/guilload">
 <i class="fa fa-twitter fa-lg"></i>
 </a>, <a class="btn btn-default btn-sm" href="https://linkedin.com/in/adrienguillo">
 <i class="fa fa-linkedin fa-lg"></i>
 </a>]
```

##### 반환 갯수 제한하기 limit
```python
# 앞에서부터 두 개만 반환한다. 
soup.find_all("a", limit=2)
```

##### 직계 자손만 조사하기 reculsive=False
<hr class="clear">
> `find_all`은 해당 태그 하위의 모든 태그를 검사한다. 직계자손만 검사하고 싶다면 `reculsive=False` 옵션을 사용하자.

```python
soup.html.find_all("title", recursive=False)
```


### 2. find()

`find_all()`은 전체 문서를 훓어서 결과를 찾지만, `find()`는 단 하나만을 반환한다. 필요한 것이 하나이거나, 하나 밖에 없음을 이미 알고 있다면 `find()`가 효율적이다. 

```python
soup.find_all('title', limit=1)
>>> [<title>The Dormouse's story</title>]

soup.find('title')
>>> <title>The Dormouse's story</title>
```

`find_all()`과 `find()`의 유일한 차이점은 반환 값의 타입이다. 전자는 리스트를, 후자는 그냥 객체를 돌려준다. 찾는 값이 없을 때는 각각 `[]`, `None`을 돌려준다. 


### 3. 기타 find 함수 ([문서참조](https://cryptosan.github.io/pythondocuments/documents/beautifulsoup4/))

1. `find_parents()`
2. `find_next_siblings()`
3. `find_previous_siblings()`
4. `find_all_next()`: 뒤에 나오는 건 뭐든지 반환
5. `find_all_previous()`


### 4. select 함수

> 뷰티풀수프는 [CSS 표준 선택자](http://www.w3.org/TR/CSS2/selector.html)를 지원한다. `CSS 선택자 표준`에 따른 문자열을 `Tag`의 `.select()` 메서드에 전달하면 된다.

```python
# body 밑의 모든 a 태그
soup.select("body a")

# head 바로 아래 title 태그
soup.select("head > title")

# class 옵션 (둘이 같은 뜻으로, class에 sister 속성이 하나라도 있는 경우를 나타낸다.)
soup.select(".sister")
soup.select("[class~=sister]")

# id 가 link2 인 a 태그
soup.select('a#link2')

# title 속성이 존재하는 a 태그
soup.select('a[title]')

# 완전일치
soup.select('a[href="http://example.com/elsie"]')
>>> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 시작 일치
soup.select('a[href^="http://example.com/"]')
>>> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
>>>  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
>>>  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 끝 일치
soup.select('a[href$="tillie"]')
>>> [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 부분일치 아무데나
soup.select('a[href*=".com/el"]')
>>> [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```


### 5. 하위 태그 제거하기, extract()

`extract()`는 해당 객체 하위의 태그나 문자열을 제거한다. 추출하고 남은 태그나 문자열을 돌려준다:

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

# soup 에서 하위의 i 태그를 제거한다. 제거된 값을 반환한다. 
# 하위에 여러 i 태그가 있다면 첫 번째 하나만 제거한다. 
i_tag = soup.i.extract()

a_tag
>>> <a href="http://example.com/">I linked to</a>

i_tag
>>> <i>example.com</i>

print(i_tag.parent)
>>> None

# tag 가 아닌 요소에도 적용할 수 있다. 
my_string = i_tag.string.extract()
my_string
>>> u'example.com'

print(my_string.parent)
>>> None
i_tag
>>> <i></i>
```


### 6. 태그 벗기기, unwrap()

`Tag.unwrap()`은 `wrap()`의 반대이다. 태그를 벗겨 버리고 그 안의 문자열만 남긴다. 

```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

# a 태그 안의 i 태그 벗기기
a_tag.i.unwrap()
a_tag
>>> <a href="http://example.com/">I linked to example.com</a>
```


### 7. 예쁘게 인쇄하기, prettify()

> `prettify()`를 사용하는데 있어서 문자 인코딩 설정이 필요할 때가 있다. 그때는 [문서를 참조하자](https://cryptosan.github.io/pythondocuments/documents/beautifulsoup4/#output-formatters)

`prettify()`는 들여쓰기가 된 문자열을 반환한다. 

```python
print(soup.prettify())
```


### 8. 얽히고 설킨 태그, 문자열만 골라내기. get_text()

`get_text()`는 문서 또는 태그 아래의 텍스트를 유니코드 문자열로 반환한다

```python
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
u'\nI linked to example.com\n'  # 앞에 u 가 붙은 문자열은 유니코드 문자열을 의미한다. 
soup.i.get_text()
u'example.com'
```

텍스트를 합칠 때 구분자로 사용될 문자열을 지정할 수 있다

```python
soup.get_text("|")
>>> u'\nI linked to |example.com|\n'
```

테스트의 앞과 뒤에 있는 공백을 걷어낼 수 있다

```python
soup.get_text("|", strip=True)
>>> u'I linked to|example.com'
```