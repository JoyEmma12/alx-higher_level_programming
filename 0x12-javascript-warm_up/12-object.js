#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

const valueToReplace = 'value';
const newValue = 89;

myObject[valueToReplace] = newValue;

console.log(myObject);
