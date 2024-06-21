# stalknights_5
Point count: 925pts

Difficulty: medium

Provided files: N/A

Description: What a weird username this starnerd starknight has. I wonder what hobbies they're into.

Maybe they have an account not mentioned on social media. Find the flag on their account's profile page.

Flag format: jellyCTF{flag_on_profile_page}

Note: The results of previous challenges are not relevant for this challenges (though clues from those sites may help)

# 

Remember how I was talking about why I did not check the "taken" accounts first from https://instantusername.com/ in my stalknight_3 writeup?

Well, instantusername.com query to all the different API's are actually broken!

How did I find this out? I manually went through each website that says it was "available" and manually checked if it was actually available. Sure enough, one of the websites had the flag!

https://leetcode.com/u/starknight1337/

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/06190cf8-9d1e-4c3b-a3b4-d94289543d46)

What did instantusername.com say?

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/756dc4e4-8255-4920-a17f-1b60a7a1c1ed)

Moral of the story: don't trust automated tools to a great extent!

Final flag: `jellyCTF{1337code_0n_str34m}`

*Update: Apparently GPT-4 could've helped you solve this problem?! WHAT?! You can view the convo in this directory titled "gpt-sn5-convo (read writeup before viewing).txt"*

*Thanks darklight_03 on discord for the GPT convo, he used it to actually get the site leetcode! Wow, AI might take over the world?!*
