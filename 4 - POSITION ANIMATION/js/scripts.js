function controle(){
    var but = document.getElementById("btn");
    var b1 = document.getElementById("bola-01");
    var b2 = document.getElementById("bola-02");
    var b3 = document.getElementById("bola-03");
    var b4 = document.getElementById("bola-04");
    var box = document.getElementById("container");

    if (but.innerText == "PAUSE"){
        box.style.backgroundColor = "#000"
        btn.innerText = "PLAY";
        b1.style.animationPlayState = "paused";
        b2.style.animationPlayState = "paused";
        b3.style.animationPlayState = "paused";
        b4.style.animationPlayState = "paused";
    } else {
        box.style.backgroundColor = "#FFF"
        btn.innerText = "PAUSE";
        b1.style.animationPlayState = "running";
        b2.style.animationPlayState = "running";
        b3.style.animationPlayState = "running";
        b4.style.animationPlayState = "running";
    }
}