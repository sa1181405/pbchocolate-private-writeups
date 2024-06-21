# cipher_check
Point count: 288pts

Difficulty: medium

Provided files: cipher_check.zip

Description: 
> Let's see if you can decode some common ciphers! Decoding ciphers may be tricky, especially when you're new to CTFs, but...
>
> jellyCTF{ _ _ _ _ _ _ _ _ _ _ _ _ } (12 characters)
#

Each of the clues has an answer format of ANSWER____

### Across
a8  ARNFSOWLEL
Every other letter gives us `ANSWERFOLL`

a7	awa awa awa awa awa awa awa awawawa awawa awa awa awawa awawa awa awa awa awa awa awawa awa awa awawa awawawa awa awawa awa awa awa awawa awawawa awa awawa awawa awa awawawa awawawawa awa awa awa awawa
This is awascii. `ANSWERISTD` (See AWA 5.0 documentation)

a6	65 78 83 87 69 82 81 67 73 78
From decimal, we get `ANSWERQCIN`

a5	41 4e 53 57 45 52 49 4c 4f 4e
From hex, we get `ANSWERILON`

a4	cipher-flags.png
This is a cipher featuring flag semaphore. `ANSWERIALL`

a3	cipher-symbols.png
This is the pigpen cipher. `ANSWERPEVE`

a2	AENNWROMSW
This is a Rail Fence cipher with key 3 and offset 0. `ANSWERWONM`

a1	cipher-pattern.png
These are Signal Flags. `ANSWERN6MO`

e8	ZMHDVILDNL
This is the Atbash cipher. `ANSWEROWMO`

e7	QFLVTKXTSB
??? Likely some substitution? `ANSWERUELX`

e6	.- -. ... .-- . .-. -.. . - .-
This is morse code. `ANSWERDETA`

e5	1000001 1001110 1010011 1010111 1000101 1010010 1010011 1010000 1000101 1000011
This is ASCII. `ANSWERSPEC`

e4	NAFJREVARH
This is ROT13. `ANSWERINEU`

e3	AJSSENNPHA
This is a Vigenere cipher with key `awawawawaw`. `ANSWERNTHE`

e2	BNTWFRBTFI
This is a Vigenere cipher with key `bababababa`. `ANSWERATEI`

e1	p}$(t#'t$P
This is ROT47. `ANSWERVES!`

Down
a8	UVU1VFYwVlNSa2xSU1E9PQ==
This is Base64 encoded twice. `ANSWERFIQI`

b8	IFHFGV2FKJHVGQ2M
This is Base32 encoded. `ANSWEROSCL`

c8	QU5TV0VSTFRJTw==
This is Base64 encoded. `ANSWERLITO`

d8	101 116 123 127 105 122 114 104 116 116
From octal, we get `ANSWERLDNN`.

e8	AAAAA ABBAB BAABA BABBA AABAA BAAAB ABBBA BABAA AAABB BAABA
This is Bacon Cipher. `ANSWEROUDS`

f8	⠁⠝⠎⠺⠑⠗⠺⠑⠑⠏
This is Braille. `ANSWERWEEP`

g8	1 14 19 23 5 18 13 12 20 5
This is A1Z26 cipher. `ANSWERMLTE`

h8	CAXOREWSNA
This is backwards. `ANSWEROXAC`

a4	✌︎☠︎💧︎🕈︎☜︎☼︎✋︎🏱︎🕈︎☠︎
This is wingdings. `ANSWERIPWN`

b4	0 26 10 1 5 36 0 5 9 48
c4	&#65;&#78;&#83;&#87;&#69;&#82;&#76;&#86;&#78;&#77;
d4	cipher-boxes.png
e4	BOTXFSJOBW
f4	JRDHCYBLAM
g4	2 66 7777 9 33 777 33 44 33 7777
h4	414e5357455255454921%    
