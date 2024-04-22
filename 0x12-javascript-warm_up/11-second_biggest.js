#!/usr/bin/node
const args = process.argv.length;
if (args <= 3) { console.log(0); } else {
  let num = parseInt(process.argv[2]);
  for (let i = 3; !isNaN(process.argv[i]); i++) {
    if (parseInt(process.argv[i]) > num) num = parseInt(process.argv[i]);
  }
  let result = parseInt(process.argv[2]);
  for (let i = 3; !isNaN(process.argv[i]) && parseInt(process.argv[i]) !== num; i++) {
    if (parseInt(process.argv[i]) > result) result = parseInt(process.argv[i]);
  }
  console.log(result);
}
