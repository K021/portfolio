


<h1 class='header'><span>Bootstrap 4</span></h1>

## 참고자료

- [부트스트랩 4 홈페이지](https://getbootstrap.com/)




# 설치

> javascript 는 컴파일된 파일을, css 는 sass 파일을 사용했다.

부트스트랩 4를 사용하기 위해선 다음 세 가지를 설치해야 한다.

1. `javascript 파일`: 부트스트랩의 동적 기능을 구현한다.
2. `css 파일`: 부트스트랩 거의 모든 기능의 기반이 된다.
3. `Font Awesome`: 부트스트랩 4에서는 아이콘 컴포넌트가 사라졌다. 아이콘을 사용한다면 필요한 사항이다. 


## 컴파일된 javascript 파일 설치

> ##### javascript file 이 필요한 부트스트랩 기능 [#](https://getbootstrap.com/docs/4.1/getting-started/introduction/#js)
> 
> - Alerts for dismissing
- Buttons for toggling states and checkbox/radio functionality
- Carousel for all slide behaviors, controls, and indicators
- Collapse for toggling visibility of content
- Dropdowns for displaying and positioning (also requires Popper.js)
- Modals for displaying, positioning, and scroll behavior
- Navbar for extending our Collapse plugin to implement responsive behavior
- Tooltips and popovers for displaying and positioning (also requires Popper.js)
- Scrollspy for scroll behavior and navigation updates



부트스트랩에 필요한 자바스크립트는 세 가지가 있고, 다음의 순서대로 불러와야 한다. 

- jquery
- popper.js
- bootstrap.js

따라서 CDN 을 사용할 때는 다음과 같이 불러오게 되는데,

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
```

CDN 은 속도가 느려지므로, 이제 저 파일들 하나 하나 다운로드해서 해결해보자.


### 1. `jquery.slim.js`

부트스트랩에 필요한 jquery 는 normal version 이 아닌 slim version 이다. 둘이 뭐가 다른지는 정확히는 모르겠으나, slim 파일이 더 가벼운 파일임은 확실하다. normal verion 에는 불필요한 기능이 많아서 slim 을 쓰는 듯하다.

다운로드 방식에는 세 가지가 있다:

1. Pycharm 에서 작업하는 html 에 CDN 연결하기
	
	다음과 같이 입력하면, 파이참에서 다운로드하라는 경고가 뜬다. 다운로드하면, `External Libraries`라는 곳에 저장되는데, 이 파일을 가져다가 원하는 곳에 두자.
	
	```html
	<body>
		...
		<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	</body>
	```
	
2. [CDN 소스 링크](https://code.jquery.com/jquery-3.3.1.slim.min.js)를 열어 내용을 복사한 후, js 파일로 저장하기
3. [jQuery 다운로드 홈페이지](http://jquery.com/download/)에서 `compressed`, `slim` 파일 다운로드 하기 (바로 브라우저에서 열리는 경우, 우클릭 '링크된 파일다운로드'를 선택하자)


### 2. `popper.js` & `bootstrap.js` = `bootstrap.bundle.js`

jquery 와 마찬가지로 CDN 소스링크에 저장된 파일을 가져올 수도 있지만, Bootstrap4 에서는 `bootstrap.bundle.js` 에 popper 기능이 포함되어 있다. 

> - [부트스트랩 홈페이지 - js 파일 설명](https://getbootstrap.com/docs/4.1/getting-started/contents/#js-files)
> - [부트스트랩 홈페이지 - 부트스트랩 js 에 관련된 전반적인 설명](https://getbootstrap.com/docs/4.1/getting-started/introduction/#js)



## Sass 파일 설치

Bootstrap 4의 Sass 소스파일은 다음과 같은 구조로 되어있다.

- mixins/
- utilities/
- 기타 여러 partial 파일들
- bootstrap.scss
- bootstrap-grid.scss
- bootstrap-reboot.scss

여기서 `bootstrap-grid.scss`와 `bootstrap-reboot.scss` 파일은 부분적인 파일로, `bootstrap.scss` 와 중복이된다. 버리자.

나는 다음과 같이 구성했다:

```
static/
|
|– sass/
|   |– vendors/   				# 외부에서 가져온 Sass 보관
|   |   |– bootstrap/			# partial file 보관
|   |   |   |– partial files	
|   |   |   |- ...
|   |   |
|   |   |- _bootstrap.scss		# partial file 하나로 모음
|   |
|   |- main.scss
|
|- css/							# 컴파일된 css 가 저장될 곳 
```

Sass 컴파일 설정 후, html 에 반영해주자.

```html
<head>
	...
	<link rel="stylesheet" href="{% static 'css/main.min.css' %}">
</head>
```

> ##### static 태그가 오류날 때 점검할 사항
> 1. html 문서 상단에 `{% load static %}` 선언
> 2. `settings.py` static directory 설정
> 	- `STATIC_DIR = os.path.join(BASE_DIR, 'static')`
> 	- `STATICFILES_DIRS = [STATIC_DIR]`
> 3. Pycharm Django Support 설정
> 	- `Preferences` &rarr; `Languages & Frameworks` &rarr; `Django`
> 4. Pycharm Template Language 설정
> 	- `Preferences` &rarr; `Languages & Frameworks` &rarr; `Python Template Languages` 


## Font Awesome 설치

> Bootstrap 4 에선 아쉽게도 아이콘 기능이 사라졌다. 별도로 설치해주어야 하고, 꼭 Font Awesome 을 쓸 필요는 없지만 이게 제일 좋아보인다.

Font Awesome 을 사용하는 방식에는 두 가지가 있다:

- Webfont 와 CSS
- SVG 와 JS

svg & js 방식은 페이지를 리로드 할 때마다 새로 생성되기 때문에 불필요한 작업을 요구한다. 이 문서에서는 웹폰트와 CSS 를 사용하는 방식을 다룰 것이다. 

[Font Awesome 다운로드 페이지](https://fontawesome.com/how-to-use/on-the-web/setup/getting-started?using=web-fonts-with-css)에서 파일들 다운로드 하면, 여러가지 폴더와 파일들이 들어있는데, 우리가 필요한 것은 딱 두 가지다:

- css/
- webfonts/


### 1. CSS 파일 설치: `all.css`

css 폴더에는 6가지 종류의 css 파일이 들어있다:

- `all.css`: brand, regular, solid, fontawesome 네 가지를 합친 것
- `brands.css`: brand font 의 경로 정보
- `fontawesome.css`: 폰트 경로 없이 CSS 만 담고 있는 것 같다.
- `regular.css`: regular font 의 경로 정보
- `solid.css`: solid font 의 경로 정보
- `svg-with-js.css`: svg & js 방식에서 필요한 파일인 듯하다
- `v4-shims.css`: 이건 뭔지 모르겠다.

css 파일을 가능한 한 가볍게 하고 싶어서, 꼭 필요한 아이콘을 제외하고는 포함시키고 싶지 않았는데, 필요한게 뭔지, 그게 어디에 속하는지 몰라 그냥 `all.css`를 가져왔다. 나중에 개발이 다 끝난 후에 솎아내려고 한다.


### 2. Webfont 파일 설치

`all.css` 파일에는 webfont 경로를 저장하고 있는데, 이 값은 `all.css` 파일 기준으로 `../webfonts/`로 되어있다. 일반적인 파일 구조를 따르고 있는 것:

```
// all.css 파일 기준으로 `../webfonts/`에 폰트를 저장해야 한다. 
static/
|
|– css/
|   |- all.css
|   
|- webfonts/
|   |- fonts
|   |- ...
```
저장위치를 변경하고 싶다면, `all.css`의 `@font-face`를 일일히 바꿔주거나, `_variables.scss` 파일의 `$fa-font-path`를 변경후 컴파일해주어야 한다. 귀찮아서 나는 위에처럼 했다.


##### all.css 의 `@font-face` 일부

```css
@font-face {
  font-family: 'Font Awesome 5 Brands';
  font-style: normal;
  font-weight: normal;
  src: url("../webfonts/fa-brands-400.eot");
  src: url("../webfonts/fa-brands-400.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-brands-400.woff2") format("woff2"), url("../webfonts/fa-brands-400.woff") format("woff"), url("../webfonts/fa-brands-400.ttf") format("truetype"), url("../webfonts/fa-brands-400.svg#fontawesome") format("svg"); }
```

##### _variables.scss 의 `$fa-font-path`

```scss
$fa-font-path:                "../webfonts" !default;
```


### Font Awesome 사용하기

1. html 에 css 링크 걸기
	
	```html
	<link rel="stylesheet" href="{% static 'css/fontawsome.all.min.css' %}">
	```
2. [홈페이지](https://fontawesome.com/)에서 아이콘을 찾으면, 사용할 수 있는 코드가 나온다. 복붙하면 끝.





# Bootstrap Sass 수정하기

## input

##### input focus 색 바꾸기

```scss
$red: #dc3545;
$component-active-bg: $red;
$input-btn-focus-color: rgba($component-active-bg, .25);
```





# 부록: Bootstrap 3.0 

## 참고자료

- [Bootstrap 공식 홈페이지](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [Tutorial Republic](https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-dropdowns.php)


### 그리드 시스템

1. `.container`(반응형 고정폭) / `.container-fluid`(반응형 최대폭)
2. `.row` > `col-크기-숫자`  


### Typography
- `p`: 본문
- `p.lead`: 얇고 큰 글자
- `small`,`.small`
- `del`, `s`: 취소선 (각각 삭제, 정정되었음의 의미)
- `ins`, `u`: 밑줄 (각각 추가로 다루어질 예정, 그냥 밑줄의 의미)
- `mark`: 형광펜 효과
- `strong`: 볼드 (강조 의미)
- `em`: 이탤릭
- `b`: 볼드
- `abbr`: 커서를 대면 설명 나타남
- `abbr.initialism`: 90% 작게 (대문자 용어를 약간 작게 표시하기 위한 용도)
- `address` > `strong` 이름 같은 거 > `br` 맨 끝에 개행
- `a[href=mailto:joo2theeon@gmail.com]`: 누르면 메일 보내지는 링크

##### 1em = 14px



### 텍스트 정렬 및 대문자
:`.text-*`

- `left`, `right`, `center`
- `justify`, `nowrap`: 각각 양쪽 정렬, 아무 것도 아님
- `lowercase`, `uppercase`, `capitalize`


### 인용구
- `blockquote`: 인용구 디자인
- `footer`: 말한 사람 (출처)
- `cite`: 출처의 소스


### 목록
- `.list-unstyled`: 점 없는 리스트
- `.list-inline`: 인라인 리스트 (세로 말고 가로 배열)
- `dl`: Description List. 하위에 `dt`와 `dd`를 가진다.
- `dt`: 볼드 형태로 제목의 자리에 간다
- `dd`: 일반체로 내용을 담당한다
- `.dl-horizontal`: 제목이 왼쪽에, 내용이 오른쪽에 오는 리스트 형태로 배열된다


### 테이블
: 기본적으로 `table` 태그여야 한다

##### 반응형 테이블
- `.table-responsive`: 테이블 위에 설정, 작은 화면 수평 스크롤


##### 테이블 스타일
- `.table-stripted`: 줄 색 교차적 배열
- `.table-bordered`: 세로줄 추가
- `.table-hover`: 호버 하면 색 변화
- `.table-condensed`: 좁은 테이블

##### 테이블 색
- `.active`: 회색
- `.success`: 초록
- `.warning`: 노랑
- `.danger`: 빨강
- `.info`: 파랑

### 맥락

##### 텍스트 색
- `.text-muted`: 연한 회색
- `.text-primary`: 하늘색
- `.text-success`: 연두색
- `.text-info`: 청록색
- `.text-warning`: 금색
- `.text-danger`: 적갈색

##### 배경색
- `.bg-primary`: 파란색
- `.bg-success`: 연녹색
- `.bg-info`: 연파랑
- `.bg-warning`: 연노랑
- `.bg-danger`: 분홍색

### Float
- `.pull-left`
- `.pull-right`

### 가운데 정렬
- `.center-block`

### clearfix
- `.clearfix`


### container
- `.container`: 양쪽에 약간 여백이 생김. 화면에 맞게 줄어들음. 작은 화면에선 좌우 꽉참
- `.container-fluid`: 늘 좌우 꽉참.

### 컨텐츠 보이고 숨기기
- `.hidden`: 아예 안 보임
- `.invisible`: 공간은 차지하되, 보이지 않음

### 반응형 유틸리티
- `.visible-<size>-<display>`: 특정 사이즈에서만 보임, 디스플레이 속성 변화
- `.hidden-<size>-<display>`: 특정 사이즈에서만 안 보임, 디스플레이 속성 변화
- `.visible/hidden-print-<display>`: 프린트하는 경우 제어 