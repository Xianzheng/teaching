console.log('hello')
//
//signUpInputPassword1
//signUpConfirmPassword1signupSubmit()
function isCapital(string){
    if(string >= 'A' && string <= 'Z'){
        return true
    }else{
        return false
    }
}

function isSmall(string){
    if(string >= 'a' && string <= 'z'){
        return true
    }else{
        return false
    }
}

function isValidPass(string){
    var small = false;
    var capital = false
    var array = string.split('')
    for (let i=0;i<array.length;i++){
        if (isSmall(array[i]) == true){
            small = true
        }
        if (isCapital(array[i]) == true){
            capital = true
        }
    }

    // console.log(small)
     
    if (small == true && capital == true && string.length >= 8){
        return true
    }else{
        return false
    }
}

// console.log(isValidPass("aA123456"))

function isValidEmail(string){
    var emailPat = /^(.+)@(.+)$/
    var matchArray = string.match(emailPat)
    // if matchArray is not empty do something
     if (matchArray){
        return true
    }else{
        return false
    }
}

// console.log(isValidEmail("mark@gmail.com"))
//string.length


function signupSubmit(){

    const signupEmail = document.getElementById("signUpEmail").value

    const signupPass = document.getElementById("signUpInputPassword1").value

    const signupConfirmPass = document.getElementById("signUpConfirmPassword1").value


    console.log(signupEmail)

    if(signupPass === signupConfirmPass){

        if (isValidEmail(signupEmail) == true && isValidPass(signupPass) == true) {
            alert('success')//connect to backend, store email, password to database
            
            const options = {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                  accept: "application/json"
                },
                body: JSON.stringify({
                  email: signupEmail,
                  password: signupPass
                })
              };
              const url = "http://localhost:3000/signupInfo";
              fetch(url, options)
                .then((res) => res.json())
                .then((res) => {
                  if (res.msg == "add success") {
                    alert("add info success");
                  } else {
                    alert("add info failed");
                  }
                });
        
    }else{
       alert('password and confirmed password does not match')
    }
}

    // password must contain at lest one small lettet and one  capital letter,
    // and the length of password can not smaller than 8



    
    console.log(signupPass)
    console.log(signupConfirmPass)
}
/*
homework:
# consider and write how to do signup and login in detail
# html -> js -> server
# how to get user input
# invoke js function when html button was clicked
# js fetch to server endpoint
*/