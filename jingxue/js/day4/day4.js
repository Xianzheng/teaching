/*
// "Mark", "Selina", "jingxue", "Kevin"
var array = ["Mark", "Selina", "jingxue", "Kevin"]
//             0        1         2          3
// console.log(array.length)

for( var i = 0; i < array.length ; i++){

    console.log(array[i])

}

// anonymous function

var a = () => {
    console.log("Hello World")
}

(item,index) => {
    console.log(item)
}


function a(){
    console.log("Hello World")
}


// invoke this anonymous function

array.map((item,index) => {
        console.log(item,index)
    }
)//callback function

*/

var mark = {name:"Mark",age:28,job:"programmer"} //class


console.log(mark.name,mark.age,mark.job)

var Jingxue = {name:"Jingxue", age:13, job:"student"}
console.log(Jingxue.name, Jingxue.age, Jingxue.job);

var Selina = {name:"Selina", age:11, job:"student"}

var classContainer = [] // [{mark...},{jingxue..}]

classContainer.push(mark)
classContainer.push(Jingxue)
classContainer.push(Selina)

// classContainer.map((item,index)=>{
//     console.log(item.age)
// })

classContainer.map((item,index) => {
    var p = document.createElement("P");
    p.innerHTML = 'name: &nbsp &nbsp &nbsp' + item.name 
    + '&nbsp &nbsp &nbsp page: &nbsp &nbsp &nbsp ' + item.age
    + '&nbsp &nbsp &nbsp job:&nbsp &nbsp &nbsp ' + item.job
    document.body.appendChild(p);

})

// create array ,

// push 5 times class to array 

//the content of class depends on you

// render data to html


