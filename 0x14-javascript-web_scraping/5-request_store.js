#!/usr/bin/node

request = require("request");
fs = require("fs");

request(process.argv[2], (e,r,b) => {
	fs.writeFile(process.argv[3], b, () => {});
});
