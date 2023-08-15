#!/usr/bin/node
const dict = require('./101-data').dict;

// Define an empty object to store the new dictionary
const occurrencesByUsers = {};

// Iterate through the original dictionary and populate the new dictionary
for (let userId in dict) {
	const occurrences = dict[userId];
	if (!occurrencesByUsers[occurrences]) {
		occurrencesByUsers[occurrences] = [];
	}
	occurrencesByUsers[occurrences].push(userId);
}

console.log(occurrencesByUsers);
