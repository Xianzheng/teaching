# tech
.front-end
    HTML,CSS,JAVASCRIPT(send request(CRUD) to backend, MANIPULATE HTML FILE(dom manipulation))
    BOOTSTRAP
.backend
    server.js(express engine)
        1.install library
            a.npm install express
            b.npm install cors
            c.npm install nedb --save
        2. create a mini server(coding)
            a. it can receive get request(with parame)
                req.query(it will get param body)
            b. post request
    nedb database(mysql, mongo db, no sql )

# scenario

    login/signup -> show page(it can look all post) /  reply other people's

# fetch record
function clickLogin(){
    const option = {
        method: 'POST',
        body : JSON.stringify({
            uid:'123',
            pwd:'456'
        })
    }
    const url = 'http://127.0.0.1:3000/dealLogin/';
    fetch(url,option)
    .then(res => res.json())
    .then(res => {
        console.log(res)
    })
} 

# homework
in front end ,create a signup page
in backend, create a database to store created username and password
(username existed can not be registed agan)
 registed username and password can login
