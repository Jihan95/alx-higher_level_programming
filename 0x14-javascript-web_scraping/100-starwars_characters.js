#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
const request1 = require('request');

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const parsedBody = JSON.parse(body);
  const chars = parsedBody.characters;
  for (let i = 0; i < chars.length; i++) {
    request1.get(chars[i], (err1, res1, body1) => {
      if (err1) {
        console.log(err1);
      }
      console.log(JSON.parse(body1).name);
    });
  }
});
