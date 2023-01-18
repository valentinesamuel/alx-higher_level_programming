#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 2) {
  process.exit();
}

let fs = require('fs');
fs.writeFile(args[0], args[1], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
