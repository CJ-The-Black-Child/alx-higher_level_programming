#!/usr/bin/node
// Initialize the counter for printed arguments
let numPrinted = 0;

// Define the logMe function
exports.logMe = function (item) {
	// Print the number of arguments already printed and the current argument value
	console.log(`${numPrinted}: ${item}`);
	numPrinted++;
	//Increments the counter for printed arguments
};
