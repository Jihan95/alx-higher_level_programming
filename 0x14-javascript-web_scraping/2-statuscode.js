#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

const options = {
  url: url,
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', res.statusCode);
});
