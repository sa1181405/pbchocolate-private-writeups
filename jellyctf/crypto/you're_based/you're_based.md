# you're_based
Point count: 766pts

Difficulty: easy

Provided files: N/A 

Description: Here's a basic encoding challenge to start with: `VGhhdCB3YXMganVzdCBhIHdhcm0gdXAuIEhlcmUgaXMgdGhlIGFjdHVhbCBmbGFnLCB0aG91Z2ggeW91IG1heSBuZWVkIGEgYmFzZSB0aGF0J3MgJ0EnIGJpdCBsYXJnZXI6CumpquqNrOehueetlPCTibvmmajpkbPmqanqhZ/wk4W16ZG06ZGh5qWi5pmz6ZGj8JSVofCUlaHwlJWh8JOBofCTja3woI2w`
# 

From the description, we can assume this first cipher is a base cipher of some kind as it is referred to as "basic"

Decrypting this with base64, we get:

```
That was just a warm up. Here is the actual flag, though you may need a base that's 'A' bit larger:
驪ꍬ硹答𓉻晨鑳橩ꅟ𓅵鑴鑡楢晳鑣𔕡𔕡𔕡𓁡𓍭𠍰
```

So, we know we are still in the base familiy for this second cipher. I actually got lost for a while trying to figure out what it meant by 'A' bit larger. Until I realized:

Base64 uses 6 bits (2^6=64. Hence the name base64) So it must be higher then base64

Base85 and Base92 did not work. So, I did some research on all the types of bases then came across this github repo: https://github.com/qntm/base65536

Hang on, there is a Base65536??

How does this make sense?

That is when it clicked me. The letter 'A' in hex is 10. (Hex goes like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) 10+6 = 16, 2^16 = 65536. 

I used this online [decoder](https://www.better-converter.com/Encoders-Decoders/Base65536-Decode) to convert the non readable text above, and we get:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/7f49eaff-9528-4724-be15-d9ad300eee9a)


There is our flag!

Final flag: `jellyCTF{th1s_i5_just_a_b4s1c_awawawarmup}`
