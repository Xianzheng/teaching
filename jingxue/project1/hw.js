// load library express, this is mini server,
// const express is a variable name, require("express") is a library from node_modules
const express = require("express");

//load library cors is inorder to translate date between front and backend
// const cors is a variable name, require("cors") is a library from node_modules
const cors = require("cors");

// load library nedb, nedb is a mini database,  inorder to store data we create
// "Nedb" is a variable name, require("nedb") is a library from node_modules

var Nedb = require("nedb");

//create a server, named hw server
//express() is a function to create hw server
hw = express();

//open server to do somework in databse
hw.use(cors()); // use cors() to translate date between front and backend
hw.use(express.json()); //translate data using json format {name: 'mark', age: '29' }

//hw server port is 8000
hw.listen(8000, () => {
  console.log("server is opened");
});

// create a Nedb instance called hwDb
var hwDb = new Nedb({
  filename: "hwDb.db",
  autoload: true,
});
//url is 127.0.0.1:8000/trigger/, it will invoke (req,res) => {} function
hw.get("/trigger/", (req, res) => {
  console.log("it works");
  res.send("pretty good");
});
//url is 127.0.0.1:8000/c/, will create data
// {name: 'balabla', course: 'balaba', 'scores':90}
// {name: 'Kevin', course: 'python', scores: 95}
// {name: 'Selina', course: 'html&css', scores: 90}
// to hwDb
hw.get("/c/", (req, res) => {
  hwDb.insert({ name: "balabla", course: "balaba", scores: 90 }, (err, doc) => {
    console.log(doc);
  });
  hwDb.insert({ name: "Kevin", course: "python", scores: 95 }, (err, doc) => {
    console.log(doc);
  });
  hwDb.insert(
    { name: "Selina", course: "html&css", scores: 90 },
    (err, doc) => {
      console.log(doc);
    }
  );
  res.send("create successfully");
});
//url is 127.0.0.1:8000/r/, will find data , check balabla is in hwDb
hw.get("/r/", (req, res) => {
  hwDb.find({ name: "Selina" }, (err, n) => {
    console.log(n);
    res.send(n);
  });
});

//url is 127.0.0.1:8000/r/, update
// {name: balabla. course: balaba, 'scores':90} to
// {name: 'Jingxue'. course: 'english', 'scores':90}
hw.get("/u/", (req, res) => {});

//url is 127.0.0.1:8000/d/, delete after delete hwDb ONLY have data
// {name: 'Kevin', course: 'python', scores: 95}
// {name: 'Jingxue'. course: 'english', 'scores':90}
hw.get("/d/", (req, res) => {});

/*
    homework complete
    //url is 127.0.0.1:8000/r/, update
    // {name: balabla. course: balaba, 'scores':90} to
    // {name: 'Jingxue'. course: 'english', 'scores':90}
    hw.get("/u/", (req, res) => {});

    //url is 127.0.0.1:8000/d/, delete after delete hwDb ONLY have data
    // {name: 'Kevin', course: 'python', scores: 95}
    // {name: 'Jingxue'. course: 'english', 'scores':90}
    hw.get("/d/", (req, res) => {});

    implement functionality 


*/
