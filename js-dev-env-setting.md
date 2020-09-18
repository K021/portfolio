
<h1 class='header'><span>js 개발 환경 설정
</span></h1>


> ##### 참고문서: 
> - <cite>[heropy: 처음 시작하는 Node.js 개발 - 1 - 설치 및 버전 관리(NVM, n)](https://heropy.blog/2018/02/17/node-js-install/)</cite>
> - <cite>[junsikshim.github.io: mac 에서 node.js 설치하기](http://junsikshim.github.io/2016/01/29/Mac%EC%97%90%EC%84%9C-Node.js-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0.html)</cite>
> - <cite>[김정환블로그: NVM으로 노드 버전 관리하기](http://blog.jeonghwan.net/2016/08/10/nvm.html)</cite>


## 목차
- [NVM 으로 node 설치](#nvm)
- [NPM 으로 패키지 관리](#npm)
- [IDE: WebStorm](#webstorm)


<a id='nvm'></a>
# NVM 으로 node 설치
NVM 은 node 의 버전을 효과적으로 관리할 수 있다. 기존에 node 를 전역 설치한 경우에는, 다음 링크에서 제안하는 방법으로 node 를 삭제하자. 

> &mdash; <cite>[mac 에서 node.js 설치하기](http://junsikshim.github.io/2016/01/29/Mac%EC%97%90%EC%84%9C-Node.js-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0.html)</cite>


## nvm 설치하기
nvm 은 cURL 또는 homebrew 로 설치할 수 있다.

##### curl
```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```
> 이 링크는 변경될 수 있다. 공식 문서를 참고하자 &mdash; <cite>[github: npm #installation](https://github.com/creationix/nvm#installation)</cite>

##### homebrew
```bash
brew install nvm
```

## shell 설정 파일 확인
nvm 이 설치가 되면, `~/.zshrc` 또는 `~/.bash_profile` 과 같은 쉘 설정 파일에 다음 스크립트가 추가된다. 

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

추가되지 않은 경우, 직접 추가해줘야 한다. 

이 과정이 완료되면, `source ~/.zshrc` (쉘 설정파일 재설정) 또는 터미널을 재시작 해야 한다. 


## 설치 확인

```bash
nvm --version
>>> 0.33.11
```

##### `nvm` 명령어가 없는 경우
위의 설치 명령을 실행하기 전에 `~/.nvm` 폴더가 없으면 오류가 발생할 수 있다. 다음의 명령어로 폴더를 생성하고, 다시 설치한다. 

```bash
mkdir ~/.nvm
```
```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

##### homebrew 오류 메세지
```
Please note that upstream has asked us to make explicit managing
nvm via Homebrew is unsupported by them and you should check any
problems against the standard nvm install method prior to reporting.

You should create NVM's working directory if it doesn't exist:

  mkdir ~/.nvm

```
##### curl 오류 메세지
```
You have $NVM_DIR set to "/Users/ElohimAwmar/.nvm", but that directory does not exist. Check your profile files and environment.
```
위 curl 메세지는, 위의 쉘 설정을 한 뒤에 curl 명령을 했을 때 발생한 오류이다.

## Node 설치
> LTS: Long Term Support 의 약자로, 일반적으로 권장되는 버전이다. 

- LTS 버전 설치: `nvm install --lts` (권장)
- 안전화 최신 버전 설치: `nvm install stable`
- 특정 버전으로 설치: `nvm install 8.9.4`
- 특정 버전 중 최신버전으로 설치: `nvm intsall v8` 

```bash
# version 8.9.4 가 필요한 경우는 nvm install 8.9.4
nvm install stable  # 이것보다 LTS 설치를 추천한다.

>>> Downloading and installing node v11.4.0...
Downloading https://nodejs.org/dist/v11.4.0/node-v11.4.0-darwin-x64.tar.xz...
######################################################################## 100.0%
Computing checksum with shasum -a 256
Checksums matched!
Now using node v11.4.0 (npm v6.4.1)
Creating default alias: default -> stable (-> v11.4.0)
```
설치된 노드의 경로는 `which` 명령어로 확인할 수 있다. 기본적으로 `~/.nvm/` 아래 저장된다.  

```bash
which node
>>> /Users/ElohimAwmar/.nvm/versions/node/v11.4.0/bin/node
```

## nvm 명령어

> 추가 사용법은 다음 공식 문서를 참고하자 &mdash; <cite>[github.com: nvm #usage-1](https://github.com/creationix/nvm#usage-1)</cite>

##### Node 버전으로 설치
`nvm install <version>`: 해당 버전으로 노드가 설치된다. 

```bash
nvm install --lts  # LTS 버전 설치 (권장)
nvm install 8.9.4
nvm install stable  # 안정화 최신 버전 설치
nvm install v8  # 해당 버전의 최신 버전을 자동 설치
``` 

##### 설치할 수 있는 버전 목록 보기
`nvm ls-remote`

##### 버전 확인
`nvm ls`: 설치된 node 버전 목록 확인

```bash
~ » nvm ls
->     v10.14.2
        v11.4.0
         system
default -> 10.14.2 (-> v10.14.2)
node -> stable (-> v11.4.0) (default)
stable -> 11.4 (-> v11.4.0) (default)
iojs -> N/A (default)
lts/* -> lts/dubnium (-> v10.14.2)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.15.1 (-> N/A)
lts/carbon -> v8.14.0 (-> N/A)
lts/dubnium -> v10.14.2
```

##### 설치된 node 버전의 alias 설정
`nvm alias <alias> <version>`

```bash
nvm alias default 8.9.4
```

##### node 버전 변경, 적용
`nvm use <version>`, `nvm use <alias>`




<a id='npm'></a>
# npm 사용하기
> 참고: [velopert: [Node.JS] 강좌 05편: NPM](https://velopert.com/241)

npm 은 javascript 의 패키지 관리자이다. 좀더 나은 속도와 캐싱 시스탬을 원한다면, Yarn 을 사용할 수 있다.

## `npm init`과 package.json

#### 1. `npm init`
npm 을 통해 패키지를 관리하기 위해서는, 내 프로젝트로 npm 패키지로 설정해야 한다. 그것이 `npm init`이며, 패키지의 모든 설정을 담고 있는 `package.json` 파일을 생성한다. 

#### 2. `package.json`

> package.json 내용에 대한 자세한 설명은 [감성프로그래맹: 모두 알지만 모두 모르는 package.json](https://programmingsummaries.tistory.com/385)을 참조하자.

- 위치: `node_project_dir/package.json`
- 용도: 프로젝트의 모든 정보를 담고 있는 파일 (의존성 관리 파일)
- 생성 시점: `npm init` 호출 시점 
- 일반 의존성과 개발 의존성
	- 개발 의존성은, 앱을 실행할 때는 필요 없으나, 개발할 때 필요한 패키지를 의미한다. 
	- `npm install <package_name>`: package.json 내부의 `dependencies` 항목에 해당 패키지를 넣는다. (`--save` 옵션이 기본값이다)
	- `npm install --save-dev <package_name>`: package.json 내부의 `devDependencies` 항목에 해당 패키지를 넣는다.  
- 이렇게 의존성 리스트를 저장하고 나면, 언제든지 `npm install` 명령으로 해당 패키지들을 설치할 수 있다. 


## 패키지 설치: local vs global
#### 로컬 설치: 
- 패키지를 명령어가 실행된 디렉토리에 설치하는 것. 프로젝트 별로 관리해야 하는 패키지를 설치하는 방식이며, 이것이 기본값이다.

#### 글로벌 설치: 
- system node 를 사용하는 경우, `usr/lib/node_modules/` 안에 설치한다.
	- 내가 사용중인 node 위치는 `which node` 로 확인할 수 있다.
	- 위에서 나온 경로에서 `bin`을 `lib/node_modules/`로 대체한 경로에 설치된다.
	- 시스템 라이브러리 폴더와, `nvm` 으로 관리되는 `~/.nvm/.../bin/` 폴더가 환경변수 `PATH` 에 저장되어 있기 때문에 어디서든 참조할 수 있는 것이다.
- `-g` 옵션을 붙여야 한다.  
- 시스템에 저장하므로, 루트 계정이 아니라면 `sudo` 권한이 필요하다. 
- node 앱에서 바로 require 할 수 없다. `npm link <package_name>`이 필요하다.
- 보통 cli 에서 바로 명령어를 사용하기 위해 글로벌 설치를 하는데, 아래의 걸프 설치에서 볼 수 있듯, `package.json` 에 `script` 를 작성하거나, `npx <module_name>` 으로 사용할 수 있으므로, 전역설치는 보통 권장하지 않는다. 이게 정말 프로젝트 마다 똑같이 중복되고, 프로젝트 의존성으로 다룰 필요가 없는 경우에만 전역에 설치하도록 하자. 

npm 은 기본적으로 로컬로 설치하기 때문에, 내 프로젝트 디렉토리 안에서 `npm intall <package_name>` 하면 된다.

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
이것을 더 간단하게 할 수 있다. NPM 은 `npm run`을 실행할 때, 임시 `PATH`에 `<prj_root>/node_modules/.bin/` 를 추가하기 때문에, `gulp` 만으로도 충분하다. 

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
위 명령으로 실행되는 gulp 는 `./node_modules/.bin/` 안에 있다. 만약 없으면, npx 는 센스있는 방법을 통해 설치여부를 확인한다.

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
```bash
npm run loadData
```

## 기타 명령들

##### 버전 확인
`npm -v`

##### 패키지 설치
`npm install <package_name>[@<tag>]`
> global 설치는 `-g` 옵션이 필요하다. 

```bash
npm install underscore
npm install underscore@1.8.0  # 버전을 명시하고 싶을 때
```

##### 패키지 제거
`npm uninstall <package_name>`

##### package.json 파일의 의존성 설치
`npm install`

##### 패키지 업데이트
`npm update <package_name>`

##### 패키지 검색
`npm search <package_name>`
> 이 명령어는 처음 사용할 때 메모리를 굉장히 많이 잡아먹는다. 클라우드 서버을 사용하는 경우, [npm package 검색 사이트](https://npmsearch.com/)에서 검색하자.

## 실행 명령어
> 참조 &mdash; <cite>[zerocho.com: npm 명령어](https://www.zerocho.com/category/NodeJS/post/58285e4840a6d700184ebd87)</cite>

#### `npm start`
- `package.json` 의 `script` 항목에 정의된 `start` 명령으를 실행하는 부분이다. 
- 이 설정이 없다면, `node server.js` 가 실행된다. 
- 관련 명령어: 
	- `npm stop`: `npm start` 한 것을 멈춘다.
	- `npm restart`: 멈췄다 재실행.

#### `npm test`
- `package.json` 의 `test` 명령어 실행

#### `npm run`
- 그 이외의 스크립트 실행






# Yarn

## 설치


#### `brew install yarn`
- `nvm` 과 같은 노드 버전 관리자를 사용하지 않을 경우
- `node.js` 가 없을 경우 같이 설치해준다.

#### `brew install yarn --without-node`
- `nvm` 과 같은 노드 버전 관리자를 사용했을 경우

## 명령어

##### 버전 확인
`yarn --version`

##### 업그레이드
`brew upgrade yarn`

> 기타 명령어는 다음을 참조하자 &mdash; <cite>[yarn 공식 문서: 사용법](https://yarnpkg.com/en/docs/usage)</cite>






<a id='webstorm'></a>
# Webstorm: Javascript IDE
> [Jetbrains Webstorm 홈페이지](https://www.jetbrains.com/webstorm/)

##### commercial license 취득하기

##### 설치 후 라이센스 적용하기