<h1 class='header'><span>js modules</span></h1>


## 목차
- [Gulp: 반복적인 작업의 자동화](#gulp)
- [Babel: 자바스크립트 버전간 번역](#babel7)
- [ESLint: 자바스크립트 스트립트 오류 검사](#eslint)





<a id='gulp'></a>
# Gulp

> Gulp 는 반복적인 작업을 자동화해준다.


## gulpfile.js
프로젝트 폴더 내에서 gulp 를 실행하면, 제일 먼저 `gulpfile.js`를 찾아 실행한다. 


## Gulp global? No! `npm run gulp`.

### 왜 gulp 를 global, local 에 중복 설치하는가?
> &mdash; <cite>[stackoverflow: Why do we need to install gulp globally and locally?](https://stackoverflow.com/questions/22115400/why-do-we-need-to-install-gulp-globally-and-locally#answer-30742196)</cite>

##### local 설치 이유
1. gulp version 관리
- script 에서 Node 가 `require()` 로 gulp 를 가져오기 위해선 gulp 가 로컬 모듈이어야 한다. 
	- 이것은 `NODE_PATH` 에 global module 이 기본적으로 들어있지 않기 때문
- 로컬 모듈이 더 빠르게 로드되기 때문

##### global 설치 이유
1. 스크립트에서 뿐 아니라 쉘에서 gulp 를 실행하기 위해선, system `PATH` 안에 포함되어 있는 글로벌에 설치가 필요

### global gulp 없이 gulp 실행하기 - 1 (script 설정)
> &mdash; <cite>[codeburst.io: Maybe don’t globally-install that Node.js package](https://codeburst.io/maybe-dont-globally-install-that-node-js-package-f1ea20f94a00)</cite>

방법은, NPM script 를 정의하는 것이다. `package.json`에 다음과 같은 항목을 추가하자:

```json
...
"scripts": {
  "gulp": "./node_modules/.bin/gulp"
},
...
```
> `./node_modules/.bin/gulp` 이 gulp 실행 파일이다. 이것은 링크 파일로, `./node_modules/gulp/bin/gulp.js` 를 링크한다.

이제 다음 명령으로 gulp 를 실행할 수 있다.

```bash
npm run gulp
```
NPM 은 `npm run`을 실행할 때, 임시 `PATH`에 `<prj_root>/node_modules/.bin/` 를 추가하기 때문에, `gulp` 만으로도 충분하다. 

```json
...
"scripts": {
  "gulp": "gulp"
},
...
``` 

이 임시 PATH 는, `npm run gulp` 로 gulp 실행 후 생성되는 로그에 들어가보면 알 수 있다. 로그의 경로와 그 내용은 다음과 같다.

```
/Users/ElohimAwmar/.npm/_logs/2018-12-18T10_37_59_151Z-debug.log
```

```
...
8 verbose lifecycle pj2@1.0.0~gulp: PATH: /usr/local/lib/node_modules/npm/bin/node-gyp-bin:/Users/ElohimAwmar/projects/practice/js/pj2/node_modules/.bin:/usr/local/Cellar/pyenv-virtualenv/1.1.0/shims:/usr/local/var/pyenv/shims:/Users/ElohimAwmar/.rbenv/shims:/Users/ElohimAwmar/.rbenv/bin:/Library/Frameworks/Python.framework/Versions/3.6/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin:/Users/ElohimAwmar/bin:/usr/local/bin
...
```

### global gulp 없이 gulp 실행하기 - 2 (gulp-cli)
Gulp 가 글로벌 설치를 지양하기 위해 cli 기능을 내놓았다. 이것은 로컬 `node_modules` 를 찾아서 그 안의 gulp 를 실행시켜주는 것에 불과하다.

```bash
npm install gulp-cli -g
```

### global gulp 없이 gulp 실행하기 - 3 (npx)
2017년 중반, npm 은 `npx` 라는 패키지를 배포했다. 이 패키지는 npm 이 설치될 때, 보이지 않게 전역으로 설치된다. npx 는 전역 설치 없이 전역에서 스크립트를 실행할 수 있게 해주는 패키지이다. 1번에서 한 것과 같은 npm run-srcipt 와 거의 비슷하게 동작한다. 

gulp 가 로컬 설치된 프로젝트 내에서 다음과 같은 명령이 동작한다:

```bash
npx gulp
``` 
위 명령으로 실행되는 gulp 는 `./node_modules/.bin/` 안에 있다. 만약 없으면, npx 는 센스있는 방법으로 통해 설치여부를 확인한다.

이것은 매우 단순하고 효과적인 방법이다. 다만, npx 와 함께 입력되어야 하는 인자값이 많아 명령이 길어진다면, npx 보다는 npm run-script 를 설정하는 것이 더 효율적일 수 있다. 

예를 들어 다음과 같은 경우를 보자:

```bash
npx myDataModule -path ./some/dir/file.txt -output ./log/data.log
```
매번 이 명령을 입력하는 것은 여러모로 지혜롭지 않은 생각이다. 따라서 이런 경우는 다음과 같이 미리 스크립트를 적어두는 것이 현명하겠다:

##### package.json
```json
...
"scripts": {
  "loadData": "myDataModule -path ./some/dir/file.sql -output ./log/data.log"
},
...
```


## Gulp 4.x 는 작업 종료를 명시적으로 알려줘야 한다. 

러닝 자바스크립트(2018.01.01 본) p63 에 기록된 다음의 예시는 오류가 난다.

##### gulpfile.js
```javascript
const gulp = require('gulp');
// gulp dependency 를 여기에 쓴다

gulp.task('default', function() {
  // gulp 작업을 정의한다.
});
```

오류는 다음과 같다:

```bash
[19:37:59] Using gulpfile ~/projects/practice/js/pj2/gulpfile.js
[19:37:59] Starting 'default'...
[19:37:59] The following tasks did not complete: default
[19:37:59] Did you forget to signal async completion?
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! pj2@1.0.0 gulp: `gulp`
npm ERR! Exit status 1
npm ERR!
npm ERR! Failed at the pj2@1.0.0 gulp script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     /Users/ElohimAwmar/.npm/_logs/2018-12-18T10_37_59_151Z-debug.log
```

`Did you forget to signal async completion?` 라는 에러를 구글에 검색해보면 [stackoverflow 답변](https://stackoverflow.com/questions/36897877/gulp-error-the-following-tasks-did-not-complete-did-you-forget-to-signal-async)이 나온다. 

> Gulp 3.x 에서는 명시적으로 비동기 종료를 알려줄 필요가 없었다. 비동기 작업이 끝나면 알아서 종료되었다. 그러나 Gulp 4.x 에서는 이 기준이 강화되었다. **반드시 명시적으로 비동기 작업 종료을 알려주어야 한다.**

따라서, 다음과 같은 작업은 가능하다:

```js
const gulp = require('gulp');
// gulp dependency 를 여기에 쓴다

gulp.task('default', function(done) {
  console.log("HTTP Server Started");
  done();  // 명시적 종료
});
```



<a id='babel7'></a>
# babel7

> Babel 은 자바스크립트 버전간 번역을 해준다. &mdash; <cite>[Babel User Guide](https://babeljs.io/docs/en/usage)</cite>

## gulp & babel7 으로 js 버전 바꾸기

### 1. 필요한 모듈

다음과 같은 모듈이 순서대로 필요하다. `npm install --save-dev` 로 설치하자.

- `gulp`
- `gulp-babel`
- `@babel/core`
- `@babel/preset-env`

### 2. .babelrc
> 참고 &mdash; <cite>[Babel: configuration document](https://babeljs.io/docs/en/configuration)</cite>

```json
{
  "presets": ["@babel/env"]
}
```
이것이 가장 기본적인 형태이다. 특정 브라우저 환경을 설정하기 위해선 다음과 기타 설정을 추가할 수 있다. 자세한 것은 [문서를 참조](https://babeljs.io/docs/en/configuration)하자.


## babel6 와의 차이점

#### 패키지 스코프
```git
- babel‐cli- babel‐core- babel‐preset‐env- babel‐polyfill
+ @babel/cli+ @babel/core+ @babel/preset‐env+ @babel/polyfill
```
#### 설정 파일에도 패키지 스코프를 명시해야 한다. 

```json
# 변경 전
{
	"presets": [
		"env"	
	],
	"plugins": [
		"transform-object-rest-spread"
	]
}

# 변경 후
{
	"presets": [
		"@babel/env"	
	],
	"plugins": [
		"@babel/proposal‐object‐rest‐spread"
	]
}
```

#### 아직 표준에 포함되지 않은 문법은 `proposal`이라고 부른다.

```git
- babel‐plugin‐transform‐class‐properties- babel‐plugin‐transform‐object‐rest‐spread+ @babel/plugin‐proposal‐class‐properties+ @babel/plugin‐proposal‐object‐rest‐spread
```

#### 표준 연도가 패키지 이름에 들어가지 않는다.

```git
- babel‐plugin‐transform‐es2015‐arrow‐functions+ @babel/plugin‐transform‐arrow‐functions
```

#### 연 표준 프리셋이 Deprecated 된다

- babel‐preset‐es2015
- babel‐preset‐es2016
- babel‐preset‐es2017
- babel‐preset‐latest

### .babelrc.js

이제 JSON 파일 대신 자바스크립트 모듈을 설정으로 사용할 수 있다.

```js
var env = process.env.BABEL_ENV || process.env.NODE_ENV;
var plugins = [];

if (env === 'production') {
	plugins.push.apply(plugins, ["a‐super‐cool‐babel‐plugin"]);
}
module.exports = { plugins };
```

#### 내부 종속성에서 `babel-runtime` 제거
Babel6 에선 모든 플러그인들이 polyfill 을 위해 내부적으로 `babel-runtime` 을포함하고 있다. 이제 구 버전 Node 를 지원하지 않기 때문에 더 이상 필요없다.

#### `babel-core` 가 peerDependency

이제 원하는 버전의 `babel-core` 를 package.json 에 명시적으로 추가해야 한다.

```git
- yarn add ‐‐dev @babel/cli+ yarn add ‐‐dev @babel/core @babel/cli
```

#### 기존 바벨에서 빠른 업그레이드
> [github: babel-upgrade](https://github.com/babel/babel‐upgrade)

```bash
npx babel‐upgrade
```



<a id="eslint"></a>
# ESLint
> ESLint 는 코드에 문제가 있는지 없는지 검사해주는 모듈이다. &mdash; <cite>[ESLint: Getting Started](https://eslint.org/docs/user-guide/getting-started)</cite>


## 설치

eslint 는 프로젝트마다 사용해야 하며, 설정에 있어 큰 차이가 없을 가능성이 크므로, 전역 설치하는 것을 추천한다고 한다.

```bash
npm install -g eslint

>>> /usr/local/bin/eslint -> /usr/local/lib/node_modules/eslint/bin/eslint.js
+ eslint@5.10.0
added 116 packages in 21.257s
```

설치 메세지를 살펴보면, `eslint@5.10.0` 이 `/usr/local/lib/node_modules/` 아래에 설치되었고, 그 안의 실행파일을 `/usr/local/bin/eslint` 가 링크한다는 것을 알 수 있다. 


## 사용하기

### 초기 설정: `eslint --init`

프로젝트마다 설정이 다를 필요가 있다. 각 프로젝트 폴더 최상단에서 `eslint --init`을 해준다. 이 명령은, `.eslintrc.js` 파일을 만든다. (설정 파일 형식을 javascript 로 설정했을 때이다.)

```
eslint --init
```

`.eslintrc.js` 파일은 다음과 같은 내용을 담고 있다.

```js
module.exports = {
    "env": {
        "es6": true,
        "node": true
    },
    "extends": "eslint:recommended",
    "parserOptions": {
        "ecmaVersion": 2015,
        "sourceType": "module"
    },
    "rules": {
        "indent": [
            "error",
            2
        ],
        "linebreak-style": [
            "error",
            "unix"
        ],
        "quotes": [
            "error",
            "single"
        ],
        "semi": [
            "error",
            "always"
        ]
    }
};
```
eslint 가 오류를 잡아내는 규칙이 `"rules"` 에 설정되어있다. 이 값을 변경하고 싶다면 아래의 링크를 참고하자.

> [ESLint 공식문서: rules](https://eslint.org/docs/rules/)

아래는, es7 과 react 를 사용하는 eslint 설정의 일부이다:

```js
{
  "extends": [
    "eslint:recommended",
    "plugin:import/errors",
    "plugin:import/warnings"
  ],
  "plugins": [
    "react"
  ],
  "parserOptions": {
    "ecmaVersion": 7,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "env": {
    "es6": true,
    "browser": true,
    "node": true,
    "jquery": true,
    "mocha": true
  }
}
```

> 기타 자세한 설정을 원한다면 &mdash; <cite>[ESLint 공식문서: configuring](https://eslint.org/docs/user-guide/configuring)</cite>



## gulp 와 사용하기: `gulp-eslint`

프로젝트를 빌드할 때마다 걸프를 사용하므로, 여기서 코드를 체크하는 것이 좋다. 

```
npm install --save-dev gulp-eslint
```
`gulpfile.js` 에 다음과 같은 내용을 추가하자.

```js
const ...
...
const eslint = require('gulp-eslint');
// gulp dependency 를 여기에 쓴다

gulp.task('default', function(done) {
  // ESLint 실행
  gulp.src(['es6/**/*.js', 'public/es6/**/*.js'])
    .pipe(eslint()
    .pipe(eslint.format());
  ...
});
```


### 3. 에러 체크하면서 바로 고쳐버리기: `--fix` 옵션

> 참조 &mdash; <cite>[githup: gulp-eslint #optionsfix](https://github.com/adametry/gulp-eslint#optionsfix), [github: gulp-eslint-if-fixed](https://github.com/lukeapage/gulp-eslint-if-fixed)</cite>

`eslint --fix <file>` 명령은 해당 파일의 오류를 수정해준다. 그런데 이걸 gulp 에서 동작시키려면 어떻게 해야 할까?

1. gulp 에서 eslint 를 실행할 때, `{fix: true}` 옵션을 넣어준다 (이 옵션을 넣어서 수정된 파일은 gulp stream 상태로 저장된다. 이것을 파일로 저장해주어야 한다)
2. `gulp-eslint-if-fixed` 모듈을 사용해 저장한다.

##### `gulp-eslint-if-fixed` 모듈 설치

```bash
npm i --save-dev gulp-eslint-if-fixed
```

##### `gulpfile.js`
```js
const gulp = require('gulp');
const eslint = require('gulp-eslint');
const eslintIfFixed = require('gulp-eslint-if-fixed');

gulp.task('default', function(done) {
  // ESLint 실행
  gulp.src(['es6/**/*.js', 'public/es6/**/*.js'])
    .pipe(eslint({fix: true}))
    .pipe(eslint.format())
    .pipe(eslintIfFixed('es6'))  // 폴더 별로 저장해주어야 한다.
    .pipe(eslintIfFixed('public/es6'));
    
   ...
});
```
