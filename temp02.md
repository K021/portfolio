## Pycharm Shortcuts

| functioning               	| shortcut  (custom) |
|-----------------------------|--------------------|
| 코드 추천                 		| `ctr+space`        |
| 단계별 블록처리 (indentation) 	| `ctr+opt+I`        |
| Formatting                  | `option+command+L` |
| viewing code structure      | `cmd+7`            |
| navigation                  | `cmd+B`/`cmd+click`|
| Searching for usages        | `opt+F7`           |
| Commenting                  | `cmd+/`            |
| wraping                     | `ctl+W`            |
| Complete Current Statement  | `shift+cmd+etr` (`ctr+cmd+etr`) |
| Code Completion Basic	(두번 치면 임포트 안된 것도 찾아준다) | `ctr+space` (`cmd+etr`)|


## 해결할 것들



# Django template

## 변수 선언 (with)
: 그냥 선언, 클래스 변수 이용, 필터링도 가능, 중복 선언 가능

```html
{% with post_tab='post' post_pk=post.pk|stringformat:"i" %}
```

## 정수를 문자열로 형변환 (stringformat)

```html
{% with post_pk=post.pk|stringformat:"i" %}
```
post.pk 에 들어있는 정수를 문자열로 변환해준다. 

- [django docs](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#stringformat)
- [python doc - stringformat의 옵션들](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

## add 
: 같은 자료형끼리만 되는 듯하다. 

```html
# 문자열과 정수형이므로 연산이 불가능하다. 
{{ 'post'|add:8 }}

# 위에 나온 with 태그와 stringformat filter로 정수를 문자열로 변환해주자
{% with post_pk=post.pk|stringformat:"i" %}
{{ 'post'|add:post.pk }}
```

## for loop 내에서 한 번만 호출하기

`forloop.first`는 for loop의 첫번째 순회에서만 참 값을 반환한다. 

```html
{% for post in posts %}
{% if post.category == 'about' %}
    {% if forloop.first %}<li class="divider"></li>{% endif %}
    <dd><a href="{% url 'about' tab=post.tab %}">new</a></dd>
{% endif %}
{% endfor %}
```

##### forloop 변수들
- `forloop.counter`: The current iteration of the loop (1-indexed)
- `forloop.counter0`: The current iteration of the loop (0-indexed)
- `forloop.revcounter`: The number of iterations from the end of the loop (1-indexed)
- `forloop.revcounter0`: The number of iterations from the end of the loop (0-indexed)
- `forloop.first`: True if this is the first time through the loop
- `forloop.last`: True if this is the last time through the loop
- `forloop.parentloop`: For nested loops, this is the loop surrounding the current one

> `forloop.parentloop` 은 `forloop.parentloop.counter`와 같은 식으로 부모 loop 관련 상수를 다룰 수 있다



# Javascript

[버튼 누르면 폼 갯수 증가 자바스크립트](http://www.randomsnippets.com/2008/02/21/how-to-dynamically-add-form-elements-via-javascript/)

```javascript
var counter = 1;
var limit = 30;
function addInput(divId, inputName){
    if (counter == limit)  {
        alert("You have reached the limit of adding " + counter + " inputs");
    }
    else {
        var targetDiv = document.getElementById(divId)
        targetDiv.innerHTML += '<input name="'+ inputName + '" type="file" class="form-control file">';
        counter++;
    }
}
```





# Django 문제 해결

## Inconsistent Migration History

##### 아래 에러가 생긴 경위는 이렇다. 

1. 먼저 사용하던 local sqlite에 이미 기존 모델들이 migrate 되어 있었으나, User model은 없는 상태였다. 
2. RDS postgresql 을 만들었다.
3. User model을 만들고, Post, Image model 과 함께 admin에 추가했다.
4. RDS postgresql 에 migrate 했다.
5. 지하철에서 로컬서버를 돌리던 중, 와이파이가 시원치 않아서 local db 설정을 db.sqlite 으로 바꿨다.
6. ./manage.py makemigration, migrate 를 모두 해보았고, member와 post, admin 각각도 해보았지만 같은 에러가 발생했다. 

```bash
django.db.migrations.exceptions.InconsistentMigrationHistory: 
Migration admin.0001_initial is applied before its dependency member.0001_initial on database 'default'.
```

: 어드민 마이그레이션은 User model에 의존한다. 이것은 User model이 먼저 migrate 되어 있어야 한다는 뜻이다. 근데 기존에 있던 db.sqlite에는 User model이 없었기 때문에 문제가 발생한 것이다. 정확한 것은 더 찾아봐야겠지만, 이런 경우 **db.sqlite를 밀고 다시 migrate 하면 문제가 해결된다**. 


## NoReverseMatch

처음에는 `NoReverseMatch`라길래 urlpattern 이 잘못되었다는 뜻이 아니라, template 내의 url tag 에서 reverse match 가 되지 않는다는 것을 의미한다. urlpattern에 문제가 있을 때는 `Page Not Found (404)`가 발생한다. 따라서 이런 경우에는 url tag 를 검사하자.

![에러 메세지](img/temp.02/no-reverse-match-error-page.png)

- `NoReverseMatch`: template 을 렌더링하는 과정에서 `url tag`의 리버스 오류가 발생했다는 것을 의미한다 
- `at /login/`: 해당 오류가 `/login/` url 에서 반환하는 template 을 렌더링하는 과정에서 발생했다는 것을 의미한다
- `In template .../base.html, error at line 18`: 아오 이것만 생각하면 화가난다. 가볍게 무시하자. 이거랑 에러 발생이랑 전혀 상관없다.

그 당시 접근했던 url은 `/login/`이고, urlpatterns는 다음과 같았다. 

```python
urlpatterns = [
	...
	path('login/', login, name='log_in'),
	...
]
```
오류가 났던 template:

```html
<form method="post" enctype="multipart/form-data" action="{% url 'login' %}">
...
```
`'login'`을 `'log_in'`으로 고쳐주니 말끔히 해결되었다.


## IntegrityError

![](img/temp.02/integrity-error-page.png)

```bash
# 쉘 에러 코드
django.db.utils.IntegrityError: duplicate key value violates unique constraint "member_user_username_key"
DETAIL:  Key (username)=() already exists.
```

- `IntegrityError`: DB에 unique field 조건이 침해되었음을 의미한다.
- unique constraint `"member_user_username_key"`: member 모듈 user 모델의 `username` 키가 중복되었음을 알 수 있다.
- `Key (username)=()` already exists: `username`이 아무것도 없는 객체가 겹친다는 것이다.

문제가 생겼을 당시 User는 다음과 같았다. 

```python
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField()

    # 이메일을 유저네임으로 설정
    USERNAME_FIELD = 'email'

    # 필수 정보 설정
    REQUIRED_FIELDS = (
        'name',
    )

    # 커스텀 유저 매니저를 사용하도록 설정
    objects = CustomUserManager()

    def __str__(self):
        return f'name: {self.name}, email: {self.email}'
```

`AbstractUser`는 기본적으로 `username`(unique) 필드를 갖는데, 이것을 상속했기 때문에 `username` 필드가 migrated 된 것이다. (해당 migration은 당연히 migrations 에서도 확인할 수 있다.)

### 이 문제의 해결방법은 두 가지다.

##### 1. `AbstractBaseUser, PermissionsMixin`를 상속한다 
: `AbstractBaseUser, PermissionsMixin`는 `AbstractUser`가 상속하는 클래스로, `username` 필드를 포함하지 않는다.

##### 2. `username=None` 설정
: 더럽긴 하지만 동일하게 작용한다. `username` 필드에 `None` 값으로 마이그레이션 되는 것이 아니라, 아예 필드가 없어진다.


## S3 file 접근이 안 돼?

### 문제
: 로컬에서 runserver를 돌리면, 생성된 s3 link가 잘 접속이 된다. 그러나 서버에서 돌릴 때는 s3 link가 생성되기는 하나, 접속하면 이상한 에러가 발생한다. (runserver와 nginx-uwsgi 상관 없이 모두)  

##### 발생한 에러 페이지
```html
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<Error>
<script>
(function (){var h,l=this;function m(a){return void 0!==a}function aa(a,b){var c=a.split("."),d=l;c[0]in d||!d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)!c.length&&m(b)?d[e]=b:d[e]?d=d[e]:d=d[e]={}}function ba(){} function ca(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null"; else if("function"==b&&"undefined"==typeof a.call)return"object";return b}function da(a){return"array"==ca(a)}function ea(a){var b=ca(a);return"array"==b||"object"==b&&"number"==typeof a.length}function p(a){return"string"==typeof a}function q(a){return"number"==typeof a}function r(a){return"function"==ca(a)}function t(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}function ga(a){return a[ha]||(a[ha]=++ia)}var ha="closure_uid_"+(1E9*Math.random()>>>0),ia=0; function ja(a,b,c){return a.call.apply(a.bind,arguments)}function ka(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}function u(a,b,c){u=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?ja:ka;return u.apply(null,arguments)}var la=Date.now||function(){return+new Date}; function y(a,b){function c(){}c.prototype=b.prototype;a.I=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.ia=function(a,c,f){for(var g=Array(arguments.length-2),k=2;k<arguments.length;k++)g[k-2]=arguments[k];return b.prototype[c].apply(a,g)}};function ma(a){if(Error.captureStackTrace)Error.captureStackTrace(this,ma);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}y(ma,Error);ma.prototype.name="CustomError";function na(a,b){for(var c=a.split("%s"),d="",e=Array.prototype.slice.call(arguments,1);e.length&&1<c.length;)d+=c.shift()+e.shift();return d+c.join("%s")}var oa=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")};function pa(){return Math.floor(2147483648*Math.random()).toString(36)+Math.abs(Math.floor(2147483648*Math.random())^la()).toString(36)} function qa(a,b){for(var c=0,d=oa(String(a)).split("."),e=oa(String(b)).split("."),f=Math.max(d.length,e.length),g=0;0==c&&g<f;g++){var k=d[g]||"",n=e[g]||"",w=RegExp("(\\d*)(\\D*)","g"),v=RegExp("(\\d*)(\\D*)","g");do{var z=w.exec(k)||["","",""],x=v.exec(n)||["","",""];if(0==z[0].length&&0==x[0].length)break;c=ra(0==z[1].length?0:parseInt(z[1],10),0==x[1].length?0:parseInt(x[1],10))||ra(0==z[2].length,0==x[2].length)||ra(z[2],x[2])}while(0==c)}return c}function ra(a,b){return a<b?-1:a>b?1:0};function sa(a,b){b.unshift(a);ma.call(this,na.apply(null,b));b.shift()}y(sa,ma);sa.prototype.name="AssertionError";function ta(a,b){throw new sa("Failure"+(a?": "+a:""),Array.prototype.slice.call(arguments,1));};function ua(){var a=va;return a[a.length-1]}var wa=Array.prototype;function A(a,b,c){for(var d=a.length,e=p(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)}function xa(a,b,c){for(var d=a.length,e=Array(d),f=p(a)?a.split(""):a,g=0;g<d;g++)g in f&&(e[g]=b.call(c,f[g],g,a));return e}function ya(a,b,c){return 2>=arguments.length?wa.slice.call(a,b):wa.slice.call(a,b,c)};function za(a,b,c){for(var d in a)b.call(c,a[d],d,a)}function Aa(a,b,c){var d={},e;for(e in a)d[e]=b.call(c,a[e],e,a);return d}function Ba(a){var b=0,c;for(c in a)b++;return b};var Ca;a:{var Da=l.navigator;if(Da){var Ea=Da.userAgent;if(Ea){Ca=Ea;break a}}Ca=""}function Fa(a){return-1!=Ca.indexOf(a)};var Ga=Fa("Mobile"),Ha=Fa("Macintosh"),Ia=Fa("Windows"),Ja,Ka="",La=/WebKit\/(\S+)/.exec(Ca);La&&(Ka=La?La[1]:"");Ja=Ka;function Ma(a,b,c,d,e){this.reset(a,b,c,d,e)}Ma.prototype.a=null;var Na=0;Ma.prototype.reset=function(a,b,c,d,e){"number"==typeof e||Na++;this.g=d||la();this.f=a;this.b=b;this.c=c;delete this.a};function Oa(a){this.s=a;this.a=this.o=this.b=this.f=null}function B(a,b){this.name=a;this.value=b}B.prototype.toString=function(){return this.name};var Pa=new B("OFF",Infinity),Qa=new B("SEVERE",1E3),Ra=new B("WARNING",900),Sa=new B("INFO",800),Ua=new B("CONFIG",700),Va=new B("FINE",500),Wa=new B("ALL",0),Xa=[Pa,new B("SHOUT",1200),Qa,Ra,Sa,Ua,Va,new B("FINER",400),new B("FINEST",300),Wa],Ya=null;function Za(){Ya={};for(var a=0,b;b=Xa[a];a++)Ya[b.value]=b,Ya[b.name]=b} function $a(a){if(a.b)return a.b;if(a.f)return $a(a.f);ta("Root logger has no level set.");return null}Oa.prototype.log=function(a,b,c){if(a.value>=$a(this).value)for(r(b)&&(b=b()),a=new Ma(a,String(b),this.s),c&&(a.a=c),c="log:"+a.b,l.console&&(l.console.timeStamp?l.console.timeStamp(c):l.console.markTimeline&&l.console.markTimeline(c)),l.msWriteProfilerMark&&l.msWriteProfilerMark(c),c=this;c;){b=c;var d=a;if(b.a)for(var e=0,f=void 0;f=b.a[e];e++)f(d);c=c.f}};var ab={},bb=null; function cb(){bb||(bb=new Oa(""),ab[""]=bb,bb.b=Ua)}function db(){cb();return bb}function eb(a){cb();var b;if(!(b=ab[a])){b=new Oa(a);var c=a.lastIndexOf("."),d=a.substr(c+1),c=eb(a.substr(0,c));c.o||(c.o={});c.o[d]=b;b.f=c;ab[a]=b}return b};function fb(a,b){a&&a.log(Va,b,void 0)};function C(a,b){this.code=a;this.a=D[a]||gb;this.message=b||"";var c=this.a.replace(/((?:^|\s+)[a-z])/g,function(a){return a.toUpperCase().replace(/^[\s\xa0]+/g,"")}),d=c.length-5;if(0>d||c.indexOf("Error",d)!=d)c+="Error";this.name=c;c=Error(this.message);c.name=this.name;this.stack=c.stack||""}y(C,Error);var gb="unknown error",D={15:"element not selectable",11:"element not visible"};D[31]=gb;D[30]=gb;D[24]="invalid cookie domain";D[29]="invalid element coordinates";D[12]="invalid element state"; D[32]="invalid selector";D[51]="invalid selector";D[52]="invalid selector";D[17]="javascript error";D[405]="unsupported operation";D[34]="move target out of bounds";D[27]="no such alert";D[7]="no such element";D[8]="no such frame";D[23]="no such window";D[28]="script timeout";D[33]="session not created";D[10]="stale element reference";D[21]="timeout";D[25]="unable to set cookie";D[26]="unexpected alert open";D[13]=gb;D[9]="unknown command";C.prototype.toString=function(){return this.name+": "+this.message};function hb(a){return t(a)&&q(a.status)?a:{status:0,value:a}}function ib(a){return t(a)&&q(a.status)?a:{status:a&&q(a.code)?a.code:13,value:{message:(a&&a.message||a)+""}}}function jb(a){var b=a.status;if(0==b)return a;b=b||13;a=a.value;if(!a||!t(a))throw new C(b,a+"");throw new C(b,a.message+"");};var kb;if(Fa("iPhone")&&!Fa("iPod")&&!Fa("iPad")||Fa("iPad")||Fa("iPod"))kb="";else{var lb=/Version\/([0-9.]+)/.exec(Ca);kb=lb?lb[1]:""};qa(kb,6);function mb(){} function nb(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(da(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),nb(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),ob(d,c),c.push(":"),nb(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":ob(b,c);break;case "number":c.push(isFinite(b)&& !isNaN(b)?b:"null");break;case "boolean":c.push(b);break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}var pb={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},qb=/\uffff/.test("\uffff")?/[\\\"\x00-\x1f\x7f-\uffff]/g:/[\\\"\x00-\x1f\x7f-\xff]/g;function ob(a,b){b.push('"',a.replace(qb,function(a){var b=pb[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),pb[a]=b);return b}),'"')};function rb(a){var b=[];nb(new mb,a,b);return b.join("")}function sb(a){a=String(a);if(/^\s*$/.test(a)?0:/^[\],:{}\s\u2028\u2029]*$/.test(a.replace(/\\["\\\/bfnrtu]/g,"@").replace(/"[^"\\\n\r\u2028\u2029\x00-\x08\x0a-\x1f]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g,"]").replace(/(?:^|:|,)(?:[\s\u2028\u2029]*\[)+/g,"")))try{return eval("("+a+")")}catch(b){}throw Error("Invalid JSON string: "+a);};function tb(a,b,c){var d=a.constructor;if(a.window===a)try{var e=a.constructor;delete a.constructor;d=a.constructor;a.constructor=e}catch(f){}return d.prototype[b].apply(a,ya(arguments,2))};var ub=eb("safaridriver.message"),vb={};function wb(a,b){vb[a]=b}function xb(a){throw Error("Invalid message: "+rb(a));}function E(a){this.a={};this.a[yb]=2;this.a[zb]=a}var yb="origin",zb="type";function Ab(a){return new E(a[zb])}function Bb(a,b){a.a.entries=b}E.prototype.b=function(a){this.a[yb]=2;if(a===window)this.f(a);else{if(!r(a.postMessage))throw Error("Unable to send message; postMessage function not available on target window");a.postMessage(this.a,"*")}}; E.prototype.f=function(){function a(a){b=a.data}this.a[yb]=2;var b;tb(window,"addEventListener","safaridriver.message.response",a,!1);Cb(this.a);tb(window,"removeEventListener","safaridriver.message.response",a,!1);return b};function Cb(a){var b=tb(document,"createEvent","MessageEvent");b.initMessageEvent("safaridriver.message",!1,!1,a,window.location.origin,"0",window,null);tb(window,"dispatchEvent",b)}E.prototype.toJSON=function(){return this.a};E.prototype.toString=function(){return rb(this.toJSON())};function Db(a){E.call(this,"loadModule");this.a.module=a}y(Db,E);Db.prototype.b=function(){throw Error("This message may only be sent synchronously.");};vb.loadModule=function(a){var b=a.module;if(!p(b))throw xb(a);return new Db(b)};function Eb(a,b,c){this.c=c;this.f=a;this.g=b;this.b=0;this.a=null}Eb.prototype.get=function(){var a;0<this.b?(this.b--,a=this.a,this.a=a.next,a.next=null):a=this.f();return a};var Gb=new Eb(function(){return new Fb},function(a){a.reset()},100);function Hb(){var a=Ib,b=null;a.a&&(b=a.a,a.a=a.a.next,a.a||(a.b=null),b.next=null);return b}function Fb(){this.next=this.scope=this.v=null}Fb.prototype.reset=function(){this.next=this.scope=this.v=null};function Jb(a){l.setTimeout(function(){throw a;},0)}var Kb; function Lb(){var a=l.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!Fa("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow,a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host,a=u(function(a){if(("*"==d||a.origin==d)&&a.data== c)this.port1.onmessage()},this);b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});if("undefined"!==typeof a&&!Fa("Trident")&&!Fa("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(m(c.next)){c=c.next;var a=c.O;c.O=null;a()}};return function(a){d.next={O:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT"); b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};document.documentElement.appendChild(b)}:function(a){l.setTimeout(a,0)}};function Mb(a,b){Nb||Ob();Pb||(Nb(),Pb=!0);var c=Ib,d=Gb.get();d.v=a;d.scope=b;d.next=null;c.b?c.b.next=d:c.a=d;c.b=d}var Nb;function Ob(){if(l.Promise&&l.Promise.resolve){var a=l.Promise.resolve(void 0);Nb=function(){a.then(Qb)}}else Nb=function(){var a=Qb;!r(l.setImmediate)||l.Window&&l.Window.prototype&&l.Window.prototype.setImmediate==l.setImmediate?(Kb||(Kb=Lb()),Kb(a)):l.setImmediate(a)}}var Pb=!1,Ib=new function(){this.b=this.a=null}; function Qb(){for(var a=null;a=Hb();){try{a.v.call(a.scope)}catch(b){Jb(b)}var c=Gb;c.g(a);c.b<c.c&&(c.b++,a.next=c.a,c.a=a)}Pb=!1};function Rb(){this.f={}}Rb.prototype.c=function(a,b){var c=Array.prototype.slice.call(arguments,1),d=this.f[a];if(d)for(var e=0;e<d.length;){var f=d[e];f.v.apply(f.scope,c);d[e]===f&&(d[e].ea?d.splice(e,1):e+=1)}};function Sb(a,b){var c=a.f[b];c||(c=a.f[b]=[]);return c}function Tb(a,b,c,d,e){b=Sb(a,b);for(var f=b.length,g=0;g<f;++g)if(b[g].v==c)return a;b.push({v:c,scope:d,ea:!!e});return a}Rb.prototype.aa=function(a,b,c){return Tb(this,a,b,c)};function Ub(a,b,c,d){return Tb(a,b,c,d,!0)} Rb.prototype.W=Rb.prototype.aa;if(!r(Error.captureStackTrace))try{throw Error();}catch(Vb){};/* Portions of this code are from the Dojo toolkit, received under the BSD License: Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. Neither the name of the Dojo Foundation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. */ function Wb(a){var b=da(a),c=b?a.length:Ba(a);if(!c)return Xb(a);var d=0;return new Yb(function(e,f){(b?function(a,b){for(var c=a.length,d=0;d<c;++d)b.call(null,a[d],d,a)}:za)(a,function(b,k){var n=ca(b);"array"!=n&&"object"!=n?++d==c&&e(a):Zb(b).then(function(b){a[k]=b;++d==c&&e(a)},f)})})}function $b(a){switch(ca(a)){case "array":return Wb(a);case "object":return ac(a)?a:q(a.nodeType)&&t(a.ownerDocument)&&q(a.ownerDocument.nodeType)?Xb(a):Wb(a);default:return Xb(a)}} function bc(a){ma.call(this,a);this.name="CancellationError"}y(bc,ma);function cc(a,b){if(a instanceof bc)return a;if(b){var c=b;a&&(c+=": "+a);return new bc(c)}a&&(c=a+"");return new bc(c)}function dc(a){a.prototype.then=a.prototype.then;try{Object.defineProperty(a.prototype,"$webdriver_Thenable",{value:!0,enumerable:!1})}catch(b){a.prototype.$webdriver_Thenable=!0}}function ec(a){if(!a)return!1;try{return!!a.$webdriver_Thenable}catch(b){return!1}} function Yb(a,b){ga(this);this.f=b||ua()||fc;this.b=this.g=null;this.a="pending";this.l=this.h=!1;this.c=void 0;try{var c=this;a(function(a){gc(c,"fulfilled",a)},function(a){gc(c,"rejected",a)})}catch(d){gc(this,"rejected",d)}}dc(Yb);h=Yb.prototype;h.toString=function(){return"Promise::"+ga(this)+' {[[PromiseStatus]]: "'+this.a+'"}'}; function gc(a,b,c){if("pending"===a.a){if(c===a)throw new TypeError("A promise may not resolve to itself");a.g=null;a.a="blocked";if(ec(c))c.then(a.J.bind(a,"fulfilled"),a.J.bind(a,"rejected"));else{if(t(c)){try{var d=c.then}catch(e){a.a="rejected";a.c=e;hc(a);return}if("function"===typeof d){ic(a,c,d);return}}a.a=b;a.c=c;hc(a)}}}function ic(a,b,c){function d(b){f||(f=!0,a.J("rejected",b))}function e(b){f||(f=!0,a.J("fulfilled",b))}var f=!1;try{c.call(b,e,d)}catch(g){d(g)}} h.J=function(a,b){"blocked"===this.a&&(this.a="pending",gc(this,a,b))};function hc(a){if(!a.l){a.l=!0;jc(a.f);var b;a.h||"rejected"!==a.a||a.c instanceof bc||(b=kc(a.f),b.S=!0);a.b&&a.b.length&&(b=lc(a.f),a.b.forEach(function(a){a.a.a||mc(b,a.a)}));Mb(u(a.ca,a,b))}} h.ca=function(){var a=this.f;--a.l;!a.l&&a.a&&a.H();this.l=!1;if(!(this.h||"rejected"!==this.a||this.c instanceof bc)){var a=this.f,b=this.c;if(a.a){var c=a.a.a;c&&c.removeChild(a.a);var d=a.a;a.a=c;d.l=cc(b,"Task discarded due to a previous task failure");nc(d,d.l);d.h||d.c("error",b)}else a.N(b)}this.b&&(a=this.b,this.b=null,a.forEach(this.da,this))}; h.da=function(a){var b=this.c,c=a.b,d=a.c;"rejected"===this.a&&(c=a.h,d=a.g);a.a.h=!1;r(c)?oc(a.a.X,a.a,u(c,void 0,b),a.c,a.g):(a.a.a&&a.a.a.removeChild(a.a),d(b))};h.cancel=function(a){this.D()&&(this.g?this.g.cancel(a):gc(this,"rejected",cc(a)))};h.D=function(){return"pending"===this.a};h.then=function(a,b){return pc(this,a,b)};h.K=function(a){return pc(this,null,a)}; function pc(a,b,c){if(!r(b)&&!r(c))return a;a.h=!0;b=new qc(a,b,c);a.b||(a.b=[]);a.b.push(b);"pending"!==a.a&&"blocked"!==a.a&&(c=a.f,c=c.C||kc(c),mc(c,b.a),hc(a));return b.f}function rc(a){function b(a){if(a===e)throw new TypeError("May not resolve a Deferred with itself");}var c,d;this.f=new Yb(function(a,b){c=a;d=b},a);var e=this;this.c=function(a){b(a);c(a)};this.g=function(a){b(a);d(a)}}dc(rc);rc.prototype.D=function(){return this.f.D()};rc.prototype.cancel=function(a){this.f.cancel(a)}; rc.prototype.then=function(a,b){return this.f.then(a,b)};rc.prototype.K=function(a){return this.f.K(a)};function ac(a){return!!a&&t(a)&&"function"===typeof a.then}function Xb(a){return a instanceof Yb?a:new Yb(function(b){b(a)})}function sc(a){return a instanceof Yb?a:new Yb(function(b,c){c(a)})}function tc(a,b){return ec(a)?a.then(b,void 0):(new Yb(function(b,d){uc(a,b,d)})).then(b,void 0)}function uc(a,b,c){ac(a)?a.then(b,c):a&&t(a)&&r(a.ba)?a.ba(b,c):b&&b(a)} function Zb(a){return ac(a)?tc(a,$b):$b(a)}function vc(){this.f={};ga(this);this.g=this.b=this.h=this.C=this.B=this.a=null;this.l=0}y(vc,Rb);h=vc.prototype;h.toString=function(){return wc(this)};h.reset=function(){this.C=this.a=null;this.c("reset");m(void 0)?delete this.f[void 0]:this.f={};xc(this);yc(this)}; function wc(a){function b(a,c){var k=a.toString();c&&(k="(pending) "+k);a===d&&(k="(active) "+k);a===e&&(k="(running) "+k);a instanceof zc?(a.b&&(k+="\n"+b(a.b,!0)),a.o&&a.o.forEach(function(c){a.b&&a.b.h()===c||(k+="\n"+b(c))})):a.h()&&(k+="\n"+b(a.h()));return"| "+k.replace(/\n/g,"\n| ")}var c="ControlFlow::"+ga(a),d=a.a,e=a.B;return d?c+"\n"+b(Ac(d)):c}function kc(a){xc(a);a.a||(a.a=new zc(a),Ub(a.a,"error",a.N,a),a.H());return a.a}function lc(a){return a.B||kc(a)} h.H=function(){this.b||this.l||!this.a||this.a.b||(this.b=new Bc(this.fa,this))};function yc(a){a.b&&(a.b.cancel(),a.b=null)}function jc(a){a.l+=1;yc(a)}h.fa=function(){this.b=null;if(!this.l)if(!this.a)Cc(this);else if(!this.a.b){var a=Dc(this);if(a){var b=this.a,c=u(this.H,this),d=function(d){b.b=null;a.l(null);a.c(d);c()},e=function(d){b.b=null;a.l(null);a.g(d);c()};b.b=a;var f=new zc(this);a.l(f);oc(this,f,a.B,function(a){uc(a,d,e)},e,!0)}}}; function Dc(a){var b=a.a,c;b.C=!0;c=b.o&&b.o[0];if(!c)return b.h||b.B||(a.a===b&&(a.a=b.a),b.a&&b.a.removeChild(b),b.c("close"),a.a?a.H():Cc(a)),null;if(c instanceof zc)return a.a=c,Dc(a);b.removeChild(c);return c.D()?c:Dc(a)} function oc(a,b,c,d,e,f){function g(a){return(!a.o||!a.o.length)&&!a.S}function k(a){var c=b.a;c&&(c.removeChild(b),Mb(function(){g(c)&&c!==n.a&&c.c("close")}),n.H());a&&nc(b,cc(a,"Tasks cancelled due to uncaught error"));n.a=w}var n=a,w=a.a;try{a.a===b||b.a||mc(a.a,b);f&&(a.a=b);try{a.B=b;a.C=b;va.push(a);var v=c()}finally{va.pop(),a.C=null,a.B=b.a}b.C=!0;if(!g(b)||f&&ac(v)){var z;ac(v)?(b.B=!0,c=function(){b.B=!1;z=new Bc(function(){g(b)&&(k(),d(v))})},v.then(c,c)):ec(v)&&v.K(ba);Ub(Ub(b,"close", function(){z&&z.cancel();g(b)&&k();d(v)}),"error",function(a){z&&z.cancel();ec(v)&&v.D()&&v.cancel(a);e(a)})}else k(),d(v)}catch(x){k(x),e(x)}finally{a.B=null}}function Cc(a){a.h||(yc(a),a.h=new Bc(a.ga,a))}h.ga=function(){this.g&&(clearInterval(this.g),this.g=null);this.h=null;this.c("idle")};function xc(a){a.h&&(a.h.cancel(),a.h=null)}h.N=function(a){this.a=null;xc(this);yc(this);this.g&&(clearInterval(this.g),this.g=null);Sb(this,"uncaughtException").length?this.c("uncaughtException",a):Jb(a)}; function Bc(a,b){this.a=!1;Mb(function(){this.a||a.call(b)},this)}Bc.prototype.cancel=function(){this.a=!0};function zc(a){this.f={};ga(this);this.X=a;this.b=this.g=this.o=this.a=null;this.S=this.h=this.B=this.C=!1;this.l=null}y(zc,Rb);function Ec(a,b){b instanceof zc?nc(b,a):(b.f.b=null,b.cancel(a))}function Ac(a){for(;a.a;)a=a.a;return a}function nc(a,b){a.o&&a.o.forEach(function(a){Ec(b,a)})} function mc(a,b){if(a.l)Ec(a.l,b);else if(a.o||(a.o=[]),b.a=a,a.C&&b instanceof zc){var c=0;a.g instanceof zc&&(c=a.o.indexOf(a.g),c+=a.g.h?1:-1);a.o.splice(Math.max(c,0),0,b);a.g=b}else a.g=b,a.o.push(b)}zc.prototype.removeChild=function(a){var b=this.o.indexOf(a);a.a=null;this.o.splice(b,1);this.g===a&&(this.g=this.o[b-1]||null);this.o.length||(this.o=null)};zc.prototype.toString=function(){return"Frame::"+ga(this)}; function qc(a,b,c){rc.call(this,a.f);this.b=b;this.h=c;this.a=new zc(a.f);this.a.h=!0;this.f.g=a}y(qc,rc);var fc=new vc,va=[];function Fc(a,b){return new Yb(function(c,d){function e(){var g=(new Db(a)).f(b);try{c(jb(g).value)}catch(k){f+=1,3==f?d(k):setTimeout(e,150)}}var f=0;e()})};function Gc(){this.g=eb("safaridriver.inject.CommandRegistry");this.f={};this.b={};this.l={};this.a={}}Gc.a=function(){return Gc.m?Gc.m:Gc.m=new Gc};Gc.prototype.c=ba;function Hc(){var a=Gc.a();a.h=window;a.c=Ic;return a}function Jc(a,b,c){fb(a.g,"Declaring module: "+b);A(c,function(a){this.f[a]=b},a);a.l[b]=c;a.a[b]=!1;return a}function Kc(a,b){var c=Gc.a(),d=[],e;for(e in b)d.push(e),c.b[e]=b[e];fb(c.g,"Defined module: "+a);c.a[a]=!0} function Lc(a,b){function c(){var a=d[b.s];if(a)return tc(a(b,l));throw Error("Unknown command: "+b);}var d=a.b,e=a.f[b.s];if(e)return Mc(a,e).then(c);try{return c()}catch(f){return sc(f)}}function Mc(a,b){return a.a[b]?Xb():Fc(b,a.h).then(u(function(a){this.c(a);this.a[b]=!0},a))};function Nc(a){this.s=a;this.a={}};var Oc,Ic=u(function(a){eval("("+a+")").call(l)},l);var Pc=window;function Qc(a){return a?a.parentWindow||a.defaultView:window}function F(a){return 9==a.nodeType?a:a.ownerDocument||a.document};function Rc(a,b){E.call(this,"encode");this.a[Sc]=a;this.a[Tc]=b}y(Rc,E);var Sc="id",Tc="css";vb.encode=function(a){var b=a[Sc],c=a[Tc];if(!p(b)||!p(c))throw xb(a);return new Rc(b,c)};function Uc(a,b,c){Nc.call(this,b);this.id=a;c&&(this.a=c)}y(Uc,Nc);Uc.prototype.toJSON=function(){return{id:this.id,name:this.s,parameters:this.a}};Uc.prototype.toString=function(){return rb(this)};function Vc(a,b){E.call(this,a);this.c=b}y(Vc,E);Vc.prototype.toJSON=function(){var a=this.c.toJSON();this.a.command=a;return Vc.I.toJSON.call(this)};Vc.prototype.b=function(a){var b=this.c.toJSON();this.a.command=b;Vc.I.b.call(this,a)};var Wc=function(a){function b(b){Vc.call(this,a,b)}y(b,Vc);b.a=a;wb(a,function(a){var d=a.command;if(!t(d))throw xb(a);d=p(d.id)&&p(d.name)&&t(d.parameters)?new Uc(d.id,d.name,d.parameters):null;if(!d)throw xb(a);return new b(d)});return b}("command"); function Xc(a,b){E.call(this,"response");this.a[Yc]=a;this.a[Zc]=b}y(Xc,E);var Yc="id",Zc="response";vb.response=function(a){var b=a[Yc],c=a[Zc];if(!p(b)||!t(c))throw xb(a);return new Xc(b,c)};function $c(a){this.b={};a.W("response",u(this.f,this))}function ad(a){for(var b="",c=a;c;c=c.parentElement){for(var d=1,e=c.previousSibling;e;e=e.previousSibling)1==e.nodeType&&d++;e=c.tagName.toLowerCase().replace(/:/g,"\\:");1<d&&(e+=":nth-child("+d+")");b=""==b?e+b:e+" > "+b}if(a.ownerDocument.querySelector(b)!==a||-1!=b.indexOf("form"))b=pa(),a.setAttribute("safaridriver-encoding",b),b=a.tagName.toLowerCase()+'[safaridriver-encoding="'+b+'"]';return b} $c.prototype.a=function(a){var b=ca(a);switch(b){case "boolean":case "number":case "string":return a;case "null":case "undefined":return null;case "array":return xa(a,this.a,this);case "object":if(t(a)&&1==a.nodeType){if(a.ownerDocument!==document){var b=new rc,c=pa(),d=ad(a);(new Rc(c,d)).b(Qc(F(a)));this.b[c]=b;return b.f}b={};b.ENCODED_ELEMENT=ad(a);return b}return ea(a)?xa(a,this.a,this):Aa(a,this.a,this);case "function":return a.toString();default:throw Error("Invalid value type: "+b+" => "+ a);}};function bd(a){var b=ca(a);switch(b){case "boolean":case "number":case "string":return a;case "null":case "undefined":return null;case "array":return xa(a,bd);case "object":b=Object.keys(a);if(1==b.length&&"ENCODED_ELEMENT"===b[0]){a=a.ENCODED_ELEMENT;b=Pc.document.querySelector(a);if(!b)throw new C(10,"Unable to locate encoded element: "+a);b.removeAttribute("safaridriver-encoding");return b}return Aa(a,bd);default:throw Error("Invalid value type: "+b+" => "+a);}} $c.prototype.f=function(a){if(2!==a.a[yb]){var b=this.b[a.a[Yc]];if(b){delete this.b[a.a[Yc]];a=a.a[Zc];try{jb(a);var c=bd(a.value);b.c(c)}catch(d){b.g(d)}}}};function cd(){0!=dd&&ga(this);this.b=this.b;this.h=this.h}var dd=0;cd.prototype.b=!1;var ed=new B("DEBUG",Ua.value);function fd(a,b,c,d){if(p(a))if("DEBUG"===a||ed.value===a)a=ed;else if(p(a))Ya||Za(),a=Ya[a]||null||Wa;else{a:if(Ya||Za(),a in Ya)a=Ya[a];else{for(var e=0;e<Xa.length;++e){var f=Xa[e];if(f.value<=a){a=f;break a}}a=null}a=a||Wa}this.a=a;this.message=b;this.b=q(c)?c:la();this.type=d||""}fd.prototype.toJSON=function(){return{level:this.a.name,message:this.message,timestamp:this.b,type:this.type}};function gd(a){E.call(this,"log");this.g=a}y(gd,E);gd.prototype.c=!1;function hd(a){a.c||(Bb(a,a.g.map(function(a){return a.toJSON()})),a.c=!0)}gd.prototype.toJSON=function(){hd(this);return gd.I.toJSON.call(this)};gd.prototype.b=function(a){hd(this);gd.I.b.call(this,a)};gd.prototype.f=function(a){hd(this);gd.I.f.call(this,a)}; vb.log=function(a){var b=a.entries;if(!da(b))throw xb(a);b=b.map(function(b){if(!(p(b.type)&&p(b.level)&&p(b.message)&&q(b.timestamp)))throw xb(a);return new fd(b.level,b.message,b.timestamp,b.type)});return new gd(b)};function id(a){cd.call(this);this.f=a;this.c=u(this.g,this);a=db();var b=this.c;a.a||(a.a=[]);a.a.push(b)}y(id,cd);id.prototype.a=!1; function jd(){var a=new id(window);function b(a,b){var f=console[a];if(f){var g=function(){(new gd([new fd(b,ya(arguments,0).join(" "),la(),"browser")])).b(c);return f.apply(console,arguments)};g.toString=function(){return f.toString()};console[a]=g}}if(!a.a&&(a.a=!0,window.console)){var c=a.f;b("debug",ed);b("error",Qa);b("group",Sa);b("info",Sa);b("log",Sa);b("warn",Ra)}} id.prototype.g=function(a){var b=a.f;a=new fd(b.value<=Wa.value?Wa:b.value===Pa.value?Pa:b.value<Sa.value?ed:b.value<Ra.value?Sa:b.value<Qa.value?Ra:Qa,"["+a.c+"] "+a.b,a.g,"driver");(new gd([a])).b(this.f)};function kd(a,b){E.call(this,"alert");this.a.message=a;this.a.blocksUiThread=b}y(kd,E);vb.alert=function(a){var b=a.message,c=a.blocksUiThread;if(!p(b)||"boolean"!=typeof c)throw xb(a);return new kd(b,c)};function ld(a,b){E.call(this,a);this.a.isFrame=!!b}y(ld,E);function md(a){function b(b){ld.call(this,a,b)}y(b,ld);b.a=a;wb(a,function(a){return new b(!!a.isFrame)});return b}var nd=md("load");md("pendingFrame").prototype.b=function(){throw Error("This message may only be sent synchronously.");};md("unload");function od(a,b){this.f={};this.g=a;this.b=eb("safaridriver.message.MessageTarget");this.a=u(this.l,this);this.h=!!b;this.g.addEventListener("message",this.a,!0);this.g.addEventListener("safaridriver.message",this.a,!0)}y(od,Rb);function pd(a){var b=qd;a.b=p(b)?eb(b):b}od.prototype.log=function(a,b,c){var d=this.b;d&&d.log(b||Sa,a,c)}; od.prototype.l=function(a){try{var b,c=a.message||a.data;p(c)&&(c=sb(c));if(!t(c)||!p(c[yb])&&!q(c[yb])||!p(c[zb]))throw xb(c);var d=vb[c[zb]];d||(fb(ub,"Unknown message type; falling back to the default factory: "+rb(c)),d=Ab);var e=d(c);e.a[yb]=c[yb];b=e}catch(f){return}this.h&&a.stopImmediatePropagation();this.c(b.a[zb],b,a)};var qd=eb("safaridriver.inject.page"); aa("init",function(){function a(a,b){var c=window[a];window[a]=b;window.constructor.prototype[a]=b;window[a].toString=function(){return c.toString()}}function b(){A(Object.getOwnPropertyNames(window),function(a){if(!(a in l)){var b=Object.getOwnPropertyDescriptor(window,a);b&&Object.defineProperty(l,a,b)}})}db().b=Sa;window!=l&&b();jd();Jc(Jc(Hc(),"page_element",["sendKeysToElement"]),"page_script",["executeScript","executeAsyncScript"]);fb(qd,"Loaded page script for "+window.location);var c=new od(window, !0);pd(c);c.W(Wc.a,rd);Oc=new $c(c);c=new nd(window!==window.top);fb(qd,"Sending "+c);c.b(window);a("alert",sd);a("confirm",td);a("prompt",ud);tb(window,"addEventListener","beforeunload",vd,!0)});var wd={name:"alert",v:window.alert},xd={name:"beforeunload",v:ba},yd={name:"confirm",v:window.confirm},zd={name:"prompt",v:window.prompt};function sd(a){Ad(wd,a)}function td(a){return Ad(yd,a)}function ud(a){return Ad(zd,a)}function vd(a){Ad(xd,a)} function Ad(a,b){var c=ya(arguments,1),d=c[0]+"",e=!0,f=a.v;if(a===xd&&(e=!1,f=window.onbeforeunload,!f))return null;fb(qd,"Sending alert notification; type: "+a.name+", text: "+d);if("1"==(new kd(d,e)).f(window))return a!==xd?(fb(qd,"Invoking native alert"),f.apply(window,c)):null;(c=qd)&&c.log(Sa,"Dismissing unexpected alert",void 0);var g;switch(a.name){case xd.name:f&&(f=f(),window.onbeforeunload=null,null!=f&&(new kd(f+"",!0)).f(window));break;case yd.name:g=!1;break;case zd.name:g=null}return g} function rd(a,b){if(2!==a.a[yb]&&b.source===window){var c=a.c;Lc(Gc.a(),c).then(function(a){a=Oc.a(a);return Zb(a)}).then(hb,ib).then(function(a){a=new Xc(c.id,a);fb(qd,"Sending "+c.s+" response: "+a);a.b(window)})}};;this.init();}).call({});
</script>
<Code>InvalidRequest</Code>
<Message>
The authorization mechanism you have provided is not supported. Please use AWS4-HMAC-SHA256.
</Message>
<RequestId>F79F436B96131D83</RequestId>
<HostId>
DaDba3xu1ngW+xY1rEXtwM+cdvpKOysKjpuql2xT5IlpXtDajt7IENh/oQJenGi2sl+oH8CQhtg=
</HostId>
</Error>
```

1. 현재까지 확인한 결과 django settings에는 아무런 문제가 없는 것 같습니다. s3 링크도 잘 생성이 되구요. 
2. s3에 파일도 잘 올라가 있습니다. 

근데 문제는 그 생성된 링크로 들어가면 이상한 것만 나옵니다. 현재 스태틱 파일 전부가 접근이 안 되는 상황입니다.

아래는 서버에서 생성된 s3 링크입니다.
https://pdxenhp.s3.amazonaws.com/static/images/ceo.jpg?AWSAccessKeyId=AKIAICGMY7DANLKIII2Q&Signature=jnjPvSr6kNWxqeZUSulcQkQ75k8%3D&Expires=1523004098

아래는 로컬 서버에서 생성된 s3링크입니다 
https://pdxenhp.s3.amazonaws.com/static/images/ceo.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAICGMY7DANLKIII2Q%2F20180406%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Date=20180406T074127Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=8f2610ea2b18fbbe1ad8b2c91243f6adf593a8d6a44ea72408a638106de76d9e 

3. ec2에 s3fullaccess 권한도 잘 주어져 있습니다.

혹시 비슷한 문제를 겪으셨던 분 계신가요?

아래는 도움이 될만한 제 코드입니다. 

django config.settings: https://dpaste.de/hpYz
nginx conf file: https://dpaste.de/XQUv

##### aws s3 문서 읽기




# django로 배우는 python

## fuction 객체를 상수 처럼 활용하기 (CASCADE)

> 시사점: if 문에서 `choice 변수`처럼 사용되는 상수가 필요할 때는, 특정 함수의 객체를 상수처럼 쓸 수 있다. 

django에서 `on_delete` 옵션을 줄 때, `models` 클래스 안의 `CASCADE` 메서드를 이용한다. 눈여겨볼 점은, 함수를 호출하지 않고 객체만 호출한다는 점이다. 

```python
# 괄호 없이 객체로만 호출했다.
on_delete=models.CASCADE
```
```python
# 상수인줄 알았더니 함수였다.
def CASCADE(collector, field, sub_objs, using):
    collector.collect(sub_objs, source=field.remote_field.model,
                      source_attr=field.name, nullable=field.null)
    if field.null and not connections[using].features.can_defer_constraint_checks:
        collector.add_field_update(field, None, sub_objs)
```
```python
def can_fast_delete(self, objs, from_field=None):
	...
	# 여기서 CASCADE 객체를 받아 True/False 를 계산한다.
	if from_field and from_field.remote_field.on_delete is not CASCADE:
		return
```

## function 객체를 매개변수로 활용하기 (upload_to)

> 시사점: 어떤 함수의 결과를 매개변수로 전달해야 하는데, 그 함수의 인자가 아직 존재하지 않아 결과를 도출할 수 없을 때, 함수 자체를 매개변수로 넘겨준다.

장고 `FileField`의 `upload_to` 옵션은, **파일 경로 문자열** 뿐 아니라, **파일 경로를 생성하는 함수의 인스턴스**도 받는다. 이는 파일 경로를 생성할 때 필요한 `file.name` 해당 클래스 상에는 존재할 수가 없기 때문이다. 

```python
def post_img_directory_path(instance, filename):
    return f'user_{instance.author.id}/Post_{instance.id}/post_img/{filename}'

# 파일 객체를 매개변수로 보내는 모습이다. 
class Post(models.Model):
post_img = models.ImageField(upload_to=post_img_directory_path, blank=True)
```
`upload_to` 매개변수는 아래 `generate_filename`에서 사용한다. 

```python
def generate_filename(self, instance, filename):
    """
    Apply (if callable) or prepend (if a string) upload_to to the filename,
    then delegate further processing of the name to the storage backend.
    Until the storage layer, all file paths are expected to be Unix style
    (with forward slashes).
    """
    # upload_to 가 함수일 때
    if callable(self.upload_to):
        filename = self.upload_to(instance, filename)
    else:
        dirname = force_text(datetime.datetime.now().strftime(force_str(self.upload_to)))
        filename = posixpath.join(dirname, filename)
    return self.storage.generate_filename(filename)
```
`upload_to` 매개변수에 `instance`와 `filename`을 넣어주는데, 이건 어디서 온 데이터일까. `generate_filename`을 호출하는 `save` 메서드를 살펴보자. 

```python
def save(self, name, content, save=True):
	# generate_filename()에 FileField 인스턴스를 전달한다.
	name = self.field.generate_filename(self.instance, name)
	self.name = self.storage.save(name, content, max_length=self.field.max_length)
	setattr(self.instance, self.field.name, self.name)
	self._committed = True
	
	# Save the object because it has changed, unless save is False
	if save:
	    self.instance.save()
	save.alters_data = True
```
`instance`는 FileField 또는 그 자식 객체임을 알 수 있다. `filename`에는 `name`이 들어가는데, 이것이 무엇인지 알기 위해서 `save` 메서드를 호출하는곳을 찾아보자. 

```python
def pre_save(self, model_instance, add):
    "Returns field's value just before saving."
    file = super(FileField, self).pre_save(model_instance, add)
    if file and not file._committed:
        # Commit the file to storage prior to saving the model
        file.save(file.name, file.file, save=False)
    return file
```
의문이 해결되었다. `uploade_to` 매개함수의 `filename` 변수는 업로드된 파일 객체의 이름(`file.name`)이었다.






# PostgreSQL

## psql command line 종료하기

### 메타커맨드

pqsl에는 메타커맨드라는 개념이 있다. 메타커맨드는 pqsl이 db에 바로 전달하지 않고 한번 검사해서 전달하는 명령어이다. 메타커맨드는 `\`로 시작힌다. psql을 종료하는 메타커맨드는 `\q`이다. (다른 메타커맨드는 `\?`로 볼 수 있다)

### EOT

`EOT`는 `End-of-Transmission character`의 약자로, 입력을 기다리는 프로그램에 마지막 입력임을 알려주는 문자이다. psql은 `EOT`를 받으면 프로그램을 종료한다. `EOT`는 `ctl+d`로 전달할 수 있다.

## postgresql.conf 파일로 서버 접속 단순화하기

> 검색어: `psql server config`, `postgresql.conf location`

## Errors

### 1. 인바운드 에러

```bash
psql \
--host=pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com \
--user=pdxen \
--port=5432 \
pdxenhp
psql: could not connect to server: Operation timed out
	Is the server running on host "pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com" (35.169.181.220) and accepting
	TCP/IP connections on port 5432?
```
##### 해결
: 보안그룹 인바운드에 현재 IP가 없는 것으로, 추가해주면 해결된다.

### 2. 인바운드 에러 (EC2 연결)

```bash
$ ./manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).

...

Is the server running on host "pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com" (35.169.181.220) and accepting 
TCP/IP connections on port 5432?
```

##### 해결
: 보안그룹 인바운드에 EC2 가 속한 보안그룹이 등록되어 있지 않은 것이다. 유형=postgresql, 포트=5432, 소스=(EC2가 속한 보안그룹) 으로 등록해준다.

### 3. DB 이름 에러

```bash
psql \
--host=pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com \
--user=pdxen \
--port=5432 \
pdxenhp-db
Password for user pdxen:
psql: FATAL:  database "pdxenhp-db" does not exist
```
##### 해결
: 존재하지 않는 DB 이다. 이름이 잘못된 것. 고쳐준다. 

### 4. RDS 주소 에러

```bash
psql \
\ --host=pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com\
\ --user=pdxen \
\ --port=5432 \
\ pdxen-db
```
##### 해결
: 언뜻 보기에는 문제 없어 보이지만, `...amazonaws.com` 바로 옆에 `\`가 붙어있다. 이러면 `...user=pdxen`까지 `host`가 되어버린다. 

### 5. RDS 주소 에러 (settings.py)
```bash
...
django.db.utils.OperationalError: could not translate host name "pdxenhp-db.cbtayqomcfdk.us-east-1.rds.amazonaws.com" to address: nodename nor servname provided, or not known
```

##### 해결
: RDS 주소가 잘못된 것으로, 고쳐준다.




# CSS problems


## 1. 중앙정렬 객체가 밀려! 

: 피디젠 메인 페이지 헤더 부분의 글씨가 모바일에서 밀린 사건   

**문제**: `postion: absolute;`로 중앙정렬하면, 객체가 밀린다. 밀린다는 게 무슨 뜻이냐면, 부모객체 폭이 400이라 가정하자. 왼쪽으로 50% 밀고, 다시 당겨서 중앙정렬 하면, `absolute` 설정된 자식 객체의 폭은 200이 된다.
	
```css
.vertical-center {
position: absolute;
top: 50%;
left: 50%;
transform: translate(-46.7%, -50%);
}
```

해결: `left: 50%;`를 버리고 `bootstrap`의 `.text-center`로 대신했다.

```html
<div class="container container-header-main text-center">
	<div class="row vertical-center">
		<div class="heading-header">
			<h1 class="big2">PDXen</h1><br>
			<h1>A company that implements</h1>
			<h1>human health and happiness</h1>
		</div>
		<div class="heading-header heading-sub">
			<p class="lead ">The next-generation biotechnology-seeking venture company</p>
		</div>
	</div>
</div>
```
```css
.vertical-center {
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
}
.text-center {
  text-align: center;
}
```

## 2. IOS, background fixed 옵션 안먹어!

아래가 최초의 코드이다. `background: fixed;` 옵션이 들어가있다. 

```css
.full-bg {
    position: relative;
    height: 100%;
    color: white;
    background: black url("../images/backgroud_main.jpg") no-repeat fixed bottom center;
    background-size: cover;
}
```
애석하게도 [해당 옵션은 IOS에서 작동하지 않는다.](https://www.joomshaper.com/forums/background-fixed-image-on-ios-mobile-devices) 
[해결책](https://stackoverflow.com/questions/24154666/background-size-cover-not-working-on-ios#answer-43058483)은 다음과 같다. 최외곽 `div`를 만들고 모든 것을 그 안에 넣은 후 스크롤을 시키는 것.

```html
<body>
	<div id="wrapper">
		...
	</div>
<body>
```

```css
#wrapper {
	width: 100%;
	height: 100%;
	overflow: scroll;
}
```
그러나 나는 이미 거의 모든 작업을 끝낸 터라 그런 사소한 이유로 코드를 뜯어고치고 싶지 않았다. 내가 생각해낸 해결책은 그냥 포기.

```css
.full-bg {
    position: relative;
    height: 100%;
    color: white;
    background: black url("../images/backgroud_main.jpg") no-repeat center center;
    background-size: cover;
}
```
그리고 처음에 그런 문제가 발생했을 때는 `fixed`가 문제인지 몰랐다. 그런 이유로 `cover` 또는 `center` 옵션이 문제인 줄 알았다. 아래는 그러한 검색으로 찾은 [해결책](https://stackoverflow.com/questions/24154666/background-size-cover-not-working-on-ios#answer-43058483).

```css
.full-bg {
    height: 100%;
    width: 100%;
    color: white;
    background: none;
}
.full-bg:before {
    content:"";
    position: absolute;
    top:0;
    height:100%;
    left:0;
    right:0;
    z-index:-1;
    background: url("../images/backgroud_main.jpg") center center;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}
```

그러나 나중에 나중에 모든 것이 다 끝나고 `fixed`옵션이 들어가 있지 않은 것을 알게 되었다. 그래서 적용해봤더니 웬걸, 안 먹는 거 아닌가. 


# Bootstrap


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


# Design & Color


## apple ux design
- body: `#f9f9f9`
- nav: `#ededed`
- footer: `#efefef`
- font: strong `#333333` h2 34px
- font: normal `#4d4d4d`

## 느낌있는 컬러
- 경쾌한 노란색, 연한 녹빛이 흐름:`#ff6`


# SSH


### scp 서버에서 로컬로 파일 복사

```bash
# local shell 에서
scp <username>@<serverIP>:<server_file_path> <local_dir_path>
```

# Linux

### Django background runserver 끄기
`ps auxw | grep runserver`
`kill 0000`



# shell


### 1. shell 이란

사람이 이해할 수 있는 명령어를 운영체제의 커널이 이해할 수 있는 기계어로 번역해 전달하는 응용 프로그램으로, command-line interpreter 라고 불린다. 

### 2. shell의 종류

1. **bash** ( Bourne-Again Shell ) 
 
	* **프롬프트**: `#`  
	* **실행파일**: `/bin/bash`  
	
	Bourne again shell은 최초로 개발된 쉘인 Bourne shell의 변종이다. 리눅스에서 가장 많이 사용되는 IEEE POSIX 호환이며 Borune shell과 호환되는 쉘로서 GNU 프로젝트에 의해 만들어지고 배포되고 있다. 명령행 편집 기능을 제공한다.

2. **ksh** ( Korn Shell )

	* **프롬프트** : $

	일반적으로 유닉스에서 가장 많이 사용되고 있는 shell이며 Bourne shell에 처음으로 현대적
	인 shell 기능(C shell로부터 차용한 것이다.)을 도입한 shell 입니다. Bourne shell과 호환
	되고, 명령행 편집 기능을 제공합니다.

3. **zsh**

	* **프롬프트** : %
	
	Korn Shell과 매우 유사한 셸이지만 Korn Shell보다 더 많고 유용한 기능 등을 추가하여 개선시킨 것이다.

### 3. 프롬프트 (Prompt)

: 사용자의 명령을 받아들일 준비가 되었음을 모니터에 나타내는 표시

```bash
# 아래의 `#`이 프롬프트이다
root@localhost:/var#
```



# Linux 명령어


### 파일 검색

```bash
# 그냥 파일 찾기
locate some-file.avi
# 정규표현식으로 찾기
locate -i "*.txt"
```

### 폴더 크기 정보

```bash
# du: disk usage
# h: human readable
# s: summary
du -hs <path>
```



# 미해결 문제


### html load 순서가 다르다?

```bash
System check identified no issues (0 silenced).
March 07, 2018 - 11:50:10
Django version 2.0.2, using settings 'config.settings'
Starting development server at http://0:8080/
Quit the server with CONTROL-C.
[07/Mar/2018 11:50:16] "GET / HTTP/1.1" 200 16713
[07/Mar/2018 11:50:16] "GET /static/bootstrap-dropdownhover/css/bootstrap-dropdownhover.min.css HTTP/1.1" 200 1230
[07/Mar/2018 11:50:16] "GET /static/custom/custom.css HTTP/1.1" 200 12166
[07/Mar/2018 11:50:16] "GET /static/images/ceo.jpg HTTP/1.1" 200 14516
[07/Mar/2018 11:50:16] "GET /static/custom/custom-module.css HTTP/1.1" 200 2393
[07/Mar/2018 11:50:17] "GET /static/bootstrap/js/bootstrap.js HTTP/1.1" 200 66732
[07/Mar/2018 11:50:17] "GET /static/bootstrap-dropdownhover/js/bootstrap-dropdownhover.min.js HTTP/1.1" 200 4055
[07/Mar/2018 11:50:17] "GET /static/bootstrap/css/bootstrap.css HTTP/1.1" 200 141414
[07/Mar/2018 11:50:19] "GET /static/images/pdxen_logo.png HTTP/1.1" 200 124678
[07/Mar/2018 11:50:20] "GET /static/images/footer-logo-wraper.png HTTP/1.1" 200 17890
[07/Mar/2018 11:50:20] "GET /static/bootstrap/fonts/glyphicons-halflings-regular.woff2 HTTP/1.1" 200 18028
[07/Mar/2018 11:50:21] "GET /static/bootstrap/js/http_ajax.googleapis.com_ajax_libs_jquery_1.11.2_jquery.js HTTP/1.1" 200 284184
[07/Mar/2018 11:50:21] "GET /static/images/company_structure.png HTTP/1.1" 200 221035
[07/Mar/2018 11:50:23] "GET /static/images/backgroud_main.jpg HTTP/1.1" 200 140781
```

```bash
System check identified no issues (0 silenced).
March 07, 2018 - 11:52:22
Django version 2.0.2, using settings 'config.settings'
Starting development server at http://0:8080/
Quit the server with CONTROL-C.
[07/Mar/2018 11:52:26] "GET /static/custom/custom.css HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET / HTTP/1.1" 200 16713
[07/Mar/2018 11:52:26] "GET /static/custom/custom.css HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/custom/custom-module.css HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap/css/bootstrap.css HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap-dropdownhover/css/bootstrap-dropdownhover.min.css HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/images/ceo.jpg HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/images/pdxen_logo.png HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap/js/bootstrap.js HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap-dropdownhover/js/bootstrap-dropdownhover.min.js HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap/js/http_ajax.googleapis.com_ajax_libs_jquery_1.11.2_jquery.js HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/images/company_structure.png HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/images/backgroud_main.jpg HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/images/footer-logo-wraper.png HTTP/1.1" 304 0
[07/Mar/2018 11:52:26] "GET /static/bootstrap/fonts/glyphicons-halflings-regular.woff2 HTTP/1.1" 304 0
```

# Orange 의 교훈

1. `[[]]*3` 안의 리스트 세 개는 정확히 같은 값을 가리킨다. 따라서 해당 연산은 상수를 대상으로 할 때만 의미가 있다. 


# etc

- [블라블라 닷컴](https://www.blahblah.tech) 개발 블로그 글들을 여럿 모아놓은 사이트
- [인스타 스크랩퍼](https://github.com/rarcega/instagram-scraper
) 인스타 그램 사진을 긁어올 수 있는 도구


