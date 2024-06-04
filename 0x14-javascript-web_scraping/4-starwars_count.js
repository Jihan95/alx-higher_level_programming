#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;

    for (let j = 0; j < characters.length; j++) {
      if (characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
