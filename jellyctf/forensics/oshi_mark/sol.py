with open('description.txt', 'rb') as f:
    bytestring = f.read()
invisible_chars = bytestring[4:-5]
list_of_bytestrings = [invisible_chars[i:i+7] for i in range(0, len(invisible_chars), 7)]
list_of_ints = [int.from_bytes(i) for i in list_of_bytestrings]
ascii_list = [(i+81) % 192 for i in list_of_ints]
print(''.join([chr(i) for i in ascii_list]))
