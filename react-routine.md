#### 설치 후 `eject`
- `npx create-react-app app-name`
- `npm run eject`
- `npm install`

#### 테스트 파일 삭제
- `testing file`, `jest file`, `package.json` 의 `script | test`, `jest` 삭제

#### Sass 와 CSS 모듈, camelCase 설정
- `npm install --save-dev node-sass`
- `config/webpack.config.js` 에서 `cssModuleRegex`, `sassModuleRegex` 검색, 그 밑에 `use` 부분에 `camelCase: true` 입력

```jsx
use: getStyleLoaders(
  {
    importLoaders: 2,
    sourceMap: isEnvProduction && shouldUseSourceMap,
    modules: true,
    camelCase: true,
    getLocalIdent: getCSSModuleLocalIdent,
  },
  'sass-loader'
),
```

#### Sass 상수 파일 기본 로드 설정
- `config/webpack.config.js`

```jsx
  // common function to get style loaders
  const getStyleLoaders = (cssOptions, preProcessor) => {
    const loaders = [
		...
    ].filter(Boolean);
    if (preProcessor) {
      loaders.push(
        preProcessor  // 요기 변경
        // {
        //   loader: require.resolve(preProcessor),
        //   options: {
        //     sourceMap: isEnvProduction && shouldUseSourceMap,
        //   },
        // }
      );
    }
    return loaders;
  };
  
  ...

  // Opt-in support for SASS (using .scss or .sass extensions).
  // By default we support SASS Modules with the
  // extensions .module.scss or .module.sass
  {
    test: sassRegex,
    exclude: sassModuleRegex,
    use: getStyleLoaders(
      {
        importLoaders: 2,
        sourceMap: isEnvProduction && shouldUseSourceMap,
      },
      // preProcessor 부분 변경
      // 원래는 'sass-loader' 뿐이었음
      {
        loader: require.resolve('sass-loader'),
        options: {
          data: `@import "${paths.appSrc}/config/variables";`,
          sourceMap: isEnvProduction && shouldUseSourceMap,
        }
      },
    ),
    // Don't consider CSS imports dead code even if the
    // containing package claims to have no side effects.
    // Remove this when webpack adds a warning or an error for this.
    // See https://github.com/webpack/webpack/issues/6571
    sideEffects: true,
  },
```

#### jsx emmet 설정
`.vscode` 의 `settings.json` 을 다음과 같이 오버라이드. `preference | settings`

```js
"files.associations": {
    "*.js": "javascriptreact",
},
```

#### node path 설정

프로젝트 폴더 바로 아래에 `.env` 파일 안에 `NODE_PATH=src` 작성. 이제 자바스크립트 모듈을 임포트할 때, `import App from component/App` 하면, `project_dir/src/component/App/index.js` 를 가져온다.

#### reset css 설정
> import 할 때 물결 표시가 필요한 이유: https://github.com/webpack-contrib/sass-loader#imports


- `npm install reset-css`
- `@import '~reset-css/reset.css';` 을 최상위 index 스타일이나 app 스타일에서 임포트


#### `.eslintrc.js` 설정

```jsx
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
                "SwitchCase": 1,
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