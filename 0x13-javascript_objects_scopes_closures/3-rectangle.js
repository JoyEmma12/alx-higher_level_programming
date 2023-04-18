#!/usr/bin/node

module.exports = class Rectangle {
   constructor (w, h) {
	   if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0)  {
		   this.width = w;
		   this.width = h;
	   }
   }


print () {
	for (let i = 0; i < this.height; ++i)  {
		let j = 0;

		for (; j < this.width; ++j) {
			process.stdout.write('X');
		}

		if (j === this.width)  {
			console.log('');
		}
	}
}
};
