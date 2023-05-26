//创建基本的web服务器，使用express lib
const express = require('express')

var cors = require('cors')
const app = express()
app.use(cors())
app.listen(3000,() => {
    console.log('express server running at localhost/127.0.0.1')
})
//app.get有两个参数
//请求我们的url地址
//服务器给出的一个反应
app.get('/hello/',(req,res) =>{
    console.log('hello')
    res.send({mes:'hello'})
})

//使用浏览器url bar输入都算get请求
//请求会有get/post/delete/update
//post info runs in back, not in front
app.post('/post1/',(req,res) =>{
    console.log('we get post request')
    res.send({mes:'we get post request'})
})

/*
 homework:

 http:// 192.168.51.23:50/hello/

 告诉我这段话内包含了哪些信息

 尝试自己做一个服务器，练习今天这节课的内容

//  当前端页面登录按钮被按下，服务器会说登录按钮被点击
//  当前端页面注册按钮被按下，服务器会说注册按钮被点击
*/