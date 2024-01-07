# 0x10-python-network_0
## Tasks

0. [cURL body size](0-body_size.sh)
   - Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
   - The size must be displayed in bytes using `curl`.
   - Test the script using the web server running on port 5000.

1. [cURL to the end](1-body.sh)
   - Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
   - Display only the body of a 200 status code response using `curl`.
   - Test the script using the web server running on port 5000.

2. [cURL Method](2-delete.sh)
   - Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
   - Use `curl` to send the request.
   - Test the script using the web server running on port 5000.

3. [cURL only methods](3-methods.sh)
   - Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
   - Use `curl` to retrieve this information.
   - Test the script using the web server running on port 5000.

4. [cURL headers](4-header.sh)
   - Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
   - Send a header variable `X-School-User-Id` with the value `98` using `curl`.
   - Test the script using the web server running on port 5000.

5. [cURL POST parameters](5-post_params.sh)
   - Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
   - Send variables `email` with value `test@gmail.com` and `subject` with value `I will always be here for PLD` using `curl`.
   - Test the script using the web server running on port 5000.

6. [Find a peak](6-peak.py), [6-peak.txt](6-peak.txt)
   - Write a function that finds a peak in a list of unsorted integers.
   - Function prototype: `def find_peak(list_of_integers):`
   - The algorithm must have the lowest complexity (O(log(n)), O(n), O(nlog(n)), or O(n^2)).
   - There may be more than one peak in the list.
   - Test cases are provided in `6-main.py`.

7. [Only status code](100-status_code.sh)
   - Write a Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.
   - Use `curl` without using pipes, redirection, `;`, `&&`, or similar constructs.
   - Test the script using the web server running on port 5000.

8. [cURL a JSON file](101-post_json.sh)
   - Write a Bash script that sends a JSON POST request to a URL passed as the first argument and displays the body of the response.
   - Send the contents of a file (passed with the filename as the second argument) in the body of the POST request.
   - Test the script using the web server running on port 5000.

9. [Catch me if you can!](102-catch_me.sh)
   - Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` causing the server to respond with a message containing `You got me!` in the body of the response.
   - Use `curl` without using `echo`, `cat`, or similar commands.
   - Test the script using the web server running on port 5000.
