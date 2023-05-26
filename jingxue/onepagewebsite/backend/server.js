const express = require("express");
var cors = require("cors");
var Nedb = require("nedb");

const server = express();
server.use(cors());
server.use(express.json());
const multer = require('multer');
const fs = require('fs');
// const multer = require('multer')
// const upload = multer({dest: 'upload'})

server.use('/uploads', express.static(__dirname + '/uploads'));

const upload = multer({
  dest: 'uploads/'
});


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

server.post("/signupInfo/", express.json(), (req, res) => {
//   console.log(req);
  signUpInfo = req.body;
  // console.log(signUpInfo)
  // console.log({"signupEmail": signUpInfo.email})
  const query = {"signupEmail": signUpInfo.email}
  signUpdb.find(query, (err, n) => {
    if (err) {
      console.log(err)
      return 
    }
    if (n.length != 0) {
      res.send({ msg: "username already exist" });
    } else {
      signUpdb.insert(
        {
          signupEmail: signUpInfo.email,
          signupPass: signUpInfo.password
        },
        res.send({ msg: "add success" })
      );
    }
  });
});

server.post("/loginInfo/", express.json(), (req, res) => {
  const info = req.body
  // console.log(info)
  const query = {"signupEmail":info.email,"signupPass":info.password}

  signUpdb.find(query,(err,doc) =>{ 
    if (err){
      console.log(err)
      return
    }
    // console.log(doc)
    // console.log(doc.length)
    if (doc.length > 0){
      res.send({'msg':'success'})
    } else{
      res.send({'msg':'fail'})
    }
  })

})

/*
we already do upload image in our js and front end
next class we will do upload file in backend.
*/

server.post('/uploads',(req, res) => {
  /*
  copy folder we choose to upload to uploads folder
  1. how to get the files we choose to upload
  2. save files to uploads folder
  3. list all info to main page
  */
  console.log('this endpoint received data')
  res.send({'msg':'success'})
})

server.get('/getImageLst/',(req,res)=>{
  res.send('happy')
  console.log(fs.readdirSync('./uploads'))
  let data = fs.readFileSync('./uploads/R-C.jpg')
  let Base64Data = data.toString('base64')
  fs.writeFileSync('./uploads/R-C.txt',Base64Data)
})

/*
homework:
do a encrpt program
file content: hello kevin, selina, jingxue
key dict: {'a':'r','e':'l','i':'p','o':'s':'u':'t'}

do a decryot program with same key dict
key dict: {'a':'r','e':'l','i':'p','o':'s':'u':'t'}
file content：'tslpa'
correct content: uoeia

*/
