const express = require("express");
var cors = require("cors");
var DB = require("nedb");

const app = express();
app.use(cors());
app.use(express.json())

var storeDatadb = new DB({
    filename: 'storeData.db',
    autoload : true,
})
app.listen(3000, (req, res) => {
  console.log("server runs at port 3000");
});

app.get("/", (req, res) => {
  res.send("server is running");
});

app.get("/sayHello/", (req, res) => {
  console.log(req.query);
  res.send("Hello " + req.query.name);
});

app.post("/storeData/", express.json(), (req, res) => {
    console.log(req);
    signUpInfo = req.body;
    storeDatadb.find({ username: req.body.username }, (err, n) => {
        if (n.length != 0) {
            res.send({ msg: "username already exist" });
        } else {
            storeDatadb.insert(
            {
                student_name: signUpInfo.student_name,
                student_id: signUpInfo.student_id,
                subject: signUpInfo.subject,
                subject_marks: signUpInfo.subject_marks,
            },
            res.send({msg:'add success'})
          );
        }
      });
});