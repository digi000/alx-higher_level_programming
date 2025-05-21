#!/usr/bin/node
const lit = process.argv;
if (lit[2]/2){
	let i;
	for(i = 0; i < parseInt(lit[2]); i++){
		console.log("C is fun");
	}
} else {
	console.log("Missing number of occurrences");
}
