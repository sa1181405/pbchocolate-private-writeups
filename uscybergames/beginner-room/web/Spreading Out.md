Spreading out

Point count: 150pts

Provided files: N/A

Description: ARIA is going out and touching files it shouldn't, can you track down where all it has gone?

Note: Fuzzing web directories is allowed.

We are presented with a website. At first, nothing out of the ordinary is shown. However, the description stating that fuzzing is allowed. This indicates to us that we need to start fuzzing to find hidden directories. 

You just had to get lucky or had great wordlists for you to get the flag. 

Wordlists I used: Common.txt from ffuf and dirbuster default wordlists and many others I cannot remember. 

Here were the results:


https://uscybercombine-s4-spreading-out.chals.io/robots.txt

1/5: `SIVBGR{ARIA_1s`

https://uscybercombine-s4-spreading-out.chals.io/.env

2/5: `_spreading_3v3rywh3r3`

https://uscybercombine-s4-spreading-out.chals.io/readme

3/5: `_4lw4ys_4nd`

https://uscybercombine-s4-spreading-out.chals.io/sitemap.xml

4/5: `_c4nnot_b3`

https://uscybercombine-s4-spreading-out.chals.io/wwwlog/development.log

5/5: `_st0pp3d}`

What tripped me up for a while was that there was a directory called /wwwlog which had a "No permission message" it wasn't until a good while later where I realized that you had to fuzz the /wwwlog directory to get the fifth and final part of the flag

Final flag: `SIVBGR{ARIA_1s_spreading_3v3rywh3r3_4lw4ys_4nd_c4nnot_b3_st0pp3d}`
