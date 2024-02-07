# JavaScript Web JQuery

This repository contains solutions to JavaScript tasks focusing on using jQuery for web development.

## Tasks

1. [No JQuery](./0-script.js)
   - **Requirements:**
     - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
       - You must use document.querySelector to select the HTML tag
       - You can’t use the JQuery API
   - **Test HTML File:** [0-main.html](./0-main.html)

2. [With JQuery](./1-script.js)
   - **Requirements:**
     - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [1-main.html](./1-main.html)

3. [Click and turn red](./2-script.js)
   - **Requirements:**
     - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header:
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [2-main.html](./2-main.html)

4. [Add `.red` class](./3-script.js)
   - **Requirements:**
     - Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag DIV#red_header
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [3-main.html](./3-main.html)

5. [Toggle classes](./4-script.js)
   - **Requirements:**
     - Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:
       - The `<header>` element must always have one class: red or green, never both at the same time and never empty.
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [4-main.html](./4-main.html)

6. [List of elements](./5-script.js)
   - **Requirements:**
     - Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item:
       - The new element must be: `<li>Item</li>`
       - The new element must be added to UL.my_list
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [5-main.html](./5-main.html)

7. [Change the text](./6-script.js)
   - **Requirements:**
     - Write a JavaScript script that updates the text of the `<header>` element to New Header!!! when the user clicks on DIV#update_header
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [6-main.html](./6-main.html)

8. [Star wars character](./7-script.js)
   - **Requirements:**
     - Write a JavaScript script that fetches the character name from the provided URL and displays it in the HTML tag DIV#character
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [7-main.html](./7-main.html)

9. [Star Wars movies](./8-script.js)
   - **Requirements:**
     - Write a JavaScript script that fetches and lists the title for all movies from the provided URL and displays them in the HTML tag UL#list_movies
       - You can’t use document.querySelector to select the HTML tag
       - You must use the JQuery API
   - **Test HTML File:** [8-main.html](./8-main.html)

10. [Say Hello!](./9-script.js)
    - **Requirements:**
      - Write a JavaScript script that fetches from the provided URL and displays the value of "hello" in the HTML tag DIV#hello.
      - The translation of “hello” must be displayed in the HTML tag DIV#hello
      - You can’t use document.querySelector to select the HTML tag
      - You must use the JQuery API
      - Your script must work when it is imported from the `<head>` tag
    - **Test HTML File:** [9-main.html](./9-main.html)

11. [No jQuery - document loaded](./100-script.js)
    - **Requirements:**
      - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):
        - You must use document.querySelector to select the HTML tag
        - You can’t use the jQuery API
      - Note: Your script must be imported from the `<head>` tag, not at the end of the HTML
    - **Test HTML File:** [100-main.html](./100-main.html)

12. [List, add, remove](./101-script.js)
    - **Requirements:**
      - Write a JavaScript script that adds, removes, and clears LI elements from a list when the user clicks:
        - The new element must be: `<li>Item</li>`
        - The new element must be added to UL.my_list
        - When the user clicks on DIV#add_item: a new element is added to the list
        - When the user clicks on DIV#remove_item: the last element is removed from the list
        - When the user clicks on DIV#clear_list: all elements of the list are removed
        - You can’t use document.querySelector to select the HTML tag
        - You must use the JQuery API
        - You script must work when imported from the `<head>` tag
    - **Test HTML File:** [101-main.html](./101-main.html)

13. [Say hello to everybody!](./102-script.js)
    - **Requirements:**
      - Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
        - You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
        - The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en, etc.)
        - The translation must be fetched when the user clicks on INPUT#btn_translate
        - The translation of “Hello” must be displayed in the HTML tag DIV#hello
        - You can’t use document.querySelector to select the HTML tag
        - You must use the JQuery API
        - You script must work when imported from the `<head>` tag
    - **Test HTML File:** [102-main.html](./102-main.html)

14. [And press ENTER](./103-script.js)
    - **Requirements:**
      - Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
        - You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
        - The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en, etc.)
        - The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
        - The translation of “Hello” must be displayed in the HTML tag DIV#hello
        - You can’t use document.querySelector to select the HTML tag
        - You must use the JQuery API
        - You script must work when imported from the `<head>` tag
    - **Test HTML File:** [103-main.html](./103-main.html)

