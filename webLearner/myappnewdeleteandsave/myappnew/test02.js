var test = require('./test01')

var array1 = [1,2,3,4,5,6,7]

console.log(test.getsmallest(array1))

console.log(test.options)

// if you want to use require then you don't need to do package.json
// if you want to use import then you have to do package.json

//useing two way to import(require, import)), write function which will be used in aother file, function file named tools.js impliment file named test.js
//1 .  var string = 'abcdefg' -> 'gfedcba'

//2.  test a string is a palindrome 'abcba' is a palindrome,'abc' is not a palindrom, 
//if it is return ture， else return false