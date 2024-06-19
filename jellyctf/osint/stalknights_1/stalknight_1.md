# stalknights_1 
Point count: 100pts

Difficulty: easy

Provided files: Link to an instagram photo (see `stalknights_1_instagram_photo.jpg` in this folder)

Description: Stumbled across this Starknight while scrolling through Instagram. Can you figure out what neighbourhood and country this photo was taken in? Flag format: jellyCTF{neighbourhood_name,country} (all lowercase)
# 

With an image file present, lets reverse google it to see where this could possibly be taken at.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/2cf132cf-8449-4d57-a06e-bd0a6fbd02ae)


We see a travel blog with a near identical image. Lets open the blog to see if we can find anything. [Blog](https://www.travelwithsimina.com/one-day-in-zaanse-schans/)

Scrolling down, we now have the exact location and neighborhood where this photo was taken.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/fa08e812-a47a-4239-8b88-bb7147494295)

The neighborhood was the heading of this blog (the heading being Zaanse Schans)

A quick google search would tell you that Zaanse Schans is located in the Netherlands.

There we have it, the final flag!

Final flag: `jellyCTF{zaanse_schans,netherlands}`
