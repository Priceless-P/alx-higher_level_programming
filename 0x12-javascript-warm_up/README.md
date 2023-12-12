# JavaScript Warm-Up

This repository contains a series of JavaScript scripts aimed at practicing JavaScript basics.

## Tasks

0. [First constant, first print](0-javascript_is_amazing.js)
    - Write a script that prints "JavaScript is amazing".
    - Create a constant variable called `myVar` with the value "JavaScript is amazing".
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

1. [3 languages](1-multi_languages.js)
    - Write a script that prints three lines:
        - "C is fun"
        - "Python is cool"
        - "JavaScript is amazing"
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

2. [Arguments](2-arguments.js)
    - Write a script that prints a message depending on the number of arguments passed:
        - If no arguments, print "No argument"
        - If one argument, print "Argument found"
        - Otherwise, print "Arguments found"
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Reference: `process.argv`.

3. [Value of my argument](3-value_argument.js)
    - Write a script that prints the first argument passed to it:
        - If no arguments, print "No argument"
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Not allowed to use `length`.

4. [Create a sentence](4-concat.js)
    - Write a script that prints two arguments passed to it in the format: " is "
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

5. [An Integer](5-to_integer.js)
    - Write a script that prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer.
        - If argument can't be converted, print "Not a number"
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Not allowed to use `try/catch`.

6. [Loop to languages](6-multi_languages_loop.js)
    - Write a script that prints three lines using an array of strings and a loop:
        - "C is fun"
        - "Python is cool"
        - "JavaScript is amazing"
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Not allowed to use any if/else statement.
    - Use only one `console.log`.
    - Use a loop (while, for, etc.).

7. [I love C](7-multi_c.js)
    - Write a script that prints "C is fun" x times, where x is the first argument of the script.
        - If the first argument can't be converted to an integer, print "Missing number of occurrences".
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Use only two `console.log`.
    - Use a loop (while, for, etc.).

8. [Square](8-square.js)
    - Write a script that prints a square.
        - The first argument is the size of the square.
        - If the first argument can't be converted to an integer, print "Missing size".
        - Use the character X to print the square.
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.
    - Use a loop (while, for, etc.).

9. [Add](9-add.js)
    - Write a script that prints the addition of two integers.
        - The first argument is the first integer.
        - The second argument is the second integer.
        - Define a function `add(a, b)`.
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

10. [Factorial](10-factorial.js)
    - Write a script that computes and prints a factorial.
        - The first argument is an integer used for computing the factorial.
        - Factorial of NaN is 1.
        - Do it recursively.
        - Use a function.
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

11. [Second biggest!](11-second_biggest.js)
    - Write a script that searches the second biggest integer in the list of arguments.
        - If no argument passed, print 0.
        - If the number of arguments is 1, print 0.
    - Use `console.log(...)` to print all output.
    - Not allowed to use `var`.

12. [Object](12-object.js)
    - Update a script to replace the value 12 with 89 in an object.
    - Not allowed to use `var`.

13. [Add file](13-add.js)
    - Write a function that returns the addition of 2 integers.
        - The function must be visible from outside.
        - The name of the function must be `add`.
    - Not allowed to use `var`.

14. [Const or not const](100-let_me_const.js)
    - Write a file that modifies the value of `myVar` to 333.
    - This exercise doesn’t pass semistandard, so no worries about it.

15. [Call me Moby](101-call_me_moby.js)
    - Write a function that executes x times a function.
        - The function must be visible from outside.
        - Prototype: `function (x, theFunction)`.
    - Not allowed to use `var`.
