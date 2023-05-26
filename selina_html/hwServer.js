const express = require("express")

var cors = require("cors")

 

const app = express();

app.use(cors())

app.use(express.json())

 

app.listen(3001,()=>{

  console.log('server running at port 3001')

})

app.post('/login/',express.json(), (req,res) =>{

    reqFromFront = req.body
    
    console.log(reqFromFront)

    res.send({msg: 'i get username and password'})
  
})