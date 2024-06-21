# head_empty
Writeup author: **lolmenow**

Point count: 508pts

Difficulty: medium

Provided files: memory.dmp

Description: what's jelly's password?

if you're having problems with the tool, try using a version prior to commit e5a5b895771b655d21c36689c33a534034c31e36 (or manually patch the contents of that commit out)

# 

We are provided with a memory file and need to find jelly's password inside of it.

Voltaility is a great tool to analyze memory dumps, and conveniently it has a plugin called [hashdump](https://github.com/volatilityfoundation/volatility/blob/master/volatility/win32/hashdump.py) to extract the hashes of all the passwords in this memory dump. 


*This was used on Voltaility Python3*

`python3 vol.py -f ~/memory.dmp windows.hashdump.Hashdump` 

Once ran, we are returned with:
```
Administrator   500     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
Guest   501     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount  503     aad3b435b51404eeaad3b435b51404ee        31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount      504     aad3b435b51404eeaad3b435b51404ee        9082e3468d0a84e876033173709cb118
jelly   1001    aad3b435b51404eeaad3b435b51404ee        aa05ab5319d59779b937bdbf9797d895
```

There is the hashes for the account jelly!

Lets run both of those hashes (one is an lmhash and another is an nthash, there are great resources online to see the difference between these two)

Website I used to see if any hashes are in a database: https://hashes.com/en/decrypt/hash

Inputting the lmhash returns nothing, however when we input the nthash, we are shown:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/7085a0cc-c9ef-4bbd-a563-8358681bf28b)

That is the password!

Final Flag: `jellynerd2`

