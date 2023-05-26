const express = require('express')
var cors = require('cors')

var DB = require('nedb')

const app = express()
app.use(cors())
app.use(express.json())

var userdb = new DB({
    filename: 'user.db',
    autoload: true,
})

app.listen(3000, () => {
    console.log('server runs at port 3000')
})

app.get('/',(req,res) =>{
    res.send('server is running')
})

app.get('/sayHello/',(req,res) => {
    console.log(req.query)
    res.send('Hello '+req.query.name)
})

app.post('/dealLogin/', express.json(), (req,res) => {
    const fakeDB = [
        {username: 'jingxue', password:1234},
        {username: 'mark', password:2345},
        {username: 'claud', password:3456},
    ]
    logInInfo = req.body

    let count = 0
    //  if logInInfo match one data from fakeDb, res send success, else send fail
    fakeDB.forEach(element => {
        if (element.username == logInInfo.username && element.password == logInInfo.password) {
            count = 1
        }
    });
    // console.log(count)
    if (count == 1) {
        res.send({msg: 'success'})
    } else {
        res.send({msg: 'fail'})
    }
})

app.post("/signUp/", express.json(), (req, res) => {
    console.log(req);
    signUpInfo = req.body;
    userdb.find({ username: req.body.username }, (err, n) => {
        if (n.length != 0) {
            res.send({ msg: "username already exist" });
        } else {
            userdb.insert(
            {
                username: signUpInfo.username,
                password: signUpInfo.password,
            },
            res.send({msg:'success'}),
            
          );
        }
      });
});