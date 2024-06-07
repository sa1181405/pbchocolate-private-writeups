I Want to Believe 

Point count: 150pts

Provided files: gift.gif

Description: We've received a GIFt from what appears to be a signal coming from extraterrestrial life! Although, it appears they've used steganography to hide it inside of this .gif file. All we know is that it's in the form of a text file named 'iwanttobelieve.txt'. Can you recover it?

Hint: Maybe there's a GIFt tool we can use to recover it?


We are provided a gif file. Opening it dosen't show anything out of the ordinary

Running common steg tools such as zsteg, exiftool, or using Aperi'Solve does not yield any results.

However, the hint says that there may be a program to extract files from a gif. After extensive research, I came across this github repo. 

https://github.com/dtmsecurity/gift

That seems to match the tool we need!

Install the tool, then you can get the "iwanttobelieve.txt" file!

`python3 gift-cli.py --source a.gif recover iwanttobelieve.txt`

![image](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/84d81019-e242-41ed-b6ea-25aedad66408)

And we get our flag!

Final flag: `SIVBGR{y0ur_g1ft_1s_h3r3}`
