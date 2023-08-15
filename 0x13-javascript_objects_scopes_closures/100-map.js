#!/usr/bin/node
const list = require('./100-data').list;

// Use the map function to create a new list with each value multiplied by its index
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);

