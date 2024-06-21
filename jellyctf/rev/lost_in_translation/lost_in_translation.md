# lost_in_translation
Writeup author: **lolmenow**

Point count: 100pts

Difficulty: easy

Provided files: `awawa.txt` and `src.py`

Description: So I tried making an AwaSCII translator to help with writing Awatalk, but I don't really know python so I just copied some code off the internet. The output looks fine on first glance, but when I try to use it, it doesn't work. Can you help me figure out what's wrong with it?

Due to technical limitations with AwaSCII, the flag format for this challenge is jellyCTF(awawawa)
# 

We are provided with a src.py file, lets examine it. 

```
flag = open("flag.txt", "r").read()
awaflag = open("awawa.txt", "w")

# lookup table containing the AwaSCII coding
lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"

# never forget the leading awa
output = "awa"

for c in flag:
    # look up character in AwaSCII coding
    awascii_code = lookup.index(c)
    
    # convert code into binary (copied this off of stackoverflow)
    binary_awascii = format(awascii_code, '#010b')[2:]
    
    # convert binary to awas
    awascii = binary_awascii.replace("0", " awa").replace("1", "wa")
    
    output += awascii
    
awaflag.write(output)
```

What this program does in a nutshell is that it takes a file called flag.txt, uses the `lookup` string and translate it based on its position (or index) in this string. 

`lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"`

It then finds the index `awascii_code = lookup.index(c)`, converts the index to an 8 bit binary, then converts this binary to awascii (replaces each 0 with `awa` and each 1 with `wa`)

This is easily reversable as we can just split the remaining string into chunks to represent binary, and convert each binary string back to its original character.

Please see `sol.py` for my script on how to reverse this.

Final flag: `jellyCTF(C0p13D_tw0_b1T_t00_MuCh)`
