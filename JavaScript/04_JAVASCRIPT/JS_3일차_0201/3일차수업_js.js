//6. 조건문
// 파이썬에서는
  // if 명제 () else ()
  // if 명제 () elif 명제 () else ()

// 자바스크립트에서는
// if (명제) { 명제가 참일 때 실행문 };
 
// if (명제) { 
//   명제가 참이 때 실행문 
// } else {
//   명제가 거짓일 때 실행문 
// };

// if (명제1) {
//  명제 1이 참일 때 실행문 
// } else if (명제2) {
// 명제2가 참일 때 실행문
// } else { 
//  명제 1과 명제2 모두 거짓일 때 실행문
// };


var a = '3'; 
// 1. if~else 기본형
//    a 가 3보다 크거나 같으면 콘솔에 3인 경우에는 3임 이라고 콘솔에 출력되도록 조건문을 변경해주세요

if (a >= 3) {
  console.log('3과 같거나 3보다 큼')
} else {
  console.log('3보다 작음')
};

// 2. if ~ else if ~ else 기본형
// a 가 3보다 크면 콘솔에 3, 3이면 3임, 3보다 작으면 3보다 작음이라고 콘솔에 출력되도록 조건문을 변경해주세요
if (a > 3) {
  console.log('3보다 큼')
} else if ( a === 3) {
  console.log('3임')
} else {
  console.log('3보다 작음')
};

// 3. 활용 - 다중조건 (a && b), 중첩조건(if 안에 if)
// 문자로 들어온 경우에는 '숫자 자료형이 아니라 값을 비교할 수 없습니다'까지 출력되도록 조건문을 변경해주세요
// typeof a == 'number'

// 1) 중첩 조건문으로 구현(조건문 안에 조건문)
// if (자료형 확인) {
//   if ~ else if ~ else }
if (typeof a == 'number') {
  if (a > 3) {
    console.log('3보다 큼')
  } else if (a == 3) {
    console.log('3임')
  } else if (a < 3) {
    console.log('3보다 작음')
  };
} else {
  console.log('숫자 자료형이 아니라서 값을 비교할 수 없습니다.')
};

// 2) 다중 조건문으로 구현 (여러개의 조건을 하나의 명제에서 판별)
// if (자료형 확인 && 값 확인) {
// } else if (자료형 확인 && 값 확인) {
// } else {
// }
var a = 5; 

if (typeof a == 'number' && a > 3) {
  console.log('3보다 큼')
} else if (a === 3) {
  console.log('3임')
} else if ( typeof a == 'number' && a < 3) {
  console.log('3보다 작음')
} else {
  console.log('숫자 자료형이 아니라서 값을 비교할 수 없습니다.')
};

// 실습. prompt 창을 활용하여 숫자로 값을 입력받고 양수, 0, 음수를 판별하는 조건문을 만들어보세요.
// var num = Number(prompt())
var num = 3;

// 양수일 때
if (num > 0) {
  console.log('양수입니다')
  // 0일때
} else if ( num == 0 ) {
  console.log('0입니다')
  // 음수일 때 
// } else if (num < 0) { // 또는
} else { 
  console.log('음수입니다')
};

/* 자바스크립트의 조건문
- switch문 : 
  조건에 따라 그 값과 일치하는 표현식을 가진 case 문으로 실행의 흐름을 옮겨 다른 코드를 실행하는 문법입니다.
  기본 구조는 아래와 같습니다.

switch (명제) { // if (명제):
  case 값1:    // 결과가 1일 경우
    실행문;
    break;
  case 값2:    // 결과가 2일 경우
    실행문; 
    break;
  default:     // else 
    실행문
    };
 */
// default문은 맨 마지막에 있어야 합니다. 맨 마지막에 있으므로 break는 생략합니다.

// break문이 없는 경우는 swith-case문의 각 case문이 끝나면 
// 바로 다음 case문이 실행되어 제대로 실행결과가 나오지 않습니다. 
// break문은 코드 블록에서 탈출하는 역할을 합니다.


// 사용자한테 값을 입력받는데 1, 2, 3일 때만 one, two, three를 출력하고 다른 숫자를 입력받으면 '몰라요'를 출력하는 switch문 
var num = 1;
switch (num) {
  case 1:    // 결과가 1일 경우
    console.log('one')
    break;
  case 2:    // 결과가 2일 경우
    console.log('two')
    break;
  case 3:    // 결과가 3일 경우
    console.log('three')   
    break;
  default:     // else 
    console.log('모르는 숫자입니다.')
}

