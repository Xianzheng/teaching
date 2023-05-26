const express = require("express");
var cors = require("cors");
var Nedb = require("nedb");

const server = express();
server.use(cors());
server.use(express.json());

var signUpdb  = new Nedb({
  filename: 'signup.db',
  autoload : true,
})

server.listen(3000, () => {
  console.log("3000 ports was listening");
});

server.get("/", (req, res) => {
  res.send("it is working");
});

server.get("/signup/",(req,res) =>{
  signUpdb.insert({"signupEmail":"a@a.com","signupPass":"aA123456","_id":"irUEc6hlylshCx4v"}, function (err, doc) {
      if (err) {
          console.log(err);
          return;
      }
      res.send('success')
  });
})

server.get("/find/",(req,res) =>{
  signUpdb.find({name: 'cuiht'}, function(err,doc) {
    if (err) {
      console.log(err);
      return;
    }
    res.send(doc)
  })
})

/*
const query = {"signupEmail":"a@a.com","signupPass":"aA123456","_id":"irUEc6hlylshCx4v"}


  console.log(query)

  signUpdb.find(query,(err,doc) =>{ 
    if(doc.length == 0){
      res.send({ msg: 'not found'});
    }else{
      res.send({msg:'find it'})
    }
  })

*/
server.get("/find1/",(req,res) =>{
  const query = {"signupEmail":"a@a.com"}
  signUpdb.find(query, function(err,doc) {
    if (err) {
      console.log(err);
      return;
    }
    res.send(doc)
  })
})