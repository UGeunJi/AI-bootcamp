// 10. 객체

// 10-1. 자바스크립트 내장객체
// 숫자 관련 메소드

var num = 10;
var num1 = 1.113;
var num2 = 1.756;
var str = '가나다라';

// Math 
// - 수학에서 자주 사용하는 상수와 함수들을 미리 구현해 놓은 
//   자바스크립트 표준 내장 객체
// - Math 객체는 다른 전역 객체와는 달리 생성자(constructor)가 존재하지 않음
// - 따로 인스턴스를 생성하지 않아도 Math 객체의 
//   모든 메소드나 프로퍼티를 바로 사용할 수 있음

// Math.ceil (올림)
// Math.floor (내림)
// Math.round (반올림)
// 소수점 이하를 반올림 할 때는 num2.toFixed(자리수) 라는 함수를 사용합니다 
// 소수점 이하 자리수를 모두 균일하게 맞춰야 하면 num2.toFixed(자리수) 를 사용할 수 있습니다
// Math.ceil(str); // Not a Number -> if 자료형 구분하지 않아도 
// isNaN(str) // true 
// isNaN(num2) // false
var num3 = NaN // "number" 자료형으로 관리됨
var liter = '14.6L'
parseInt(liter) // 14
parseFloat(liter) // 14.6
var liter2 = '14.67.5.3L'
parseInt(111.3, 2) // 다른 기수법을 적용할 수도 있습니다. 2의 2승 + 2의 1승 + 2의 0승 = 7
Math.random() // 0과 1 사이의 임의의 숫자를 골라서 우리에게 출력해줍니다
parseInt(Math.random()*10)   
parseInt(Math.random()*100 + 1) // 1~100 사이의 임의의 숫자
Math.sign(num2) // 양수이면 1, 0이면 0, 음수이면 -1을 출력합니다. 자료형 "number"를 유지하기 위해서
var num5 = -1234.1111
Math.abs(-1.3245) // 절대값
Math.PI // 3.14~~~~~~~
Math.max(1,3,4,5,6) // 최대값
Math.min(1,3,4,5,6) // 최소값

var array = [1,2,3,4,5,6,111]
Math.max(...array) // 111
Math.max(array) // NaN
Math.pow(2, 3) // 거듭제곱 2**3과 같음
Math.sqrt(16) // 4 // root를 의미합니다

// 실습. 로또번호 뽑기 - ramdom()을 사용하여 1~46 사이의 6개의 양의 정수를 뽑고 가장 큰 수, 가장 작은수를 출력하세요.

// 1개만 만들고 거기서 무엇을 반복할지 고민해보시면 됩니다 

// 기왕이면 함수로 동작을 묶는 훈련을 해 주세요
function lottery() {
// 빈 배열을 만든다
 var lotto = []
 // 6번 반복: 값을 하나씩 추가한다
 for (var i = 0; i < 6;){
   var result = Math.round(Math.random() * 45 + 1) 
   if (!lotto.includes(result)) {   // 겹치는 번호가 있는지 확인
     lotto.push(result)   // 겹치지 않으면 lotto에 넣음
     i++;
   } 
}
  // max, min 출력
  console.log(Math.max(...lotto))
  console.log(Math.min(...lotto))
  return lotto
}

// str, 배열에서 자주 사용되는 내장함수들
var sentence = 'This is my dog. My dog is 17 years old.'

// my라는 단어가 들어있는지 찾겠습니다 
sentence.indexOf('my') // 있으면 해당 단어가 시작되는 인덱스 번호
sentence.indexOf('mine') // 없으면 -1 

sentence.indexOf('is') // true가 되는 첫번째 자리수를 출력 

sentence.lastIndexOf('is') // true가 되는 마지막 자리수를 출력

if (sentence.lastIndexOf('This') > -1) // this의 인덱스 번호가 0이라서 false -> 아래 내용 출력 안 됨 -> -1보다 큰 조건식으로 변경 
{
  // console.log('right sentence')
}
sentence.slice(2) // 해당 인덱스부터 나머지 전부를 가져옵니다

sentence.slice(2, 5) // 시작인덱스, 끝인덱스 

sentence.slice(2, -5) // 시작인덱스, 끝인덱스(음수인덱싱)

