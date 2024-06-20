# really_special_awawawas
Point count: 728pts

Difficulty: medium

Provided files: vals.txt

Description: A specially chosen modulus for a really special awatistic musical princess.

dCode couldn't crack it so I'm sure it's secure... right?
# 

We are given a vals.txt file, lets open it.

```
n = 40095322948381328531315369020145890848992927830000776301309425505
e = 65537
c = 35622053067320123838840878683947610930876835359945867019927573838
```

This is an RSA cipher because we are given a modulus, a cipher text, and the exponent. Now, the modulus is relatively small, so we can go two ways here.

First option: Use [RsaCracker](https://github.com/skyf0l/RsaCracker)

RsaCracker is one of the best ctf tools to see if any RSA cipher is vulnerable to any attacks. Using RSA cipher, it identified the factors easily because of the small modulus.

```
adam@DESKTOP-J07EICU:~$ rsacracker -n 40095322948381328531315369020145890848992927830000776301309425505 -e 65537 -c 35622053067320123838840878683947610930876835359945867019927573838
     Running [00:00:04] (3 factors found) [==============================================================>     ] 36/39  Elapsed time: 7.66667152s
Succeeded with attack: ecm
Unciphered data:
Int = 667859681674751630937423997247174474842427366359093200105853
Hex = 0x6a656c6c794354467b6177617761735f345f6576657279317d
String = "jellyCTF{awawas_4_every1}"
```
That is one way to get the flag.

Second option: Manually getting the factors of `n` and use a python script to decrypt the RSA.

There are many websites online to factorize `n` for you, this [website](https://www.alpertron.com.ar/ECM.HTM) can get you the factors of `n`. You can then use many python scripts online to decrypt it since you already have the factored `n` (sometimes referred to as `p` and `q`)

OR you can use [factordb](http://factordb.com/) to see if its already been factorized before.

Sure enough it has already been factored, and you can use a python script to decrypt it. There are many python scripts online for you to decrypt RSA knowing the factors.

Final flag: `jellyCTF{awawas_4_every1}`
