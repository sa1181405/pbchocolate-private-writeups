# stalknights_4
Writeup author: **lolmenow**

Point count: 643pts

Difficulty: medium

Provided files: N/A

Description: What is the real name of this starknight? Flag format: jellyCTF{firstname_lastname}

# 

Going back to the twitter page, we can see the following tweet:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/af356caf-f72a-4808-a032-80df8788ef89)

From this, we can assume that starknight1337 has a github. Lets search this person up!

And indeed, starknight1337 does have a github. [Github](https://github.com/starknight1337)

Now, from prior knowledge, names can be leaked if you don't hide them while doing commits. So, instead of going through all the commits, I thought "why not just use the API and query the repo and the username?"

So, I used curl to query the API, here is my request:

`curl -H "Accept: application/vnd.github+json" https://api.github.com/repos/starknight1337/rustlings_practice/events `

*Rustlings_practice is the repo that starknight1337 owns*

*application/vnd.github+json is needed to query githubs api as it is a custom media type*

Running this, we are presented with:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/736e18e9-c628-4db4-a3d6-7428ab04948a)

There is the name! And our flag!

Final flag: `jellyCTF{luke_ritterman}`