// str.substring(m,n) : m과 n 사이 
sentence.substring(2, 10)
// sentence.split(): 파라미터 자리에 무엇으로 split 할 지 적어주셔야 동작합니다 
sentence.split()
'   hi hello   welcome    '.split(' ')
'   hi hello   welcome    '.split(' ', 5) // ' ' 구분자(seperator)로 분리된 인덱스에서 n개만 쓸게요  
'   hi hello   welcome    '.trim() // 앞뒤 공백만 제거 

'   hi hello   welcome    '.repeat(4) // 해당 문자열을 4회 반복

// 실습. exceptBerry(str) 이라는 함수를 만들어주세요  
exceptBerry('딸기주스 주세요') // 품절입니다 
// 딸기가 들어있지 않은 모든 주문은 '기다리세요' 출력, 
// '딸기'라는 단어가 어디에든 들어있으면 '품절입니다'를 출력하는 함수를 만들어주세요 


function exceptBerry(str) {
    // 딸기가 들어있는지 확인 
         // 있으면 - 품절입니다
    if (str.indexOf('딸기') > -1) { // 인덱스 번호를 출력
      console.log('품절입니다')
    } else { // 없으면 - 기다리세요 
      console.log('기다리세요. 제조해드릴게요.')
    }   
  }
  
  function exceptBerry1(str) {
    // 딸기가 들어있는지 확인 
         // 있으면 - 품절입니다
    if (str.includes('딸기')) { // true/false로 출력
      console.log('품절입니다')
      console.log(str.includes('딸기'))
    } else { // 없으면 - 기다리세요 
      console.log('기다리세요. 제조해드릴게요.')
    }   
  }
  
  // 업종을 딸기전문점으로 변경 - 딸기가 들어있는 음료만 제조하겠습니다
  // 메뉴판 array가 있어야 할 것
  // 그 메뉴판 array에 포함되지만 딸기 외의 것들을 탐색
  // if ~ 로직이 필요 
  menu = ['딸기주스', '포도주스', '포도딸기에이드'] // 메뉴를 보면 딸기가 들어있는 경우 앞의 2글자에 딸기 있음

  function exceptBerry2(str) {
    // 딸기가 들어있는지 확인 
         // 없으면 - 품절입니다
    if (!str.includes('딸기')) {
      console.log('품절입니다')
      console.log(str.includes('딸기'))
    } else {   // 있으면 - 기다리세요
      console.log('기다리세요. 제조해드릴게요.')
    }   
  }
  
  
  function exceptBerry3(str) {
    // 딸기만 들어있는지 확인 
         // 있으면 - 기다리세요
    if (str.indexOf('딸기') > -1) {
      console.log('기다리세요. 제조해드릴게요.')
    } else { // 없으면 - 품절입니다 
      console.log('품절입니다')
    }   
  }
  
  function exceptBerry4(str) {
    // 딸기만 들어있는지 확인 
         // 있으면 - 기다리세요
    if (str.slice(0, 2) == '딸기') {
      console.log('기다리세요. 제조해드릴게요.')
    } else { // 없으면 - 품절입니다 
      console.log('품절입니다')
    }   
  }

  
/* 고급! 조건부 연산자 '물음표(question mark) 연산자’라고도 불리는 
'조건부(conditional) 연산자’를 사용하면 
if-else문을 더 짧고 간결하게 변형할 수 있습니다.
피연산자가 세 개이기 때문에 조건부 연산자를 
'삼항(ternary) 연산자’라고 부르는 사람도 있습니다. 
참고로, 자바스크립트에서 피연산자가 3개나 받는 연산자는 
조건부 연산자가 유일합니다.

let result = condition ? value1 : value2;
평가 대상인 condition이 truthy라면 value1이, 
그렇지 않으면 value2가 반환됩니다.
*/ 
  
  // 삼항연산자 (명제) ? 참 : 거짓 
function exceptBerry5(str) {
// 딸기만 들어있는지 확인 
        // 있으면 - 기다리세요
(str.slice(0, 2) == '딸기') ?
    console.log('기다리세요. 제조해드릴게요.') : console.log('품절입니다')   
}

var age = 10
age > 18 ? '맞습니다' : '틀립니다';

// ? 뒤를 안 써줘도 true, false로 반환됩니다.

var age = 20
age > 18;

let accessAllowed = age > 18;
accessAllowed

// 다중 ?
let message = (age < 3) ? '우쭈쭈?' :
  (age < 18) ? '어린이 안녕!' :
  (age < 100) ? '환영합니다!' :
  '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';

console.log( message );

