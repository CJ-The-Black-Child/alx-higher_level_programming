#!/usr/bin/node
const fs = require('fs');
// Get command line arguments
const args = process.argv.slice(2);

if (args.length !==3) {
	console.error('Usage: ./102-concat.js <file1> <file2> <destiantion>');
	process.exit(1);
}

const file1Path = args[0];
const file2Path = args[1];
const destinationPath = args[2];

// Read the content of the first file
fs.readFile(file1Path, 'utf8', (err, data1) => {
		if (err) {
		console.error(`Error reading ${file1Path}: ${err}`);
		process.exit(1);
		}

		// Read the content of the second file
		fs.readFile(file2Path, 'utf8', (err, data2) => {
				if (err) {
				console.error(`Error reading ${file2Path}: ${err}`);
				process.exit(1);
				}

				// Concatenate the contents of both files
				const concatenatedData = data1 + data2;

				// Write the concatenated content to the
				// destination file
				fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
						if (err) {
						console.error(`Error writing to ${destinationPath}: ${err}`);
						process.exit(1);
						}

						console.log(`Files ${file1Path} and ${file2Path} concatenated and saved to ${destinationPath}`);
						});
				});
});
