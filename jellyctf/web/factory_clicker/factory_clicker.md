# factory_clicker
Writeup author: **taodragon_**

Point count: 100pts

Difficulty: easy

Provided files: factory_clicker.zip

Url: https://factory-clicker.jellyc.tf/

Description: N/A
#

It appears that we need to make 500,000,000,000 pipes to get the flag. If we click 3 times and look at the network tab of Inspect Element, we see that after clicking, a POST request is sent to `/increment?increment_amount=1`. Sending a POST request to `/increment?increment_amount=500000000000` gives us enough pipes made for the flag.

Flag: `jellyCTF{keep_on_piping_jelly}`
