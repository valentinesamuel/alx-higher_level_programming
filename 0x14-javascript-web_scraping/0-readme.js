#!/usr/bin/node
let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 1) {
  process.exit();
}

let fs = require('fs');
fs.readFile(args[0], 'utf8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
