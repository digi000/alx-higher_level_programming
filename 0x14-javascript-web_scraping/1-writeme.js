#!/usr/bin/node

filePath = process.argv[2];
text = process.argv[3];

fs = require('fs');

fs.writeFile(filePath, text, (err) => {
	if (err) {
		console.log(err);
	}
});
