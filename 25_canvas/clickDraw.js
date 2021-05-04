/* Team e -- Ari Schechter, Eric Lo, William Yin
SoftDev
K25 -- I See a Red Door...: Learning to use the canvas tag with JavaScript
2021-05-03 */

// get the canvas html element
const canvas = document.getElementById("slate");
const ctx = canvas.getContext("2d");

const toggleButton = document.getElementById("toggle-button");
let toggleButtonState = "Rectangle";

// no need to clear canvas for refresh, page resets

// on click for canvas runs a function
canvas.onclick = (e) => {
    /* the difference between offsetX and clientX is that
    offsetX is focused on the element (for example the x coordinate
        relative to the canvas) while clientX is focused on 
    the page as a whole (the DOM) */
    console.log(e.offsetX, e.offsetY);

    if (toggleButtonState == "Rectangle") {
        ctx.fillStyle = randColor();
        /* if you make the width, height values negative, 
        you can build the rectangle from any corner */
        ctx.fillRect(e.offsetX, e.offsetY, 100, 200);
    } else {
        // beginPath starts listening for a method call to draw a certain
        // shape or path.
        ctx.beginPath();

        // arc draws the circle shape, but cannot immediatly be seen on the canvas
        ctx.arc(e.offsetX, e.offsetY, 5, 0, (2 * Math.PI));

        ctx.strokeStyle = randColor();

        // stroke adds an outline to the circle shape so that it can be seen
        ctx.stroke();

        ctx.fillStyle = randColor();

        // fill fills in the circle, finishing our shape
        ctx.fill();
    }
}

/* method called on toggleButton click which swaps the state of the button
and some styling properties as well as the innerHTML */
toggleButton.onclick = () => {
    if (toggleButtonState == "Rectangle") {
        toggleButtonState = "Dot";
        toggleButton.innerHTML = toggleButtonState;
        toggleButton.style.backgroundColor = "dodgerblue";
    } else {
        toggleButtonState = "Rectangle";
        toggleButton.innerHTML = toggleButtonState;
        toggleButton.style.backgroundColor = "cadetblue";
    }
}

const clearCanvas = () => {
    // clears the screen using the clearRect method. 
    // starts at 0, 0 and clears the space given by canvas width x canvas height
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// returns a random hex value for styling rectangles/dots
function randColor() {
    const colors = ["black", "dodgerblue", "cadetblue", "aquamarine", "green", "blue", "red", "maroon", "brown"];
    return colors[Math.floor(Math.random() * colors.length)];
}


/* event.preventDefault() prevents the default HTML behavior, assuming that no function
to override the default behavior exists. */