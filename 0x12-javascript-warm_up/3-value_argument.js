#!/usr/bin/node
const lit = process.argv;
let i = 0;
lit.forEach(item => {i++});
if (i === 2)
{
	console.log("No argument");
} else {
	console.log(lit[2]);
}
