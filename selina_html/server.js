
//load express library to create server
const express = require("express")
// load cors can let our front end and backend get communication
var cors = require("cors")
//load nedb to create databse(to store data)
var Nedb = require("nedb")
//using express library as app
const app = express(); //run server
app.use(cors())
app.use(express.json())

var signUpdb = new Nedb(
  {
    filename: 'signup.db',
    autoload: true,
  }
)

app.get('/addData/',(req,res) =>{
  signUpdb.insert({uid:'Selina',pwd:123})
  signUpdb.insert({uid:'Mark',pwd:123})
  signUpdb.insert({uid:'Kevin',pwd:123})
  res.send('add success')
})

app.get('/find/',(req,res) => {
  signUpdb.find({pwd:123},(err,doc) =>{
    // if there is a error, report error info
    if (err){
      console.log(err)
    }
    // if find something related to {uid:'Selina'} show info
    if (doc){
      console.log(doc)
      res.send('find info')
    }
  })
})
//create a server, create a dababase(you can define database name by yourself, try to add some data to db, do search by what you want, if you finish then send me server.js)
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

app.post('/dealSignUp/',express.json(),(req,res) =>{
  console.log('received data is ',req.body)
  console.log(req.body.uid)
  // we need to check is there is a user already taken this uid
  // if does not we need to let it register
  // if does, we would not let it register
  signUpdb.find({uid:req.body.uid},(err,doc) => {
    //if doc's length > 0 means there is no uid was taken, we can register
    // else it means this uid already was token
    if(doc.length > 0){
      res.send({msg:'this email was taken, please try another one'})
    }else{
      signUpdb.insert(req.body)
      res.send({msg:'sign up successfully'})
    }
  })

})

/* homework

  try to using data from database to login
  
  check is login email and login password in databse, 
  alert login successfully

  else

  alert username or password does not exist
 
next class talk how to do check signup confirm, login, and after login
*/

