#!/usr/bin/node
// This script prints all characters of a Star wars movie

const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;
request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
