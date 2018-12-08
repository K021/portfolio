

# Javascript


## 기본

**출력하기**  
`alert('afds')`: 경고창에 띄워준다.  
`console.log(변수)`: 콘솔창에 띄워준다.  

**입력 받기**  
`prompt("string")`: 프롬프트 입력을 받아 출력해준다.  

**기타**  
`parseInt()`, `parseFloat()`:  각각 정수, 실수로 변환해준다. 둘 다 자료형은 `number`이다. `185.3 입니다`처럼 숫자로 시작하되, 뒤에 비숫자 문자열이 와도 능숙히 숫자만 분리해낸다. 그러나 `저는 키가 185.3 입니다`처럼 시작하는 값이 숫자가 아니라면, 숫자를 인식하지 못하고 `NaN`(Not a Number)를 출력한다. (`var a=1/0;`의 경우 `a`는 `Infinity`라는 값을 가진다.)  

`SyntaxError`: 문법 오류 에러  

**자료형**  
`Number`, `String`, `Boolean`와 함께 `Object`도 자료형이다   
`undefined`: 정의되지 않은 변수. 정의되지 않은 객체의 속성.  
`null`: 아무것도 없음을 나타내는 값으로, 자료형은 `object`이다.  

**Object**  
객체 자료형 정의: `var man = { name:"Martin", age:30 }`, `man.name` 또는 `man["age"]`로 접근할 수 있다.  
`Object.keys(obj)`: `obj`의 키로 이루어진 리스트를 반환한다.  


## 연산자

`a++`: `a`를 사용하고 1 증가  
`++a`: 1 증가하고 `a` 사용
`Math.pow(2, 3)`: `power`함수. 2의 3승.  
`Math.sqrt(4)`: `squear root`함수. 제곱근.  
`Math.random()`: `0-1` 사이의 난 수 생성  


`&&`: & 연산자, `||`: or 연산자  
연산자 순서: `not`, `산술`, `비교`, `and`, `or`  


## 함수

```javascript
// javascript에서 함수 정의하기
function 함수이름(파라미터1, 파라미터2){
    return 반환값;
}
```


## 문자열

문자열 길이: `'string'.length`, `'string'.['length']`  
문자열 연결: `'str'+'str'`, `str.concat(str).concat(str)`  
> : 꼭 문자열끼리 연결할 필요는 없다. 불리언도 되고, 숫자도, 심지어 객체도 된다. (concatenate: 사슬같이 연결하다) 연결된 문자열을 리턴할 뿐, 연결하는데 사용된 문자열을 바꾸지는 않는다.  
	
인덱스로 값 찾기  
`str.charAt(3)`: 스트링에서 인덱스가 3인 값 출력. 인덱스가 존재하는 범위를 넘어서면 `""` 빈 스트링을 반환한다.  
`str[3]`: 문자열에서 인덱스 3 출력. 인덱스가 존재하는 범위를 넘어서면 `undefined`  
`str.substring(2,4)`: 인덱스 2, 3 출력. `2 에서 4 전까지`  
`str.substr(2,4)`: 인덱스 2, 3, 4, 5 출력. `2 부터 4 개`  
`str.substr(-5,2)`: 맨 뒤에서 5번째 부터 오른쪽으로 2개. 왼쪽으로 갈 방법은 없다.  
`str.sunstring(2)`, `str.substr(2)`: 인덱스 2 부터 끝까지 출력.  

값으로 인덱스 찾기  
`str.indexOf("bc")`: 문자열 `"bc"`가 출현하는 첫 번째 인덱스를 반환한다.  
`str.lastIndexOf("bc")`: 문자열 `"bc"`가 출현하는 마지막 인덱스를 반환한다.  

문자열로 배열 만들기  
`str.split(",")`: 문자열을 구분자(`","`)로 나누어 배열을 만들어준다.  


## 배열

`arr.pop()`: 배열의 마지막 항을 뽑아오고 삭제.  
`arr.shift()`: 배열의 첫째 항을 뽑아오고 삭제.  
`arr.push(3)`: 배열 끝에 3 추가.  
`arr.unshift(3)`: 배열 앞에 3 추가.  

`arr.reverse()`: 배열을 뒤집고, 뒤집힌 배열을 리턴.  
`arr.sort()`: 순서대로 정렬, 리턴.   

`str.split(",")`: 문자열을 구분자(`","`)로 나누어 배열을 만들어준다.  

**문자열과 함께 사용되는 함수**  
`arr.length`, `arr.concat(arr)`, `arr.indexOf(3)`, `arr.lastIndexOf(3)`  
`.includes(value)`: 존재하는가. `in` 연산자로도 같은 것을 수행할 수 있다.   


## 주석

`//`, `/* */`: 한 줄 주석, 여러 줄 주석  


## 조건문

```javascript
if (조건식) {
	코드;
}
else if(조건식) {
	코드;
}
else {
	코드;
}
```  

```javascript
// break 가 없으면 조건이 부합되는 부분 이후의 모든 코드가 실행된다.
// 변수가 value2 인 경우, 해당 코드와 default 가 실행된다. 
switch (검사하려는 변수){
    case value1:
        // 변수 == value1 이면 실행
        break;
    case value2:
        // 변수 == value2 이면 실행
        break;
    default:
        // 변수 값이 어떤 케이스에도 해당되지 않는 경우 실행 
        break;
}

switch (var) {
	case 1, 2: // 맨 뒤의 2만 인식된다. 
}
```

## 반복문

```javascript
while (조건) {
}
```
```javascript
do{
	// 일단 한 번은 실행
}while(조건)
```
```javascript
for (초기화; 조건식; 변수 변화) {
}

for (var i in arr) {
	// i는 arr의 인덱스가 순서대로 반환된다. 0, 1, 2, ...
	// 문자열도 같은 방식
}
for (var i in obj) {
	// i는 obj의 속성이름(key) 값이 순서대로 반환된다. 
}
``` 