binary_string = "1000001010010011101111101011101011111010000010100100110000111001110111010000111011100111110100111100100110101111000001110010110110010001100011011001000011001110011101000110101100010110011111111"
#1000 001 010 010 011 101111 101011 1010111 110100 000 10100100110000111001110111010000111011100111110100111100100110101111000001110010110110010001100011011001000011001110011101000110101100010110011111111

huffman_codes = {
    "000": "_",
    "001": "e", #y
    "010": "l", #y
    "011": "y", #y
    "1000": "j", #y
    "1001": "o",
    "1010": "r",
    "10110": "a",
    "10111": "c", #y
    "11000": "d",
    "11001": "s",
    "11010": "t", #y
    "11011": "u",
    "11100": "w",
    "111010": "f", #y
    "111011": "h",
    "111100": "k",
    "111101": "m",
    "111110": "{",
    "111111": "}",
}

decoded_string = ""
i = 0

while i < len(binary_string):
    match_found = False
    for length in range(3, 8):
        if i + length <= len(binary_string):
            code = binary_string[i:i+length]
            if code in huffman_codes:
                decoded_string += huffman_codes[code]
                print(f"found code: {code}, decoded character: {huffman_codes[code]}, Position: {i}")
                i += length
                match_found = True
                break
    if not match_found:
        print(f"huffman code not found at {i}. current binary segment: {binary_string[i:i+8]}")
        break

print("Decoded String:", decoded_string)
