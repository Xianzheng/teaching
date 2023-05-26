const publicMomentSubmit = () =>{
    let momentTxt = document.getElementById('momentContent').value

    // let momentImage = document.getElementById('momentImage')

    // momentImage.files[0] it is upload Image
    const inp = document.getElementById("customFile");
    const formData = new FormData()

    console.log(inp.files[0])

    formData.append("key", inp.files[0]);
    formData.append('name', momentTxt)

    fetch("http://localhost:3000/uploads/", {
      method: "POST",
      body: formData //自动修改请求头,formdata的默认请求头的格式是 multipart/form-data
    }).then(res => res.json())
      .then(res => {
        alert('上传成功')
        
        // console.log(res)
        // document.getElementById("createApp").disabled = true
      })
}

function changLable(){
  const inp = document.getElementById("customFile");
  let file = inp.files[0]
  let fileName = file.name
  document.getElementById('fileLabel').innerHTML = fileName
  // alert('I was invoked')
} 