#!/usr/bin/node
// Import the rectangle from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define the Square class using the class notation and extends
class Square extends Rectangle {
	constructor(size) {
		// Call the constructor of the Rectangle class using super()
		super(size, size);
	}
}

// Export the Square class
module.exports = Square;
