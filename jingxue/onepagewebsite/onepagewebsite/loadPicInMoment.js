function autoLoad(){
    console.log("Hello this is auto load")

    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          accept: "application/json"
        },

      };
      const url = "http://localhost:3000/getImageLst/";
      fetch(url, options)
        .then((res) => res.json())
        .then((res) => {

            res.msg.forEach(element => {
                // console.log(element)
                 const root = document.getElementById('pricingGroup')

                const addDiv = document.createElement('div')

                addDiv.setAttribute('class','imgDiv')

                const addImg = document.createElement('img')
                addImg.setAttribute('src','../backend/uploads/'+element)
                addImg.setAttribute('width','350px')
                addImg.setAttribute('height','200px')

                addDiv.append(addImg)
                root.append(addDiv)
            });
            console.log('picture number is ',res.number)
            let element1 = document.getElementById("product")
            element1.style.height = (45 * res.number).toString()+'vh'

           
        });
}

window.onload = autoLoad()