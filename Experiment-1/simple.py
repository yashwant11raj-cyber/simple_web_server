from http.server import HTTPServer,BaseHTTPRequestHandler
content='''<html>
<head>
    <title>My Laptop Configuration</title>
    <style>
        table, th, td, tr {
            border: 2px solid black;
            border-collapse: collapse;
        }
        table {
            margin-left: auto;
            margin-right: auto;
            background-color: #f2f2f2;
        }
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
</body>
</html>'''
class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8080)
httpd=HTTPServer(server_address,Myserver)
httpd.serve_forever()