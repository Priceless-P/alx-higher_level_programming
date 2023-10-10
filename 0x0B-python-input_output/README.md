# 0x0B. Python - Input/Output

This repository contains Python scripts and programs related to input and output operations in Python.

## Tasks

### 0. Read file
**File:** [0-read_file.py](0-read_file.py)

Write a function that reads a text file (UTF8) and prints it to stdout.

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement.
- You don't need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.

### 1. Write to a file
**File:** [1-write_file.py](1-write_file.py)

Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement.
- You don't need to manage file permission exceptions.
- Your function should create the file if it doesn't exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module.

### 2. Append to a file
**File:** [2-append_write.py](2-append_write.py)

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

- Prototype: `def append_write(filename="", text=""):`
- If the file doesn't exist, it should be created.
- You must use the `with` statement.
- You don't need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.

### 3. To JSON string
**File:** [3-to_json_string.py](3-to_json_string.py)

Write a function that returns the JSON representation of an object (string).

- Prototype: `def to_json_string(my_obj):`
- You don't need to manage exceptions if the object can't be serialized.

### 4. From JSON string to Object
**File:** [4-from_json_string.py](4-from_json_string.py)

Write a function that returns an object (Python data structure) represented by a JSON string.

- Prototype: `def from_json_string(my_str):`
- You don't need to manage exceptions if the JSON string doesn't represent an object.

### 5. Save Object to a file
**File:** [5-save_to_json_file.py](5-save_to_json_file.py)

Write a function that writes an Object to a text file, using a JSON representation.

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement.
- You don't need to manage exceptions if the object can't be serialized.
- You don't need to manage file permission exceptions.

### 6. Create object from a JSON file
**File:** [6-load_from_json_file.py](6-load_from_json_file.py)

Write a function that creates an Object from a "JSON file."

- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement.
- You don't need to manage exceptions if the JSON string doesn't represent an object.
- You don't need to manage file permissions/exceptions.

### 7. Load, add, save
**File:** [7-add_item.py](7-add_item.py)

Write a script that adds all arguments to a Python list and then saves them to a file.

- You must use your function `save_to_json_file` from [5-save_to-json-file.py](5-save_to-json-file.py).
- You must use your function `load_from_json_file` from [6-load-from-json-file.py](6-load-from-json-file.py).
- The list must be saved as a JSON representation in a file named `add_item.json`.
- If the file doesn't exist, it should be created.
- You don't need to manage file permissions/exceptions.

### 8. Class to JSON
**File:** [8-class_to_json.py](8-class_to_json.py)

Write a function that returns the dictionary description with simple data structures (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class.
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer, and boolean.
- You are not allowed to import any module.

### 9. Student to JSON
**File:** [9-student.py](9-student.py)

Write a class `Student` that defines a student by:

- Public instance attributes: `first_name`, `last_name`, `age`.
- Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`).
- You are not allowed to import any module.

### 10. Student to JSON with filter
**File:** [10-student.py](10-student.py)

Extend the `Student` class from task 9 to include a public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):

- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
- Otherwise, all attributes must be retrieved.
- You are not allowed to import any module.

### 11. Student to disk and reload
**File:** [11-student.py](11-student.py)

Extend the `Student` class from task 10 to include a public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:

- You can assume `json` will always be a dictionary.
- A dictionary key will be the public attribute name.
- A dictionary value will be the value of the public attribute.
- You are not allowed to import any module.

### 12. Pascal's Triangle
**File:** [12-pascal_triangle.py](12-pascal_triangle.py)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal's triangle of `n`:

- Returns an empty list if `n <= 0`.
- You can assume `n` will always be an integer.
- You are not allowed to import any module.

### 13. Search and update (Advanced)
**File:** [100-append_after.py](100-append_after.py)

Write a function `def append_after(filename="", search_string="", new_string=""):`

- Inserts a line of text to a file after each line containing a specific string (see example).
- You must use the `with` statement.
- You don't need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module.

### 14. Log parsing (Advanced)
**File:** [101-stats.py](101-stats.py)

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (see example below).
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    - Total file size: `File size: <total size>`
    - where `<total size>` is the sum of all previous `<file size>` (see example below).
    - Number of lines by status code:
        - possible status codes are `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500` (see example below).
        - if a status code doesn't appear or is not an integer, don't print anything for this status code.
        - format: `<status code>: <number>`
        - status codes should be printed in ascending order.
