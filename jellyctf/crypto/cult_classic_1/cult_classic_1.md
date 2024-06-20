# cult_classic_1
Point count: 100pts

Difficulty: easy

Provided files: `01.zip` and `01_welcome.txt`

Description:  
> We are not a cult" - Starknights (probably)

This challenge contains two flags:

    Submit the first flag to cult_classic_1
    Submit the second (final) flag to cult_classic_2

Flags for this challenge are case insensitive.
# 

The zip file for the next stage is password protected, and the password is somewhere in the `01_welcome.txt` file. 

I heavily overthinked the first password, however it was just the starting letter of each sentence.

01_welcome.txt contents:

**P**leased to meet you.

**R**ecruitment: we are currently looking for highly intelligent individuals. 

**I**n order to do this, we have devised a test. 
**N**ested in this text is the first key to a series of challenges. 
**C**apture the final flag to prove your worth. 

**E**xcitedly awaiting the few who make it through to the end.

**S**incerely,
**S**tarknights (not a cult)

First password: PRINCESS

The password unlocks the zip file, and now we are presented with 02.txt:

```
Congratulations on passing stage 1.
TGkgYnJ4IGZkcSBnaGZyZ2ggd2tsdiwgYnJ4IGZkcSBrZHloIHdraCBxaGF3IG5oYjogRUxKUUhVRw==
```

This is base64 encoding due to the 2 equal signs at the end of the string, decoding this gives:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/e5dabdfc-07e4-4196-b4d8-66ec49cbad58)

`Li brx fdq ghfrgh wklv, brx fdq kdyh wkh qhaw nhb: ELJQHUG`

If you see jumbled up text like this without much special characters, assume its some type of rotational cipher. In this case, it was a caeser cipher (caeser ciphers can easily be bruteforced)

Using dcode's [Caeser Cipher Bruteforce](https://www.dcode.fr/caesar-cipher) we get this output:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/76277e58-f57c-4cef-94dd-af2f47f8ccea)

Second password: BIGNERD

Once unlocking the next stage, we get `03.txt`

```
OWZ OEU, KFZKF E WOBO LBV PRVZ KSJFUUA YB JRU: KMRYCTWG{BNVW_ZV_KCYG_E_NDSU_AC}
LFZFDKE CFXS RUHVEHZ QY ASK RWMX, GEBH UPOF OVB BVJ CVFFFMJ SSIZBZJ: NPZHO
```

This time, it was not a ROT or caeser cipher. But instead, a vigenere cipher with the key "BIGNERD" (this was guessy to figure out, but vigenere is common)

Using [Cyberchef's](https://gchq.github.io/CyberChef/) vigenere decode, we get:

```
NOT BAD, HERES A FLAG FOR YOUR EFFORTS SO FAR: JELLYCTF{THIS_IS_JUST_A_WARM_UP}
HOWEVER YOUR JOURNEY IS NOT OVER, TAKE THIS KEY AND PROCEED FORWARD: ALIEN
```

And there is our flag! That key will be important for the second edition of this challenge.

Final flag: `JELLYCTF{THIS_IS_JUST_A_WARM_UP}`
