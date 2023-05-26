const express = require("express");
var cors = require("cors");
// introduce library nedb ad Nedb
var Nedb = require("nedb");
const app = express();
//userdb is instance of Nedb
/*
create database in here
*/
var blogDb = new Nedb({
  filename: "blogDb.db",
  autoload: true,
});

var userdb = new Nedb({
  filename: "user.db",
  autoload: true,
});

var userInfoDb = new Nedb({
  filename: "userInfo.db",
  autoload: true,
});


app.use(cors());
app.use(express.json());
app.listen(3000, () => {
  console.log("server running at localhost/127.0.0.1");
});

// app.get("/test", (req, res) => {
//   userInfoDb.find({ Username: "a" }, (err, n) => {
//     console.log(n);
//   });
// });

app.post("/POSTLOGIN/", express.json(), (req, res) => {
  // console.log(req.body);
  userdb.find(req.body, (err, doc) => {
    if (doc.length == 0) {
      // doc.length == 0 代表着输入的、用户名密码不存在于数据库中
      res.send({ msg: "not found" });
    } else {
      res.send({ msg: "exist" });
    }
    // console.log("the result of finding is ", doc);
  });
});

app.post("/POSTSIGNUP/", express.json(), (req, res) => {
  // console.log(req.body);
  //we need to make username is uqiue
  userdb.find({ username: req.body.username }, (err, n) => {
    if (n.length != 0) {
      res.send({ msg: "username already exist" });
      // console.log("username already exist");
    } else {
      // console.log(0);
      userdb.insert(
        {
          username: req.body.username,
          password: req.body.password,
        },
        function (err, doc) {
          // console.log("account register successfully", doc);
          res.send({ msg: "add account successfully" });
        }
      );
    }
  });
  // userdb.insert({ username: req.body.username, password: req.body.password });
  // res.send({ msg: "WE RECEIVED POSTSIGNUP REQUEST" });
});

app.post("/EDITUSER/", express.json(), (req, res) => {
  // console.log("what we get from edit user:");
  // console.log(req.body);
  userInfoDb.find({ Username: req.body.Username }, (err, n) => {
    // console.log(n);
    if (n.length != 0) {
      userInfoDb.update(
        { Username: req.body.Username },
        {
          $set: req.body,
        },
        (err, n) => {
          res.send({ msg: "edit userInfo" });
        }
      );

      // we have date related with this username
    } else {
      //we don't have date related with this username, just insert req.body
      userInfoDb.insert(req.body, function (err, doc) {
        // console.log("add userInfo successfully", doc);
      });
    }
  });
  /*
  check userInfo.db 
    if username from req.db exists in userInfo, 
      we need to edit this user's info
    if username from req.db exists in userInfo,
      we just need to insert user's info in userInfo.db
  */
});

app.post("/getUserInfo/", express.json(), (req, res) => {
  var username = req.body.Username;
  userInfoDb.find({ Username: username }, (err, n) => {
    // console.log(n[0]);
    res.send(n[0]);
  });
});

app.post("/postBlog/",express.json(),(req,res) => {
  // console.log(req.body)
  blogDb.insert(
    {
      username: req.body.Username,
      content: req.body.Content,
      tile: req.body.Title,
    },
    function (err, doc) {
      console.log("data added successfully", doc);
      res.send({ msg: "data added successfully" });
    }
  );
  
  /*
  20230120 homework
  1. create database named 'blogDb.db
  2 insert data {'username':"#",Content:"",Tile:""} from req.body
  "}'
  */
})

app.post('/loadBlog/',express.json(),(req,res) => {
  // console.log(req.body)
  blogDb.find({username:req.body.Username},(err,doc) => {
    console.log(doc)
    res.send({mes:doc})
  })
  // console.log('hello')

})

app.post('/FINDDETAIL/',express.json(),(req,res) => {
  blogDb.find({_id:req.body._id}, (err,doc) => {
  console.log(req.body)
    res.send({mes:doc})
  })
})

app.post('/deleteBlog/',express.json(),(req,res) => {
  blogDb.remove(req.body)
  res.send({mes:'delete success'})
})

app.post('/updateBlog/',express.json(),(req,res) => {
  blogDb.update(req.body)
  res.send({mes:'update success'})
})

/*
homework:
1.

do practice CRUD for db ,{name: balabla. course: balaba, 'scores':90}
{name: 'Kevin', course: 'python', scores: 95}
{name: 'Selina', course: 'html&css', scores: 90}
 2.
 a.before we insert signupInfo to db, we need to do authenticate,   // befor we insert signupInfo to db, we need to do authenticate
   make sure user name is unique
   wether username is in db

b. when we login authenticate where username and password are  matched in database
*/
//nosw
//npm i nodemon -g -f
// db.insert({
//   name: "Jingxue",
//   course: "java",
//   score: 100,
// });
// db.insert({ name: "Kevin", course: "python", scores: 95 });
// db.insert({ name: "Selina", course: "html&css", scores: 90 });
//CRUD
// db.find({}, (err, docs) => {
//   console.log(docs);
// });
// db.update(
//   { name: "Selina" },
//   {
//     $set: {
//       scores: 98,
//     },
//   },
//   (err, n) => console.log(n)
// );

// db.remove({ name: "Selina" });
