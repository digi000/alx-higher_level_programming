#!/usr/bin/node
const myarr = process.argv
const al = myarr.length
if (al === 2)
{
	console.log("No argument");
} else if (al === 3){
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
