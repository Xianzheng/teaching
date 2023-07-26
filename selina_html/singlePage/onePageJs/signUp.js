function signUpButtonClicked(){
    
    let email = document.getElementById("signUpEmail").value

    let password = document.getElementById('signUpPassword').value

    // alert("typed email "+email)
    // alert("typed password "+password)

    const option = {

        method :'POST',

        headers: {

            "Content-type":'application/json',

            accept:'application/json',

        },

        body: JSON.stringify({

            uid: email,

            pwd: password,

        })

    }

    const url = 'http://127.0.0.1:3000/dealSignUp/'

    fetch(url,option)

    .then(res => res.json())

    .then(res => {
        console.log(res)

        alert(res.msg)

    })
}

/*
1.
for signup page
get user typed password and confirmed password

2.
fir login page
we need to get user type email, password

after finished send me code or picture

*/