// 1. age를 prompt로 입력 받습니다.
var age = 18

// 2. age가 18보다 작으면 '미성년자', 18보다 크거나 같으면 '어른' 이라고 출력합니다.
// (삼항연산자로 구현)
var message = (age < 18) ? '미성년자' : '어른'
console.log(message)

// // 3. 중첩 if문으로 풀어서 확인해보세요. 다중 조건 아니고 중첩 조건이더라구요.
var age = 18
let message = (age < 3) ? '우쭈쭈?' :
  (age < 18) ? '어린이 안녕!' :
  (age < 100) ? '환영합니다!' :
  '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';

  // 삼항연산자의 다중조건 
var message; 
if (age < 3) {
  message = '우쭈쭈?'
} else {
  if (age < 18)
    { message = '어린이 안녕!' 
    } else {
      if (age < 100) {
        message = '환영합니다!'
      } else {
        message = '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';
      }
    }
}
console.log(message);

// 이거 아니라 위에꺼가 삼항연산자의 다중조건문입니다.
if (age < 3) { message = '우쭈쭈?'
   } else if (age < 18) {
     message = '어린이 안녕!'
   } else if (age < 100) {
     message = '환영합니다!'
    } else {
      message = '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';
    }

// 배열(Array)
'hello'.slice(2,2) // m에서 n까지 쓰겠다 
var arr1 = ['one', 'two', 'three', 'four', 'five'] // arr1.slice(1, 3) 1에서 3까지 쓰겠다 
var arr2 = ['six', 'seven']
var arr3 = arr1.concat(arr2) // arr1에 arr2를 더하겠다 
// 참조자료형 자료구조는 웬만한 메소드들이 원본을 변경(파괴)하지 않는 방식으로 구현되어 있습니다 -> 메모리를 아끼기 위해서 

// forEach - 순서대로 값을 꺼낼 수 있는 자료형에서만 사용됩니다. 
arr3.forEach((num) => {console.log(num)})  // 값만 꺼내옴
arr3.forEach((num, i) => {console.log(num, i)}) // 값, 인덱스 번호를 함께 꺼내옴 

// 배열(Array) - String과 겹치거나 비슷한 방식으로 구현된 메서드 많음
'hello'.slice(2,2) // m에서 n까지 쓰겠다 
var arr1 = ['one', 'two', 'three', 'four', 'five'] // arr1.slice(1, 3) 1에서 3까지 쓰겠다 
var arr2 = ['six', 'seven']
var arr3 = arr1.concat(arr2) // arr1에 arr2를 더하겠다 
// 참조자료형 자료구조는 웬만한 메소드들이 원본을 변경(파괴)하지 않는 방식으로 구현되어 있습니다 -> 메모리를 아끼기 위해서 

// forEach - 순서대로 값을 꺼낼 수 있는 자료형에서만 사용됩니다. 
// arr3.forEach((num) => {console.log(num)})  // 값만 꺼내옴
// arr3.forEach((num, i) => {console.log(num, i)}) // 값, 인덱스 번호를 함께 꺼내옴 

// arr3.forEach((num, i) => {console.log(i+1, num)}) // 값, 인덱스 번호를 함께 꺼내옴 

arr3.find((item) => {  // three
  return item == 'three'
})

arr3.findIndex((item) => { // 2
  return item == 'three';  
})

arr3.findIndex((item) => { // 없으니까 -1을 출력
  return item == 'eight';
})

// arr3에 5글자짜리 글자가 있는지 확인하고 있으면 그 글자를 출력하고, 없으면 아무것도 출력되지 않게 해주세요
var arr3 =  ["one","two","three","four","five","six","seven"]

// arr3에 5글자짜리 글자가 있는지 확인하고 있으면 그 글자를 출력하고, 없으면 아무것도 출력되지 않게 해주세요
arr3.find((item) => {
  if (item.length ===5) {
    return item
  } 
})

arr3.findIndex((item) => {
  if (item.length===5) {
    console.log(item)
  }
})

// filter: 만족하는 모든 요소를 배열로 반환 -> 결과만 보여줌 
arr3.filter( (item) => {
   return (item.length % 5) === 0;
})

// 역순으로 재정렬 -> 원본도 변경됨 
arr3.reverse()

// map : 함수를 받아서 t/f로 결과를 판단해서 배열로 출력 -> 해당 결과만 우리에게 보여줌 
var arr4 = arr3.map( (item) => {
   return (item.length % 5) === 0;
})

