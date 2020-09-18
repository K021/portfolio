## react 의 장점

- 모든 것이 자바스크립트 문법으로 동작한다. 새로운 언어나 로직을 배울 필요가 없다. 
- html 을 쪼개서 컴포넌트 별로 사용할 수 있다.
- 단방향 데이터 플로우를 가지고 있다. 데이터는 UI를 변경하지만, 반대는 안 된다. 
- 커뮤니티가 방대하다. 라이브러리, 오픈소스, 질문과 답이 매우 잘 되어있다.
- 프레임워크가 아니라 UI 라이브러리일 뿐이다. python, ruby on rails 등 다른 것에도 쓸 수 있다. 

> https://yts.am/api





# 리액트 설치


## Create React App 2.0 소개

- 페이스북에서 제공하는 패키지로, 웹팩을 설정할 필요 없이 리액트를 사용할 수 있게 해준다. 자잘한 설정작업을 알아서 해주기 때문이다.
- 원래는 `creat-react-app` 이라는 npm 모듈을 설치해야 했으나, 2.0 부터는 `npx` 지원이 되어 무설치로 진행할 수 있다.

### 추가된 기능
1. 웹팩 설정 없이 `Sass`와 `CSS`을 모듈로 이용할 수 있다.
- 리액트 컴포넌트는 한 개의 요소로 감싸진 템플릿만 렌더링할 수 있는데, 때에 따라선 공통 부모가 없는 요소 여러개가 한 컴포넌트 안에 있을 수 있다. 그런 경우 그것들을 다 감싸주는 `React Fragment Syntax` 기능이 추가되었다. 
	- 이전에는 사용하기가 힘들었는데, 이제 바벨 7이 적용되어 가능해졌다.
- 오래된 브라우저에서 새로운 `CSS` 기능을 사용할 수 있게 해주는 `PostCSS`. 알아서 변환해준다.
- `svg` 파일을 리액트 컴포넌트 형태로 임포트할 수 있는 기능
- `node_modules`가 필요없는 `Yarn Plug&Play mode`. 사전 설치 없이 필요할 때 바로 바로 다운로드 한다. 그러나 아직은 실험적인 단계. 니콜라스는 노드 모듈이 그리 크지 않아서 필요성을 느끼지 않는다고 한다.
- 구글의 `Workbook` 기능


> 더 많은 내용은 다음을 참고 &mdash; <cite>[reactjs.org: create react app 2.0](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html)</cite>

## 환경 설정

아래의 링크 중 하나를 골라 시키는대로 실행하자: 

