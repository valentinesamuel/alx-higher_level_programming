#!/usr/bin/node

let request = require('request');

let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('No argument');
} else if (args.length !== 1) {
  process.exit();
}

request(args[0], function (error, response, body) {
  if (error) {
    // Handle error if one occurred
  }
  console.log('code:', response && response.statusCode); // Print response status code if a response was received
  // console.log('body: ', body); // Print the HTML of webpage
});
