
const myfetch = (url,data) =>{
    const postOptions={
        method:'POST',
            headers:{
                'Content-Type':'application/json',
                'Accept':'Application/json'
            },
            body:JSON.stringify({data})
        }

    var result = fetch(url,postOptions)
            .then(res=>res.json())
    return result
}

function postLogin(){
    
    const user=document.getElementById("user").value
    const pass=document.getElementById("pass").value
    data={user:user,pass:pass}
    console.log(data)
    const url= 'http://localhost:8000/login/'
    myfetch(url,data)
        .then(res=>{
            console.log(res)
            if (res=='Success login'){
                //alert('You have successfully logged into your account')
                window.localStorage.setItem('username',user)
                window.location.href='mainPage.html'
                
            }else if (res=='Wrong username or password'){
                alert('You have the wrong username or password')
                
            }
        })
   
}