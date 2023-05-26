


var getsmallest=(arg)=>{
    let smallest=arg[0]
    arg.forEach(element => {
        if (smallest>element)
        smallest=element
    });
    return smallest
}

var options={
    method:'POST',
        headers:{
        'Content-Type':'application/json',
        'Accept':'Application/json'
        },
        body:JSON.stringify({a:1,b:2})
}

module.exports = { getsmallest,options}

