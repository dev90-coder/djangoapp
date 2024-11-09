const time = document.getElementById("times")
    setInterval(function(){
        var d = new Date()
        let times = d.getDate()
       
        time.innerText=d
    },1000)