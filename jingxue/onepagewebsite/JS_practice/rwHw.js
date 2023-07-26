
const fs = require('fs')
/*
//it will print binary content
// var content = fs.readFileSync('temp1.txt')

var content = fs.readFileSync('temp1.txt','utf-8')

console.log(content)

key_DIC = {'a':'r','e':'l','i':'p','o':'s','u':'t'}
//          key value
key = Object.keys(key_DIC)

value = Object.values(key_DIC)

console.log(key)

console.log(value)

for(let i = 0; i < 5; i++){
    content = content.replaceAll(key[i],value[i])

}

fs.writeFileSync('temp2.txt',content)
*/

var content2 = fs.readFileSync('temp2.txt','utf-8')

key_DIC = {'a':'r','e':'l','i':'p','o':'s','u':'t'}

// change hllls klvpn, sllpnr, jpngxtl to hello kevin, selina, jingxue
// write in temp3.txt
console.log(content2)
keylst = Object.keys(key_DIC)

valuelst  = Object.values(key_DIC)

for(let i = 0; i < 5 ; i++){
    content2 = content2.replaceAll(valuelst[i],keylst[i])
}

console.log(content2)
