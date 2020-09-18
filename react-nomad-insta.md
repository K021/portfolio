#### 읽으면 좋을 글들
- [codementor.io: Redux, Store, Actions, Reducers and logger (1)](https://www.codementor.io/kiok46/redux-store-actions-reducers-and-logger-get-started-b35h1pvpc)





# 시작하기

> `#2-0` &darr; 

## 공부할 내용
- Route Management: `React Router`
- State Mangagement: `Reduc`, `Redux Ducks`
- React Design Patterns
- Reduc Middlewares
- Module Bundling
- SCSS
- Developer Tools


> `#2-1` &darr; 

## 리액트 소개
- React (JSX, Redux, Ducks, Thunk)
- JSX 사용 없이 `React.creatElement()`를 사용할 수도 있으나, 별로다.


## Webpack
- Module bundler: 모듈 번들러는 코드를 변환해서 결합하는 기능이 있다.
- 웹팩은 통째로 자바스크립트 오브젝트이다. 커스터마이징이 가능하다.
- 기능
	- 코드 변환 (`jsx`&rarr;`js`, `sass`&rarr;`css`)
	- 파일 관리
	- 플러그인 관리


## NodeJS
- javascript runtime: 브라우저 밖에서 자바스크립트를 실행할 수 있게 한다.
- 그래서 자바스크립트 모듈을 NPM 으로 사용할 수 있다.
- NPM 은 Node Package Manager 로, 노드 패키지 관리자이다. 
- Yarn 은 npm 이 약간 향상된 것으로, 오프라인 기능과 `Lockfiles` 를 제공한다. 






> `#2-2` &darr; 

# Webpack

## 웹팩을 구성하는 4가지
- Entry: 웹팩이 어디서부터 코드를 변환할지 알려줌
- Output: 변환이 된 코드를 어디에 놓을 것인지 알려줌
- Loader: 각 파일을 어떻게 변환하고 관리해야 하는지 알려줌. 파일 타입마다 하나씩 있다. 이미지 파일을 위한 로더, SCSS 파일을 위한 로더, 자바스크립트 파일을 위한 로더 등.
- Plugins: 파일별로 변환된 코드 전체를 변환한다.
	- 파일별로 변환된 코드: 이미지 파일, 텍스트 파일, CSS 파일, 구버전 JS 파일 등
	- 코드 전체를 변환한 코드: html 파일

### Entry
```js
module.exports = {
  entry: './path/to/my/entry/file.js'
};
``` 
entry point 가 여러개라면, 다음과 같이 쓸 수 있다:

```js
module.exports = {
  entry: {
    app: './src/app.js',
    search: './src/search.js',
  }
};
``` 

### Output
```js
const path = require('path');

module.exports = {
  entry: './path/to/my/entry/file.js',
  output: {
    path: path.resolve(__dirname, 'dist'),  // __dirname: 현재 파일의 디렉토리
    filename: 'my-first-webpack.bundle.js',
  }
};
```
output 은 다음과 같이 간단하게 작성할 수도 있다.

```js
output: {
  filename: '<name>.js',
  path: __dirname + '/dist'
}
```

### Loader
- 작동방식: 변환 시킬 파일을 고르고 &rarr; 어떻게 변환할지 결정

```js
const path = require('path');

module.exports = {
  entry: './path/to/my/entry/file.js',
  output: {
    path: path.resolve(__dirname, 'dist'),  // __dirname: 현재 파일의 디렉토리
    filename: 'my-first-webpack.bundle.js',
  },
  // 여기가 로더 설정
  module: {
  	 rules: [
  	   { test: /\.txt$/, use: 'raw-loader' }  // 특정 파일 확장자와 로더 매치
  	 ]
  }
};
```

### Plugins
```js
const HtmlWebpackPlugin = require('html-webpack-plugin');  // npm 으로 설치
const webpack = require('webpack');  // built-in plugin 에 접근
const path = require('path');

module.exports = {
  entry: './path/to/my/entry/file.js',
  output: {
    path: path.resolve(__dirname, 'dist'),  // __dirname: 현재 파일의 디렉토리
    filename: 'my-first-webpack.bundle.js',
  },
  // 여기가 로더 설정
  module: {
  	 rules: [
  	   { test: /\.txt$/, use: 'raw-loader' }  // 특정 파일 확장자와 로더 매치
  	 ]
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin(),
    new HtmlWebpackPlugin({template: './src/index.html'}),  // 최종 파일을 넣을 곳
  ]
};
```

## 웹팩의 특징
- 모든 파일을 모듈로 인식한다.
- 자바스크립트만 이해한다
- 다수의 entry point 를 가질 수 있지만, output 은 하나다.


## 웹팩 루틴
- 웹팩 프로젝트 생성
- ES6 자바스크립트 작성
- 웹팩이 변환한 구 자바스크립트의 `bundle.js` 파일 생성
- 플러그인을 사용해 압축, 못생기게 만듦

> `#2-3` &darr; 

# Webpack 연습

> `yarn` 으로 webpack 깔면 `npx webpack` 명령어가 안 된다. 정확한 이유는 모르겠으나, 아래의 패키지 중, `webpack` 만 `npm`으로 깔아주면 된다. 아니면 전부 `npm` 으로 설치하자.

1. `yarn init` package.json 생성 프로젝트 설정 값을 담고 있음
- `yarn global add webpack`: 웹팩 클로벌 설치
	- `webpack` 명령어를 바로 실행시키기 위한 것이다.
	- `npx webpack` 으로 실행할 수도 있으니, 로컬로만 설치해도 된다.
- `yarn add --dev`로 다음 설치:
	- `babel`: 바벨 컴파일러
	- `@babel/core`: 바벨의 핵심 기능 라이브러리
	- `babel-loader`: 웹팩에서 바벨을 사용하기 위한 패키지 
	- `@babel/preset-env`: 필요한 변환 라이브러리만 다운 받기 위한 것
	- `webpack`: 실제 실행되는 웹팩 로컬 패키지
	- `webpack-cli`: cli 상에서 `webpack` 명령어를 쓰기 위한 패키지
	- `uglifyjs-webpack-plugin`
- `touch webpack.config.js`: 웹팩 설정파일 생성, 입력
- `touch index.js`: 기본 js 파일 생성. 무언가 es6 코드 넣기

##### `webpack.config.js`
```js
const path = require("path")
// const webpack = require("webpack")
const UglifyJsPlugin = require("uglifyjs-webpack-plugin")

module.exports = {
  entry: "./index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js"
  },
  mode: "development",
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"]  // @babel/preset-react 면 그걸로
        }
      }
    ]
  },
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        /* your config */
      })
    ]
  }
}
```

`output` 부분은 이렇게 바꿀 수도 있다:

```js
output: {
  path: __dirname + '/dist',  // 더해줄 때는 '/' 가 반드시 필요하다.
  filename: 'bundle.js'
}
```

이제 웹팩을 실행해보자. `webpack` 

> `#2-4` &darr; , 유튜브에 올라온 새로운 것으로 봄 




# Creat React App 2.0

> 일종의 configuration base 라고 할 수 있다. react 개발에 필요한 중요한 것들을 다 담고 있는 것.
> 
> ##### 공식문서
> - <cite>[reactjs.org: create react app 2.0](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html)</cite>
> - <cite>[facebook 깃헙 페이지: Create React App](https://github.com/facebook/create-react-app)</cite>

- 페이스북에서 제공하는 패키지로, 웹팩을 설정할 필요 없이 리액트를 사용할 수 있게 해준다. 자잘한 설정작업을 알아서 해주기 때문이다.
- 원래는 `creat-react-app` 이라는 npm 모듈을 설치해야 했으나, 2.0 부터는 `npx` 지원이 되어 무설치로 진행할 수 있다.

## 추가된 기능
1. 웹팩 설정 없이 `Sass`와 `CSS`을 모듈로 이용할 수 있다.
2. 리액트 컴포넌트는 한 개의 요소로 감싸진 템플릿만 렌더링할 수 있는데, 때에 따라선 공통 부모가 없는 요소 여러개가 한 컴포넌트 안에 있을 수 있다. 그런 경우 그것들을 다 감싸주는 `React Fragment Syntax` 기능이 추가되었다. 
	- 이전에는 사용하기가 힘들었는데, 이제 바벨 7이 적용되어 가능해졌다.
3. 오래된 브라우저에서 새로운 `CSS` 기능을 사용할 수 있게 해주는 `PostCSS`. 알아서 변환해준다.
4. `svg` 파일을 리액트 컴포넌트 형태로 임포트할 수 있는 기능
5. `node_modules`가 필요없는 `Yarn Plug&Play mode`. 사전 설치 없이 필요할 때 바로 바로 다운로드 한다. 그러나 아직은 실험적인 단계. 니콜라스는 노드 모듈이 그리 크지 않아서 필요성을 느끼지 않는다고 한다.
6. 구글의 `Workbook` 기능


> 더 많은 내용은 다음을 참고 &mdash; <cite>[reactjs.org: create react app 2.0](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html)</cite>

## 환경 설정

아래의 링크 중 하나를 골라 시키는대로 실행하자: 

> - [facebook 깃헙 페이지: Create React App](https://github.com/facebook/create-react-app)
> - [React 공식 문서: Create React App](https://facebook.github.io/create-react-app/docs/getting-started)
> - [방구석엔지니어 블로그: create-react-app으로 프로젝트 시작하기](https://eunvanz.github.io/react/2018/06/05/React-create-react-app으로-프로젝트-시작하기/)

리액트 앱을 생성하자. 아주 간단하다: `npx create-react-app <app_name>`


## 새로운 기능 사용하기

### 1. Sass 웹팩 없이 사용하기
- `node-sass` 설치가 필요하다. 
- 그 이후엔 마음대로 쓰면 된다. 

### 2. CSS 모듈 사용하기
> CSS 모듈은, 큰 프로젝트를 할 때 선택자가 겹쳐서 일어날 수 있는 불상사를 막기 위한 것이다. 웹팩이 작성된 css 선택자에 해쉬를 붙여서 아무 것도 중복되지 않게 한다.  
> `잠깐`, 같은 파일에 있는 같은 선택자는 같은 값으로 변환되는가? 아마 그런 것 같다. 

- `<file_name>.module.scss` 또는 `<file_name>.module.css` 로 파일 저장
- 클래스 명을 자바스크립트 변수 만들 듯 만들어주기. `appHeader` 처럼.
	- 사실 이 과정이 꼭 필요한 것은 아니다. 자바스크립트 변수 타입이 아니라면, `style['App-header']`와 같이 사용할 수 있기 때문. 근데 ... 좀 별로잖아?
- 아래 처럼 자바스크립트 파일을 수정한다.

##### App.js
```jsx
...
import styles from './App.module.scss';

class App extends Component {
  render() {
    return (
      <div className={styles.app}>  // 클래스 명을 프로퍼티로 갖고 있는 스타일 모듈처럼 사용가능하다.
      </div>
    )
  }
}
```

그리고 브라우저에서 요소 검사를 하면, `{styles.app}` 부분이 `App_app__2ff0n` 과 비슷한 형태로 바뀐 것을 볼 수 있는데, 이것은 내부에 설정된 웹팩이 알아서 변경해준거다. 겹치지 않게. 

클래스가 겹치지 않으니, 클래스 명을 마음대로 지을 수 있다. 고려할 필요가 없어진다. (상속 문제는 유지되는 듯하다)

### 3. React Fragment Syntax

```jsx
<React.Fragment>
  렌더할 템플릿
</React.Fragment>
```
와 같은 것을 아래와 같이 사용할 수 있다:

```jsx
<>
  렌더할 템플릿 
</>
```

### 4. `svg` 모듈로 사용하기
```jsx
import logo from './logo.svg';

<img src={logo} className="App-logo" alt="logo"/>
```
와 같던 것을 다음과 같이 사용할 수 있다:

```jsx
import {ReactComponent as Logo} from './logo.svg';

<Logo/>
```

> `#2-5``#2-6` &darr; 

## 고급 기능: 내 맘대로 설정하기

### `npm run eject`

- 이 기능은 한번 하면 돌이킬 수 없다.
- 빋드 도구와 설정이 마음에 들이 않을 때 사용하는 것.
- `package.json` 에 작성된 스크립트에는 `react-scripts` 라는 것을 실행하도록 되어있는데, 원래는 접근할 수 가 없다. 이걸 하면 접근하고 수정할 수 있다. 

> 나는 지금 할 계획이 없으므로 스킵. 자세한 것은 다음 참조 &mdash; <cite>[facebook.github.io: #npm-run-eject](https://facebook.github.io/create-react-app/docs/available-scripts#npm-run-eject)</cite>
> 
> ##### 다음의 니콜라스 유튜브 강의도 참고하자
> - https://www.youtube.com/watch?v=w9Zf0hpohQM
> - https://youtu.be/KZW99D2LuuQ
> - https://youtu.be/rZOduIgjKYI


# Redux - 기본

> - 강의자료 &mdash; [React, Redux 로 타이머 앱 만들기](https://academy.nomadcoders.co/courses/enrolled/235420)
> - 코드 &mdash; [github: nomadcoders/tomato-timer](https://github.com/nomadcoders/tomato-timer)

## 설치

#### `npm install redux react-redux --save`

> redux 는 리액트만을 위한 것이 아니므로, `react-redux` 가 필요하다. 

## Redux 란

- 모든 컴포넌트의 state를 한 곳에서 관리하는 모델.
- 각 컴포넌트들이 자신이 필요한 state 를 가지고 있state를 변경해야 할 때, 그 정보를 컴포넌트 끼리 주고 받던 기존
- 기존의 모델을 버렸다:
	- 각 컴포넌트들이 자신이 필요한 state 를 각자 가지는 것
	- 기존 state 를 변경해야 할 때, 그 정보를 컴포넌트 끼리 주고 받는 것
- 모든 state 를 한 곳에서 관리한다: `Store`
- state 변경을 한 곳에서 관리한다: `Reducer`

### Redux Store

- 모든 state 는 js object 로 저장된다. 

### Reducer

- state 변경은 변경 `action`을 `Reducer`에 보내는 것으로 이루어진다. 
- `Reducer` 가 액션의 종류에 따라 지정된 함수를 실행하여 state 를 바꾼다. 

> - `action`은 state 를 변경하는 특정 행위를 가리키는 `type` 프로퍼티를 갖고 있는 객체이다.
> - `action creator`는 `action`을 반환하는 함수이다.
> - `reducer` 는 `action.type`에 대응하는 `reducer function`을 작동시키는 함수이다.
> - `reducer function` 은 실제로 state 를 변경하기 위한 함수이다. 기존 state 를 받아서 새로운 state 를 반환할 뿐이지만, 내부적으로 이 함수를 사용해 state 를 변경한다.


### With Redux vs Without Redux
[with redux gif](https://www.filepicker.io/api/file/rPmpyjOLRiK6iUWb054s)
[without redux gif](https://www.filepicker.io/api/file/t7O9woo2RUyRoM7JK0FH)


## Reducer 설계하기
> - [React, Redux 로 타이머 앱 만들기: #10. Creating the tomato reducer](https://academy.nomadcoders.co/courses/235420/lectures/3671565)
> - [Github commit](https://github.com/nomadcoders/tomato-timer/commit/975e90d88cd7ba70fce61011d775fbc0b0f4328d)

##### `reducer.js` 예시
```jsx
// Imports
	
// Action Types (just indicators of actions)
	
const START_TIMER = "START_TIMER";
const PAUSE_TIMER = "PAUSE_TIMER";
const RESUME_TIMER = "RESUME_TIMER";
const STOP_TIMER = "STOP_TIMER";
const ADD_SECOND = "ADD_SECOND";
	
// Action Creators
// return value of these functions are real 'Actions'.
	
function startTimer() {
  return {
    type: START_TIMER
  };
}
	
function pauseTimer() {
  return {
    type: PAUSE_TIMER
  };
}
	
function restartTimer() {
  return {
    type: RESTART_TIMER
  };
}
	
function addSecond() {
  return {
    type: ADD_SECOND
  };
}
	
// Reducer
	
const TIMER_DURATION = 1500;
	
const initialState = {
  isPlaying: false,
  elapsedTime: 0,
  timerDuration: TIMER_DURATION
};
	
function reducer(state=initialState, action) {
  switch (action.type) {
    case START_TIMER:
      return applyStartTimer(state, action);
    case PAUSE_TIMER:
      return applyPauseTimer(state, action);
    case RESUME_TIMER:
      return applyResumeTimer(state, action);
    case STOP_TIMER:
      return applyStopTimer(state, action);
    case ADD_SECOND:
      return applyAddSecond(state, action);
    default:
      return state;
  }
}
	
// Reducer Functions
	
function applyStartTimer(state, action) {
  return {
    ...state,
    isPlaying: true,
    elapsedTime: 0
  };
}
	
function applyPauseTimer(state, action) {
  return {
    ...state,
    isPlaying: false
  };
}
	
function applyResumeTimer(state, action) {
  return {
    ...state,
    isPlaying: true
  };
}
	
function applyStopTimer(state, action) {
  return {
    ...state,
    isPlaying: false,
    elapsedTime: 0
  };
}
	
function applyAddSecond(state, action) {
  const { elapsedTime } = state;
  if (elapsedTime < TIMER_DURATION) {
    return {
      ...state,
      elapsedTime: elapsedTime + 1
    };
  } else {
    return {
      ...state,
      isPlaying: false
    };
  }
}
	
// Exports
// 단 한개의 디폴트를 제외한 나머지는 객체 하나에 묶어서 보낸다.
// 나중에 임포트 할 때 해체할당으로 가져간다.
	
const actionCreators = {
  startTimer,
  pauseTimer,
  restartTimer,
  addSecond
};
export { actionCreators };
	
// Default (단 한개 뿐)
	
export default reducer;
```

## Reducer 사용하기

### 1. 초기 state 설정하기

```jsx
import { createStore } from "redux";
import reducer from "./reducer";
	
let store = createStore(reducer);  // reducer 를 사용해 state 초기값 설정
```

### 2. 하위 컴포넌트에서 store 에 접근할 수 있게 하기

`Provider`는 Store 의 state 를 하위 컴포넌트 state 에 복사한다. 정확히는 접근가능하게 하는 것 같다.

```jsx
import { Provider } from "react-redux";

...
<Provider store={store}>  // store 의 내용을 하위 컴포넌트에 전달해줌
  <Timer />
</Provider>
...
```

##### 여기까지 `App.js` 에서의 사용 예시
```jsx
import React from "react";
import { StyleSheet, Text, View } from "react-native";
import { Provider } from "react-redux";
import { createStore } from "redux";
import reducer from "./reducer";
import Timer from "./components/Timer";
	
let store = createStore(reducer);  // reducer 를 사용해 state 초기값 설정
	
console.log(store.getState());  // 현재 state 로그로 출력
	
export default class App extends React.Component {
  render() {
    return (
      <Provider store={store}>  // store 의 내용을 하위 컴포넌트에 전달해줌
        <Timer />
      </Provider>
    );
  }
}
```

### 3. 하위 컴포넌트: state 에서 property 가져오기

- 컴포넌트를 둘로 나눈다:
	- state 를 관리하는 부분과 `index.js`
	- 보여줄 것을 정의하는 부분 `presenter.js`

##### `components/Timer/index.js`
```jsx
import { connect } from "react-redux";
import Timer from "./presenter";
	
function mapStateToProps(state) {
  const { isPlaying, elapsedTime, timerDuration } = state;
  return {
    isPlaying,
    elapsedTime,
    timerDuration
  };
}
	
// state 의 정보 중 필요한 것을 props 에 연결
export default connect(mapStateToProps)(Timer);  
```

##### `components/Timer/presenter.js`
```jsx
class Timer extends Component {
  render() {
    const { isPlaying, elapsedTime, timerDuration } = this.props;
    return (
      <View style={styles.container}>
        <StatusBar barStyle="light-content" />
        <View style={styles.upper}>
          <Text style={styles.time}>25:00</Text>
        </View>
        <View style={styles.lower}>
          {isPlaying && <Button iconName={"ios-pause"} />}
          {!isPlaying && <Button iconName={"ios-play"} />}
          {isPlaying && <Button iconName={"ios-square"} />}
        </View>
      </View>
    );
  }
}
```

### 4. action 전달해서 Store state 바꾸기

- `dispatch` 는 action 을 reducer 에  보내는 함수다.
- 여기서는 `dispatch` 함수에 `action creator` 함수를 바인딩하고, 
- 바인딩된 함수를 컴포넌트의 프로퍼티로 연결하는 작업을 수행한다.

##### `components/Timer/index.js`
```jsx
...
import { bindActionCreators } from "redux";
import { actionCreators as tomatoActions } from "../../reducer";

...

function mapDispatchToProps(dispatch) {
  return {
    // 여기 앞의 이름은 마음대로 바꿀 수 있다.
    // action creator 와 dispatch 함수를 바인딩한다.
    startTimer: bindActionCreators(tomatoActions.startTimer, dispatch),
    pauseTimer: bindActionCreators(tomatoActions.pauseTimer, dispatch),
    restartTimer: bindActionCreators(tomatoActions.restartTimer, dispatch),
    addSecond: bindActionCreators(tomatoActions.addSecond, dispatch)
  };
}

// Timer component 에 속성으로 연결해주고 끝
export default connect(mapStateToProps, mapDispatchToProps)(Timer);
```

##### `components/Timer/presenter.js`
```jsx
...
render() {
  const {
    isPlaying,
    elapsedTime,
    timerDuration,
    startTimer,  // 함수 타입의 프로퍼티가 된다. 
    restartTimer
  } = this.props;
  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" />
      <View style={styles.upper}>
        <Text style={styles.time}>
          {formatTime(timerDuration - elapsedTime)}
        </Text>
      </View>
      <View style={styles.lower}>
        {!isPlaying && <Button iconName={"play-circle"} onPress={startTimer} />}
        {isPlaying && <Button iconName={"stop-circle"} onPress={restartTimer} />}
      </View>
    </View>
  );
}
...
```

## state 가 변할 때 작업 수행하기

- state 가 갱신되면 컴포넌트의 `componentWillReceiveProps(nextProps)` 가 실행되며, 첫번째 인자로 갱신된 props 를 받아온다.
- 이 안에서 `this.setState()` 를 해도 추가적으로 렌더링하지 않는다.

### Props update 할때 사용되는 메서드 순서
1. `componentWillReceiveProps()`
2. `shouldComponentUpdate()`
3. `componentWillUpdate()`
4. `render()`
5. `componentDidUpdate()`

### 업데이트 메서드 이해하기
- `componentDidUpdate()`에선 이미 `this.props` 가 갱신되어 있다. 이 메서드는 첫번째 인자로 이전 props 를 가져온다.
- 나머지 메서드는 첫번째 인자로 새로운 `props` 를 가져온다.
- `shouldcomponentUpdate()` 에선 아직 렌더링을 하기 전이기 때문에, `return false`로 렌더링을 취소할 수 있다. 성능 최적화에 사용된다. 필요 없는 렌더링은 걷어내는 것.
- `componentWillUpdate()`에서는 state를 바꿔서는 안 된다. props가 갱신되지 않았기 때문에 state를 바꾸면 또 `shouldComponentUpdate()`가 발생한다.
- `componentWillReceiveProps()`는 v16.3 부터 deprecate 된다. v16.3 부터는 `UNSAFE_componentWillReceiveProps()` 라는 이름으로 사용된다. 그리고, 이 기능은 상황에 따라 새로운 API, `getDerivedStateFromProps` 로 대체 될 수도 있다.


> #### `static getDerivedStateFromProps()`
> 
> 이 함수는, v16.3 이후에 만들어진 라이프사이클 API 로, 이 API 는 props 로 받아온 값을 state 로 동기화 하는 작업을 해줘야 하는 경우에 사용된다.
> 
> ```jsx
> static getDerivedStateFromProps(nextProps, prevState) {
>   // 여기서는 setState 를 하는 것이 아니라
>   // 특정 props 가 바뀔 때 설정하고 설정하고 싶은 state 값을 리턴하는 형태로
>   // 사용됩니다.
>   /*
>   if (nextProps.value !== prevState.value) {
>     return { value: nextProps.value };
>   }
>   return null; // null 을 리턴하면 따로 업데이트 할 것은 없다라는 의미
>   */
> }
> ```

아래 메서드를 `Timer` 컴포넌트 안에 선언하자.

```jsx
componentWillReceiveProps(nextProps) {
  const currentProps = this.props;  // 현재 속성 저장
  if (!currentProps.isPlaying && nextProps.isPlaying) {  // false -> true 로 변할 때
    const timerInterval = setInterval(() => {
      currentProps.addSecond();  // 1초에 한번씩 state 의 `elapsedTime` 을 1씩 증가
    }, 1000);
    this.setState({  // 이 메서드는 render() 를 부르지 않는다.
      interval: timerInterval  // 반복을 중지할 수 있게 intervalId 를 컴포넌트 state 에 저장
    });
  } else if (currentProps.isPlaying && !nextProps.isPlaying) {  // true -> false 로 변할 때 
    clearInterval(this.state.interval);  // 반복작업 취소
  }
}
```




# Redux - 심화

> - `npx create-react-app fronend`
> - VS code 설치. 사용법 참조 &mdash; <cite>[vs code doc: getting started](https://code.visualstudio.com/docs/?dv=osx), [vs code doc: react tutorial](https://code.visualstudio.com/docs/nodejs/react-tutorial)</cite>
> 	- `eslint` 설치, enable
> 	- `key binding` 설정, 나는 intellij 로 
> 	- `Preference | keyboard Shortcuts` &rarr; `Fix all auto-fixable problems` or `eslint.executeAutofix` 단축키 설정

## configureStore.js 생성하기

모든 리듀서를 모아두고, Store 를 한 곳에서 관리하기 위한 `configureStore.js` 파일을 생성한다. 프로젝트 폴더 구조는 다음과 같다:

- `src/`
	- `redux/`
		- `modules/`
			- `users.js`
		- `configureStore.js`
	- `App.js`
	- `App.scss`
	- `index.css`
	- `index.js`

#### `configureStore.js`

```jsx
import { createStore, combineReducers } from 'redux';
import base from './reducer';

// 여러개의 리듀서 합치기
const reducer = combineReducers({
  base,
});

// 다음 처럼 하면 초기값을 지정할 수 있음:
// initialStore => createStore(reducer, initialStore)
// initialStore => createStore(reducer, initialStore || undefined) 되는지 확인하기
const store = initialStore => createStore(reducer);

export default store();
```

## 최상단 `index.js` 에 적용하기

#### `index.js`

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

import store from 'redux/configureStore';  // 요거 추가

import App from 'components/App';
import styles from './styles.scss';

// 원래 코드
// import reducer from 'redux/reducer';
// const store = createStore(reducer); 

ReactDOM.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById('root')
);
```

### `state` 가져오는 방식 바꾸기

위에서 처럼 `configureStore.js` 의 `store` 를 가져다가 적용한다. 오류는 나지 않지만 이것 만으로는 원래 기능이 실행되지 않는데, 이는 `store.getState()` 객체가 모양이 다르기 때문이다. 이 문제를 해결하기 위해선, 각각의 컴포넌트에서 state 를 가져오는 방식을 바꿔야 한다. 

##### 원래 객체:
```jsx
{
  isNavShrink: false,
  isNotifPaneOn: false,
  isPrefPaneOn: false,
  isProfilePaneOn: false,
  isSearchOn: false,
}
```

##### 새로운 객체:
```jsx
{
  base: {  // 위에서 합칠 때 가져온 리듀서 이름
    isNavShrink: false,
    isNotifPaneOn: false,
    isPrefPaneOn: false,
    isProfilePaneOn: false,
    isSearchOn: false,
  }
}

```

원래의 컴포넌트는 다음과 같다. 주석에 집중하자: 

```jsx
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { actionCreators } from 'redux/reducer';
import Header from './presenter';

function mapStateToProps(state) {
  console.log('Header.index', state);
  const {
    isSearchOn,
    isProfilePaneOn,
    isNotifPaneOn,
    isPrefPaneOn,
  } = state;  // 그냥 가져온다. 

  return {
    isSearchOn,
    isProfilePaneOn,
    isNotifPaneOn,
    isPrefPaneOn,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    toggleSearch: bindActionCreators(actionCreators.toggleSearch, dispatch),
    openProfile: bindActionCreators(actionCreators.openProfile, dispatch),
    openNotif: bindActionCreators(actionCreators.openNotif, dispatch),
    openPref: bindActionCreators(actionCreators.openPref, dispatch),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Header);
```

이걸 이렇게 바꾸어야 한다. 

```jsx
...

function mapStateToProps(state) {
  console.log('Header.index', state);
  const {
    base: {  // createStore.js 에서 combineReducers() 의 인자로 넣었던 녀석
      isSearchOn,
      isProfilePaneOn,
      isNotifPaneOn,
      isPrefPaneOn,
    }
  } = state;

  return {
    isSearchOn,
    isProfilePaneOn,
    isNotifPaneOn,
    isPrefPaneOn,
  };
}

...
```




## 미들웨어 적용하기 (thunk)

> [redux thunk 깃헙 공식문서](https://github.com/reduxjs/redux-thunk)

리덕스 미들웨어는 리액트 앱과 스토어 사이의 교신을 담당한다. 액션을 원하는 타이밍에 스토어로 보낼 수 있게 한다. 

> 다음은 니꼴라스의 설명이다: 
> 
> - We use thunk to dispatch actions in our own time.
- This means we want to wait to call the API first and then after the result we can dispatch logOut actions or dispatch some other thing.
- Basically, thunk gives us access to the dispatch object so we can dispatch actions in our own time.
- Without it, we would not be able to wait for the API call and react to the response from the server.

#### 설치: `npm install redux-thunk`

#### configureStore 에 적용

```jsx
// applyMiddleware 불러오기
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';  // thunk 불러오기
import base from './reducer';

const middlewares = [thunk];  // 미들웨어 리스트 정의. thunk 외에 다른 미들웨어도 추가할 수 있다.

const reducer = combineReducers({
  base,
});

// 다음 처럼 하면 초기값을 지정할 수 있음:
// initialStore => createStore(reducer, initialStore)
// initialStore => createStore(reducer, initialStore || undefined) 되는지 확인하기
const store = initialStore => 
  createStore(reducer, applyMiddleware(...middlewares));  // 미들웨어 추가해서 Store 생성

export default store();
```


## 개발용 미들웨어 적용하기 (logger)

> [redux-logger 깃헙 공식문서](https://github.com/LogRocket/redux-logger#log-only-in-development)

#### 설치 `npm install --save-dev redux-logger`

#### configureStore.js 설정 반영

`logger` 는 개발과정에서만 사용될 것이므로, 미들웨어 적용할 때도 구분해주어야 한다. 이를 위해선 node js 의 전체 정보를 갖고 있는 `process` 변수를 사용해야 한다. 개발과정인지 아닌지를 알려주는 환경변수 `NODE_ENV` 는 `process.env.NODE_ENV` 로 가져올 수 있다.

```jsx
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import base from './reducer';

const env = process.env.NODE_ENV;  // 현재 환경 가져오기

const middlewares = [thunk];

if (env == 'development') {  // 개발환경일 경우 로거 연결
  const { logger } = require('redux-logger');
  middlewares.push(logger);
}

const reducer = combineReducers({
  base,
});

// 다음 처럼 하면 초기값을 지정할 수 있음:
// initialStore => createStore(reducer, initialStore)
// initialStore => createStore(reducer, initialStore || undefined) 되는지 확인하기
const store = initialStore => 
  createStore(reducer, applyMiddleware(...middlewares));

export default store();
```
이제 state 를 변화시킬 때마다 변화를 로그로 볼 수 있다. 이런 식으로 나온다:

```js
redux-logger.js:389  action OPEN_NOTIF @ 19:52:35.903
redux-logger.js:400  prev state {base: {…}}
redux-logger.js:404  action     {type: "OPEN_NOTIF"}
redux-logger.js:413  next state {base: {…}}
```
리듀서를 통하지 않고 바로 store 에서 `dispatch` 함수로 액션을 전달할 수도 있다:

##### 최상위 index.js

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

import store from 'redux/configureStore';

import App from 'components/App';
import styles from './styles.scss';

// 바로 dispatch 함수 사용
store.dispatch({ ...store.getState(), type: 'whatever'});

ReactDOM.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById('root')
);
```



# React Router

> https://velopert.com/3417

## 설치

#### `npm install react-router-dom`

> - [리액트 라우터 공식 문서 홈](https://reacttraining.com/react-router/)
> - [리액트 라우터 DOM Quick Start Document](https://reacttraining.com/react-router/web/guides/quick-start)


## BrowserRouter 적용

##### 최상단 `index.js`

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from 'components/App';
import styles from './styles.scss';
import { BrowserRouter } from 'react-router-dom';  // 요거랑


ReactDOM.render(
  <BrowserRouter>  // 요거 추가
    <App />
  </BrowserRouter>,
  document.getElementById('root')
);
```

## Route 적용

적용하려는 컴포넌트의 의 `index.js` 에 다음과 같이 `Route` 불러오자:

```jsx
import { Route } from 'react-router-dom';
```

그리고는, 라우팅 하려는 컴포넌트를 연결한다:

```jsx
<Route component={BoardHeader}/>  // 얘는 path 가 없으므로 항상 보인다
```
이때, `component` 가 전부 소문자인지 확인하자. 그렇지 않으면 에러는 안 나는데 안 보인다.


##### Board `index.js`
```jsx
import React, { Component } from 'react';
import styles from './styles.module.scss';
import connector from './container';

import { Route } from 'react-router-dom';  // 이거 추가

import { ReactComponent as PlusSvg } from '../../svgs/plus.svg';
import { ReactComponent as PencilSvg } from '../../svgs/pencil-alt.svg';
import { ReactComponent as ExpandSvg } from '../../svgs/expand.svg';


...

class Board extends Component {
  render() {
    return (
      <div className={styles.board}>
        <div className={styles.header}>
          // 바로 이런 식으로 적용
          // 얘는 path 와 상관 없이 항상 보이는 녀셕
          <Route component={BoardHeader}/>
          {/* <BoardHeader /> */}
        </div>
        <div className={styles.body}>
          <Card /><Card /><Card /><Card /><Card /><Card />
          <Card /><Card /><Card /><Card /><Card /><Card />
        </div>
      </div>
    );
  }
}

...
```

## Switch 적용

`Switch` 컴포넌트를 적용하면, 그 아래 있는 라우트 중 path 에 가장 적합한 녀석만 살아남고 나머지는 버려진다:

```jsx
import { Route, Switch } from 'react-router-dom';

...

<Switch>
  <Route exact path="/" component={Home} />
  <Route path="/about" component={About} />
  <Route path="/contact" component={Contact} />
  {/* 여기 위에 매칭되는 path 가 없으면 아래가 실행된다. */}
  <Route component={NoMatch} />
</Switch>
```


## Link 적용

> 상세한 옵션은 다음을 참조 &mdash; <cite>https://reacttraining.com/react-router/web/api/Link</cite>

React Router 를 사용해 생성된 링크로 이동할 때에는 `Anchor` 태그를 쓰는 것이 아니라, `Link` 라는 특별한 컴포넌트를 사용해야 한다. 그래야 Store 에 저장된 정보가 유지된다. `Anchor` 를 사용하게 되면 페이지가 리로딩 되면서 Store 가 리셋된다. 

```jsx
import { Link } from 'react-router-dom'

<Link to="/about">About</Link>
```


## Match props 사용하기

> 상세한 옵션은 다음을 참조 &mdash; <cite>https://reacttraining.com/web/api/match</cite>

Route 에 연결된 컴포넌트에는 `match` 라는 속성이 전달된다. State Component 의 경우에는 `this.props.match` 로, Functional Component 에선 `{match}` 로 인자를 받아 사용할 수 있다. 전달된 `match` 에는 다음과 같은 속성과 메서드가 있다:

- `params`: (object) URL 에서 전달된 인자의 Key - Value 객체
- `isExact`: (boolean) URL 이 남는 문자 없이 정확하게 매치됐을 경우
- `path`: (string) 매치에 사용된 URL 패턴. 하위 `Route`를 만드는데 주로 사용된다.
- `url`: (string) 매치에 사용된 URL 패턴 중 매치된 부분. 하위 `Link`를 만드는데 주로 사용된다.

### `params`
여기서의 `params` 는 Route 의 path 가 `/something/:likeThis` 와 같을 때, 뒤의 값을 가져오는 것을 의미한다. 우리가 일반적으로 발하는 get parameter 를 가져오는 것은 약간 까다롭다:

- `/new` path 에 `/new?option=false` 와 같은 요청이 들어왔다고 가정하자.
- 연결된 컴포넌트 내에서 다음과 같은 과정을 수행해야 한다:

```jsx
let params = new URLSearchParams(this.props.location.search);

console.log(params.get('option'))
```
> 공식 문서의 예시도 참조하자 &mdash; <cite>https://reacttraining.com/react-router/web/example/query-parameters</cite>

### `path` vs `url`
몇 번 해봤는데, `path` 와 `url` 은 아래의 몇몇 경우를 제외하고 같을 수 밖에 없는 것 같다.  

##### 끝에 슬래쉬가 있는 경우
- path=`/new/town`, 주어진 url=`/new/town/`
- match: path=`/new/town`, url=`/new/town/`

##### 인자를 받아오는 경우
- path=`/new/town/:townName`, 주어진 url=`/new/town/grandvill`
- match: path=`/new/town/:townName`, url=`/new/town/grandvill`
 




# Redux Reducer 와 함께 Router 사용하기

> router 는 navigation step 을 저장하고 있다. 그것을 store 에 올려 사용하기 위해선 router 와 redux 를 연결한 모듈을 사용해야 한다:
> 
> 참조 문서 &mdash; <cite>https://github.com/supasate/connected-react-router, https://redux.js.org/advanced/usage-with-react-router</cite>

## 설치

#### `npm install history connected-react-router`

> - `react-router-dom` 은 당연히 설치되었다고 가정한다.
> - `react-router-redux` 는 deprecated 되었다. 니콜라스의 [codesandbox](https://codesandbox.io/s/mz2w10o76j) 를 참조하자.
> - `connected-react-router` 공식 문서 &mdash; <cite>https://github.com/supasate/connected-react-router</cite>


## configureStore.js 에 연결하고 history 객체 생성하기

history 객체는 사용자가 어플리케이션 안에서 어떤 네비게이션을 밟았는지 저장한다. 말 그대로 앱의 히스토리이며, 이 정보 덕분에 뒤로가기를 할 수 있다. 

순서는 다음과 같다:

- 필요한 객체 임포트
	- `{ routerReducer, routerMiddleware }` from `'connected-react-router'`
	- `createHistory` from `'history/createBrowserHistory'`
- `history` 객체 생성
	- `const history = createHistory();`
- `middlewares` 에 `routerMiddleware(history)` 추가

눈여겨볼 사실은 다음과 같다:

- history 모듈에는 여러 모듈이 있다. 그 중 브라우저용을 사용하는 것
	- hash, memory 용 히스토리 모듈이 있다.

첫째로, 히스토리 객체를 생성하자: 

```jsx
import createHistory from 'history/';
const history = createHistory();
```

히스토리로 `routerMiddelware` 에 연결해 미들웨어를 생성하고, `middlewares` 에 추가한다:

```jsx
import { routerMiddleware } from 'connected-react-router';
import createHistory from 'history/';

const history = createHistory();
const middlewares = [thunk, routerMiddleware(history)];
```

`combineReducers` 에 `connectRouter` 를 추가한다. 

```jsx
import { connectRouter, routerMiddleware } from 'connected-react-router';
import createHistory from 'history/createBrowserHistory';

const history = createHistory();
const middlewares = [thunk, routerMiddleware(history)];

// history 객체가 필요하므로 함수형으로 정의한다.
const reducer = history => combineReducers({
  base,
  router: connectRouter(history),
});

// reducer() 에 history 를 넣어 넘겨준다.
const store = initialStore => 
  createStore(reducer(history), applyMiddleware(...middlewares));
```

생성한 히스토리 객체를 export 한다. 라우터를 생성할 때 이 라우터와 미들웨어에 연결된 히스토리가 필요하기 때문이다. 

```jsx
export { history };
```

이제 최상위 `index.js` 에서 `ConnectedRouter` 를 불러오자. store 와 함께 history 객체도 불러온다:

```jsx
import { ConnectedRouter } from 'connected-react-router';
import store, { history } from 'redux/configureStore';
```

`Provider` 컴포넌트 바로 밑에 `ConnectedRouter` 컴포넌트로 `App` 을 감싼다:

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { ConnectedRouter } from 'connected-react-router';
import store, { history } from 'redux/configureStore';

import App from 'components/App';
import styles from './styles.scss';


ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      {/* <BrowserRouter> */}  // 라우터만 사용했던 브라우저 라우터는 더이상 필요 없다.
      <App />
      {/* </BrowserRouter> */}
    </ConnectedRouter>
  </Provider>,
  document.getElementById('root')
);
```


## component 안에서 history 접근하기

### 방법 1: 컴포넌트에 Route 씌우기

원래있던 헤더를 지우고 `Route`를 씌운다.

```jsx
import React, { Component } from 'react';
import styles from './styles.module.scss';
import { Route } from 'react-router-dom';


import Header from 'components/Header';
import Nav from 'components/Nav';
import Board from 'components/Board';
import RightPane from 'components/RightPane';


class App extends Component {
  render() {
    return (
      <>
        {/* 원래 있던 헤더를 지우고 Route 를 씌운다. */}
        <Route component={Header}/>
        {/* <Header /> */}
        <div className={styles.body}>
          <Nav />
          <Board />
          <RightPane />
        </div>
      </>
    );
  }
}

export default App;
```

그러면 컴포넌트에서 `this.props` 로 다양한 객체를 받게 되는데, 이 중 `history` 객체가 있다. 

```js
this.props:
	history: {length: 23, action: "POP", location: {…}, createHref: ƒ, push: ƒ, …}
	isNotifPaneOn: false
	isPrefPaneOn: false
	isProfilePaneOn: false
	isSearchOn: false
	location: {pathname: "/", search: "", hash: "", state: undefined, key: "4feyxk"}
	match: {path: "/", url: "/", params: {…}, isExact: true}
	openNotif: ƒ ()
	openPref: ƒ ()
	openProfile: ƒ ()
	staticContext: undefined
	toggleSearch: ƒ ()
	__proto__: Object
```

이 히스토리 안에는 여러 메서드와 속성이 있다.

```js
history:
	action: "POP"
	block: ƒ block()
	createHref: ƒ createHref(location)
	go: ƒ go(n)
	goBack: ƒ goBack()
	goForward: ƒ goForward()
	length: 23
	listen: ƒ listen(listener)
	location: {pathname: "/", search: "", hash: "", state: undefined, key: "4feyxk"}
	push: ƒ push(path, state)
	replace: ƒ replace(path, state)
	__proto__: Object
```

이 중, `history.goBack()`, `history.goForward()` 함수를 이용해 앞으로 가기 뒤로가기를 기능을 구현할 수 있다.

```jsx
class Header extends Component {
  render() {
    const { isSearchOn, isProfilePaneOn, isNotifPaneOn, isPrefPaneOn } = this.props;
    const { toggleSearch, openProfile, openNotif, openPref } = this.props;

    return (
      <header className={styles.header}>
        ...
        <div className={styles.column3}>
          <LarrowSvg className={styles.navSvg} onClick={this.props.history.goBack}/>
          <RarrowSvg className={styles.navSvg} onClick={this.props.history.goForward}/>
          ...
        </div>
      </header>
    );
  }
}
```

### 방법 2: `withRouter` 이용하기
> 공식 문서 참조 &mdash; <cite>https://reacttraining.com/web/api/withRouter</cite>

이것도 컴포넌트를 라우터로 씌우는 것 같다. 다만 렌더링시에 태그로 씌우는 것이 아닐 뿐. 다음은 공식문서에서 예시로 제시한 코드이다.

```jsx
import React from "react";
import PropTypes from "prop-types";
import { withRouter } from "react-router";

// A simple component that shows the pathname of the current location
class ShowTheLocation extends React.Component {
  static propTypes = {
    match: PropTypes.object.isRequired,
    location: PropTypes.object.isRequired,
    history: PropTypes.object.isRequired
  };

  render() {
    const { match, location, history } = this.props;

    return <div>You are now at {location.pathname}</div>;
  }
}

// Create a new component that is "connected" (to borrow redux
// terminology) to the router.
const ShowTheLocationWithRouter = withRouter(ShowTheLocation);

withRouter(connect(...)(MyComponent))
// or
compose(
  withRouter,
  connect(...)
)(MyComponent)

// This does not
connect(...)(withRouter(MyComponent))
// nor
compose(
  connect(...),
  withRouter
)(MyComponent)
```

 