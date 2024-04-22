#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (!isNaN(times)) {
  for (let i = 0; i < times; i++) {
    for (let j = 0; j < times; j++) process.stdout.write('X');
    console.log();
  }
} else console.log('Missing size');
