function loginClick() {
    console.log('login')
    var email = document.getElementById("loginEmail").value;
    var password = document.getElementById("loginPassword").value;
  
    console.log(email, password);
  
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        accept: "application/json"
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    };
    const url = "http://localhost:3000/loginInfo/";
    fetch(url, options)
      .then((res) => res.json())
      .then((res) => {
        if (res.msg == "success") {
          // alert('success ')
          localStorage.setItem('email',email)
          console.log('localStorage item',localStorage.getItem('email'))
          /*
          using javascript add html code to onepagewebsite.html
          step:
          1.find place to add code,add li under ul
          <li><a href="#"  onclick='logout()'>Contact</a></li>
          
          */
          ulEle = document.getElementById('menu')
          
          newLi = document.createElement('li')
          newLi.setAttribute('id','logoutHeader')

          newA = document.createElement('a')

          newA.innerHTML = 'Logout'

          newA.setAttribute('href','#')
          newA.setAttribute('onclick','logout()')

          newLi.append(newA)

          ulEle.append(newLi)

          console.log(ulEle)
          
          document.getElementById('loginHeader').style.display = 'none'
          document.getElementById('signupHeader').style.display = 'none'
          document.getElementById('productHeader').style.display = ''
          document.getElementById('pricingHeader').style.display = ''
          document.getElementById('contactHeader').style.display = ''

          document.getElementById('login').style.display = 'none'
          document.getElementById('signup').style.display = 'none'
          document.getElementById('product').style.display = ''
          document.getElementById('pricing').style.display = ''
          document.getElementById('contact').style.display = ''


        } else {
          alert("username or password does not exist");
        }
      });
  }

  /*
  in one single website page there are tw0 button, it can switch paragraph content to show

  when we press button 1, it will paragraph1
  when we press button 2, it will paragraph2

  we better use less html and using more js to dynamic change html content
  */