#!/usr/bin/node
const lit = process.argv;
if (lit[2]/2){
	console.log(`My number: ${parseInt(lit[2])}`);
} else {
	console.log("Not a number");
}
