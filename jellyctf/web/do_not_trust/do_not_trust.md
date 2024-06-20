# do_not_trust
Point count: 100pts

Difficulty: easy

Provided files: N/A

Description: there's a flag hidden somewhere on this site (jellyc.tf) in a common location for websites, see if you can find it
# 

The common location that the description refers to is the `robots.txt` file. This file is for crawlers to see what the crawler can access in terms of certain URLs.

Upon visiting `jellyc.tf/robots.txt`, we are presented with:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/9d9e2a6b-525d-4616-93d5-9bbdce36d69a)


There it is! Our flag!

Final flag: `jellyCTF{g0d_d4mn_cL4nk3r5}`
