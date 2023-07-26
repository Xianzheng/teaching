

// var initValue = 1

// function add(value){
//     /*
//         implement adding method    
//     */
//    console.log('value is',value, typeof value)
//    initValue += value
// }

// function minus(value){
//     /*
//         implement minus method    
//     */
// }
// argument for function must be a string
// add("1")
// console.log(initValue) // it shoud  be 2

// add("1.2")
// console.log(initValue) // it shoud  be 3.2

// minus("1")
// console.log(initValue)

// parseInt("1") //convert string type to int type

// console.log(parseInt("1.2")+ parseInt("1.2"))
// console.log(parseFloat("1.2")+ parseFloat("1.2"))

// console.log(1.2 + 1.2)

var initValue = 1

function addOne(value){
    // console.log('value is ',value,' type is ',typeof value)
    // passed argument value is string, if we want to add 1 we need to convert string to integer
    value = parseFloat(value)
    initValue += value;
}

function minusOne(value){
    // console.log('value is ',value,' type is ',typeof value)
    // passed argument value is string, if we want to minus 1 we need to convert string to integer
    value = parseFloat(value)
    initValue -= value;
}
addOne('1')
addOne('1')
addOne('1')
for (let i=0; i<5;i++)
    addOne("1")
console.log(initValue)
minusOne('1')
minusOne('1')
minusOne('1')
minusOne('1')
minusOne('1')
for (let i=0; i<10;i++)
    minusOne("1")
console.log(initValue)

function addTwoArg(arg1,arg2){
    arg1 = parseFloat(arg1)
    arg2 = parseFloat(arg2)
    return arg1 + arg2
}

console.log(addTwoArg(1,45))

//why we need to understand string converting stuff