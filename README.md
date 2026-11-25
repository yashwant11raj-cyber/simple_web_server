# EX01 Developing a Simple Webserver

# Date: 17/10/2026

# AIM:

To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:

## Step 1:

HTML content creation.

## Step 2:

Design of webserver workflow.

## Step 3:

Implementation using Python code.

## Step 4:

Serving the HTML pages.

## Step 5:

Testing the webserver.

# PROGRAM:

simple.py

```
from http.server import HTTPServer,BaseHTTPRequestHandler
content='''<html>
<head>
    <title>My Laptop Configuration</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #fafafa; }
        table, th, td, tr {
            border: 2px solid black;
            border-collapse: collapse;
        }
        table {
            margin-left: auto;
            margin-right: auto;
            background-color: #f2f2f2;
        }
        th, td { padding: 8px 12px; text-align: left; }
        th { background-color: #0b5ed7; color: white; }
        tr { background-color: #e6e6e6; }
        tr:hover { background-color: #ffe9a8; }
    </style>
</head>
<body>
<table>
    <caption><h1>My Laptop Configuration</h1></caption>
    <tr>
        <th>Component</th>
        <th>Specification</th>
    </tr>
    <tr>
        <td>CPU</td>
        <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
    </tr>
    <tr>
        <td>Installed RAM</td>
        <td>16.0 GB (15.7 GB usable)</td>
    </tr>
    <tr>
        <td>Storage</td>
        <td>110 GB of 477 GB used</td>
    </tr>
    <tr>
        <td>Graphics card</td>
        <td>Intel(R) Graphics (128 MB)</td>
    </tr>
    <tr>
        <td>System type</td>
        <td>64-bit operating system, x64-based processor</td>
    </tr>
    <tr>
        <td>Pen and touch support</td>
        <td>No pen or touch input is available for this display</td>
    </tr>
    <tr>
        <td>OS</td>
        <td>Windows 11 Home Single Language</td>
    </tr>
</table>
<p style="text-align:center">Name: YASHWANT RAJ P | Reg No: 26006135</p>
</body>
</html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received for path: ",self.path)
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8080)
httpd=HTTPServer(server_address,Myserver)
httpd.serve_forever()
```

# OUTPUT:

![alt text](<Screenshot 2026-11-25 203735.png>)
![alt text](<Screenshot 2026-11-25 203751.png>)
![alt text](<Screenshot 2026-11-25 203808.png>)

# RESULT:

The simple web server was developed using Python's http.server module. The laptop configuration page was served and tested successfully at 127.0.0.1:8080.
