# stalknights_3 
Point count: 100pts

Difficulty: medium

Provided files: N/A

Description: 

> Hmm, I wonder where this starknight is from...

Find the city and country where this starknight lives.

Flag format: jellyCTF{name_of_city,name_of_country}

Note: This challenge does not required paid services and can be done only using free tools
# 

Lets query starknight1337 (we know this is the username from the instagram profile) on a username checker website. I like to use this [website](https://instantusername.com/) to check usernames on common social media sites. 

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/e23755b5-c104-4873-b472-79e842603788)

Lets check out their twitter.

*But why won't you check the ones that say taken first? This will be further explained in my stalknights_5 writeup.*


Scrolling down, we see a post about an picking up their friend at an airport.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/836d92d7-3f7c-4023-b203-1f1836af0e92)

We must identify where the plane landed so we can see where this individual lives.

Reverse image searching the plane returns this website:

https://www.ana.co.jp/en/jp/international/theme/pikachujet/

The website gives us the plane number as JA784A

We can put this into flighera.net to see the historical flights

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/9dd88787-59c7-401e-b8a3-3c9cde362385)


Clicking on "View all" in recent flights

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/e3775445-0ae1-4fb1-8a7f-93f82fa93929)

Gives us the historic flight paths for this specific aircraft.

We know the image was taken somewhere around May 9th, so lets see the arrival of this plane at around this time.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/1e1f195e-738e-4ebd-bb05-cc1e7958c081)

The exact date of May 9th is not shown, so I guessed until I got it correct!

Final flag: `jellyCTF{san_francisco,united_states}`




