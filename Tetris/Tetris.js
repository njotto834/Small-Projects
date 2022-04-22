document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('.grid');
    let squares = Array.from(document.querySelectorAll('.grid div'));
    const scoreDisplay = document.getElementById("score");
    const startBtn = document.getElementById("startButton");
    const width = 10; //Width of the grid
    let nextRandom = 0
    let timerID
    
    //The Tetrominoes
    const lTetromino = [
        [1, width+1, width*2+1, 2], 
        [width, width+1, width+2, width*2+2], 
        [1, width+1, width*2+1, width*2], 
        [width, width*2, width*2+1, width*2+2] 
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
    let currentRotation = 0

    //randomly select a Tetromino and its first rotation
    let random = Math.floor((Math.random()*theTetrominoes.length))
    console.log(random)
    let current = theTetrominoes[random][currentRotation]

    //draw the Tetromino
    function draw(){
        current.forEach(index => {
            squares[currentPosition + index].classList.add('tetromino')
        })
    }

    //undraw the Tetromino
    function undraw(){
        current.forEach(index => {
            squares[currentPosition + index].classList.remove('tetromino')
        })
    }

    //assign functions to keycodes
    function control(e){
        if (e.keyCode === 37){
            moveLeft()
        }
        else if (e.keyCode === 38){
            rotate()
        }
        else if (e.keyCode === 39){
            moveRight()
        }
        else if (e.keyCode === 40){
            moveDown()
        }
    }
    //Checks for the 'keyup' event
    document.addEventListener('keyup', control)

    //timer down function
    function moveDown(){
        undraw()
        currentPosition += width
        draw()
        freeze()
    }

    //freeze function
    function freeze(){
        //If the index of any of the current squares in our tetrimino + width (1 row down)
        //contains the class 'taken'
        if(current.some(index => squares[currentPosition + index + width].classList.contains('taken'))){
            //Add the class 'taken' to each of our tetromino squares.
            current.forEach(index => squares[currentPosition + index].classList.add('taken'))
            //start a new Tetromino falling
            random = nextRandom
            nextRandom = Math.floor(Math.random() * theTetrominoes.length)
            current = theTetrominoes[random][currentRotation]
            currentPosition = 4
            draw()
            displayShape()
        }
    }

    //move the tetromino left, unless is at the edge or there is a blockage
    function moveLeft(){
        undraw()
        const isAtLeftEdge = current.some(index => (currentPosition + index) % width === 0)
        if (!isAtLeftEdge) currentPosition -= 1

        if (current.some(index => squares[currentPosition + index].classList.contains('taken'))){
            currentPosition += 1
        }
        draw()
    }

    //move the tetromino right, unless is at the edge or there is a blockage
    function moveRight(){
        undraw()
        const isAtRightEdge = current.some(index => (currentPosition + index) % width === 9)
        if (!isAtRightEdge) currentPosition += 1

        if (current.some(index => squares[currentPosition + index].classList.contains('taken'))){
            currentPosition -= 1
        }
        draw()
    }

    //rotate the tetromino
    function rotate(){
        undraw()
        currentRotation ++
        if (currentRotation == 4){ //If currentRotation is 4, wrap around to 0
            currentRotation = 0
            current = theTetrominoes[random][currentRotation]
        }
        else{
            current = theTetrominoes[random][currentRotation]
        }
        draw()
    }

    //show up-next tetromino in mini-grid
    const displaySquares = document.querySelectorAll('.mini-grid div')
    const displayWidth = 4
    let displayIndex = 0

    //the Tetrominoes without rotations
    const upNextTetrominoes = [
        [1, displayWidth+1, displayWidth*2+1, 2], //lTetromino
        [displayWidth+1, displayWidth+2, displayWidth*2, displayWidth*2+1], //zTetromino
        [1, displayWidth, displayWidth+1, displayWidth+2], //tTetromino
        [0, 1, displayWidth, displayWidth+1], //oTetromino
        [1, displayWidth+1, displayWidth*2+1, displayWidth*3+1] //iTetromino
    ]

    //display the shape in the mini-grid display
    function displayShape(){
        displaySquares.forEach(square => {
            square.classList.remove('tetromino')
        })
        upNextTetrominoes[nextRandom].forEach(index => {
            displaySquares[displayIndex + index].classList.add('tetromino')
        })
    }

    //add functionality to the button
    startBtn.addEventListener('click', () =>{
        if (timerID){
            clearInterval(timerID)
            timerID = null
        }
        else{
            draw()
            timerID = setInterval(moveDown, 500)
            nextRandom = Math.floor(Math.random()*theTetrominoes.length)
            displayShape()
        }
    })
})