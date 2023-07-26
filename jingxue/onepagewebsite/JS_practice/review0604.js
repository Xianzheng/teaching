obj = { a : 1,  b : 2,   c : 3,    d :  4} // {} object, []array, 1 => obj['a']
//     k1  v1  k2  v2   k3  v3    k4   v4
var list = Object.keys(obj)


console.log(obj['a'])

console.log(list) //list ['a','b','c','d'] -> array
//                         0   1   2   3

// for (let i = 1; i <= 20; i+=2) {
//     console.log(i)
//   }


//print all even number between 1-20
list.forEach((element,index) => {

    console.log(obj[element])
})

//fs read dir folder

const fs = require('fs')

var lst1 = fs.readdirSync('img_list')
console.log(lst1)
