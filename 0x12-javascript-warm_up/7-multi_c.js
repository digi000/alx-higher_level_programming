#!/usr/bin/node
const lit = process.argv;
const mk = "C is fun"
if (lit[2]/2){
	let i;
	for(i = 0; i < parseInt(lit[2]); i++){
		console.log(mk);
	}
} else {
	console.log("Missing number of occurrences");
}
