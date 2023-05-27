
function loginClick(){
    alert('welcome login')
    const email = document.getElementById('loginEmail').value
    const password = document.getElementById('loginPassword').value
    alert('email is '+email)
    alert('password is '+password)
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

    const url = 'http://127.0.0.1:3000/dealLogin/'

    fetch(url,option)

    .then(res => res.json())

    .then(res => {

        console.log(res)

    })
}