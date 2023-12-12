#!/usr/bin/node

const fs = require('fs');
const [, , file1, file2, destFile] = process.argv;

const contentsFile1 = fs.readFileSync(file1, 'utf8');
const contentsFile2 = fs.readFileSync(file2, 'utf8');

const bothContents = `${contentsFile1.trim()}\n${contentsFile2.trim()}\n`;

fs.writeFileSync(destFile, bothContents);
