# vlookup_hot_singles_2 
Point count: 766pts

Difficulty: hard

Provided files: N/A (same as first edition of challenge)

Description: oh. it's her. well, see if you can get the flag at /app/flag.txt and then get out of there
# 

This challenge did leave me stuck for a while, as I had no idea how to create spreadsheet type vulnerabilities. I kept digging around the source code, and noticed something unusual.

The pipfile had certian libraries installed on a specific version.

```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
openpyxl = "==2.4.1"
lxml = "==4.9.4"
flask = "*"
pyjwt = "*"

[dev-packages]

[requires]
python_version = "3.11"
```

Huh, why is openpyxl forced to install on version 2.4.1?

Lets google and see if there are any vulnerabilities specific to that version.

And there is!

There is XML External Entity (XXE) on that library!

*openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files Openpyxl 2.4.1 resolves external entities by default, which allows remote attackers to conduct XXE attacks via a crafted .xlsx document.*

*XXE Injection is a type of attack against an application that parses XML input. XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. By default, many XML processors allow specification of an external entity, a URI that is dereferenced and evaluated during XML processing. When an XML document is being parsed, the parser can make a request and include the content at the specified URI inside of the XML document.*
[Source](https://security.snyk.io/vuln/SNYK-PYTHON-OPENPYXL-40459)

Okay, now that we know there is XXE in this library, this should be pretty straight forward.

During my research process, I came across a proof of concept of a security researcher conducting this. [POC](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=854442)

xlsx files are actually zip files, so we can rename the xlsx file the POC gave us to .zip and see whats inside.

Looking around, we see something in docProps/core.xml

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///app/flag.txt" >]><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:creator>Ulikowski, Marcin</dc:creator><cp:lastModifiedBy>Ulikowski, Marcin</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">2017-01-31T09:02:33Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2017-01-31T09:02:53Z</dcterms:modified><dc:subject>&xxe;</dc:subject></cp:coreProperties>
```
*Note: the file:///app/flag.txt was renamed to this for the purpose of getting the flag. Originally, in the POC, it wanted to read passwd.*

Thats it! So we can just modify what the POC gave us to read /app/flag.txt

Zip all the spreadsheet files back into a .zip file. Rename it to .xlsx, and upload it to the website!

The website gives us a `your_location_has_been_recorded.xlsx`

Opening this does not show anything. What took me a while was that the POC injected the XXE into the subject metadata of the spreadsheet.

It wasn't until I tried moving the file to my linux home directory while the spreadsheet was opened to notice it.

How did I notice it? Well windows tells you that you can't move files if the app is open, and I tried to, and I noticed that the flag was in the subject metadata!

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/9f4bcef5-946c-42ed-9827-4b3fc4795a44)

There is our flag! Lesson learned, always read the payloads in proof of concepts fully!

Final flag: `jellyCTF{th1s_1snt_a_r3d_0n3_r1gh7?}`
