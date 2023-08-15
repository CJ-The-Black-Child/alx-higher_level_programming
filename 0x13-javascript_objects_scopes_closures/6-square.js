#!/usr/bin/node
// Import the Square class from 5-square.js
const Square5 = require('./5-square');
// Define the Square class using the class notation and extends
class Square extends Square5 {
	// Defne the charPrint method that prints the rectangle
	// using the character c
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}

		for (let i = 0; i < this.height; i++) {
			console.log(c.repeat(this.width));
		}
	}
}

// Export the Square class
module.exports = Square;
