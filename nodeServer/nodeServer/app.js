//1.导入express
const express = require('express')
//2.创建 web服务器
const app = express()
var cors = require('cors')

var NeDB = require('nedb')

app.use(cors())
var db = new NeDB({
    filename: './user.db',
    autoload: true,
})


//3.调用app.listen(端口，启动成功后的回调函数)  ， 启动服务器
app.listen(50,()=>{
   console.log('express server running at http://127.0.0.1')
})

app.get('/hello/',(req,res)=>{
    db.find({
        name: 'Alice',
    }, function(err, docs) {
        res.send(docs)
    })

    
})

app.post('/hello1/',(req,res) =>{

    res.send({mes:'请求成功'})
    
})