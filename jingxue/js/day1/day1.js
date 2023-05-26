// public static void main(String []args){
//    System.out.println("Hello World")
//}

//console.log("Hello World");

//String str = new String("Hello");
//int i = 10;

// var str = "Hello World"
// var i = 10
// console.log(str)
// console.log(i)

//java is compiled language
//javac day1.java
//java day1

//javascript is a interpreted language
//node day1.js

// var i = 0

// while (i < 20){
//     i += 1
//     console.log(i)
// }
/*
for (var i = 0; i<10; i++){
    console.log(i)
}

var i = 0
console.log(typeof i)

var array = [0,1,2,3,4] // object
// index           3
console.log(array)
console.log(array[3])
console.log(typeof array)

var person = {name:'Mark',age:29,job:['programmer','teacher']}
console.log(person)
console.log(person.age)
console.log(person.job[1])
console.log(typeof person)
*/
console.log('Hello world')
function clickTest(){
    // console.log('button was clicked')
    document.getElementById('p')
    .innerText = 
    'button was clicked'
}

function checkAnswer1(){
    var userInp = document.getElementById('inp1').value
    console.log(userInp)
    var right = 5050
    if (userInp == right){
        document.getElementById('a1')
    .innerText = 
    'correct'
    } else {
        document.getElementById('a1')
        .innerText = 
        'incorrect'
    }
}