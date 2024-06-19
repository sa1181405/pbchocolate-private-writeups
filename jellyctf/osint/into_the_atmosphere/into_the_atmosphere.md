# into_the_atmosphere
Point count: 559pts

Difficulty: medium

Provided files: N/A

Url: https://discord.gg/yG37ycs8t4

Description: my friend sent me an epic video in discord - I pasted the link into the #chal-into_the_atmosphere channel in the jellyCTF Discord.

what time was the channel the video was originally uploaded to created? (NOT when it was posted in the jellyCTF discord).

be accurate to the nearest millisecond, use UTC, and answer in ISO8601 or unix epoch format, e.g. one of:

    2024-04-30T17:59:00.995000+00:00
    2024-04-30T17:59:00.995+00:00
    2024-04-30T17:59:00.995000Z
    2024-04-30T17:59:00.995Z
    1714499940.995
    1714499940.995000

free hint: it's not in 2024
# 

You needed to grab the url of the video that was posted in that channel. The video itself is not related to the problem.

Url: `https://cdn.discordapp.com/attachments/225994578258427904/1249437169056088176/Punting_Jelly.mov?ex=6673d2ca&is=6672814a&hm=756470939eaa7c4db0d8338cb37dcb30d5c094f6890a82a4c732a8ddd703d677&`

The first set of numbers, `225994578258427904` (also called a snowflake) is the ID of the channel where the attachment was posted. Discord uses these IDs to uniquely identify different entities (like users, channels, messages, etc.) within its system.

With this ID, we can see the exact time the channel of the video was originally uploaded. 

A good website to search for snowflake ids is [snowsta.mp](https://snowsta.mp)

By inputting the channel ID, we are returned with:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/214aa2c0-2b18-45e1-aa7d-469eaebaa3fe)

There is the UNIX time! (be sure to toggle the "units" button to get to milliseconds!)

And now we have our flag!

Final flag: `1473951706233`
