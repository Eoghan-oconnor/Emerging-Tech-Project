// Resources : https://www.w3schools.com/graphics/canvas_drawing.asp
//             http://www.williammalone.com/articles/create-html5-canvas-javascript-drawing-app/
//             http://bencentra.com/code/2014/12/05/html5-canvas-touch-events.html?fbclid=IwAR0mCUF5uZYTQUk4zXebQCWWw6Iau31fEsGhRm_OaMvRGNysZ5piTqP4LHA

// Variables
// Setting up Canvas

// debug
console.log("js file loaded");
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "#222222";
ctx.lineWith = 2;

// Setting up mouse event variables
var drawing = false;
var mousePosition = { x:0, y:0 };
var lastPosition = mousePosition;


//Debug
//console.log("before listeners");
// Captures mouse events
canvas.addEventListener("mousedown", function (e) {
    console.log("mousedown");
        drawing = true;
  lastPosition = getMousePos(canvas, e);
}, false);
canvas.addEventListener("mouseup", function (e) {
    console.log("mouseup");
  drawing = false;
}, false);
canvas.addEventListener("mousemove", function (e) {
    console.log("mouseup");
  mousePosition = getMousePos(canvas, e);
}, false);


// == Get mouse position ==
function getMousePos(canvasDom, mouseEvent) {
  var rect = canvasDom.getBoundingClientRect();
  return {
    x: mouseEvent.clientX - rect.left,
    y: mouseEvent.clientY - rect.top
  };
}



// == Gives regular intervals for draw animation ==
window.requestAnimFrame = (function (callback) {
  return window.requestAnimationFrame || 
     window.webkitRequestAnimationFrame ||
     window.mozRequestAnimationFrame ||
     window.oRequestAnimationFrame ||
     window.msRequestAnimaitonFrame ||
     function (callback) {
        window.setTimeout(callback, 1000/60);
     };
})();


// This function draws to the canvas
function renderCanvas() {
  if (drawing) {
    ctx.moveTo(lastPosition.x, lastPosition.y);
    ctx.lineTo(mousePosition.x, mousePosition.y);
    ctx.stroke();
    lastPosition = mousePosition;
  }
}

// Allows Animation

(function drawLoop () {
  requestAnimFrame(drawLoop);
  renderCanvas();
})();

// Button controller
$("#clearButton").click(function(e) {
    clearTheCanvas();
});

// Clear the canvas
function clearTheCanvas(){
    ctx.clearRect(0,0,150,200)
    document.getElementById("canvas").style.display = "none"
}

// button controller and data transfer for image.
$("#submitButton").click(function (e)
{
    console.log("submit")

    // prevent the form from submitting
    e.preventDefault();

    var Sendingdata = {"imageData": JSON.stringify(canvas.toDataURL())};
    console.log(Sendingdata);

    $.post("/image", Sendingdata, function(data){
        console.log(data);

         $("#prediction").text(data["prediction"]);
    });
});





