
let canvas;
let context;

function drawImage(image) {
  // Set the canvas the same width and height of the image
  canvas.width = image.width;
  canvas.height = image.height;

  context.drawImage(image, 0, 0);
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function changeToWhite(data, pixels) {
    for (var i = 0; i < data.length * (1 - pixels); i++) 
    {
        data[index+3] = 0; 
    }
}

function main() {
    let image = document.querySelector("img");
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    drawImage(image); 
    let percent = 100; 
    let a = document.querySelector("h2");

    let forever = async () => {
        percent -= getRandomInt(10) / 5; 
        a.innerHTML = `${percent.toFixed(4)}`;
        let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
  
      changeToWhite(imageData.data, percent / 100);

      // Update the canvas with the new data
      context.putImageData(imageData, 0, 0);
    }
    setInterval(forever, 1000);
}

document.addEventListener("DOMContentLoaded", main);


