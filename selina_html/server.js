
//load express library to create server
const express = require("express")
// load cors can let our front end and backend get communication
var cors = require("cors")
 
//using express library as app
const app = express(); //run server
app.use(cors())
app.use(express.json())
//3000 is port which will be listening for this program
app.listen(3000,()=>{ //pot thing
  console.log('server running at port 3000')
})
// / is also an endpoint
// / is a endpoint backend get request from front end
// res.send is backend send message to frontend
app.get('/',(req,res) =>{
  res.send('server is running')
})

app.get('/sayHello/',(req,res) => {
  var parm = req.query
  console.log(req.query)
  res.send('Hello '+parm.name)
})

//if we are using brower input bar to send request, we use method get
app.get('/howAreYou/',(req,res) =>{
  res.send('I am good')
})

app.post('/dealLogin/',express.json(),(req,res) => {
  console.log(req.body)
  const fakeDb = [
    {uid:'a@a.com',pwd:'a12345'},
    {uid:'b@b.com',pwd:'s56789'},
    {uid:'c@c.com',pwd:'aaa123'}
  ]

  //javascript call [] as an array
  //javascript call [] as an class/json data
  console.log(req.body)
  console.log('I GET REQUEST')
  // res.send({msg:'I get post request'})
  // console.log(fakeDb[2].uid,fakeDb[2].pwd)

  // how to loop the data structure
  let check = 0
  for(let i = 0; i < fakeDb.length; i++){
    if (req.body.uid == fakeDb[i].uid && req.body.pwd == fakeDb[i].pwd){
      check = 1
    }
    // console.log(req.body)
    // console.log(fakeDb[i])
  }
  if (check == 0){
    res.send({msg:'fail'})
  }else{
    res.send({msg:'success'})
  }
})
/*

1. set up signup function
(make sure we are in sign up page, click submit we can get alert)

2.make sure we can get alert about email address, password info, confirm password

3. transfor info to backend, at least show in our terminal
*/