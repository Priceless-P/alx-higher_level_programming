#!/usr/bin/node
const dict = require("./101-data");
const newDict = {};

const uniqueKeys = [...new Set(Object.values(dict.dict))];

for (let index = 0; index < uniqueKeys.length; index++) {
  const keysWithSameValue = Object.keys(dict.dict).filter(
    (key) => dict.dict[key] === uniqueKeys[index]
  );
  newDict[uniqueKeys[index]] = keysWithSameValue;
}
console.log(newDict);
