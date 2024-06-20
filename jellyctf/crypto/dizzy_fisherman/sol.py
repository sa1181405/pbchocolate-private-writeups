# mandatory libraries
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES


secret = 1 # we know the secret is 1 because g = p-1

encoded_key = secret.to_bytes(32, byteorder='big') # convert first to bytes

cipher = AES.new(encoded_key, AES.MODE_ECB) # create a new AES cipher object with the shared secret key

encrypted_flag = bytes.fromhex('2c6783bc372fbf601a4159080bf295e439c30e16fecde63dc7066abb40825383b1d8b2267d641fc17fd54d8bb0a60203b1d8b2267d641fc17fd54d8bb0a60203') # encrypted flag

flag = unpad(cipher.decrypt(encrypted_flag), 32) # decrypt

print(flag.decode())

# some code was inspired from this blog: https://onboardbase.com/blog/aes-encryption-decryption/
