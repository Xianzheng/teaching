function signUp() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var password = document.getElementById("password1").value;

    console.log(username, password, password1);
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
    const url = "http://localhost:3000/signUp/";
    fetch(url, options)
        .then((res) => res.json())
        .then((res) => {
            console.log(res)
            if (res.msg == 'success') {
                alert('add account success')
            } else {
                alert("username or password does not exist")
            }
            // console.log(res);
            // alert("logged in");
        });
}