Container Chronicles

Point count: 150pts

Provided files: containers.png

Description: Welcome, aspiring digital detectives, to the Container Chronicles challenge! Your mission, should you choose to accept it, is to delve into the depths of a seemingly ordinary image of a shipping container and uncover its hidden secrets.

Within the confines of this digital cargo hold lies a treasure trove of information waiting to be unearthed. Your task revolves around deciphering the manufacturing date of the shipping container concealed within the image. But beware, for the information you seek is not readily visible to the naked eye.

Utilizing your skills, you must meticulously examine every pixel, every byte, and every **hidden layer** within the image to extract the elusive manufacturing date. Employ various techniques, ranging from simple visual inspection to advanced data analysis, to uncover the truth lurking beneath the surface.

Remember, in the world of digital forensics, every detail matters. Stay vigilant, think outside the box, and be prepared to embark on a journey through the intricate labyrinth of data concealed within the confines of this innocuous image.

Are you ready to unravel the mysteries of the Container Chronicles? The fate of the cargo rests in your hands. Good luck, and may the digital winds guide you to victory!


This problem was a forensics and an OSINT problem mixed together.

From the description, we can assume that stegonography would need to be done to find a "hidden layer" as it is the only bolded phrase in the description. This hints that we need to find and search through all of the different colored planes.

Using Aperi'Solve, we can see that in Red Plane 0, a secret message has been hidden.


![image](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/93bb5d82-277b-4685-8d6c-fb0bc62eb22b)

![image_r_1](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/3d658c60-c1e7-43b0-8720-80e85d259caa)


We now know the flag format is SIVBGR{MM_DD_YYY_d0ck3r}. We now have to find the manufacture date on the internet.

Reversing the image, we get this site

http://intermodalnetwork.blogspot.com/2011/12/nyk-line-container-nyku-257454-2-high.html

We now know who manufactured the container.


![image(1)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/85570144-dc3e-4263-9d56-1823c4dfc514)


I then googled "40' high-cube Seacube" and got a Sea Cube website. What took me long to solve this was that on the Sea Cube website, there is a button to lookup any crate


