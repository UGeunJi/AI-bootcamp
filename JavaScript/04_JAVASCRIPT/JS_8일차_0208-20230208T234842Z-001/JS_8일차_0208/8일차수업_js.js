// Date - 자바스크립트의 날짜, 시간 표현 내장 객체
var now = new Date();	// 현재 날짜 및 시간
console.log("현재 : ", now);
// new Date(year, month, date, hours, minutes, seconds, ms)
// new Date(2011, 0, 1, 0, 0, 0, 0); // 2011년 1월 1일, 00시 00분 00초
new Date("2020-10-23") // 원하는 날짜의 Date 객체

var now = new Date();	// 현재 날짜 및 시간

// 그러나 연/월/일/시/요일 등으로 분리해서 가져올 때는 0부터 시작하는 배열들이 있음.
var year = now.getFullYear();	// 연도
console.log("연도 : ", year);

var month = now.getMonth();	// 월  0: 1월, 11: 12월 이라서 +1해서 가져와야 함
console.log("월 : ", month);

var date = now.getDate();	// 일
console.log("일 : ", date);

var day = now.getDay();	// 요일
console.log("요일 : ", day); // 0~6 사이의 숫자 일요일 0 ~ 토요일 6 // 별도의 [일,월,화,수,목,금,토] 배열 만들어서 인덱스번호로 사용하거나 switch 문으로 변경해야 함

var hours = now.getHours();	// 시간 : 0~24 - 오전/오후 구분하는 조건문
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

// 10_clock.html, 11_clock_eventListener.html 참조

// 💡 비동기 : 페이지 변경 없이 그 상태에서 변화가 일어난다.

// - 입력이 지속되는 중에 응답도 지속된다.
// - 검색창에 글자가 바뀔 때마다 자동 완성이 실시간으로 바뀌는 것
// - 예시: setTimeout / clearTimeout, setInterval/clearInterval

// 일정 시간이 아니라 서버와의 통신 등 성공/실패 여부를 지금 당장 알 수 없는 비동기 함수를 구현한다면?
// Ajax(XMLHttpRequest ), Promise, async-await 등으로 구현

// 가. Ajax
// 12_ajax.html 참조

// 나. Promise 
// 일을 하는 Producer 객체, 그 객체를 사용하는 Consumer 부분으로 나뉨

// 1. Producer
// 새로운 프로미스가 만들어지면 우리가 전달한 executor라는 콜백함수가 바로 동작 시작된다. 그러므로 promise 안에는 꼭 필요한 것을 요청할 것
const promise = new Promise((resolve, reject) => {
    // promise 안에서는 시간이 꽤 걸리는 heavy한 일들을 합니다 (네트워크 통신, 파일 읽기 등)
    console.log('일하는 중...');
    setTimeout(() => {         
        // resolve('성공');       
        reject(new Error('네트워크 에러')); // 에러는 디테일하게 써주셔야 합니다 
    }, 2000);
});  

// 2. Consumer : then, catch, finally 통해서 값을 받아옵니다
promise
.then((value) => { // then : 성공시 - value는 resolve에서 전달한 값이 들어와서 promise가 return 됨
    console.log(value); // reject시 promise.js:18 Uncaught (in promise) Error: no network -> then으로 resolve 케이스만 제시해서
})
.catch(error => { // catch : 실패시 - promise 안에서 에러가 발생하면 여기로 전달됨
    console.log(error); // Error: no network
})
.finally(() => { // finally : 성공시나 실패시 무조건 실행됨
    console.log('finally');
});

// 3. Promise chaining
const fetchNumber = new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
    });

    // then은 값을 바로 전달해도 되고, 프로미스를 전달하기도 한다
fetchNumber
.then(num => num * 2) // 2
.then(num => num * 3) // 6
.then(num => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(num -1), 1000); // 5
        // 총 걸리는 시간은? 2초
    });
})
.then(num => console.log(num));


// 다. async-await