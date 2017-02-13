//Inspired from http://p5js.org/learn/examples/Math_Distance_2D.php

function setup() {
  createCanvas(700., 700);
  background(255,220,84);
}

var counter = 1000;
var spacer = 50;

function draw() {
	background(255,220,84);
	for (i = 0; i < width; i+=spacer) {
		for (j = 0; j < height; j+=spacer) {
			
			fill(0);
		
			var maxDistance = dist(0,0,width,height);
			
			
			var size = dist(mouseX,mouseY,i,j);
			
			size = size / maxDistance * 86;
			
			stroke(156,137,69,100);
			line(i, j, mouseX, mouseY);
			noStroke();
			ellipse(i, j, size, size);

		}
	}
}
