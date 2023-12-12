#!/usr/bin/node

const numArray = require("./100-data");

const newArray = numArray.list.map((number, index) => number * index);
console.log(numArray.list);
console.log(newArray);
