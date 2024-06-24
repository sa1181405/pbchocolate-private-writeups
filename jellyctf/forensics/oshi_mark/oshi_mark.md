# oshi_mark
Writeup author: **taodragon_**

Point count: 953pts

Difficulty: hard

Provided files: N/A

Description: (provided in description.txt)
#

First, we open the file as bytes in python.
```
with open('description.txt', 'rb') as f:
    bytestring = f.read()
```
We then take out both visible characters.
```
invisible_chars = bytestring[4:-5]
```
Each invisible unicode character takes up 7 bytes, so we break the bytestring into sections of length 7.
```
list_of_bytestrings = [invisible_chars[i:i+7] for i in range(0, len(invisible_chars), 7)]
```
We convert each of these segments into int.
```
list_of_ints = [int.from_bytes(i) for i in list_of_bytestrings]
```
Then we add 81 then find the remainder modulo 192. (These values were found via trial and error.)
```
ascii_list = [(i+81) % 192 for i in list_of_ints]
```
Then we convert to ascii.
```
print(''.join([chr(i) for i in ascii_list]))
```

Script: `sol.py`

This gives us

```
well, well, well, look who finally decoded my secret oshi mark message! congratulations on wasting countless hours (and probably brain cells) figuring out that "awawawa" means "i love you!" maybe you've finally found a use for all that nerdy knowledge you've accumulated over the years. and let's be honest, you probably couldn't even figure out the message without relying on a silly unicode decoding site you found using hints. don't worry though, i won't tell anyone! how about this? let's give you a prize for your efforts. how about... jellyCTF{a_cut3_alic3_hugg4bl3_plush13}! awawawawawawawa! it's cute how nerdy you are.
```

Flag: `jellyCTF{a_cut3_alic3_hugg4bl3_plush13}`
