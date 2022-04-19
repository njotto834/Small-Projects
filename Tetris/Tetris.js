document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('.grid');
    let squares = Array.from(document.querySelectorAll('.grid div'));
    const ScoreDisplay = document.getElementById("score");
    const StartBtn = document.getElementById("startButton");
    const width = 10;
    
    //The Tetrominoes
    const lTetromino = [
        [1, width+1, width*2+1, 2], //1, 11, 21, 2
        [width, width+1, width+2, width*2+2], //10, 11, 12, 22
        [1, width+1, width*2+1, width*2], //1, 11, 21, 20
        [width, width*2, width*2+1, width*2+2] //10, 20, 21, 22
    ]

    const zTetromino = [
        [width+1, width+2, width*2, width*2+1],
        [0, width, width+1, width*2+1],
        [width+1, width+2, width*2, width*2+1], 
        [0, width, width+1, width*2+1] 
    ]
    
    const tTetromino = [
        [1, width, width+1, width+2], 
        [1, width+1, width+2, width*2+1], 
        [width, width+1, width+2, width*2+1], 
        [1, width, width+1, width*2+1] 
    ]

    const oTetromino = [
        [0, 1, width, width+1], 
        [0, 1, width, width+1], 
        [0, 1, width, width+1], 
        [0, 1, width, width+1] 
    ]

    const iTetromino = [
        [1, width+1, width*2+1, width*3+1], 
        [width, width+1, width+2, width+3], 
        [1, width+1, width*2+1, width*3+1],
        [width, width+1, width+2, width+3] 
    ]

    const theTetrominoes = [lTetromino, zTetromino, tTetromino, oTetromino, iTetromino]

    let currentPosition = 4
    let current = theTetrominoes[0][0]

    function draw(){
        current.forEach(index => {
            squares[currentPosition + index].classList.add('tetromino')
        })
    }

    draw();
    
    function fun(){
        alert("Hello");
    }

})