# dizzy_fisherman
Writeup author: **lolmenow**

Point count: 666pts

Difficulty: hard

Provided files: `dizzy_fisherman.zip` and `nc chals.jellyc.tf 4000` 

Description: Sakana is sending some suspicious looking messages to Dizzy - looks like they're exchanging a shared secret key to encrypt the messages.

Alice has hacked into their key exchange system but needs more help with the exploit. Can you find a way to reveal their secret key and decrypt the message?
# 

Lets take a look at the source before using netcat on the server

```
import time
from Crypto.Util import number
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

P_LENGTH = 256
MAX_INT = 10000

p = number.getPrime(P_LENGTH)
secret_A = number.getRandomRange(2, MAX_INT)
secret_B = number.getRandomRange(2, MAX_INT)

print("Intercepting communications...")
time.sleep(1)

print("Randomly selected prime p = ", p)
g = int(input("Inject a generator g: "))

if not (1 < g < p):
    print("ALERT: Invalid g detected, requires 1 < g < p. Communications terminated!")
    exit()

public_key_A = pow(g, secret_A, p)
print("Dizzy's public key (integer) : ", public_key_A)
time.sleep(1)

public_key_B = pow(g, secret_B, p)
print("Sakana's public key (integer): ", public_key_B)
time.sleep(1)

print("Dizzy and Sakana are calculating their secret keys...", end='\n')
secret_dizzy = pow(public_key_B, secret_A, p)
secret_sakana = pow(public_key_A, secret_B, p)
# The secret key should be the same for both parties
assert(secret_dizzy == secret_sakana)

print("Encrypting flag with AES-256 using shared secret key")
with open('flag.txt', 'r') as f:
    flag = f.read().strip("\n").encode()

secret = secret_dizzy
encoded_key = secret.to_bytes(32, byteorder='big')
cipher = AES.new(encoded_key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(flag, 32))
print("Encrypted flag received: ", ciphertext.hex())
```

Seems like standard AES encryption but we can't write the secret as `1`. Well, we need to find a generator `g` that, when raised to any power `a`, will result in a small number of possible values modulo `p`. This would limit the possible values for the public and shared secret keys, making it feasible to brute force the shared secret key.

If `g=1`, then `(g^a mod p) = 1` for any `a`, and the public keys and shared secret key will always be 1. But we can't make `g` 1, or can we?

We can actually choose our own generator, `g`. So, in order to make `g` one, we can just simply do `g=p-1`

So, the public keys will always be either `1` or `p - 1`, and the shared secret key will also always be either `1` or `p - 1`

Here is how we can do this:

```
adam@DESKTOP-J07EICU:~$  nc chals.jellyc.tf 4000
Intercepting communications...
Randomly selected prime p =  86899728650592841884861211249399967893443125213865378821666077709714002156393
Inject a generator g: 86899728650592841884861211249399967893443125213865378821666077709714002156392
Dizzy's public key (integer) :  86899728650592841884861211249399967893443125213865378821666077709714002156392
Sakana's public key (integer):  1
Dizzy and Sakana are calculating their secret keys...
Encrypting flag with AES-256 using shared secret key
Encrypted flag received:  2c6783bc372fbf601a4159080bf295e439c30e16fecde63dc7066abb40825383b1d8b2267d641fc17fd54d8bb0a60203b1d8b2267d641fc17fd54d8bb0a60203
```

Now that the secret shared key is `1`, we can simply decrypt this with a python script! Please refer to `sol.py` in this directory

Running the script, we get: `jellyCTF{SOS_stuck_in_warehouse}`

And that is our flag!

Final flag: `jellyCTF{SOS_stuck_in_warehouse}`
