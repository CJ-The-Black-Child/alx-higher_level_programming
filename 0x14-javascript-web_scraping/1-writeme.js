#!/usr/bin/node

const fs = require('fs');
const string = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
