let restartEl = document.getElementById("r")
let scoreEl = document.getElementById("score")
let highscoreEl = document.getElementById("highscore")

/* restart btn */
restartEl.addEventListener("click", restart)
function restart(){
    window.location.reload()
}

// SNAKE Canvas JS, omtrent likt som pygame
var blockSize = 25; 
var cols = 20; // y-retning 
var rows = 20; // x-retning

//board til å tegne på med matte 
var board; 
// til å tegne med senere 
var context; 

// hodet start
var snakeX = blockSize * 5;
var snakeY =  blockSize * 5;

// snake kropp
var snakeKropp = [];

// mat start 
var matX;
var matY;

//fart slange 
var vx = 0;
var vy = 0;

// score teller 
var score = 0;

/* for å sjekke game over eller ikke, false = spiller fortsatt */
var gameOver = false;

// når siden loader, kjør følgende funksjon, som run løkken i pygame
function load(){
    board = document.getElementById("board");
    board.height = rows * blockSize;
    board.width = cols * blockSize;
    //endre scoreEl sin width for å passe canvas boxen
    scoreEl.style.width = `${ cols * blockSize}px`
    context = board.getContext("2d"); //for å tegne på brettet
    highscoreEl.innerHTML = `Highscore: ${localStorage.highscore}`
    
    matPos();
    document.addEventListener("keydown", endreRetning);

    /* hvor ofte det skal oppdateres, litt som fps */
    setInterval(update, 1000/10); // 100 ms

}
load()



function endreRetning(e){
    //objekt.code er som key.pressed i pygame
    if (e.code == "ArrowUp" && vy != 1){
        vx = 0;
        vy = -1; 
    }
    else if (e.code == "ArrowDown" && vy != -1){
        vx = 0;
        vy = 1;
    }
    else if (e.code == "ArrowLeft" && vx != 1){
        vx = -1; 
        vy = 0;
    }
    else if (e.code == "ArrowRight" && vx != -1){
        vx = 1;
        vy = 0;
    }

    /* restart med space */
    /* else if (e.code == "Space"){
        console.log("space")
        restart()
    } */
}

function update(){
    //board tegn 
    context.fillStyle = "black";
    context.fillRect(0,0,board.width, board.height); // samme som pygame. for å lage et svart lærret 

    // mat tegn 
    context.fillStyle = "red";
    context.fillRect(matX,matY,blockSize, blockSize); 

    /* hvis hodet matcher matPos, spis maten og legg til en blokk i lengden */
    if (snakeX == matX && snakeY == matY){

        if(snakeKropp.length == 0) snakeKropp.push([snakeX, snakeY])
        
        else{
            snakeKropp.push([snakeKropp[snakeKropp.length - 1][0], snakeKropp[snakeKropp.length - 1][1]])
        }
       
        matPos()
        score += 1
        scoreEl.innerHTML = `Score: ${score}`
    }

    //snake tegne slangen
    context.fillStyle = "#d3ad7f";
    snakeX += vx * blockSize;
    snakeY += vy * blockSize;
    /* xpos, ypos, bredde, høyde */
    context.fillRect(snakeX,snakeY,blockSize, blockSize);

    for (let i = 0; i < snakeKropp.length; i++){
        context.fillStyle ="#d3ad7f";
        context.fillRect(snakeKropp[i][0], snakeKropp[i][1], blockSize, blockSize);
    }

    //halen skal ta igjen kroppen, for at brikkene skal vite hvor de skal
    for (let i = snakeKropp.length-1; i > 0; i --){
        snakeKropp[i] = snakeKropp[i-1];
    }

    //hvis slangen har en kropp, det etter hodet (snakeKropp[0]) lik x og y kordinatet til hodet
    if (snakeKropp.length){
        snakeKropp[0] = [snakeX, snakeY];
    }

   //gameOver om veggtreff eller om du går inn i deg selv 
   if (snakeX < 0 || snakeX + blockSize > cols * blockSize || snakeY < 0 || snakeY +  blockSize > rows * blockSize){
    gameOver = true; 
   }
   // sjekke om hodet har gått inn i kroppen, da erru dau
   for (let i = 1; i < snakeKropp.length; i ++){
    if (snakeX == snakeKropp[i][0] && snakeY ==snakeKropp[i][1]){
        gameOver = true
        console.log(score)
    }
   }

   /* local storage for å lagre highscore */
    if (!localStorage.highscore){
        localStorage.highscore = 0
    }
    if (score > Number(localStorage.highscore)){
        localStorage.highscore = score
        highscoreEl.innerHTML = `SCORE to BEAT: ${localStorage.highscore}`
    } 
   end()
}

function end(){
    if(gameOver){
        gameOverScreen()
        backgroundDynam()
    }
}

function gameOverScreen(){
    //fyll skjermen svart
    context.fillStyle = "#000000";
    context.fillRect(0,0,board.width,board.height)
    //game over 
    context.font = "50px Arial";
    context.fillStyle = "#FFFFFF"
    context.fillText("GAME OVER", board.width/2 - 150, board.height/2)
    context.font = "30px Arial";
    context.fillStyle = "#FFFFFF"
    context.fillText("Your score: " + score, board.width/2 - 150, board.height/2 + 50)
    
   }

/* gjør skjermen samme farge som slangen så det ser ut som slangen går utover hele skjermen// dør */
function backgroundDynam(){
    document.body.style.backgroundColor = "#d3ad7f";
}

function matPos(){
    // random(0,1) * 20 -> (0,19.999) * floor, for å få 19 og ikke 20 (tegner utfor) -> (0,19) * str på block = random start punkt
    matX = Math.floor(Math.random(0,1) * cols) * blockSize;
    matY = Math.floor(Math.random(0,1) * rows) * blockSize;
}