/* reduce()
- 인수로 함수를 받음
(누적 계산값, 현재값) => { return 계산값 };
*/ 

arr = [1,2,3,4,5];

// price 50원씩 올려서 새 배열 over50 에 담아주세요 
// productInfo[0].price += 50 
var productInfo = [
    {name: '사과', price: 900},
    {name: '딸기', price: 1000},
    {name: '포도', price: 2000}
    ]
    
var over50 = JSON.parse(JSON.stringify(productInfo)) // 깊은복사 
over50.map((item) => { item.price += 50}) 

// 1000원이 넘는 금액을 가진 배열만 over1000 라는 새 배열에 담아주세요 
// function hello(item) 
//     {if (item.price > 1000) return item}

hello = (item) =>
    {if (item.price > 1000) return item}
// 함수 안에서 함수를 실행하는(부르는) 구조: 콜백(Callback) 함수 
var over1000 = over50.filter(hello)

// 자바스크립트의 정렬 관련된 함수는 원본을 변경합니다(destructive)  

// fruit.sort()
var fruit = ['orange', 'apple', 'banana'];
var score = [4, 11, 2, 10, 3, 1]; // 아스키코드로 정렬하기 때문에  [1,10,11,2,3,4]

// 그래서 나름의 index 정렬 콜백함수를 넣어줍니다 - 오름차순 정렬
score.sort(function(a, b){return a - b})

// 내림차순 정렬 
score.sort(function(a, b){return b - a})

var student = [
    { name : "재석", age : 21},
    { name : "광희", age : 25},
    { name : "형돈", age : 13},
    { name : "명수", age : 44}
]

// 이름순 ㄱ~ㅎ 정렬
student.sort(function(a, b){
    return a.name < b.name ? -1 : a.name > b.name ? 1 : 0; 
})

// 나이순 0~100 정렬
student.sort(function(a, b){
    return a.age < b.age ? -1 : a.age > b.age ? 1 : 0; 
})

// reduce - 팩맨을 생각하세요
var arr6 = [1,2,3,4,5]

var after = arr6.reduce((previous, current) => {
    return previous * current
}, 3) // 3 : 초기값 (안 넣으면 0), 꼭 넣어야 하는 경우도 일부 있음

// 모든 사람들 나이의 합을 구해보세요
resultReduce = student.reduce((prev, cur) => {
return (prev += cur.age);
}, 0);

console.log(resultReduce);

//나이가 25살보다 크거나 같은 사람 이름만 출력해보시고요 (다른 변수에 집어넣어보세요) 
var resultReduce = student.reduce((prev, cur) => {
if (cur.age >= 25) {
    prev.push(cur.name);
}
return prev;
}, []); // 초기값으로 빈 리스트를 넣음

console.log(resultReduce);


// Date - 자바스크립트의 날짜, 시간 표현 내장 객체
var now = new Date();	// 현재 날짜 및 시간
console.log("현재 : ", now);
// new Date(year, month, date, hours, minutes, seconds, ms)
// new Date(2011, 0, 1, 0, 0, 0, 0); // 2011년 1월 1일, 00시 00분 00초
new Date("2020-10-23") // 원하는 날짜의 Date 객체

var now = new Date();	// 현재 날짜 및 시간
var year = now.getFullYear();	// 연도
console.log("연도 : ", year);

var month = now.getMonth();	// 월  0: 1월, 11: 12월
console.log("월 : ", month);

var date = now.getDate();	// 일
console.log("일 : ", date);

var day = now.getDay();	// 요일
console.log("요일 : ", day); // 0~6 사이의 숫자 일요일 0 ~ 토요일 6

var hours = now.getHours();	// 시간 : 0~24 
console.log("시간 : ", hours);

var minutes = now.getMinutes();	// 분
console.log("분 : ", minutes);

var seconds = now.getSeconds();	// 초
console.log("초 : ", seconds);

// 자동고침
let date = new Date(2013, 0, 32); // 2013년 1월 32일은 없습니다.
alert(date); // 2013년 2월 1일이 출력됩니다.

let today = new Date();

today.setHours(0);
alert(today); // 날짜는 변경되지 않고 시만 0으로 변경됩니다.

today.setHours(0, 0, 0, 0);
alert(today); // 날짜는 변경되지 않고 시, 분, 초가 모두 변경됩니다(00시 00분 00초).