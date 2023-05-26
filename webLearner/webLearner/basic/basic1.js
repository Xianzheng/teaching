// console.log('Hello World')// control + shift + ~

// scope is not same
const name = 'Mark'// static variable, if we define this variable, variable can not be changed
/*
var name1 = 'Kevin'// global variable

name1 = 'Justin'

let name2 = 'Selina'// functional variable
name2 = 'Jingxue'
console.log(name2)



function fun1(arg1){
    console.log(arg1)
    
    
    let name1 = 'Fenghua'
    
}

for(let i = 1; i <= 10 ; i++){
    console.log(i)
}

fun1('Kevin')

*/
//[] list in python, append, insert
//[] array in JS, push

var array = []

array.push('apple')
array.push('banana')
array.push('pear')
array.push('1')
array.push('2')
array.push('3')

//, map
array.forEach((item,index) => {
    console.log(item,index)
})// forEach is run a loop in array
console.log(array)

/*
homework:
talk some and test, const, let, and var

create a array, add '5','6','7','10','8' 
list all element of array
revolve array three times
'5','6','7','10','8' 
'8','5','6','7','10',
'10','8','5','6','7',
'7','10','8','5','6',

*/
array.map((item,index) =>{
    return (item,index)

})

array.filter((item,index) =>{
    if(item === 1){

    }else{
        
    }
})

