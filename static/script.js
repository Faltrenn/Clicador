idplayer = 0;
var seconds = document.getElementById("sec");
var miliseconds = document.getElementById("milisec");
var countClicks = document.getElementById("clicks");



var init = false;
var mili = 10000;
var sec = 0;
var clicks = 0;
var inter;
function clk(){
    clicks ++;
    countClicks.innerText = clicks;

    if(!init){
        init = true;
        inter = setInterval(plusMili, 10);
    }
}

function plusMili(){
    mili -= 10;
    sec = Math.floor(mili / 1000);
    if(sec == 0 && mili == 0){
        clearInterval(inter);
    }
    if(mili == 0){
        miliseconds.innerText = "00";
        let form = document.getElementById("saveScore");
        let playername = document.getElementById("playerid");
        let player_score = document.getElementById("playerscore");
        playername.value = document.getElementById("playername").innerText;
        player_score.value = clicks;
        form.submit();
    }else{
        miliseconds.innerText = mili.toString().substring(1, 3);
    }
    seconds.innerText = sec;
}