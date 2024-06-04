#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title)
});
