#!/usr/bin/node
// Must install module, sync-request with
// $npm install sync-request

let args = process.argv.slice(2);
if (args[0] === undefined) { // No user argument
  process.exit();
} else if (args.length !== 1) {
  process.exit();
}

let base = 'http://swapi.co/api/films/' + args[0] + 'schema';
const promiseSerial = funcs =>
  funcs.reduce((promise, func) =>
    promise.then(result => func().then(Array.prototype.concat.bind(result))),
    Promise.resolve([]))

let request = require('request');
let charList = [];
request(url, function (error, response, body) {
  if (error) {
    // Handle error if one occurred
  }
  if (response.statusCode === 200) {
    let characters = body['characters'];
    characters.forEach(function (element2) {
      request(element2, function (error2, response2, body2) {
        if (error2) { // Handle error if one occurred
        }
        if (response2.statusCode === 200) {
          console.log(body2['name']);
        }
      });
    });
  }
});




// some url's to resolve
const urls = ['/url1', '/url2', '/url3']

// convert each url to a function that returns a promise
const funcs = urls.map(url => () => $.ajax(url))

// execute Promises in serial
promiseSerial(funcs)
  .then(console.log.bind(console))
