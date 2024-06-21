# awassmbely
Writeup author: **taodragon_**

Point count: 271pts

Difficulty: easy

Provided files: `code.s`

Description: 
>My AWA 5.0 code got jumbled up with my Assembly code help! What's in register eax?
>Put the answer in the decimal number base for example if your answer is 0x11 the flag would be jellyCTF{17}

# 

According to the AWA 5.0 documentation provided, "awa" means 0 and "wa" means 1. This means that we can translate each awa string into binary.
```
wawawa   : 111 : 7
wawaawa  : 110 : 6
waawaawa : 100 : 4
```
This means that the final value of eax is `(7+6) << 4` which is `208`.

Flag: `jellyCTF{208}`
