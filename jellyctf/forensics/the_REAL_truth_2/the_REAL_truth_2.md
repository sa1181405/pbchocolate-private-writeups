# the_REAL_truth_2
Writeup author: **lolmenow**

Point count: 896pts

Difficulty: hard

Provided files: N/A

Url: https://therealtruthaboutjellyhoshiumi.carrd.co/

Description: this chal is web/forensics

looks like jelly still has some more secrets on her site

#

With the description stating "looks like jelly still has more secrets on her site" clues me into fuzzing the website. However, this is not allowed.

So, I tried common directories. `robots.txt` came back as valid and this was shown:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/13480b77-c0a0-4321-ae78-367953f54065)

sitemap.xml?! That is exactly what we need to see how this website is organized.

Visiting it, we are presented with:

`https://therealtruthaboutjellyhoshiumi.carrd.co 2024-04-29 daily 1.0 https://therealtruthaboutjellyhoshiumi.carrd.co/assets/images/image01.png https://therealtruthaboutjellyhoshiumi.carrd.co/assets/images/image02.png`

With this info, we know there is a second photo. Lets view it!

![image02](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/3180e63c-c4af-4b80-8dbb-c987d686c12e)

Hmm, seems pretty similar to the last one.

After taking the same steps as `the_REAL_truth`, nothing of interest came up.

Until I realized: "Wait, we have 2 images. Why not combine them using Caesum's steg feature of "image combiner"

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/7afcbb20-a1e9-43ca-90af-90edb084347e)

That looks like a flag! Lets flip through the different filters so we can see it better.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/b47e383f-98de-4354-8bbe-4e4fa495e131)

After much trial and error of trying to get the right flag, we indeed get it!

Final flag: `jellyCTF{tw0_h41v3s_m4k3_a_wh0l3}`


