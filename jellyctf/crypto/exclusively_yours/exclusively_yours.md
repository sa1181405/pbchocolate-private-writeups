# exclusively_yours
Writeup author: **lolmenow**

Point count: 424pts

Difficulty: easy

Provided files: encrypted.txt

Description: I encrypted this flag exclusively for you... but I lost the key. I'm sure you can figure it out :>

Reminder: The flag format is jellyCTF{...}
# 

The description heavily reminded me of the XOR cipher. Because, in many ctfs, we already know the flag format. So, the key for the XOR cipher can be found. This is called a *known plaintext attack*

Inside encrypted.txt, we are presented with:

`06 1C 2F 38 3F 38 2C 29 09 0A 16 2D 1C 16 2B 31 17 1B 2D 0A 16 0F 18 1C 11`

Converting this from hex gives gibberish, but since I know its a XOR cipher, lets put in the key for XOR as `jellyCTF{` and see what happens. *Don't forget to convert from hex first! And if your using [Cyberchef](https://gchq.github.io/CyberChef/), make sure your in UTF-8 mode when inputting the key!*

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/f63e83c7-dea7-49b6-867b-92ce75d3ec23)

Hmmm, that might be our key!!

`lyCTF{xor` sounds familiar to `jellyCTF{xor` as our flag format!

Lets put `jellyCTF{xor` in as the key. 

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/dab80058-8207-48f6-9768-6f58ae26d6c7)

Woah! We are discovering plaintext, lets keep putting this plaintext as the key.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/f96c4c32-0fbf-4014-a22a-0e86bf049593)

More plaintext is being revealed! Lets keep going.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/0e6e8780-ea04-4490-80f4-2171ac3f1944)

That seems like our flag!

Final flag: `jellyCTF{xorry_not_xorry}`

Final cyberchef recipe: `https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'jellyCTF%7Bxorry_not_xorry%7D'%7D,'Standard',false)&input=MDYgMUMgMkYgMzggM0YgMzggMkMgMjkgMDkgMEEgMTYgMkQgMUMgMTYgMkIgMzEgMTcgMUIgMkQgMEEgMTYgMEYgMTggMUMgMTE`





