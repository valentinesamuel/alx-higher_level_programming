#!/usr/bin/node
const request = require('request');
let args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('Error');
  process.exit();
} else if (args.length !== 1) {
  console.log('Error');
  process.exit();
}

let url = args[0];
request(url, function (error, response, body) {
  if (error) { // Handle error if one occurred
    console.log(error);
    process.exit();
  }
  if (response.statusCode === 200) {
    let count = 0;
    let films = JSON.parse(body).results;

    // For every movie
    for (let i = 0; i < films.length; i++) {
      // For every character
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].endsWith('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
