
var num=0
console.log('username is', window.localStorage.getItem('username'))
var uniqueuser=window.localStorage.getItem('username')

function automatic(){
    document.getElementById('userbtn1').innerText=uniqueuser;
    data={username:uniqueuser}
    const options={
        method:'POST',
            headers:{
            'Content-Type':'application/json',
            'Accept':'Application/json'
            },
            body:JSON.stringify(data)
    }
    const url= 'http://localhost:8000/getProfile/'
    fetch(url,options)
        .then(res=>res.json())
        .then(res=>{
            console.log(res)
            
            const na='Name: '+res.name+''
            const n='Nicname: '+res.nick+''
            const o='Occupation: '+res.occ+''
            const a='Address: '+res.add+''
            const h='Hobby: '+res.hobb+''
            document.getElementById("user").innerText=na
            document.getElementById("nick").innerText=n
            document.getElementById("occ").innerText=o
            document.getElementById("add").innerText=a
            document.getElementById("hob").innerText=h
    })  

    const title=document.getElementById('bloginp').value
    const content=document.getElementById('bloginp1').value
    console.log(title)
    console.log(content)
    data2={title:title,content:content}
    const option2={
        method:'POST',
            headers:{
            'Content-Type':'application/json',
            'Accept':'Application/json'
            },
            body:JSON.stringify('')
        }
    const url2= 'http://localhost:8000/getBlog/'
    const ele=document.getElementById('showBlogs')
    fetch(url2,option2)
        .then(res=>res.json())
        .then(res=>{
        console.log(res)
            res.forEach(element => {
                console.log(element)
                const h=document.createElement('a')
                h.innerHTML=element[1]
                h.setAttribute('href','blogdata.html?id='+element[0])

                //h.setAttribute('style','display: block')
                h.setAttribute('class','setclass')
                ele.append(h)
            //homework: create class that allows the blog to move right instead of going down. in styles.css tip:use display block to make it go right instead of down(not sure)
            });
            
         })

//<a href='blogdata.html'/<id>></a>    

}

window.onload= automatic

function logout(){
    window.localStorage.removeItem('username')
    window.location.href='login.html'
}
function makeshow(){
    
    num+=1
    console.log('Show')
    const userDiv1=document.getElementById('userDiv1');
    userDiv1.setAttribute('class','')
    console.log(num/2)
    if (num%2 == 0){
        document.getElementById('userbtn1').innerHTML=uniqueuser
        const userDiv2=document.getElementById('userDiv1');
    userDiv2.setAttribute('class','div1')
    }else{
        document.getElementById('userbtn1').innerHTML='Hide'
    }
    const userDiv2=document.getElementById('userDiv2');
    userDiv2.setAttribute('class','div1')
    
  
const options={
    
    method:'POST',
        headers:{
        'Content-Type':'application/json',
        'Accept':'Application/json'
         },
        body:JSON.stringify({data})
}
data={'a':1}
const url= 'http://localhost:8000/profile/'
    fetch(url,options)
        .then(res=>res.json())
        .then(res=>{
            console.log(res)
            
})



    }
var num2=0
function openchangepassword(){
    window.location.href="changepassword.html"
}

function profile(){
    const user=uniqueuser
    const name=document.getElementById("userinp").value
    const nick=document.getElementById("nickinp").value
    const occupation=document.getElementById("occinp").value
    const address=document.getElementById("addrinp").value
    const hobby=document.getElementById("hobinp").value
    
    const na='Name: '+name+''
    const n='Nicname: '+nick+''
    const o='Occupation: '+occupation+''
    const a='Address: '+address+''
    const h='Hobby: '+hobby+''
    console.log(user,nick,occupation,address,hobby)
    document.getElementById("user").innerText=na
    document.getElementById("nick").innerText=n
    document.getElementById("occ").innerText=o
    document.getElementById("add").innerText=a
    document.getElementById("hob").innerText=h
    //unique user will relplace user and then add a name which will ne the inp
    data={user:user,name:name,nick:nick,occupation:occupation,address:address,hobby:hobby}
    const options={
        method:'POST',
            headers:{
            'Content-Type':'application/json',
            'Accept':'Application/json'
            },
            body:JSON.stringify({data})
    }
    const url= 'http://localhost:8000/profile/'
    fetch(url,options)
        .then(res=>res.json())
        .then(res=>{
            console.log(res)
            

    })
}

//homework: change button user at top right to the username name logged in, same thing for the username in the div after clicking user, the one with the occupation.
//homework: build another table(database) named UserInfo, store user information, user: sadfdasf, nickname: asdfsadf, occupation : asdfasdf, address: asdfasdf, hobby: asdf (asdf=input). In mainpage.
//after it is clicked it stores to the database and the information div in mainpage changes. use create and update for db
var num3=0
function showblog(){
    num3+=1
    if (num3%2==0){
        const userDiv3=document.getElementById('add1');
        userDiv3.setAttribute('class','div1')
    }else{
        const userDiv3=document.getElementById('add1');
        userDiv3.setAttribute('class','')
    }
}
function getblog(){
    const title=document.getElementById('bloginp').value
    const content=document.getElementById('bloginp1').value
    console.log(title)
    console.log(content)
    data={title:title,content:content}
    const options={
        method:'POST',
            headers:{
            'Content-Type':'application/json',
            'Accept':'Application/json'
            },
            body:JSON.stringify(data)
    }
    const url= 'http://localhost:8000/blogData/'
    fetch(url,options)
        .then(res=>res.json())
        .then(res=>{
            console.log(res)
            

    })
}
//homework:make the blog appear after submit using backend like the previous problem about the occupation,name thing.cconnect to backend create new page once a former bblbog is clicked(will be a and former blbog are shown when u make a blog)
//new page name is blog detail.
//homework is just to make the blog appear in mainpage after you submit it and move the blog to the right if there is too much. Also after add bbutton is clicked we change name to hide
//


//homework 2022/12/08:
//use style to make the blog appear to the right of another blog and make it so that once a blog title is clicked it will appear on the screen