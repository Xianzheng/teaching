const fs = require('fs')

function readFile_Asys(){
    
    //异步读取（Asynchronous）
    fs.readFile('read.txt','utf-8',function(err,data){
        if(err){
            return console.error(err);
        }
        return data.toString()
    })
   
    
}


function readFile_Sync(){
    //同步读取（synchronous）
     return fs.readFileSync('read.txt','utf-8')
    
}


function writeFile(){
    var readdata = readFile_Sync()
    readdata = readdata.replaceAll('a','e')
    readdata = readdata.replaceAll('o','f')
    readdata = readdata.replaceAll('i','*')
    fs.writeFileSync('read.txt',readdata)
    // fs.writeFile('read1.txt','utf-8',function(err){
    //     if(err){
    //         return console.error(err)
    //     }
    //     fs.writeFileSync('read1.txt',readdata)
    // })
}

function dealImg(){
    // fs.readFile('R-C.jpg','binary',funtion(err,data){
    //     if (err) {
    //         console.log(err)
    //         return 
    //     }
       
    // })
    let data = fs.readFileSync('R-C.jpg')
    console.log(data)
    fs.writeFileSync('A.jpg',data)
}

dealImg()