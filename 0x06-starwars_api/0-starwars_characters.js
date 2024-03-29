#!/usr/bin/node

const req = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
req(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the res body
  const charURLList = JSON.parse(body).characters;

  // loop through the character URLs
  // Make a req to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      req(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter formation & print the character's name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
