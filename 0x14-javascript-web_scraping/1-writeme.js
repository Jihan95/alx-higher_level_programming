#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
const text = args[1];

fs.writeFile(args[0], text, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
