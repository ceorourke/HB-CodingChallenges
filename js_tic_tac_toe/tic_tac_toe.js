var board = document.getElementById('board');
var winMessage = document.querySelector('.win-message');

var zeroZero = document.getElementById('00');
var oneZero = document.getElementById('10');
var twoZero = document.getElementById('20');
var zeroOne = document.getElementById('01');
var oneOne = document.getElementById('11');
var twoOne = document.getElementById('21');
var zeroTwo = document.getElementById('02');
var oneTwo = document.getElementById('12');
var twoTwo = document.getElementById('22');

var counter = 0;

function handleMove(e) {
    if(e.target.innerText !== 'O' && e.target.innerText !== 'X') { // if the box is empty
        if(counter % 2 == 0) {
            e.target.innerText = 'O'
            counter ++;
            if(checkWin('O')) {
                endGame();
                winMessage.innerText = "You won, O!";
            }
        } else {
            e.target.innerText = 'X'
            counter ++;
            if(checkWin('X')) {
                endGame();
                winMessage.innerText = "You won, X!";
            }
        }
    }
}

function checkWin(player) {
    if((zeroZero.innerText === player) && (zeroOne.innerText === player) && (zeroTwo.innerText === player) || // top row
        (oneZero.innerText === player) && (oneOne.innerText === player) && (oneTwo.innerText === player) || // middle row
        (twoZero.innerText === player) && (twoOne.innerText === player) && (twoTwo.innerText === player) || // bottom row
        (zeroZero.innerText === player) && (oneOne.innerText === player) && (twoTwo.innerText === player) || // diagonal, top left to bottom right
        (zeroTwo.innerText === player) && (oneOne.innerText === player) && (twoZero.innerText === player) || // diagonal, top right to bottom left
        (zeroZero.innerText === player) && (oneZero.innerText === player) && (twoZero.innerText === player) || // left column
        (zeroOne.innerText === player) && (oneOne.innerText === player) && (twoOne.innerText === player) ||  // middle column
        (zeroTwo.innerText === player) && (oneTwo.innerText === player) && (twoTwo.innerText === player)) { // right column
        return true;
    } else {
        return false;
    }
}

function endGame() {
    board.removeEventListener('click', handleMove);
}


board.addEventListener('click', handleMove);
