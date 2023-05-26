//hw1. draw htl layout

//hw2
const mes = [
    {"username":"a","content":"AAAAAA","title":"A","_id":"KjVJTwxCFLMq6L8u"},
    {"username":"a","content":"BBBB","title":"B","_id":"tmcdHNtuLQG5hD71"}
]

// console.log(mes)

// mes.forEach((element,index) =>{
//     console.log(element.username,element.content,element.title)
// })

//JSON IS USED FOR transfer data, {key1:value1,key2:value2}

const json1 = {suit:'SUIT',number:3}

const json2 = {name: 'JingXue',testScore:100}

console.log(json1.suit,json1.number)

const array = []

array.push(json1)

array.push(json2)

array.forEach(element => {
    console.log(element)
})