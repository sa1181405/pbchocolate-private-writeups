# vlookup_host_singles
Point count: 100pts

Difficulty: easy

Link: https://vlookup-hot-singles.jellyc.tf/

Provided files: vlookup_host_singles.zip

Description: looks like this is some kind of dating site for nerds? weird, figure out who the admin is and access their panel
# 

We are presented on the website with what looks like a messaging app. None of the buttons work besides the "Admin Panel" next to the users profile.

Upon visiting it, we cannot access the admin page and are simply given a denied access. From this, I decided to look at the cookies to see anything interesting. 

Our cookies show a `cf_clearance` cookie and a `token` cookie. 

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/bbceb63a-e6fa-4fb4-9ed0-612ca9cf6e0b)

Extension I used: [Extension](https://addons.mozilla.org/en-US/firefox/addon/edit-cookie/)

The token cookie looks to be in a jwt format, but we don't have a secret needed to sign a new jwt token and we don't know the admin account username.

Lets open the source!

```
#!/usr/bin/env python3
from io import BytesIO
from flask import Flask, request, send_file, redirect, url_for, make_response, send_from_directory
from openpyxl import load_workbook
import jwt

app = Flask(__name__)
# keep requests in memory to avoid disk exhaustion
# https://stackoverflow.com/a/28322143
# https://github.com/pallets/werkzeug/blob/2bcb43c3574de33b36174c6dc964182ccbc14a69/src/werkzeug/formparser.py#L59
app.config["MAX_CONTENT_LENGTH"] = 1024 * 500

# not redacted
JWT_SECRET = "singaQu5aeWoh1vuoJuD]ooJ9aeh2soh"

def is_admin(token):
    data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    return data["user"] == "jelly"

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def index():
    resp = make_response(send_file("chat.html"))
    resp.set_cookie('token', jwt.encode({"user":"starknight"}, JWT_SECRET, algorithm="HS256"))
    return resp

@app.route("/admin")
def admin():
    if not is_admin(request.cookies.get('token')):
        return "Unauthorized"

    return """
        <div>part 1 flag: jellyCTF{redacted}</div>
        <div>part 2:</div>
        <div>please upload a spreadsheet to populate with mutually beneficial partner candidates:</div>
        <form action="/spreadsheet" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="upload">
        </form>
    """

@app.route("/spreadsheet", methods=["POST"])
def spreadsheet():
    if not is_admin(request.cookies.get('token')):
        return "Unauthorized"
    
    if "file" not in request.files:
        return redirect(url_for("admin"))
    
    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("admin"))

    if file:
        wb = load_workbook(filename=file)
        ws = wb.active
        ws.append(["Username", "Email", "Socials", "Real Name", "Age", "Height", "Country", "MBTI", "Job", "Income", "Relationship status", "Favorite Sanrio Character", "Favorite Minecraft Version"])
        resp_sheet = BytesIO()
        wb.save(resp_sheet)
        resp_sheet.seek(0)
        return send_file(
            resp_sheet,
            download_name="your_location_has_been_recorded.xlsx",
            as_attachment=True,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```

Conveniently, the jwt secret is not redacted.
```
# not redacted
JWT_SECRET = "singaQu5aeWoh1vuoJuD]ooJ9aeh2soh"
```

And we know the admin account username being `jelly`

```
def is_admin(token):
    data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    return data["user"] == "jelly"
```

So, by using a site to sign new tokens (eg: jwt.io) we can just sign a token with the username `jelly` and with the secret.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/63e077bb-ab64-4df1-a7bc-c1df06e98ddb)

Lets modify the token cookie now with our new token.

Once done, by refreshing the page, we are redirected to this screen:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/fbe2c05f-22b6-425a-a102-9f2d1be4a14d)

And there is our flag!

Final flag: `jellyCTF{i_am_b3c0m3_awawa_d3str0y3r_0f_f3m4135}`

