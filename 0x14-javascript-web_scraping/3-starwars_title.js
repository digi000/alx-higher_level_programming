#!/usr/bin/node

request = require("request");

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (e, r, b) => {
	js = JSON.parse(b);
	console.log(js.title);
});
