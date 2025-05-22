#!/usr/bin/node
class Rectangle
{
	constructor(w,h)
	{
		if (w >= 1 && h >= 1)
		{
			this.width = w;
			this.height = h;
		}
	}

	print()
	{
		let i;
		for (i = 0; i < this.height; i++)
		{
			console.log('x'.repeat(this.width));
		}
	}
}
module.exports = Rectangle;