/* switch문을 사용하는 이유: 
1) 자료형 일치를 === 연산자 없이도 적용 가능, 
2) '딱 그 조건'에 부합할 때를 편하게 작성 가능 */ 
// Number 타입의 정수 1, 2, 3이 들어오면 '압니다' 출력하는 switch문, 
// if 문으로 만든다면 &&과 ===을 많이 써야 가능.
var num = 3;
switch (num) {
  case 1: case 2: case 3:
    console.log('압니다')   
    break;
  default:     // else 
    console.log('모르는 숫자입니다.')
}

// 정수인 거는 무시하고 3보다 작거나 같은 경우 압니다, 3보다 큰 경우 모릅니다를 출력하는 if문을 만들어보세요. 
// 
var num = 2
if (num <= 3) {
  console.log('압니다')
} else {
  console.log('모릅니다') 
}


// 1일때 one 2일때 two, 3일때 three, 나머지는 모릅니다를 출력하는 if문을 만들어보시고, -> switch문으로 바꿔보세요. 
var num = 1
// if, 비교연산자는 기왕이면 자료형까지 비교하는 완전항등연산자(===)를 손에 익히시기를 권장합니다.
if (num === 1) {
  console.log('one')
} else if (num === 2) {
  console.log('two')
} else if (num === 3) {
  console.log('three')
} else {
  console.log('모릅니다')
}

switch (num) {
  case 1:  // '1'과 1이 자료형이 다르므로 다르다고 인식하기 때문 
    console.log('one')
    break;
  case 2:
    console.log('two')
    break;
  case 3:
    console.log('three')
    break;
  default:
    console.log('모릅니다') // default문을 맨 위에 쓸 수도 있습니다
}

// 실습.
// login.html을 만들고 loginCheck.js 파일을 연동해주세요
// 1. id: user, pw:1234 라는 변수가 들어있습니다
// 2. login.html 파일을 열면 prompt 창이 2개가 뜹니다. id를 입력하세요 -> pw를 입력하세요 
// document.write()
// 2개가 다 맞으면 '로그인 되셨습니다.' 라고 login.html에 출력이 될거에요. 
// 둘중에 하나라도 틀리면 'id나 비밀번호를 다시 입력하세요'라고 화면에 출력이 될거에요.  

// loginCheck.js + 3_login.html 참조

/* 7. 반복문
- for, while, for each
- 반복문도 조건문처럼 for (명제)가 만족하는 동안 반복 실행되는 코드를 말합니다.
for (변수 선언문 및 초기값; 조건; 증감) {
 조건식이 참인 경우 반복 실행될 문;
 문2;
 문3;
}
*/

for (var i=1; i < 11; i++) {
  console.log(i)
}
// 변수 선언 자체는 밖에서 해도 괜찮습니다
var i;
for (i=1; i < 11; i++) {
  console.log(i)
}

// 조건식은 정해진 숫자가 아니어도 됩니다.
var str = prompt("지금 입력받은 글자수만큼 반복 부탁드려요")
var i;
for (i=0; i < str.length ; i++) {
  console.log(str[i])
}

// 반복문 안에 반복문을 넣어서 사용하는 것도 가능합니다 (중첩반복문)  
// -> 반복이 너무 깊어지면 복잡해집니다. 
// 이중 혹은 삼중 반복문을 넘어서게 되면 보통은 flag 변수를 활용합니다. 
for (var i=0; i < 3 ; i++) {
  for(var j =1; j<4 ; j++){
    console.log(i, j)
  }
}

// 실습. 우리반 사람 모두에게 맛점하세요~ 를 출력해주세요
var names = ['강동엽', '고석주', '김건영', '남정우', '양효준', '이상훈', '이재영F', '전현준', '정제경', '주한솔', '지우근', '최세현', '이재영M'] 
for (var i=1; i<names.length ; i++) {
  console.log(i, names[i]+'님 맛점하세요!')
}

// 홀수번 사람에게만 점심인사
// break, continue는 파이썬과 동일한 방식으로 사용합니다
// 좋은 코드는 간결하고, 반복을 덜 하는(빠른) 코드입니다. 
// 1) 증감식 
// for (var i=1; i<names.length ;i = i + 2) {
for (var i=1; i<names.length ; i+=2) {
  console.log(i, names[i]+'님 맛점하세요!')
}

// 2) if문
for (var i=0; i<names.length ; i++) {
  if ((i % 2) !== 0)
    console.log(i, names[i]+'님 맛점하세요!')
}

// 3) if문 2
for (var i=0; i<names.length ; i++) {
  if ((i % 2) === 0) {
    continue;
  } else {
    console.log(i, names[i]+'님 맛점하세요!')
  }
}

// 집합자료형에서 반복문을 쓰는 경우는 너무 많기 때문에 
// 자바스크립트는 좀더 간결한 문법을 제공합니다.
// for in문은 인덱스가 기본출력

