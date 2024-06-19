# the_REAL_truth
Point count: 439pts

Difficulty: medium

Provided files: image01.png (see `the_REAL_truth_image.png` in this directory)

Url: https://therealtruthaboutjellyhoshiumi.carrd.co/

Description: note: this is the only subdomain in scope. do not bruteforce/dirbust.

# 

The website presents itself with a long speech and a photo in the middle. Since the category is forensics, I assumed that this is stegonography with the image on the website. 

Using Aperi'Solve yields no results, so I used stegsolve by Caesum to see if I can go through the filters and find a hidden flag.

Going through the filters showed nothing, so I used stegsolve's data extraction feature. This extracts all the data from the bit plane.

I did not know which plane had the flag, so I checked all the planes.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/57a564a3-b506-4803-80f3-98ae623fc422)

We can save the data, and examine the file.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/61ae6a0e-3b1a-44d9-8495-a94a0f196db6)

Hmmm, this seems like it spells out a message! Lets continue digging.

We see our flag not far down!

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/94e1bd72-664a-4069-9948-3c0d6217cfee)


Final flag: `jellyCTF{th3_w0man_in_th3_r3d_ch4nn3l}`
