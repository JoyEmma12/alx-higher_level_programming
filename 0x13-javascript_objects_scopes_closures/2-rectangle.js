#!/usr/bin/node

module.exports = class Rectangle {
	constructor(w, h)  {
		if (((w || h) === 0) || ((w || h) === 'number'))  {
			this.width = w;
			this.height = h;
		}
	}
};