// for 변수 in 집합자료형: 변수에 키를 저장

//    for(변수선언 in 객체){
//    객체의 요소의 개수만큼 반복할 문장; ...
//    }
for (let i in names) {
  console.log(names[i], '님, 맛점하세요!')
}

// for 변수 of 집합자료형: for of는 변수에 값을 저장

// for(변수선언 of 객체){
// 객체의 요소의 개수만큼 반복할 문장; ...
// }
// name:  i는 iterable 혹은 index의 약자입니다.
// 숫자가 아닌 경우 객체의 단수명을 반복문의 공갈문자로 
// 써주시는 것이 좋은 코딩습관입니다.

for (let name of names) { 
    console.log(name, '님, 맛점하세요!')
}


/* while 조건문

형식:
  조건식을 좌우할 변수 선언 및 초깃값; 

  while (조건식) {
  조건을 만족하는 동안 반복될 실행문 
  조건을 끝낼 수 있는 실마리 
  }
*/
var i=1; 
while (i < 11) {
  console.log(i)
     i++;
}

// 무한루프를 조심하세요!
var i = 0;
while (true){
    console.log(i)
    i++;
    if (i === 10) break;
}

// 숫자를 하나씩 깎아나간다면 num = 0이 되는 순간 
// 명제가 false가 되어 반복문을 빠져나갈 수 있습니다.
var num = prompt('INPUT num');
while (num) {
  console.log(num);
  num--;
}

// do - while문 : 일단 한번은 true/false를 따지지 않고 실행하고, 그 다음부터 조건식을 평가하기 시작하는 구문입니다 
// do..while 문법을 사용하면 조건문을 
// 반복문 본문 아래로 옮길 수 있습니다.
// 사용 예시: 0초부터 시작하는 소리나 영상 데이터 
// -> 저장해야하는데 0은 false이므로 녹음을 시작할 수 없다면....
// 실행되기도 전에 멈추는 것을 방지하기 위해 do-while 문을 많이 사용합니다.

var i=1; 
do {
  console.log(i)
  i++;
} while (i < 11);


var num1 = 8
// var num2 = -1
// var num3 = 15

// if 안에 while
if (0 < num1 && num1 < 11){
  while (0 <num1){
    console.log(num1);
    num1--;
  }
} else {
  console.log(num1);
}

// do-while : 1회 무료체험 
do {
    console.log(num1);
    num1--;
} while (0 < num1 && num1 < 11)


var names = ['강동엽', '고석주', '김건영', '남정우', '양효준', '이상훈', '이재영F', '전현준', '정제경', '주한솔', '지우근', '최세현', '이재영M'] 

// for (초기값; 조건식; 증감식){
//   실행문
// }

for (var prop in names){
  console.log('index:', prop, 'value:', names[index])
}

for (var prop of names){  // index가 있는 Array, string 등 순서가 있는 객체에서만 사용 가능합니다
  console.log('value:', prop)
}



let mycar = {
  color : ['black', 'grey'],
  name : 'Cayenne',
  company : 'Porsche',
  speed : 250,
  domestic : false
};
// 인덱스가 없는데 어떻게 값을 호출해서 꺼내올 것인가??
// 순서가 없는 집합자료형에서는 for~in을 사용해서 값을 꺼내올 수 있습니다 
for (var prop in mycar){
  console.log('key:', prop, 'value:', mycar[prop])
}

// 반복문과 많이 사용되는 배열의 함수들 
a.includes('마') // false -> '전체요소'가 일치하는지를 검색하는 함수 
a.indexOf('마') // -1
a.indexOf('가') // 0
a.lastIndexOf('가') // 4
a.indexOf('파') // 찾는 값이 없으면 indexOf 함수는 -1을 출력합니다.

// a 배열에 있는 '가'를 모두 제거해주세요 

// '가'가 있는 인덱스번호를 조건으로 걸면 되겠다 
var index = a.indexOf('가') // 선언 및 초기값 
// -1이 아닌 경우에는 계속 반복하면서 값을 삭제하도록 
while (index > -1) {  // 조건 
   a.splice(index, 1)   // 실행문
  index = a.indexOf('가')        // 이 반복을 끝낼 실마리 
}
console.log(a)

// 실습.  사용자한테 몇개를 입력할 것인지 리스트의 개수를 입력받고, 입력된 항목수만큼 내용을 받아서 똑같은 형식으로 출력을 해볼게요 
// 4_list.html 참고

// 실습2. "이미지 주소를 리스트에 넣으시고 
// 몇개 보실래요? 물어본 다음에 1개만, 2개만, 3개만 등 입력한 개수만큼만 이미지를 보여주는 화면을 만들어 보세요"