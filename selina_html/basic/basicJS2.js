/*
var array = [1,2,3,4]//each item os array is number type
// index     0 1 2 3 4 5
//  array = [ '1', '2', '3', '4' ]//each item os array is number type

//function, callback function, arrow function
array.forEach((item, index) =>{
    console.log(item, index)
})
*/

// array is important
// allmost stuff shows in Screen is a sreen, 
//if we want do calculation we need to use array
//if we want do communicate with backend we also need to use array

//some code can get context of screen

context = '1.2+2.5+3.3+4.6'
var array1 = context.split('+')
var sum = 0;
array1.forEach(item =>{
    // since item is a string
    // if we want to math adding 
    // we need to convert string to number int(integer), float, boolean
    //item = parseInt(item)// convert string to integer
    item = parseFloat(item)// convert string to float
    sum += item
})
console.log(sum)

// concept about type: string, int(integer), float, true:1/false:0(boolean)

//hw
var initValue = 1

function add(value){
    /*
        implement adding method    
    */
   initValue += value
}

function minus(value){
    /*
        implement minus method    
    */
}
// argument for function must be a string
add("1")
console.log(initValue) // it shoud  be 2

add("1.2")
console.log(initValue) // it shoud  be 3.2

minus("1")
console.log(initValue)

//hint: better reference parseFloat
