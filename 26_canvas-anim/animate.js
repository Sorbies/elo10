// Team e -- Ari Schechter, Eric Lo, William Yin
// SoftDev pd1
// K26 -- canvas based JS animation
// 2021-05-05

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "red" // YOUR CODE HERE

var requestID = 0;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
    // YOUR CODE HERE
    ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
    if (requestID === 0) requestID = animateCircle();
};

var animateCircle = () => {
    // YOUR CODE HERE
    clear()
    ctx.beginPath();

    // arc draws the circle shape, but cannot immediatly be seen on the canvas
    ctx.arc(c.width / 2, c.height / 2, radius, 0, (2 * Math.PI));

    // stroke adds an outline to the circle shape so that it can be seen
    ctx.stroke();

    // fill fills in the circle, finishing our shape
    ctx.fill();

    if (radius >= 250) {
        growing = false
    } else if (radius <= 0) {
        growing = true;
    }
    if (growing) radius++;
    else radius--;

    requestID = window.requestAnimationFrame(animateCircle);
    return requestID;
};

//var stopIt = function() {
var stopIt = () => {
    // YOUR CODE HERE
    if (requestID !== 0) {
        window.cancelAnimationFrame(requestID);
        requestID = 0;
    }
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);