const express = require("express");
var cors = require("cors");


const server = express();
server.use(cors());
server.use(express.json());

server.listen(3000, () => {
    console.log("3000 ports was listening");
  });

server.get('/',(req,res) =>{
    res.send('server is open')
})

server.post('/getImgName/',(req,res) =>{
    
})