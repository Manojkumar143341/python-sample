#!/usr/bin/env python3

import cgi
import datetime

form = cgi.FieldStorage()
name = form.getvalue("name")
message = form.getvalue("message")

with open("data.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} - {name}: {message}\n")

print("Content-type: text/html\n")
print("<html><body>")
print("<h3>Thanks for your message!</h3>")
print("<a href='/index.html'>Go back</a>")
print("</body></html>")
