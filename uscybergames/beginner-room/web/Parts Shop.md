Parts Shop

Point count: 150pts

Provided files: N/A

Description: We've found an online shop for robot parts. We suspect ARIA is trying to embody itself to take control of the physical world. You need to stop it ASAP! (Note: The flag is located in /flag.txt)

We are not provided with a source, so we must do some pentesting.

Once opening the website, we see many items for parts. However what caught my attention was the green plus icon on the bottom of the page.

Clicking on it, we are allowed to make parts. This is where a potential vulnerability may be in. 

Opening the source of the page, I noticed something out of the usual.

```

      var name = document.getElementById('name').value;
      var author = document.getElementById('author').value;
      var image = document.getElementById('image').value;
      var description = document.getElementById('description').value;

      var payload = '<?xml version="1.0" encoding="UTF-8"?>\n' +
        '<part>\n' +
        '  <name>' + name + '</name>\n' +
        '  <author>' + author + '</author>\n' +
        '  <image>' + image + '</image>\n' +
        '  <description>' + description + '</description>\n' +
        '</part>';
```

Hmmm, this section reminds me of a vulnerability called `XML External Entity (XXE)`

*XXE is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any backend or external systems that the application itself can access.* [Source](https://github.com/payloadbox/xxe-injection-payload-list)

So I tried different payloads from the source above. We know the file in `/flag.txt` from the description.

This payload worked

`<! DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag.txt"> ]>`

With `&xxe;` as the description to execute the payload.

I have had many difficulties trying to do this on the actual website, probably as something is blocking input. So I used burpsuite to execute this payload


![image(10)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/30b131e0-fa5d-489c-bbf1-32a7b31d77a2)


Seemed like it went through!

![image(11)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/666a83fb-e8a7-41a0-928a-4a4cecc60889)

Lets go back to the homepage. 

![image(12)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/24fcf14e-0bf1-4b08-91b8-bb24d1ce4d9e)

There it is! Our flag!

Final flag: `SIVBGR{fu11y_upgr4d3d}`


