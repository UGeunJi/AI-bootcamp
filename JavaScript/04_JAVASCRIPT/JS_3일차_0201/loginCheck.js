// const id = 'user';
// let pw = '1234';

const user = {
    id : 'user',
    pw : '1234'
}

        //  기본적으로 js 코드는 html 파일의 가장 아랫단에 씁니다
        var inputId = prompt('id를 입력하세요')
        var inputPw = prompt('pw를 입력하세요') 

        if (inputId === id && inputPw === pw) {
            document.write(inputId+'님, 로그인 되셨습니다!')
        } else {
            document.write('id나 비밀번호를 다시 입력하세요')
        }
       
        // 못해서 안하는 게 아니라 보안, 사용자 관점 때문에 아래와 같은 방식은 사용하지 않습니다.
        // id가 틀렸습니다. 비밀번호가 틀렸습니다. id와 비밀번호가 틀렸습니다. 중첩조건문으로 만들어보세요. 
        // 보통은 2-3개까지 안으로 들어가는 중첩조건문은 어쩔 수 없이 사용합니다
        // 중첩조건문은 헷갈리기 때문에 권장하지 않습니다. 
        // if (inputId === id) {
        //     if  (inputPw === pw) {
        //         document.write(inputId+'님, 로그인 되셨습니다!')
        //     } else {
        //         document.write('비밀번호가 틀렸습니다!')
        //     }
        // } else {
        //     if (inputPw === pw) {
        //         document.write('id가 틀렸습니다. id를 다시 입력하세요')
        //     } else {
        //         document.write('id와 비밀번호가 틀렸습니다')
        //     }
        // }

        // if (inputId === user.id && inputPw === user.pw) {
        //         document.write(inputId+'님, 로그인 되셨습니다!')
        // } else if (inputId === user.id && inputPw !== user.pw)  {
        //         document.write('비밀번호가 틀렸습니다!')
        // } else if (inputId !== user.id && inputPw === user.pw) {
        //         document.write('id가 틀렸습니다. id를 다시 입력하세요')
        // } else {
        //         document.write('id와 비밀번호가 틀렸습니다')
        // }