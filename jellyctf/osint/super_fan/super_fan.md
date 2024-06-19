# super_fan
Point count: 856pts

Difficulty: hard

Provided files: N/A

Description: this guy is like some kind of jelly superfan or something... what a weirdo. he deleted all his old tweets and changed his username, can you find his new handle?

`@j3llyfan7`

note: unrelated to the stalknights challenges
# 

We are given with a twitter handle and know that this user has changed their username, NOT deleted their account. Lets check the way back machine and see if this tiwtter page has been archived in the past. 

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/d1e65199-a21c-4c69-a1ea-01be83c2ada8)

In fact, it has been archived!

Lets try to open one of the old archives and see the contents of the page.

It takes a while, but twitter will not allow us to view the profile unless we login. This would just be time consuming as this is an archive of the page.

I was stuck for a while, and started reading twitter's documentation about this and how to get new twitter handles.

Then, I stumbled across a quora article where your twitter ID is actually static and does NOT change even if you change your username.

Question is, how can we get this ID?

I did some more research, and realized that the profile banner actually contains their ID! Since we have an archive of the page, we can grab the image link (profile banners are stored under the `pbs.twimg.com` domain, so right click the profile banner and click "copy image link") and see the before twitter asks us to login!

Once doing so, we get this: `https://web.archive.org/web/20240329134833/https://pbs.twimg.com/profile_banners/1772301250572263429/1711456007`

`1772301250572263429` is the twitter ID!

Using a website to reverse twitter ID (eg: https://commentpicker.com/twitter-id.php) we can get the new twitter username

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/f1678b14-3bbb-4ca0-b5db-0bba62de69ef)

Visiting this, we have 3 posts which are encrypted in base 64

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/0e5ca288-3e02-43a4-b65a-2680681d8c4a)

Lets decode these strings:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/f5b55ff9-61e9-4fbb-b435-f7e7112b8983)

And there is our flag!

Final flag: `jellyCTF{this_was_not_my_intention}`



