// console.log("Hello") Debug to make sure the js file was linking the Home.html

// Resources : https://www.w3schools.com/graphics/canvas_drawing.asp
//             http://www.williammalone.com/articles/create-html5-canvas-javascript-drawing-app/
//             http://bencentra.com/code/2014/12/05/html5-canvas-touch-events.html?fbclid=IwAR0mCUF5uZYTQUk4zXebQCWWw6Iau31fEsGhRm_OaMvRGNysZ5piTqP4LHA

// Variables
// Setting up Canvas
var canvas = document.getElementById("numberCanvas");
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "#222222"
ctx.lineWidth = 2;

// Setting up mouse events
var drawing = false;
var mousePosition = { x:0, y:0 };
var lastPosition = mousePosition;

// Captures mouse events
canvas.addEventListener("mousedown", function (e) {
        drawing = true;
    lastPos = getMousePos(canvas, e);
    }, false);
    canvas.addEventListener("mouseup", function (e) {
    drawing = false;
    }, false);
    canvas.addEventListener("mousemove", function (e) {
    mousePos = getMousePos(canvas, e);
    }, false);

    // Get the position of the mouse relative to the canvas
    function getMousePos(canvasDom, mouseEvent) {
    var rect = canvasDom.getBoundingClientRect();
    return {
    x: mouseEvent.clientX - rect.left,
    y: mouseEvent.clientY - rect.top
    };
}
