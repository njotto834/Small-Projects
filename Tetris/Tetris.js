document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('.grid');
    let squares = Array.from(document.querySelectorAll('.grid div'));
    const ScoreDisplay = document.getElementById("score");
    const StartBtn = document.getElementById("startButton");
    const width = 10;
    
    //The Tetrominoes
    const lTetromino = [
        [1, width+1, width*2+1, 2] //Picks grid indices 1, 11, 21, 2
        [width, width+1, width+2, width*2+2]
        [1, width+1, width*2+1, width*2]
        [width, width*2, width*2+1, width*2+2]
    ]

    
})