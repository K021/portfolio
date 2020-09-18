<h1 class='header'><span>Sass 사용하기</span></h1>

> ##### 참고 
> - [Sass 작성 가이드](https://sass-guidelin.es/ko/)
> - [Sass 공식 홈페이지 가이드](http://sass-lang.com/guide)
> 	- [Sass 공식 홈페이지 - 자세한 문서](http://sass-lang.com/documentation/file.SASS_REFERENCE.html)
> 	- [Sass 공식 홈페이지 - 함수 총괄 문서](http://sass-lang.com/documentation/Sass/Script/Functions.html)
> - [poiemaweb](https://poiemaweb.com/sass-script)
> - [The Sass way: Sass 관련 조언을 난이도별로 모아둔 곳](http://thesassway.com/beginner)



## 컴파일 하기

##### 1. 파일 하나 컴파일 하기

`sass input.scss output.css`: 앞에가 컴파일하려는 Sass 파일이고, 뒤가 저장하려는 CSS 파일 이름이다. 

##### 2. Sass 파일이 바뀔 때마다 자동 컴파일 하기

`sass --watch input.scss output.css`: 해당 Sass 파일을 저장할 때마다 새로 컴파일된다.

##### 3. 아예 폴더를 지정하기

`sass --watch app/sass:public/css`: `app/sass` 폴더에 있는 모든 Sass 파일의 변화를 감지하여 `public/css` 폴더에 컴파일한다.

##### 4. 용량 최소화하기

`sass input.scss output.css --style compressed`

이렇게 공백이 없는 파일로 컴파일하기 위해서는 스타일 옵션을 주면 되는데, 스타일 옵션에는 네 가지가 있다. 

- `nested`: 기본으로, 닫는 괄호가 줄 끝에 붙는다. 

```scss
.btn-red {
  color: red; }

.btn-black {
  color: black; }
``` 

- `compact`: 각 설정이 한 줄로 정리된다.

```scss
.btn-red { color: red; }

.btn-black { color: black; }
```

- `compressed`: 가장 압축된 형태로 모든 공백이 사라진다.

```scss
.btn-red{color:red;}.btn-black{color:black;}
```

- `expanded`: 가장 열린 형태로, 마지막 괄호가 줄바꿈 해서 붙는다.

```scss
.btn-red {
  color: red;
}

.btn-black {
  color: black;
}
```

##### 5. 파이참에서 자동 컴파일 설정하기

파이참에서 scss file 을 처음 생성하면 이 watcher 를 만들거냐고 물어본다. 그때 상당부분 알아서 작성된다. 

1. `Preferences` &rarr; `Tools` &rarr; `File Watchers` &rarr; `add button` (`+`)
2. `Name`: 아무거나 설정 (기본값 `SCSS`)
3. `File Type`: `SCSS` 선택
4. `Scope`: `Project Files` 선택
5. `Program`: `/Users/<owner_name>/.rbenv/shims/scss`
6. `Arguments`: `Working directory` 를 기준 상대경로로, 다음과 같이 적어야 한다
	
	```bash
	// --no-cache: sass 캐쉬 파일을 만들지 않는다
	// --update: 파일 뿐 아니라 폴더 기준으로도 컴파일 한다
	--no-cache --update scss/$FileName$:css/$FileNameWithoutExtension$.css
	```
	
	이 watcher 를 복사해서 새로운 워쳐를 만든 후, 다음과 같이 입력하면 min.css 파일도 만들 수 있다
	
	```bash
	--no-cache --update scss/$FileName$:css/$FileNameWithoutExtension$.min.css --style compressed
	```
	
7. `Output paths to refresh`: css 파일과 scss 파일을 이어주는 `map` 파일을 어떤 이름으로 저장할지 설정하는 변수인 듯하다. 아래처럼 적어주면, 일반적인 방법 대로 css 파일 바로 옆에 css.map 파일이 저장된다. 이걸 바꾼다고 저장되는 경로가 바뀌는 것은 아니다. 출력 문서 저장 경로는 당연하게도 `Arguments 에 의해 결정된다.` ― <cite>[jetbrains docs - watcher](https://www.jetbrains.com/help/pycharm/2018.1/new-watcher-dialog.html)</cite>
	
	```bash
	$FileNameWithoutExtension$.css:$FileNameWithoutExtension$.css.map
	```
	
8. `Working directory`: 상대경로를 지정하기에 적절한 작업 폴더. 상대경로의 기준이 된다. 

![](img/sass/pycharm-sass-preference-2.png)

> sass 파일이 클 경우에는, 파이참이 컴파일하는데 시간이 걸릴 수 있으며, 컴파일 후에도 파일 목록에 나타나지 않을 수도 있다. 그런 경우에는 파인더에서 보면 보이고, 파인더에서 본 후에 파이참에 다시 들어가면 보인다.  
> 
> 


## Sass vs SCSS

Sass 는 전처리기를 의미하기도 하고, 구문을 의미하기도 한다. 구문으로서의 Sass 는 들여쓰기를 감지하는 구문을 가리키는 용어였고, Sassy CSS 라는 의미의 SCSS 구문이 생기게 되었다. 

구문적인 차이만 있고, 기능은 같다. SCSS 가 콜론이나 괄호를 써야한다는 점에서 더 CSS 스럽다고 할 수 있다. CSS 와 비슷하고 친숙하다는 이유로 많은 개발자들이 SCSS 를 선호한다. 본 문서는 SCSS 문법을 기준으로 작성되었다. 



## 주석

- Sass 에만 주석을 달고자 할 때: `// 한 줄 주석`
- CSS 에도 주석을 남기고자 할 때: `/* 여러 줄 주석 */`


## 변수  

```scss
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

### interpolation (`#{}`)

interpolation 을 사용하여 태그나 속성에 변수를 사용할 수 있다. 

```scss
$name: foo;
$attr: border;
p.#{$name} {
  #{$attr}-color: blue;
}

@mixin red-on($selector, $selector2) {
  #{$selector}:#{$selector2} {
    color: #d00;
  }
}

@include red-on("box", focus);
```

`@fuction`으로 만든 색을 조절하는 함수를 사용했을 때 셍긴 오류를, interpolation 으로 해결했다. 변수나 함수 출력값이 잘 작동하지 않으면 한 번씩 써보면 좋을 듯하다. 

```scss
@function tint($color, $percentage) {
  @return mix(white, $color, $percentage);
}

$co: tint(red, 100%);  // 이건 항상 잘 된다

.box {
  color: #{tint(red, 70%)};  // 수정후 작동하는 코드
}

.box-2 {
  color: tint(red, 70%);  // 왜인지는 모르겠으나 오류가 발생한다. 
}
```



## 상수

어떤 상황에서도 변경되지 않아야 하는 변수를 다룰 일이 생긴다. Sass 는 상수를 특별히 구분하지 않지만, 일반적인 작명 관례를 따라주는 것이 좋다. 모두 대문자에 언더스코어로 구분하자.

```scss
// Yep
$CSS_POSITIONS: (top, right, bottom, left, center); 
// Nope
$css-positions: (top, right, bottom, left, center); 
```



## 문자열

### 인코딩

문자열 인코딩 문제를 피하기 위해서는, 메인스타일 시트에서 `UTF-8` 인코딩을 설정할 필요가 있다. 맨 앞에, 가장 첫번째 요소가 되도록 하자. 

```scss
@charset 'utf-8';
```

> ##### 메인 스타일 시트란?
> 
> sass 를 사용할 때는, 앞에 언더스코어가 붙지 않은 파일은 `main.scss` 하나만 있기를 권장한다. 이 파일은 `@charset`, `@import`, 그리고 주석 외에는 아무것도 포함하지 않는 것이 좋다고 한다. ― <cite>[sass guideline](https://sass-guidelin.es/ko/#main-)</cite>


### 따옴표

- css 와 같이 sass 역시 문자열이 따옴표로 둘러싸일 필요가 없습니다.
- 그러나 문자열에 따옴표가 필요 없는 언어는 소수라는 점과, 다음 몇가지의 문제로 인해 **문자열은 따옴표로 감싸는 것이 좋습니다.**
	- 색 이름은 따옴표가 없으면 색으로 취급된다. 
	- 가독성에 도움이 된다. 
	- 문자열을 따옴표로 감싸지 않아야 하는 타당한 이유가 없기에, 다른 언오와의 일관성을 유지하는 것이 더 좋다. 



## 숫자

##### 단위 붙이거나 떼기
숫자에 단위를 붙이거나 뗄 때에는 1 단위를 곱하거나 나누자. 

```scss
$value: 42;
$length: $value * 1px;  // 42px
```

##### 숫자 연산에서 단위 조심하기
두 숫자를 곱할 때에는 단위가 중복되지 않나 검사하자. `2px * 2px` 은 제곱픽셀이 되어 오류가 나고, `2px / 2px`은 단위가 사라진다. 

```scss
$width: 2px * 2px // 오류
$height: 2px / 2px // 단위 없이 그냥 1
```

##### 최상위 계산에는 괄호
최상위 숫자 계산은 언제나 괄호로 감싸자. 가독성을 향상시킬 뿐아니라, 계산을 강제하기 때문에 예외적인 상황을 방지할 수 있다. 


```scss
// Yep
.foo {
  width: (100% / 3);
}

// Nope
.foo {
  width: 100% / 3;
}
```

##### 매직넘버에는 주석을 달자
매직넘버를 사용할 때는 주석을 달아두자. 

```scss
// 0.327em: .foo 의 상단을 부모에 맞추기 위한 값
.foo {
  top: 0.327em;
}
```

> 매직넘버: 특정 목적을 달성하기 위해 세밀하게 조정한 숫자 값으로, 어쩌다보니 맞아 떨어지지만, 왜 그래야 하는지는 설명하기 어려운 임의의 숫자를 가리킨다. 



## 색 서식


##### HSL, RGB 이용하기
색 서식은 쉽게 이해할 수 있는 HSL 표기법이나 RGB를 이용하자. 

```scss
.foo {
  color: hsl(0, 100%, 50%);
}

.foo {
  color: rgb(255, 0, 0);
}
```

##### 색 이름과 용도 변수를 지정하기
색을 한 번 이상 사용할 때는 변수에 저장하여 활용하자. 이때, 색 이름을 저장하는 변수와, 그 색의 용도를 저장하는 변수를 따로 지정하면 더 좋다. 

```scss
$baby-pink: hsl(330, 50%, 60%);
$main-theme-color: $baby-pink;
```

이렇게 저장하면 `$baby-pink: blue;` 와 같은 불상사를 막을 수 있다. 

##### 명도조절하기
간단한 명도 조절을 위해서는 `lighten()`, `darken()`, 또는 `mix()`를 사용할 수 있다. `mix(색1, 색2, 1번 색의 비율)` 함수가 좀더 세밀하게 변하므로, 다음과 같은 함수를 정의해서 사용하면 편하다. 

```scss
// 색을 약간 밝게 한다
// $color: 밝게 만들려는 색
// $percentage: 반환될 색 내 white의 백분율
@function tint($color, $percentage) {
  @return mix(white, $color, $percentage);
}

// 색을 약간 어둡게 한다
@fuction shade($color, $percentage) {
  @return mix(black, $color, $percentage);
}

$co: tint(red, 100%);  // 이건 항상 잘 된다

.box {
  color: #{tint(red, 70%)};  // 수정후 작동하는 코드
}

.box-2 {
  color: tint(red, 70%);  // 왜인지는 모르겠으나 오류가 발생한다. 
}
```


## 리스트

- CSS 상에서 그대로 사용되지 않는 한, 언제나 쉼표로 분리하는 것이 좋다.
- 늘 괄호로 감싸는 것이 좋다.  

```scss
$font-stack: ('Helvetica', 'Arial', sans-serif);

$font-stack: (
  'Helvetica',
  'Arial',
  sans-serif,  // 여러 줄인 경우 맨 마지막에 쉼표를 붙여주어야 한다. 
);
```

##### 요소 추가는 append(리스트, 추가요소, 대문자)

```scss
append(리스트, 추가하려는 요소, 구분자)
// 구분자에는 comma, space, auto 가 들어갈 수 있다.
// auto 는 기존 리스트의 구분자를 따라가며, 아무것도 입력하지 않을 때의 기본값이다. 
```

```scss
$shadows: (0 42px 13.37px hotpink);

// Yep
$shadows: append($shadows, helvetica, comma);

.col {
  font-family: $shadows;
}
```

##### 인덱스는 index(리스트, 값)

`index($list, $value)` : 리스트 안에 있는 값의 인덱스를 출력한다. 

##### 길이는 length(리스트)

`length($list)` : 리스트의 길이를 출력한다.

##### 인덱스로 값 꺼내기 nth(리스트, 인덱스)

`nth($list, $n)` : 리스트 안의 값을 인덱스에 맞게 꺼낸다.


## Map

breakpoint mixin 모듈을 만들 때 맵을 사용할 수 있다. 맵은 파이썬의 딕셔너리에 해당하는 자료형으로, 키와 그에 대응하는 밸류 값을 저장하고 있다.   

```sass
// _config.scss
$breakpoints: (
  small: 767px,
  medium: 992px,
  large: 1200px
);

// _mixins.scss
@mixin respond-to($breakpoint) {
  @if map-has-key($breakpoints, $breakpoint) {
    @media (min-width: #{map-get($breakpoints, $breakpoint)}) {
      @content;
    }
  }

  @else {
    @error "Unfortunately, no value could be retrieved from `#{$breakpoint}`. "
        + "Please make sure it is defined in `$breakpoints` map.";
  }
}

// _component.scss
@include respond-to(small) {
  .ele {
    color: tomato;
  }
}
```



## Nesting

```scss
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}
```



## Partials

앞에 언더스코어를 붙이면 임포트는 되지만, CSS로 변환되지 않는다. `_partial.scss`



## Import

`_reset.scss` 파일을 `base.scss` 파일에서 임포트해보자.

```scss
// _reset.scss

html,
body,
ul,
ol {
  margin:  0;
  padding: 0;
}
```

```scss
// base.scss

@import 'reset';

body {
  font: 100% Helvetica, sans-serif;
  background-color: #efefef;
}
```

보이는 것 처럼, 확장자 `.scss`를 쓸 필요가 없고, partial file 임을 나타내는 언더스코어도 무시할 수 있다. 



## Mixins

```scss
@mixin transform($property) {
  -webkit-transform: $property;
      -ms-transform: $property;
          transform: $property;
}

.box { @include transform(rotate(30deg)); }
```


## 확장과 상속, 그리고 Placeholder

`@extend` 로 표현되는 상속은 서로 비슷한 태그가 있을 때 불필요한 중복을 없애준다. 태그나 Placeholder 를 상속할 수 있는데, Placeholder 는 태그는 아니지만 태그처럼 CSS 정보를 포함하고 있는 임시 태그 정도로 이해하면 좋다. 상속되지 않은 Placeholder 는 컴파일되지 않는다. Placeholder 는 `%`를 앞에 붙여줌으로써 구분된다. 

```scss
// This CSS won't print because %equal-heights is never extended.
%equal-heights {
  display: flex;
  flex-wrap: wrap;
}

// This CSS will print because %message-shared is extended.
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

.message {
  @extend %message-shared;
}

.success {
  @extend %message-shared;
  border-color: green;
}

.error {
  @extend %message-shared;
  border-color: red;
}

.warning {
  @extend %message-shared;
  border-color: yellow;
}
```

아래와 같이 그냥 태그도 상속할 수 있다. 

```scss
.error {
  border: 1px #f00;
  background-color: #fdd;
}
.seriousError {
  @extend .error;
  border-width: 3px;
}
```



## 연산자

scss file 에선 `+`, `-`, `*`, `/`, `%` 연산자를 사용할 수 있다.

```sass
.container { width: 100%; }


article[role="main"] {
  float: left;
  width: 600px / 960px * 100%;
}

aside[role="complementary"] {
  float: right;
  width: 300px / 960px * 100%;
}
```

`==`, `!=`, `&&`, `||`, `!`(not) 과 같은 불리언 연산도 가능하다.



## 조건문

### if(조건, 참일 때 출력 값, 거짓일 때 출력 값)

```scss
$type: ocean;

p {
  color: if($type == ocean, blue, black); // color: blue;
}
```

### @if

```scss
$type: monster;

p {
  @if $type == ocean {
    color: blue;
  } @else if $type == matador {
    color: red;
  } @else if $type == monster {
    color: green;
  } @else {
    color: black;
  }
}
```


## 반복문

### 1. @each 문

`@each` 문은 `@each $아무변수 in 리스트` 로 이루어진다. 리스트 원소를 순서대로 변수에 대입하고, 주어진 작업을 수행한다. 

```scss
@each $animal in puma, sea-slug, egret, salamander {
  .#{$animal}-icon {
    background-image: url('/images/#{$animal}.png');
  }
}
```

결과물은 다음과 같다. 

```css
.puma-icon {
  background-image: url("/images/puma.png"); }

.sea-slug-icon {
  background-image: url("/images/sea-slug.png"); }

.egret-icon {
  background-image: url("/images/egret.png"); }

.salamander-icon {
  background-image: url("/images/salamander.png"); }
```

한 번에 여러개의 변수를 할당할 수도 있다. 

```scss
@each $animal, $color, $cursor in (puma, black, default),
                                  (sea-slug, blue, pointer),
                                  (egret, white, move) {
  .#{$animal}-icon {
    background-image: url('/images/#{$animal}.png');
    border: 2px solid $color;
    cursor: $cursor;
  }
}
```

맵에서 키 밸류를 꺼낼 수도 있다.

```scss
each $key, $value in $map {
  .section-#{$key} {
    background-color: $value;
  }
}
```

### 2. For 문

아래와 같이 특정 범위 안의 연속적인 숫자를 다룰 때를 제외하고는 `@each` 문을 사용하도록 하자. 

```scss
// 1 부터 10까지 반복 (10을 포함한다)
// 10을 제외하려면 `from 1 to 10`을 사용하면 되나, 아는 사람이 많이 없으므로 through 를 사용하자. 
@for $i from 1 through 10 {
  .foo:nth-of-type(#{$i}) {
    border-color: hsl($i * 36, 50%, 50%);
  }
}
```

### 3. while 문

Sass 에는 while 문도 있으나 왠만하면 사용하지 말자. 실수하면 무한 루프가 생길 위험이 있기 때문이다. 




## breakpoint manager

```scss
// _config.scss
$breakpoints: (
  small: 767px,
  medium: 992px,
  large: 1200px
);

// _mixins.scss
@mixin respond-to($breakpoint) {
  @if map-has-key($breakpoints, $breakpoint) {
    @media (min-width: #{map-get($breakpoints, $breakpoint)}) {
      @content;
    }
  }

  @else {
    @error "Unfortunately, no value could be retrieved from `#{$breakpoint}`. "
        + "Please make sure it is defined in `$breakpoints` map.";
  }
}

// _component.scss
@include respond-to(small) {
  .ele {
    color: tomato;
  }
}
```

이것은 아주 단순한 타입의 매니저로, 좀 더 많은 기능이 필요하다면, [Sass-MQ](https://github.com/sass-mq/sass-mq), [Breakpoint](http://breakpoint-sass.com/), [include-media](https://github.com/eduardoboucas/include-media)와 같은 검증된 것을 사용하자.




## Mixin

##### 1. 믹스인 활용 예시

```scss
// 아래의 높이 설정은 기본값 설정이다. 
@mixin size($width, $height: $width) {
      width: $width;
      height: $height;
}
```

아래와 같은 position 믹스인을 만들 수도 있으나, 나는 사실 그 필요성을 느끼지 못한다. 하지만 `@each` 문의 사용과, 믹스인의 사용 예시를 위해 첨부한다. 

```scss
@mixin position($position, $args) {
  @each $o in top right bottom left {
        $i: index($args, $o);

    @if $i and $i + 1< = length($args) and type-of(nth($args, $i + 1)) == number  {
          #{$o}: nth($args, $i + 1);
    }
  }

  position: $position;
}

@mixin absolute($args) {
        @include position("absolute", $args);
}

@mixin fixed($args) {
        @include position("fixed", $args);
}

@mixin relative($args) {
        @include position("relative", $args);
}
```

##### 2. 믹스인 매개변수가 여러개일 때, `arglist`를 사용하자

변수에 `...`을 붙이면 `arglist`라는 새로운 형태의 클래스를 의미한다. 이는 파이썬의 `*args` 또는 `**kwargs`와 같은 형태로, 리스트나 맵을 바로 믹스인의 매개변수로 전달할 수 있도록 한다. 

```scss
@mixin shadows($shadows...) {
  // type-of($shadows) == 'arglist'
  // …
}
```

이렇게 믹스인을 선언할 때 사용할 수도 있고, 아래 처럼 믹스인 매개변수가 여러 개일 때, 매개변수를 전달해주는 용도로 사용할 수도 있다. 

```scss
@mixin dummy($a, $b, $c) {
  // …
}

// 아래릐 1, 2, 3 번은 같은 효과를 지닌다. 
// 1
@include dummy(true, 42, 'kittens');

// 2
$params: (true, 42, 'kittens');
@include dummy($params...);

// 3
$params: (
  'c': 'kittens',
  'a': true,
  'b': 42,
);
@include dummy($params...);
```



## @warn 과 @error 의 차이

`@error`는 컴파일이 불가능하지만, `@warn`은 컴파일이 된다. 둘 다 컴파일 시에 메세지를 보여준다. 




# Sass 구조 설계

## 패턴

```scss
sass/
|
|– base/
|   |– _base.scss        # html 요소의 표준 스타일
|   |– _reset.scss       # Reset/normalize
|   |– _typography.scss  # 타이포그래피 규칙
|   …                    # 기타.
|
|– components/
|   |– _buttons.scss     # 버튼
|   |– _carousel.scss    # 캐러셀
|   |– _cover.scss       # 커버
|   |– _dropdown.scss    # 드롭다운
|   …                    # 기타.
|
|– layout/
|   |– _navigation.scss  # 네비게이션
|   |– _grid.scss        # 그리드 시스템
|   |– _header.scss      # 헤더
|   |– _footer.scss      # 푸터
|   |– _sidebar.scss     # 사이드바
|   |– _forms.scss       # 폼
|   …                    # 기타.
|
|– pages/
|   |– _home.scss        # 홈 한정 스타일
|   |– _contact.scss     # 연락처 한정 스타일
|   …                    # 기타.
|
|– themes/
|   |– _theme.scss       # 디폴트 테마
|   |– _admin.scss       # 관리자 테마
|   …                    # 기타.
|
|– utils/
|   |– _variables.scss   # Sass 변수
|   |– _functions.scss   # Sass 함수
|   |– _mixins.scss      # Sass 믹스인
|   |– _helpers.scss     # 클래스 & 플레이스홀더 헬퍼
|
|– vendors/
|   |– _bootstrap.scss   # Bootstrap
|   |– _jquery-ui.scss   # jQuery UI
|   …                    # 기타.
|
|
`– main.scss             # 메인 Sass 파일
```

##### 폴더별 특징

- `base/`: 기본적인 정보를 담는다. 
- `layout/`: 레이아웃 디자인 정보. 헤더나 풋터, 그리드시스템, 또는 폼 디자인들.
- `components/`: 레이아웃보다 더 작은 것들이 들어간다. 레이아웃이 전반적인 뼈대를 정한다면, 컴포넌트는 작은 위젯에 초첨을 둔다. `modules/`라는 쵸현도 자주 사용한다. 
- `themes/`: 여러 테마가 필요한 앱을 설계하는 경우에 필요하나, 그러려면 규모가 꽤 있어야 하므로, 대부분 프로젝트에는 필요가 없을 수도 있다. 
- `utils/`: 프로젝트에서 사용되는 모든 Sass 도구를 저장해둔다. 변수, 함수, 믹스인, 플레이스홀더 등이 포함된다. 이 폴더는, 그 자체만으로는 컴파일 될 것이 없는 것을 모아두어야 한다. 
- `vendors/`: 대부분의 프로젝트는 Normalize, Bootstrap, jQueryUI, FancyCarouselSliderjQueryPowered 등의 외부 라이브러리를 사용하는데, 이때 이 폴더가 필요하다. 내가 하지 않은 것들을 모아두는 곳이다. 
- `main.scss`: 이 파일은 전체 프로젝트에서 언더스코어로 시작하지 않는 유일한 Sass 파일이어야 한다. 이 파일은 `@charset`, `@import`와 주석 외에는 다른 것이 기록되지 않아야 한다. 


##### main.scss 의 예시
```scss
@import
  'abstracts/variables',
  'abstracts/functions',
  'abstracts/mixins',
  'abstracts/placeholders';

@import
  'vendors/bootstrap',
  'vendors/jquery-ui';

@import
  'base/reset',
  'base/typography';

@import
  'layout/navigation',
  'layout/grid',
  'layout/header',
  'layout/footer',
  'layout/sidebar',
  'layout/forms';

@import
  'components/buttons',
  'components/carousel',
  'components/cover',
  'components/dropdown';

@import
  'pages/home',
  'pages/contact';

@import
  'themes/theme',
  'themes/admin';
```