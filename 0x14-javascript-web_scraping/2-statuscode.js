#!/usr/bin/node

request = require('request')

request(process.argv[2], (err, res) => {
	console.log(`code: ${res.statusCode}`);
});
