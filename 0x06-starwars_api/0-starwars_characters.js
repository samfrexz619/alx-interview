#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Makes an API request to get film information
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the res body
  const charURLList = JSON.parse(body).characters;

  // loop through the character URLs
  // Make a req to each character URL
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter formation & print the character's name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
