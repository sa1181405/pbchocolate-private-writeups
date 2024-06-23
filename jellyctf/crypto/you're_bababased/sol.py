thing = 'ʿ蛧鸩ઞ假备㮝螖𐱇𓉺澟嬚ᱸ芋ᗋޥ𒒽瀏即𑠌獀ʞ'
with open('list_of_safe_unicode_chars.txt') as f:
    chars = f.read()
numbers = []
for i in thing:
    numbers.append(chars.index(i))
numbers = numbers[::-1]

base = 0xbaba
number = 0
while numbers:
    number *= base
    number += numbers.pop()

print(bytes.fromhex(hex(number)[2:]).decode())

