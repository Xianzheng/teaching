// load library explress, this is a nimi server
// const express is a variable name, require("express") is a library from node_modeules
const express = require("express");

// load library cors is in order to translate data between front and backend
// const cors is a variable name, require("cors") is a library from node_modules
const cors = require("cors");

// load library nedb, nedb is a mini database, inorder to store data we create
// "Nedb" is a variable name, require("nedb") is a library from node_modules
var Nedb = require("nedb");


// create a server, named hw server
hw = express();

// open server to edit database
hw.use(cors()); // use cors() to translate date between front and backend
hw.use(express.json()); // translate data using json format {name: 'mark, age: 29}

// hw server port is 8000
hw.listen(8000, () => {
  console.log("server is opened");
});

var hwDb = new Nedb({
  filename: "hwDb.db",
  autoload: true,
});

// url is 127.0.0.1:8000/trigger
hw.get("/trigger", (req, res) => {
  console.log("it works");
  res.send("is working");
});

// url is 127.0.0.1:8000/c, will create to hwDb.db
// {name: blalabla, course: blalabla, score: 90}
// {name: kevin, course: python, score: 95}
// {name: selina, course: html&css, score: 90}
hw.get("/c/", (req, res) => {
  hwDb.insert(
    { name: "blalabla", course: "blalabla", score: 90 },
    (err, doc) => {
      console.log(doc);
    }
  );
  hwDb.insert({ name: "kevin", course: "python", score: 95 }, (err, doc) => {
    console.log(doc);
  });
  hwDb.insert({ name: "selina", course: "html&css", score: 90 }, (err, doc) => {
    console.log(doc);
  });
  res.send("create successfully");
});

hw.get("/r/", (req, res) => {
  hwDb.find({ name: "selina" }, (err, n) => {
    console.log(n);
    res.send(n);
  });
});

hw.get("/u/", (req, res) => {
  hwDb.update({ name: "blalabla", course: "blalabla", score: 90 },  {name: "Jingxue", course: "python", score: 90}, (err, u) => {
    res.send("updated successfully");
  });
});

hw.get("/d/", (req, res) => {
  hwDb.remove({ name: "blalabla", course: "blalabla", score: 90}, (err, d) => {
    console.log(d);
    res.send("removed successfully");
  });
  hwDb.remove({name: "kevin", course: "python", score: 95}, (err, d) => {
    console.log(d);
    res.send("removed successfully");
  });
});
