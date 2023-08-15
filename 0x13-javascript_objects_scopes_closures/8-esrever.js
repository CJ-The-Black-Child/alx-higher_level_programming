#!/usr/bin/node
// Define the esrever function
exports.esrever = function (list) {
	// Create an empty array to store the reversed elements
	const reversedList = [];

	// Iterate through the list in reverse order and add elements to the new array
	for (let i = list.length - 1; i >= 0; i--) {
		reversedList.push(list[i]);
	}

	// Return the reversed array
	return reversedList;
};
