#!/usr/bin/node
// Define the converter function
exports.converter = function (base) {
	// Defineand return the inner converter function
	return function (number) {
		return number.toString(base);
	};
};
