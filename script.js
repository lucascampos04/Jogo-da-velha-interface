const cellElements = document.querySelectorAll("[data-cell]");
const board = document.querySelector('[data-board]');
const winningMessage = document.querySelector('[data-winning-message]');
const drawMessage = document.querySelector('[data-draw-message]');
const restartButton = document.querySelectorAll('button');

let circleJogar = true;
let movesCount = 0;
let winner = false;

const placeMark = (cell, classToAdd) => {
    cell.classList.add(classToAdd);
};

const swapTurns = () => {
    board.classList.remove('circle');
    board.classList.remove('x');

    if (circleJogar) {
        board.classList.add('circle');
    } else {
        board.classList.add('x');
    }
};

const checkWin = (classToCheck) => {
    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    return winningCombinations.some(combination => {
        return combination.every(index => {
            return cellElements[index].classList.contains(classToCheck);
        });
    });
};

const displayWinningMessage = (classToAdd) => {
    winningMessage.style.display = 'flex';
    winningMessage.querySelector('p').textContent = `${classToAdd.toUpperCase()} Venceu!`;
};

const displayDrawMessage = () => {
    drawMessage.style.display = 'flex';
};

const restartGame = () => {
    movesCount = 0;
    winner = false;
    circleJogar = true;
    board.classList.remove('x');
    board.classList.remove('circle');
    cellElements.forEach(cell => {
        cell.classList.remove('x');
        cell.classList.remove('circle');
        cell.addEventListener('click', handleClick, { once: true });
    });
    winningMessage.style.display = 'none';
    drawMessage.style.display = 'none';
};

const handleClick = (e) => {
    const cell = e.target;
    const classToAdd = circleJogar ? 'circle' : 'x';

    placeMark(cell, classToAdd);
    movesCount++;

    if (checkWin(classToAdd)) {
        winner = true;
        displayWinningMessage(classToAdd);
        cellElements.forEach(cell => cell.removeEventListener('click', handleClick));
    } else if (movesCount === cellElements.length) {
        displayDrawMessage();
        cellElements.forEach(cell => cell.removeEventListener('click', handleClick));
    } else {
        swapTurns();
        circleJogar = !circleJogar;
    }
};

cellElements.forEach(cell => cell.addEventListener('click', handleClick, { once: true }));
restartButton.forEach(button => button.addEventListener('click', restartGame));
