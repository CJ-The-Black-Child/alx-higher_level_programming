#!/usr/bin/node
const rounds = process.argv.length;
console.log(rounds === 2 ? "No argument" : rounds === 3 ? "Argument found" : 'Arguments found');
