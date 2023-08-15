#!/usr/bin/node
// Define the Rectangle class using the class notation
class Rectangle {
	constructor(w, h) {
		// Check if width and height are +ve integers
		if (w > 0 && h > 0) {
			// Initialize Instance attributes width and height
			this.width = w;
			this.height = h;
		}
	}

	//Define the print method to print the rectangle using the character X
	print() {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}

	//Define the rotate method to exchange width and height
	rotate() {
		[this.width, this.height] = [this.height, this.width];
	}

	//Define the double method to multiply width and height by 2
	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

// Export the Rectangle class
module.exports = Rectangle;