> - [facebook 깃헙 페이지: Create React App](https://github.com/facebook/create-react-app)
> - [React 공식 문서: Create React App](https://facebook.github.io/create-react-app/docs/getting-started)
> - [방구석엔지니어 블로그: create-react-app으로 프로젝트 시작하기](https://eunvanz.github.io/react/2018/06/05/React-create-react-app으로-프로젝트-시작하기/)

리액트 앱을 생성하자. 아주 간단하다: `npx create-react-app <app_name>`

성공 메세지는 다음과 같다:

```
npx: 63개의 패키지를 4.175초만에 설치했습니다.

Creating a new React app in /Users/ElohimAwmar/projects/practice/movie-app.

Installing packages. This might take a couple of minutes.
Installing react, react-dom, and react-scripts...

yarn add v1.12.3
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 📃  Building fresh packages...
success Saved lockfile.
success Saved 10 new dependencies.
info Direct dependencies
├─ react-dom@16.7.0
├─ react-scripts@2.1.2
└─ react@16.7.0
info All dependencies
├─ @babel/runtime@7.1.5
├─ babel-plugin-transform-react-remove-prop-types@0.4.20
├─ babel-preset-react-app@7.0.0
├─ eslint-config-react-app@3.0.6
├─ react-app-polyfill@0.2.0
├─ react-dev-utils@7.0.0
├─ react-dom@16.7.0
├─ react-error-overlay@5.1.1
├─ react-scripts@2.1.2
└─ react@16.7.0
✨  Done in 31.56s.

Initialized a git repository.

Success! Created movie-app at /Users/ElohimAwmar/projects/practice/movie-app
Inside that directory, you can run several commands:

  yarn start
    Starts the development server.

  yarn build
    Bundles the app into static files for production.

  yarn test
    Starts the test runner.

  yarn eject
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd movie-app
  yarn start

Happy hacking!
```

그러면 현재 작업폴더 바로 밑에 `movie_app/` 디렉토리가 생긴 것을 볼 수 있을 것이다. 

### 어쩌면 발생할 수도 있는 오류

왠지 모르지만, 처음에 할 때는 다음과 같은 에러가 났다. 하지만 다시 해보니 되었다

```
error https://registry.yarnpkg.com/@csstools/convert-colors/-/convert-colors-1.4.0.tgz: 
Extracting tar content of undefined failed, the file appears to be corrupt: 
"Unexpected end of data"
info Visit https://yarnpkg.com/en/docs/cli/add for documentation about this command.
 
Aborting installation.
  yarnpkg add --exact react react-dom react-scripts --cwd /Users/ElohimAwmar/projects/practice/movie-app has failed.
```


## React App 설치 확인하기 

### 기본 서버 돌려보기

movie_app 으로 이동해서 `yarn start` 를 입력하자. `react-script` 가 실행되면서, 서버가 켜진다. 


##### 실행 결과
```
Compiled successfully!

You can now view movie_app in the browser.

  Local:            http://localhost:3000/
  On Your Network:  http://192.168.0.9:3000/

Note that the development build is not optimized.
To create a production build, use yarn build.
```
- `http://localhost:3000/` 는 로컬 서버 주소이고,
- `http://192.168.0.9:3000/` 는 핸드폰과 같은 다른 기기에서 들어올 수 있는, 내 와이파이 ip 를 포함한 주소이다.

### App.js 수정하기

`movie_app/src/App.js` 를 수정하면 바로 기본 서버에 반영된다. 자동 컴파일이 짱이다. 이래서 CRA 가 좋은 것.

##### 기본 페이지 색상
- 검은색: `1E2027`
- 하늘색: `54D1FA`


## WebStorm 설정

#### 자바스크립트 indent 설정
- 위치: `Preferences | Editor | Code Style | JavaScript` &rarr; `Tabs and Indents`
- `Tab size`, `indent`, `Continuation Indent` 모두 `2` 로 설정

#### 자바스크립트 버전 설정
- 위치: `Preferences | Languages & Frameworks | JavaScript` 
- `JavaScript language version` 을 `React JSX` 설정

#### ESLint 설정
- `Preferences | Languages & Frameworks | JavaScript` &rarr; `Code Quality Tools | ESLint`
- `Enable` 체크 (프로젝트 내의 `node_modules` 안에 )

#### `.eslintrc.js` 파일 작성

```js
module.exports = {
    "env": {
        "es6": true,
        "node": true,
        "browser": true,
    },
    "extends": "eslint:recommended",
    "plugins": [
        "react",
    ],
    "parser": "babel-eslint",
    "parserOptions": {
        "ecmaVersion": 6,
        "sourceType": "module",
        "ecmaFeatures": {
            "jsx": true,
            "modules": true,
        }
    },
    "rules": {
        indent: [
            "error",
            2,
            // 아래 내용 https://eslint.org/docs/rules/indent 참조
            {
                "ignoredNodes": [
                    // 3항 조건 연산자 안에 있는 객체 선언문 무시
                    // "ConditionalExpression > ObjectExpression",
                    "ConditionalExpression > *",  // 3항 조건 연산자 안에 있는 모든 인덴트 무시
                ]
            }
        ],
        "linebreak-style": [
            "error",
            "unix"
        ],
        "quotes": [
            "warn",
            "single"
        ],
        "semi": [
            "error",
            "always"
        ],
        "no-console": "off",  // 개발 중 콘솔 출력을 에러로 평가하는 것 off
        "no-unused-vars": "off",
    }
};

```


# 리액트 프로젝트 시작하기

## 컴포넌트

#### 컴포넌트 디자인
- 내가 어떤 컴포넌트를 만들어야 하는지 정해야 한다.
- 제일 큰 컴포넌트 또는 제일 위에 있는 컴포넌트 부터 차례 차례 분석한다. 

#### jsx
- 리액트 컴포넌트 안의 html을 작성할 때 사용하는 규칙이다. 간단하다.
 
#### 컴포넌트 클래스 생성
- 리액트 컴포넌트 클래스는 `component`를 상속한다. 
- 모든 컴포넌드는 `render()` 메서드를 갖고 있다. 이 메서드는 무엇을 보여줄 것인지 결정한다.
- 이 `render()` 메서드는 반드시 리턴 값이 있어야 한다. 이 안에 html 비스무리한 것을 작성하는데, 이때 사용하는 규칙을 jsx 라고 부른다.


## 불러오기

```jsx
import React, { Component } from 'react';  // React.Component 불러오기
import PropTypes from 'prop-types';  // PropTypes 불러오기
import './App.css';  // css 파일 불러오기
import Movie from './Movie';  // 현재 폴더의 Movie.js 에서 Movie 클래스 불러오기
```

## 부모 컴포넌트에서 자식 컴포넌트에 값 보내기
```jsx
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>
            Hello, <br/>Daniel Kim.
          </h1>
          {movies.map((movie, index) => {
          	// 태그 속성 값으로 값을 보내줄 수 있다.
          	// 여러 프로퍼티를 보낼 때는 유니크한 키값이 필요하다.
            return <Movie title={movie.title} poster={movie.poster} key={index}/>
          })}
        </header>
      </div>
    );
  }
}
```
위와 같이 `Movie` 컴포넌트에 `title` 과 `poster` 프로퍼티를 보낼 수 있다. `Movie` 컴포넌트 안에선 `this.props.title` 로 그 값을 가져올 수 있다.

```jsx
class Movie extends Component {
  static propTypes = {
    title: PropTypes.string.isRequired,
    poster: PropTypes.string.isRequired,
  };  // prop type 을 지정

  render() {
    return (
      <div>
        <MoviePoster poster={this.props.poster}/>
        <p>{this.props.title}</p>
      </div>
    )
  }
}
```


## propType 지정하기

#### propType
- propType 은 컴포넌트가 받을 프로퍼티의 타입을 지정한 것으로, 혼돈이 없는 프로그래밍을 가능하게 한다.
- `PropTypes.string`: 해당 프로퍼티를 문자열 타입으로 강제한다.
- `PropTypes.string.isRequired `: 해당 프로퍼티를 문자열 타입으로 강제하고, 반드시 넘겨주어야 하도록 강제한다. 해당 프로퍼티가 주어지지 않았을 경우 에러를 낸다. 

##### ES7
```js
// 클래스 안에서 호출
static propTypes = {
  title: PropTypes.string.isRequired, // 강제하는 항목
  poster: PropTypes.string,
};  // prop type 을 지정
```

##### ES6
```js
// 클래스 밖에서 호출
App.propTypes = {
  title: PropTypes.string.isRequired,
  poster: PropTypes.string,
};  // prop type 을 지정
```


## Component Life Cycle

컴포넌트 안에는 여러 메서드들이 있는데, 이 기능들은 실행 순서가 정해져 있다. 

##### render 할때 사용되는 메서드 순서
1. `componentWillMount()`
2. `render()`
3. `componentDidMount()`

> 렌더링 전 데이터를 받아올 때 `componentWillMount()` 를 사용하는 식으로 응용할 수 있다. 

##### update 할때 사용되는 메서드 순서
1. `componentWillReceiveProps()`
2. `shouldComponentUpdate()`
3. `componentWillUpdate()`
4. `render()`
5. `componentDidUpdate()`


## State 속성

#### `state` 속성 선언

컴포넌트 안에는 상태를 저장하는 `state` 속성이 있다. 

```jsx
class App extends Component {

  state = {
    movies: [
      {
        title: 'Inception',
        poster: 'https://cdn.shopify.com/s/files/1/1416/8662/products/inception_2010_french_original_film_art_spo_2000x.jpg?v=1543425422',
      },

      {
        title: 'Transcendence',
        poster: 'https://i.pinimg.com/originals/42/56/6d/42566daff7cfe843d51780e73802a83c.jpg',
      },

      {
        title: 'Interstellar',
        poster: 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',
      },

      {
        title: 'Catch me if you can',
        poster: 'https://cdn.shopify.com/s/files/1/1416/8662/products/catch_me_if_you_can_2002_original_film_art_spo_2000x.jpg?v=1543418719',
      },
    ]
  };
  
  ...
```

#### `state` 속성 사용

`state` 속성은 다음과 같이 사용할 수 있다. 

```jsx
...

render() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Hello, <br/>Daniel Kim.
        </h1>
        // 이렇게 this 로 불러온다
        {this.state.movies.map((movie, index) => {
          return <Movie title={movie.title} poster={movie.poster} key={index}/>
        })}
      </header>
    </div>
  );
}
```

#### `state` 속성 변경

- `state` 속성을 변경할 때에는, `this.setState()` 메서드를 사용해야 하며, 일부분만 변경할 수 없고 아예 새로운 것으로 대체해줘야 한다.
- 이 속성이 변경되면, `render()` 메서드가 다시 호출된다. 

```jsx
componentDidMount() {
  setTimeout(() => {
    this.setState({
      movies: [
        ...this.state.movies,  // 아예 새로운 것으로 대체되므로 기존 것 붙여넣기
        {
          title: 'Borne Identity',
          poster: 'https://m.media-amazon.com/images/M/MV5BM2JkNGU0ZGMtZjVjNS00NjgyLWEyOWYtZmRmZGQyN2IxZjA2XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg',
        }
      ]
    })
  }, 3000);
}
```

## 초기 렌더링에 데이터가 없는 경우

초기 렌더링에 데이터가 항상 있는 것이 아니다. API 서버에서 정보를 받아오는데는 시간이 걸릴 수 있다. 이 경우는 어떻게 처리하는 것이 좋을까. 

#### 1. `componentDidMount()` 에 데이터를 가져오는 로직

- 데이터를 가져오는 로직을 모방하기 위해 `setTimeout()` 함수를 사용하였다.
- 가져온 데이터를 `state` 에 넣어준다.

```jsx
componentDidMount() {
  setTimeout(() => {
    this.setState({
      movies: [
        {
          title: 'Inception',
          poster: 'https://cdn.shopify.com/s/files/1/1416/8662/products/inception_2010_french_original_film_art_spo_2000x.jpg?v=1543425422',
        },

        {
          title: 'Transcendence',
          poster: 'https://i.pinimg.com/originals/42/56/6d/42566daff7cfe843d51780e73802a83c.jpg',
        },

        {
          title: 'Interstellar',
          poster: 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',
        },

        {
          title: 'Catch me if you can',
          poster: 'https://cdn.shopify.com/s/files/1/1416/8662/products/catch_me_if_you_can_2002_original_film_art_spo_2000x.jpg?v=1543418719',
        },
        {
          title: 'Borne Identity',
          poster: 'https://m.media-amazon.com/images/M/MV5BM2JkNGU0ZGMtZjVjNS00NjgyLWEyOWYtZmRmZGQyN2IxZjA2XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg',
        },
      ]
    })
  }, 3000);
}
```

#### 2. `state` 에 데이터가 있을 때, 그 데이터를 가공한 컴포넌트를 반환하는 함수

```jsx
// 언더스코어는 리액트 내부 함수와의 구별을 위한 것이다.
_renderMovies = () => {
  return this.state.movies.map((movie, index) => {
    return <Movie title={movie.title} poster={movie.poster} key={index}/>
  });
};
```

#### 3. `render()` 에서 `state` 에 데이터가 있는지 검사하는 로직

```jsx
render() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Hello, <br/>Daniel Kim.
        </h1>
        {this.state.movies ? this._renderMovies() : 'Loading...'}
      </header>
    </div>
  );
}
```

## Stateless Functional Component

모든 컴포넌트가 `state`가 필요한 것은 아니다. `componentWillMount()` 같은 메서드도 필요 없을 수 있다. 단순히 몇개의 `props` 를 받아서 리턴만 해주는 컴포넌트라면, 함수로 선언하면 된다.

유의할 점은 다음과 같다:

- 인자는 `{}` 로 묶어준다.
- `propTypes` 설정은 함수 밖에서 프로퍼티를 입력하는 식으로 해준다.

##### class component (smart component)
```jsx
class Movie extends Component {
  static propTypes = {
    title: PropTypes.string.isRequired,
    poster: PropTypes.string.isRequired,
  };  // prop type 을 지정

  render() {
    return (
      <div>
        <MoviePoster poster={this.props.poster}/>
        <p>{this.props.title}</p>
      </div>
    )
  }
}

class MoviePoster extends Component {
  static propTypes = {
    poster: PropTypes.string.isRequired,
  };

  render() {
    return (
      <img className="poster" src={this.props.poster} alt="inception poster"/>
    )
  }
}
```

##### functional component (dumb component)
```jsx
function Movie({title, poster}) {
  return (
    <div>
      <MoviePoster poster={poster}/>
      <p>{title}</p>
    </div>
  );
}

function MoviePoster({poster}) {
  return (
    <img className="poster" src={poster} alt="Movie Poster"/>
  );
}

Movie.propTypes = {
  title: PropTypes.string.isRequired,
  poster: PropTypes.string.isRequired,
};

MoviePoster.propTypes = {
  poster: PropTypes.string.isRequired,
};
```





# Ajax 기능 구현하기

#### Ajax 란
- Asynchronous Javascript and XML
- 원래는 비동기 자바스크립트 XMLHttpRequest 를 사용하는 부분적 html 변경 방식을 일컬었으나, 
- 현재는 전체 페이지 새로고침 없이 데이터를 받아와 페이지 일부만을 변경하는 기법을 통칭

## fetch
- 리액트에서는 서버에서 데이터를 받아오는 과정을 `fetch` 메서드로 간단하게 해결할 수 있다.
- `fetch` 메서드는 promise 객체를 반환한다. 따라서 `then`, `catch` 메서드를 사용할 수 있다.

> https://yts.am/api/v2/list_movies.json?sort_by=rating

```jsx
componentDidMount() {
  fetch('https://yts.am/api/v2/list_movies.json?sort_by=like_count')
    .then(response => response.json())
    .then(jsonData => console.log(jsonData))
    .catch(err => console.log(err))
}
```

## `async`, `await`

- 콜백 헬에서 빠져나오기 위한 기능이다. 
- `awync` 는 비동기 함수를 만들어주고, 그 안에서 `await` 은 특정 비동기 함수가 끝날 때까지 기다렸다가 값을 받아온다.
- `await` 는 `async` 함수 안에서만 사용할 수 있다.

### 비동기 처리 분해하기
비동기 처리는 복잡하면 콜백헬에 빠진다. 아래의 코드는 다음과 같은 로직을 지닌다:

1. `_callApi()`: Api json data 를 받아온다
- `_getMovies()`: `_callApi()` 가 넘겨주는 데이터를 `state` 에 저장한다
- `componentDidMount()`: `_getMovies()` 를 호출한다

```jsx
class App extends Component {

  state = {};
  
  // 요녀석은 가벼운 것이 좋다. 많은 일을 해야 하기 때문에. 그래서 함수를 쪼갰다.
  componentDidMount() {
    this._getMovies();
  }

  async _getMovies() {  // async 비동기 함수
    const movies = await this._callApi();  // await: 비동기 함수의 종료를 기다린다. 성공 여부는 상관없다.
    this.setState({movies})  // movies: movies 가 된다.
  }

  _callApi = () => {
    return fetch('https://yts.am/api/v2/list_movies.json?sort_by=like_count')  // 반환해줘야 한다.
      .then(response => response.json())
      .then(jsonData => jsonData.data.movies)  // 요 값을 반환
      .catch(err => console.log(err))
  };

  _renderMovies = () => {
    return this.state.movies.map(movie => {
      // movie 객체를 내가 만든 것이 아니므로, Api json data 형태를 잘 보고 사용해줘야 한다.
      // key 로 영화의 id 값을 사용할 수 있다. 인덱스를 사용하는 것 보다 빠르다고? 한다
      return <Movie title={movie.title} poster={movie.medium_cover_image} key={movie.id}/>
    });
  };

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>
            Hello, <br/>Daniel Kim.
          </h1>
          {this.state.movies ? this._renderMovies() : 'Loading...'}
        </header>
      </div>
    );
  }
}
```