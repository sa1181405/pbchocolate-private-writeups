# you're_bababased
Writeup author: **taodragon_**

Point count: 968pts

Difficulty: medium

Provided files: `list_of_safe_unicode_chars.txt` 

Description:
>nerd is you
>BABA is based
>flag is win
>
>ʿ蛧鸩ઞ假备㮝螖𐱇𓉺澟嬚ᱸ芋ᗋޥ𒒽瀏即𑠌獀ʞ
# 

`you're_based` was about bases, so we can assume that this challenge is also about some base relating to baba. `0xbaba` is valid hex, so lets try that. We can first convert each character into a number by finding the index of each character in the provided file.
```
with open('list_of_safe_unicode_chars.txt') as f:
    chars = f.read()
numbers = []
for i in thing:
    numbers.append(chars.index(i))
```
Then we can use the base `0xbaba` like so.
```
numbers = numbers[::-1]
base = 0xbaba
number = 0
while numbers:
    number *= base
    number += numbers.pop()
```
Then we can convert the resulting integer into a string to print it.
```
print(bytes.fromhex(hex(number)[2:]).decode())
```
Sure enough, this works.

Script: `sol.py`

Flag: `jellyCTF{baba_is_cool_but_j3lly_i5_COOLER}`
