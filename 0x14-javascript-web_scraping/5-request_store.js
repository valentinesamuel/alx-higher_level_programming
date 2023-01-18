#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 2) {
  process.exit();
}

let url = args[0];
let destFilename = args[1];
let request = require('request');
request(url, function (error, response, body) {
  if (error) {
    // Handle error if one occurred
  }
  if (response.statusCode === 200) {
    let fs = require('fs');
    fs.writeFile(destFilename, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    process.exit();
  }
});
