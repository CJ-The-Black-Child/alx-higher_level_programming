#!/usr/bin/node
// Define the nbOccurences function
exports.nbOccurences = function (list, searchElement) {
	// Initialize a counter for occurrences
	let count = 0;

	// Iterate through the list and count occurences of searchElement
	for (let element of list) {
		if (element === searchElement) {
			count++;
		}
	}

	// Return the total count of occurrences
	return count;
};
