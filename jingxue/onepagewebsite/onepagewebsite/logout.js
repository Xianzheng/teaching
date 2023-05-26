function logout(){
    localStorage.removeItem('email')
    alert('successfully logout')
    document.getElementById('loginHeader').style.display = ''
    document.getElementById('signupHeader').style.display = ''
    document.getElementById('productHeader').style.display = 'none'
    document.getElementById('pricingHeader').style.display = 'none'
    document.getElementById('contactHeader').style.display = 'none'

    document.getElementById('login').style.display = ''
    document.getElementById('signup').style.display = ''
    document.getElementById('product').style.display = 'none'
    document.getElementById('pricing').style.display = 'none'
    document.getElementById('contact').style.display = 'none'

    document.getElementById('logoutHeader').style.display = 'none'



}