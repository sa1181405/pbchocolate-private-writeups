# awascii_validator
Point count: 380pts

Difficulty: easy

Provided files: awascii_validator.zip

Url: https://awascii-validator.jellyc.tf/

Description:
> Learning a new language is hard... maybe this could help with practice
#

There is an interesting function in `awafier_decoder.py`:
```
def debug(text):
    os.system('''echo {}'''.format(text))
```
This function is vulnerable to command injection if we can control `text`. The debug function is used in the `awascii_to_text` function, which is used to convert awascii to text.
```
def awascii_to_text(text: str):
    debug("Decoding AWASCII to sane human text: " + text)

    if len(text) < 3 or not text[0:3] == 'awa':
        debug("Invalid start code - mising starting awa")

    text = text[3:].lstrip()
    binary_string = awascii_to_binary_string(text)

    valid_chars_only = set(text) <= set('aw ')
    repeated_a = 'aa' in text
    repeated_b = 'ww' in text
    multiple_of_AWASCII = len(binary_string) % DIGITS_PER_AWASCII == 0

    if (not valid_chars_only) or repeated_a  or repeated_b or (not multiple_of_AWASCII):
        debug("Input is invalid AWASCII - do better.")
        exit()

    result = ""

    for character in [binary_string[i:i+DIGITS_PER_AWASCII] for i in range(0, len(binary_string), DIGITS_PER_AWASCII)]:
        value = int(character, 2)
        result += awafier_maps.REVERSE_AWASCII_MAP[value]

    debug(result)
```
To use the command injection vulnerability, we need to input correct awascii that translates to the payload `;cat flag`. (From the provided files, we know that the file containing the flag is at `./flag`.)

Program: sol.py

Flag: `jellyCTF{m4st3rs_1n_awat1sm}`
