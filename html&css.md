[HTML](#170904)  
[공부할 것](#?)
[질문할 것](#??)



# <a name='170904'></a>HTML
* 주석: 원하는 블럭을 선택 후 `cmd + /`

## 표준화 시스템
* 웹표준 (W3C)  
웹 표준 지원 정도 테스트 <http://html5test.com>
* 웹 접근성 (웹 접근성 지침 WCAG)

## HTML의 기본 구조  

```html
<!DOCTYPE html> # 문서유형 지정
<html> # html 문법의 적용 영역
  <head> # html 문서의 기본정보 포함
    <meta charset="utf-8">
    <title></title> # 브라우저 제목 표시줄
  </head>
  <body> # 문서 본문
  <!-- 이것은 주석이당 --> # 주석
  </body>
</html>
```

## 절대경로와 상대경로
* 절대경로: 일반적인 주소
* 상대경로: 해당 HTML 파일 위치를 기준으로 한 경로. (`./`생략가능)

```html
<img src='./img/IMG_6666.jpg'>
```
## 기타
- p 태그의 기본적 속성

```html
  p {
    display: block;
    -webkit-margin-before: 1em; # 위에 현재 글자 크기만큼 공백
    -webkit-margin-after: 1em; # 아래
    -webkit-margin-start: 10px; # 왼쪽 여백
    -webkit-margin-end: 0px; # 오른쪽 여백
  }
```

## head 와 body 태그
* head: 문서의 메타데이터 설정.
* body: 문서의 내용.

## 요소: 블록 / 인라인
* 블록 요소
	* 무조건 줄바꿈
	* width 기본값이 전체 넓이
	* `h1``p``div``blockquote` 등을 포함한다.
* 인라인 요소
	* 줄바꿈 없음
	* 내용 만큼의 너비
	* `strong``a``span``br` 등을 포함한다.

> **블록은 인라인을 포함하지만	 인라인은 블록을 포함할 수 없습니다*   
> **div와 span은 오직 블록과 인라인 방식의 레이아웃을 구성하는데만 사용됩니다.*

## HTML 태그
#### Text tag
* `h1`, `h2` ... : Heading. 제목. 
* Line breaks: 줄바꾸기
	* `p`: paragraph. 태그 위아래에 공백.
	* `br`: linebreak. 줄 바꾸기. 위아래 공백 없음. 닫힘태그 필요없음. 
* 줄바꿈 없는 텍스트 태그
	* `strong`: 볼드체 및 의미론적 강조.
	* `b`: bold. 
	* `em`: 이탤릭체 및 의미론적 강조.
	* `i`: italic.
	* `mark`: <mark>형광펜 효과</mark>
* 그외
	* hr: horizontal rule. 수평선. 닫힘태그 필요없음
	* blockquote: 인용문
	* pre: preformatted text. 형식이 그대로 출력.

#### Anchor: link tag
```html
<a href="http://naver.com" target='_blank' title="open naver">link text</a>
```

* `target`: 링크 페이지를 여는 방법
	* `_self`: 그냥 지금 당장 열기
	* `_blank`: 새 창에서 깔끔하게 열기
* `title`: 마우스 커서를 올리면 나타나는 텍스트

#### Image
```html
<img src="./img/IMG_6666.jpg" width="200" alt="이미지가 뜨지 않을 경우 표시">
```

* `height`: 높이
* `alt`: alternative text

#### Data tags
* **List**: 목록형태는 전부 리스트로 쓴다.   
	* `ol`: ordered list
	* `ul`: unordered list
	* 속성
		* `type`: 목록 기호 타입 (`1`, `a`, `A`, `i`, `I`)
		* `start`: 목록 시작 숫자
		* `reversed`: 거꾸로 카운트

* Description list: 정의 목록
	* 

```
정의목록은 그 양이 적을 때에만 쓰이고 나머지는 테이블을 많이 쓴다
tr table row
th table header
hd table data
colgroup은 속성에 제한이 있기 때문에 잘 사용하지 않는다. 
```
```html
table>(tr>th[colspan=3]{이름}+th{제목$}*3)+(tr>td[colspan=3]{뭔가요}+td[rowspan=2]{항목}*3)+(tr>td{항목$}*3)
```
```html
<table>
  <tr>
    <th colspan="3">이름</th>
    <th>제목1</th>
    <th>제목2</th>
    <th>제목3</th>
  </tr>
  <tr>
    <td colspan="3">뭔가요</td>
    <td rowspan="2">항목</td>
    <td rowspan="2">항목</td>
    <td rowspan="2">항목</td>
  </tr>
  <tr>
    <td>항목1</td>
    <td>항목2</td>
    <td>항목3</td>
  </tr>
</table>
```
```html
<style>
colgroup:nth-of-type(1) {
  background-color: #fcf;
}
colgroup:nth-of-type(1) > col:nth-of-type(2) {
  background-color: red;
}
</style>

<caption>제에목</caption>
  <colgroup span='3'></colgroup>
  # 요고 위에랑 아래랑 같은 것. col로 나눠둘 경우, 따로 값을 설정할 수 있다.
  <colgroup>
    <col>
    <col>
    <col>
  </colgroup>
  <colgroup></colgroup>
```
### Table


### 컬러코드
* `#fcc`는 `#ffcccc`를 의미한다. 중복될 경우, 두 개를 하나로 줄일 수 있다.
* `rgb(200,255,200,0.1)`: RGB에 값 배정, 선명도 10%

# CSS
## Basic Information
* html은 문서의 구조만이, css는 그것이 표현되는 방식을 다뤄야 한다.
* css basic syntax: selector(선택자), property(속성), value(값)   

```css
selector {
property: value;
}
```	
## CSS 사용법
* 인라인 스타일 시트 (inline)
* 내부 스타일 시트 (internal)
* 외부 스타일 시트 (external)
	* `rel`: relation
	* `href`: hyperlink reference	

```html
  <link rel="stylesheet" href="./05.css">
```
## CSS 선택자
* 전체 (Universal)
	* `*`
	* html 문서 내 모든 요소에 적용
	* margin 혹은 padding 값의 초기화에 종종 사용된다.
	* 문서의 모든 요소를 읽기 때문에 로딩 시간이 길어질 수 있다.
* 태그 (Tag)
	* 태그 선택자는 공통적으로 공유하는 부분만 설정하자. 투머치 노노
* class, id
	* `tag.class`, `.class`
	* `tag#id`, `#id`
* 체인 (Chain)
	* `.class1.class2`: 두 개 이상의 클래스를 모두 지니는 요소만 선택
* 그룹 (Group)
	* `#id1#id2`: 여러 요소에 한 번에 적용.
* 복합 (Combinator)
	* 하위 (Descendent): `tag tag` 하위 모든 태그 선택
	* 자식 (Child): `tag > tag` 자식 태그만
	* 인접 형제 (Adjacent Sibling): `tag + tag` 가장 가까운 동생 태그 선택
	* 일반 형제 (General Siblibg): `tag ~ tag` 동생은 전부 호출
* 속성 (Attribute)
	* `tag[attribute]`: 특정 속성을 포함하는 경우
	* `tag[attribute="val"]`: 속성 값이 딱 이 모양 그대로인 경우
	* `tag[attribute~="val"]`: 속성 값이 공백으로 분리된 `val`을 포함하는 경우
	* `tag[attribute|="val"]`: 속성 값이 공백분리 `val`/ `val-`을 포함하는 경우
	* `tag[attribute^="val"]`: 속성 값이 `val`로 시작하는 모든 경우
	* `tag[attribute$="val"]`: 속성 값이 `val`로 끝나는 모든 경우
	* `tag[attribute*="val"]`: 어떤 형태로든 속성 값에 `val`이 포함되는 경우
* 가상 (Pseudo)
	* html 문서에 없어도 사용할 수 있는 가상의 선택자
	* 가상 클래스 (Pseudo-Class)
		* `tag:selector`의 형태를 지닌다.	
	* 가상 엘리먼트 (Pseudo-Element)
		* `tag::selector`의 형태를 지닌다.

## CSS Cascading (우선순위)
* 특정도 값이 높은 순서대로 적용된다.
* 특정도 순서
* !important
	* 해당 스타일의 value값 마지막에 `!important`추가
	* `font-size: 30px !important;`
* inline
* id
* class
* tag

> *`!important`와 inline 방식의 css 적용은 프로그램 규모가 커지면 완전히 꼬여버릴 수 있으므로 사용하지 않는다.  
> * 같은 유형의 선택자가 중복되어 적용된 코드일 수록 우선순위가 높아진다. (`p.class1.class2`)

## CSS Typography (서체)
* 글자 색: `color: #HEX코드, rgb(), rgba(), 색상이름;`
* 글씨체: `font-family: '돋움', arial;`
	* 기록된 순서대로 사용자 컴퓨터 설치 여부 판단. 설치된 폰트 우선 사용.
* 글씨체 종류: serif, monospace, sans-serif, cursive
* 글자 크기:
	* `font-size: 14px;`
	* `font-size: 2em;`: 부모요소(body)의 font-size를 기준으로 한 비율.
* 글자 스타일: `font-style: italic;`
* 글자 굵기: `font-weight:`
* 줄 간격: `line-height:`
* 문자 꾸미기: `text-decoration:`
* 문자 정렬: `text-align:`
* 문자 들여쓰기: `text-indent:`
* 대소문자 변환: `text-transform:`
* 자간: `letter-spacing: 5px;`
* 단어간격: `word-spacing:`
* 인라인 요소간 수직 정렬: `vertical-align:`
* 줄바꿈 설정: `white-space:`

## CSS Background
* 배경색:
* 배경 이미지:
* 배경 반복:
* 배경 위치:
* 배경 고정:
* 속기법:


## CSS Border
* 요소 방향 (Element's Direction): 상우하좌. 상단부터 시계방향.
* 테두리 굵기:
* 테두리 스타일:
* 테두리 색상:
* 속기법:

## CSS Box model
* css는 박스 형태를 이루며, 박스는 content, padding, border, margin으로 구성된다.
* 블록요소는 상하좌우 마진, 인라인 요소는 좌우마진만을 가진다.
* 마진 겹침 (margin collapse): 상하 마진만 겹침이 일어난다. 
* padding
* content: width, height
* 보더 기준 크기 지정: box-sizing

## CSS List Style
* 블릿 이미지: list-style-image:
* 블릿 타입: list-style-type:
* 블릿 위치: list-style-position:
* 속기법:

## CSS Table Style
* 테두리 겹침: `table { border-collapse: }`
* 테두리 간격: `table { border-spacing: }`
* 빈 셀 표시: `tr, td { empty-cells: }`
* 테이블 레이아웃: `table { table-layout: }`

## CSS Display
* display: block;
* display: inline;
* display: inline-block;
* display: none;
* visibility: hidden; visible;
* 


## <a name='170904'></a>Chrome Developer Tools 
### 단축키
* 요소검사 : `cmd + opt + i`
* 요소선택 : `cmd + shift + c`


## <a name='170904'></a>Terminal
* 컴퓨터 / HDD / Users / 사용자명
	* `cd /`: HDD 접근
	* `cd ~/`: 사용자명 접근
* `open .`: 현재 폴더 오픈
* `.`: 현재 폴더 의미
* `..`: 상위 폴더 의미
  
***  

# <a name='?'></a>공부할 것
1. `div`와 `span`의 사용  
2. 예습		
3. 백 그라운드 포지션 위치 변경해보기.  
4. margin 속기법

* css 선택자 적재 적소에 활용하기
* `flexbox` (float 대신 사용하는 것. 예전 브라우저를 지원하는 것이 단점일 뿐.)
* ko.learnlayout.com/flexbox.html
	* 위 페이지 
* css// `calc` ?
* css// `transition-duration: 0.1s;`
* css// `transform: translate(x,y);`
* 다방 호버링할 때 색 변하는 것 이미지 `opacity`가 `.6`으로 변하는 것이다!!!!!
* `text-overflow: ellipsis` 국경없는 의사회 페이지에 나와있는 코드로, 오버플로우 되어 있는 텍스트를 `...`으로 처리해준다.
* [CSS]배경이미지 풀화면 100%로 보여주는 방법
* jekill 테마적용
* 맥 재설치


# <a name='??'></a>질문

* image vertical align


* sass 부모 참조 선택자가 뒤에 있을 때 130쪽

#### 다방  
* div.terms의 width가 왜 1% 씩을 가지나요 :   
display가 table-cell로 되어 있다. table의 경우 각 요소간의 비율로 너비가 설정된다. % 총합이 부모 영역을 초과하지 않는 선에서 각 요소가 1%이든 2%이든 같은 비율로 분배된다는 것. 
* * `position: relative`속성을 지니는 `div.mid-theme-hanger`를 상속하는   
두 형제 division`div.mid-theme-link-image`와 `div.mid-theme-link-image-layer`가   
모두 `position: relative` 속성을 지닐 때, 왜 둘이 충돌하나요
	* 두 번째만 absolute로 바꾸는 것은 된다. 하지만 top과 left를 줘야 동작한다.
* `opacity`적용 속도가 해결이 안 됩니다. transition: transform 0.3s, opacity 0s;

* 다방의 링크 없는 anchor 태그는 도데체 무엇인가. datareacted 사용.  
* 아래 코드가 왜 적용이 안 되는지 노이해.---- 아아아아아ㅏㄱ 언어스코어 때문이다!!!!!

```css
section.mid-section > nav.mid-sitemap div.mid_sitemap ul h3 {
  font-size: 15px;
  line-height: 1.9;
}
```

* sitemap에서 clearfix를 붙여도 상위 nav가 그 크기를 인식하지 못하는 이유는?
