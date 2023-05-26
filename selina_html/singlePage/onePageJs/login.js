function loginClick(){
    const email = document.getElementById('loginEmail').value
    const password = document.getElementById('loginPassword').value
    
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