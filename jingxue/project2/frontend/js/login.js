function logIn() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    console.log(username, password);
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            accept: "application/json",
        },
        body: JSON.stringify({
            username: username,
            password: password,
        }),
    };
    const url = "http://localhost:3000/dealLogin/";
    fetch(url, options)
        .then((res) => res.json())
        .then((res) => {
            // console.log(res.msg);
            if(res.msg == 'success'){
                window.location.href = 'mainPage.html'
            }else{
                alert('username or password are not exist')
            }
            // alert("logged in");
        });
}