#!/usr/bin/node
// Define the Rectangle class using the class notation
class Rectangle {
	constructor(w, h) {
		// Check if width and height are +ve integers
		if (w > 0 && h > 0) {
			// intiailze instance attributes width and height
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
}

// Export the Rectangle class
module.exports = Rectangle;
