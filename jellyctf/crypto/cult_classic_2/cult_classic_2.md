# cult_classic_2
Writeup author: **lolmenow**

Point count: 864pts

Difficulty: easy

Provided files: N/A (same as cult_classic_1, continue from last stage)

Description: See cult_classic_1 for challenge files. Enter the second flag into this challenge.

Clarifications for Stage 5:

Make sure you're using the original source without modification (otherwise you may notice larger numbers than expected)

If using online decoders but it's not working, try a quick manual check to see if the decoders doing what you expect

# 

Lets continue off from the last stage! We left off with the key of `ALIEN` which is most likely the next key for the protected zip file.

Using the password, we now have 04.txt:

```
Welcome to stage four.
Cheating is not tolerated. We hope you play fair and square.

LBPTTULD
```

The text file obviously hints to the `playfair` cipher. However, we need a key. Lets use the key `ALIEN` as that is the last key we have. 

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/17987524-0f99-400f-a96f-e8f498ebe41c)

Thats the next key! Lets use it to unlock the next zip file.

We are presented with 05.txt:

```
🌠Don't Look Away... 🌠

36.1 34.11 35.10 3.29 25.18 1.14 25.13 38.10 19.4 40.15
9.10 17.31 27.13 20.11 3.6 14.27 25.26 25.24 6.15 10.40 13.3 28.16 19.23 27.34 18.26 36.8
9.37 25.23 14.17
33.12 23.30 19.31
39.25 13.29 18.25 35.28
1.12 39.7 39.5 29.21 34.4 10.28 20.14 15.26
```

This reminds me of a book cipher. But, what text should we use? It took me a while, but the book/"song" we need to use is made by Jelly herself! The song is called `Luminary` and we can verify this is the correct song from the description:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/31bdedda-f432-483f-9c16-84c531d4983d)

Lets use the lyrics from the [Youtube](https://www.youtube.com/watch?v=1x6oPy3Hwcw) description to decrypt this cipher. With book ciphers, you need to know how its decrypted. number.other_number.sometimes_another_number

Usually, its common to be line.character OR line.word.character

Since there are only 2 numbers in the cipher (eg: `36.1`) it most likely is line.character. What this means is that, for example `36.1`, in the 36th line at the 1st character is the first letter of the decrypted message.

I made a python script to do this. With 3 files called `code.txt` `song.txt` and `sol.py`. Please refer to them in this directory. Its in the folder called `stage5_script`.

Using the script, we get:

`Capitalise'megalencephaly'forthenextpassword`

There is the password! Which would be `MEGALENCEPHALY`

Using this, we unlock the final zip file. The last text file 06.txt has:

```
WAAWW AAWWW AAWAA AAWAW AWAAA AWWAW AAAAA AWAWW AWWWW AAAAA WAAWA WAAWA WAWWA AWWWA WAAAW AAAWW AWAAA WAAWA WAAWA AAAAA AAAWW AAWWA AWAAA WAAAW AWAWW
```

I instantly thought binary code/bacon cipher, as there is only W's and A's.

So, I replaced every `W` with a `0` and every `A` with a `1` (binary usually starts with 0, hence why I replaced `W` with 0)

This gives us: `01100 11000 11011 11010 10111 10010 11111 10100 10000 11111 01101 01101 01001 10001 01110 11100 10111 01101 01101 11111 11100 11001 10111 01110 10100`

Decoding this with bacon cipher, we get: `THEFINALPASSWORDISSADGIRL`

That is the final password! `SADGIRL` which unlocks the flag.txt file!

Final flag: `jellyctf{jelly_was_probably_older_than_these_ciphers}`


