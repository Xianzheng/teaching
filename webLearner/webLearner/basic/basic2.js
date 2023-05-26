// object (looks lick dictionary in python)

obj1 = {
 name : 'Mark', Object:'GYM',TestScore: 90   
}

obj2 ={
    name: 'Kevin',Object:'Book',TestScore:99
}

obj3 ={
    name: 'Justin',Object:'Pencil',TestScore:85
}
obj4 ={
    name: 'Selina',Object:'paper',TestScore:92
} //json data


var array=[]
array.push(obj1)
array.push(obj2)
array.push(obj3)
array.push(obj4)

// if TestScore is bigger than 93 we print out obj 

//React use JSx

array.forEach((item,)=>{
    if(item.TestScore >=93){
       return <h1>item.TestScore</h1>
    }
})

array.filter((item) =>{
    if(item.TestScore >=93){
        return <h1>item.TestScore</h1>
    }
})

//connect frontend and back end 
//use JS to do frontend, we use python to do backend

//JS, JS Framework is ReactJs
//PYTHON, PYTHON Framework is Django
// HTML JS CSS

// build a django, build react
// home work , review what we did