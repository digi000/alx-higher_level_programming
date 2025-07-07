#!/usr/bin/node

request = require("request");

request(`${process.argv[2]}`, (e,r,b) => {
	js = JSON.parse(b);
	films = js.results;

	let i = 0;
	let count = 0;
	while(i < films.length) {
		let c = 0;
		while (c < films[i].characters.length) {
			parts = films[i].characters[c].split("/");
			id = Number(parts[parts.length - 2])
			if (id === 18) {
				count++;
			}
			c++;
		}
		i++;
	}
	console.log(count);
});
