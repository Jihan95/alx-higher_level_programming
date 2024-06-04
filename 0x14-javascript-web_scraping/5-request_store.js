#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    }
  });
});
