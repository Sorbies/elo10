// Clyde Sinclair
// SoftDev pd0
// K26 -- canvas based JS animation
// 2021-05-05w

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

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
    console.log("clear invoked...")
    ctx.clearRect(0, 0, c.width, c.height);
    // YOUR CODE HERE
};


var radius = 0;
var growing = true;
var start;


//var drawDot = function() {
var drawDot = () => {
    requestID = window.requestAnimationFrame(animateCircle);
};

var animateCircle = (timestamp) => {
    console.log("drawDot invoked...")
    if (start === undefined)
        start = timestamp;
    const elapsed = timestamp - start;
    // YOUR CODE HERE
    clear()
    ctx.beginPath();

    // arc draws the circle shape, but cannot immediatly be seen on the canvas
    ctx.arc(250, 250, radius, 0, (2 * Math.PI));

    // stroke adds an outline to the circle shape so that it can be seen
    ctx.stroke();

    // fill fills in the circle, finishing our shape
    ctx.fill();

    if (growing) {radius++;}
    else {radius--;}
    requestID = window.requestAnimationFrame(animateCircle);
    if (radius == 250) {growing = false;}
    /*
      ...to
      Wipe the canvas,
      Repaint the circle,
      ...and somewhere (where/when is the right time?)
      Update requestID to propagate the animation.
      You will need
      window.cancelAnimationFrame()
      window.requestAnimationFrame()
     */
};

//var stopIt = function() {
var stopIt = () => {
    console.log("stopIt invoked...")
    console.log(requestID);

    // YOUR CODE HERE
    /*
      ...to
      Stop the animation
      You will need
      window.cancelAnimationFrame()
    */
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);