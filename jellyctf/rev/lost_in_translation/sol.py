encrypted = open("awawa.txt", "r").read()

# removes the initial "awa"
encrypted = encrypted[3:]

# table with awascii coding
lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"

# function to reverse the binary to awascii
def reverse(binary_string):
    return binary_string.replace(" awa", "0").replace("wa", "1")

# convert back to binary
binary = reverse(encrypted)

# split the binary content into 8-bit chunks
binary_strings = [binary[i:i+8] for i in range(0, len(binary), 8)]

# convert each binary string back to its original character
original_text = ""
for binary_string in binary_strings:
    if len(binary_string) == 8:
        awascii_code = int(binary_string, 2)
        original_text += lookup[awascii_code]


print(original_text)
