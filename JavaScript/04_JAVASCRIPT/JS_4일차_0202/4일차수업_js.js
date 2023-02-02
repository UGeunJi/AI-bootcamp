// 실습2. "이미지 주소를 리스트에 넣으시고 
// 몇개 보실래요? 물어본 다음에 1개만, 2개만, 3개만 등 입력한 개수만큼만 이미지를 보여주는 화면을 만들어 보세요"
// 5_imageList.html 참고

/* 8. 함수(return 문)
- 변수에 데이터는 저장할 수 있지만, 코드는 저장할 수 없습니다. 
- 함수를 사용하면 코드를 메모리에 저장해서 필요할 때마다 호출해 
  사용할 수 있습니다.
- 자바스크립트는 'function' 키워드로 함수를 선언합니다.
- 함수는 이름과 함수 내용을 가지고 있습니다.
- 함수를 호출하는 방법은 함수의 이름을 사용하여 호출합니다.
- return문의 역할 : 결과값을 반환할 때 사용합니다. 
       결과를 반환하며 break문과 비슷하게 코드가 강제로 종료됩니다.

1) function func(param) {
  함수가 실행될 때 실행문
}

2) 익명함수(파이썬의 람다와 유사): (param) => {
  함수가 실행될 때 실행문 
}
 let func = (param) => {
  함수가 실행될 때 실행문 
}

func()
    
*/
// hello 라는 이름을 가진 콘솔에 hello javascript를 찍는 함수를 만들어 볼게요
// 1) input(매개변수(가변인자), 파라미터)도 output(return)도 없는 함수
function hello() {
    console.log('hello javascript');
  }
  
// 2) input은 있고 output(return)은 없는 함수
function hello1(param) {
console.log('hello ' + param);
}

// 3) input은 없고 output은 있는 함수 
function hello2() {
console.log('hello javascript');
return 'javascript';
}

// 4) input도 있고, output도 있는 함수
function hello3(param) {
console.log('hello' + param);
return 'hello ' + param + ' returned'
}

var ret


// calculatePrice라는 함수를 만들어주시는데요 
// 10불을 먹으면 10%는 세금, 15%는 팁이 붙어서 결과가 리턴되는 
function calculatePrice(total, tax=0.1, tip=0.15){
    return total * (1+tax+tip)
}

// calculatePrice1 으로 화살표함수(arrow function)로 변경해보세요
var calculatePrice1 = (total, tax=0.1, tip=0.15) => {return total * (1+tax+tip, 0)}
// 10 + 3 + 1.5 -> 14.5

calculatePrice1(10, undefined, 0.3) // 특정 파라미터는 디폴트값으로 사용하고 싶으면 그 자리를 undefiend로 남겨두세요

// tax는 기본값으로 두고 tip만 변경하고 싶을 때는 해당 파라메터의 자리를 undefined로 넣어주셔야 동작합니다.
console.log(calculatePrice(10, undefined, 0.5))

// undefined 없이 디폴트 파라메터를 변경해서 넣고 싶을 때는 함수에 아래처럼 인자를 줍니다
function calculatePrice({total=0, tax=0.1, tip=0.05} = {}) {
    return total + (total * tax) + (total * tip);
}  

console.log(calculatePrice({total:10, tip:0.5}))

var names = ['짱구', '짱아', '훈이']

function hello(arr){
  return `${arr}님 안녕하세요!`  // 백틱 `${변수명}` - 템플릿 리터럴: 파이썬의 f-string과 같은 역할
}

function hello(arr){
    for (var i=0; i < arr.length; i++){
      return `${arr[i]}님 안녕하세요!`
      console.log('이거 리턴 다음에 있는 문구입니다')  
      // 영영 실행되지 않을 실행문이 되어버립니다
    }
  };
  
  var names = ['짱구', '짱아', '훈이']
  
  // 자바스크립트 언어 자체가 갖고 있는 숨은 매개변수 arguments: 
  // 함수에 매개변수를 따로 선언하지 않더라도 arguments라는 숨은 매개변수가 값을 받아냅니다. 
  function hello(){  // 매개변수 선언 안 했는데
     for (var i=0; i < arguments.length; i++){ // arguments는 어디서 나온 것인가?
      console.log(`${arguments[i]}님 안녕하세요!`)
    }
  };
  
  hello(names)
  hello('짱구', '짱아')

// 실습. 6_function.html을 만들고 
// 버튼을 클릭할 때마다 배경 색깔이 변하는 함수를 만들어 동작시켜 주세요

// 6_function.html 참고

// Document Object Tree -> 12일차 수업 자료 및 7_DOM.html 참고