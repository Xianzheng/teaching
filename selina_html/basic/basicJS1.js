//About Array

var array = [1,2,3,4,5,6,7,8,9,10]
//  index    0 1 2 3 4 5 6 7 8 9         
// question: get the sum of array 's content

// 1. how to get array's content, example we just want to print 7
// index always from 1, step is add by 1, array[index]
// we can use index to access the content 
//  console.log(array[6])
// node name.js will run js file


// 2 . how to print all the index and content of array
// print all the index
// for(let index = 0; index < array.length; index++){

//     console.log('index is ',index)
//     console.log('content is ',array[index])
//     // print content

// }

// 3. how to the sum of of array 's content
// addResult = 0 
// addResult += 1
// addResult += 2
// addResult += 3
// ....
// addResult += 10
// addResult + 1 + 2 + 3 + ... + 10
// addResult = 0

// for(let index = 0; index < array.length; index++){

//     addResult += array[index]
//     // print content

// }
// console.log(addResult)

// final version, using array function
// get all even number in this array
// result = 0
array.forEach((item,index) => {
    // console.log(item)
    // console.log(index)
    // result += item
    if (item % 2 == 0){
        console.log(item)
    }
})
// we will talk string convert next class
// suppose we screen show 2 + 2, 4 + 10

var string = '2+2'
let array1 = string.split('+')
addResult = 0
array1.forEach((item,index)=>{
    addResult += parseInt(item)
})
console.log(addResult)

// console.log(string.split('+'))

/*
    var array = [1,2,3,4,5,6,7,8,9,10]

    // print first 10 nature numbers of array
    // print first 5 even numbers of array
    // print first 5 odd numbers of array
    // get the sum of first 5 even numbers of array
    // get result of 1 * 2 * 3 ... * 10

    // * choose using array function or normal way
*/

