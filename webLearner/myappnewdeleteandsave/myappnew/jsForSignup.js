import myfetch from './jsForLogin.js'
function signup(){
    const newuser=document.getElementById("newuser").value
    const newpass=document.getElementById("newpass").value
    const confirmpass=document.getElementById("passconfirm").value
    const data={newuser:newuser,newpass:newpass}
    console.log("^(?=.*[a-z])")
    lnewpass=newpass.length
    lnewuser=newuser.length
    var upper=0
    var lower=0
    var userupper=0
    
    for (var i = 0; i<lnewpass; i++){
        if (newpass[i]===newpass[i].toUpperCase()){
            upper++
        }else if (newpass[i]===newpass[i].toLowerCase()){
            lower++
        }
    }
    console.log(upper,lower)
    // const options={
    //     method:'POST',
    //         headers:{
    //             'Content-Type':'application/json',
    //             'Accept':'Application/json'
    //         },
    //         body:JSON.stringify({data})
    //     }
    if (lnewuser>=5){
    if (newpass == confirmpass){
        if(upper>=1){
            if(lower>=1){
                if (lnewpass>=8){
                    
                    console.log(url,data)
                    const url='http://localhost:8000/signUp/'
                    myfetch(url)
                    .then(res=>{
                        console.log(res)
                        if (res=='success'){
                            alert('You have successfully created a account')
                        }
                        else{
                            alert('Someone already has the same username that you placed')
                        }
                        
                
                
                
                    
        })}else{
            alert('Your password is not 8 characters')
        }   
    }   else{
                alert('You need at least a lowercase for your password')
        }

    }   else{
        alert('You need at least a uppercase for your password')
    }

    }else {
        alert('Not the same password')
    }
    
}else{
    alert('Your username is not 5 characters')
}

    
    
    
    
}