var num = 0
function makeshow(){
    
    num+=1
    console.log('Show')
    const userDiv1=document.getElementById('userDiv1');
    userDiv1.setAttribute('class','')
    console.log(num/2)
    if (num%2 == 0){
        document.getElementById('userbtn1').innerHTML='User'
        const userDiv2=document.getElementById('userDiv1');
    userDiv2.setAttribute('class','div1')
    }else{
        document.getElementById('userbtn1').innerHTML='Hide'
    }
    
    

}