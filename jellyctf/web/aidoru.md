# aidoru
Point count: 100pts

Difficulty: easy

Provided files: [aidoru.zip](https://jellyc.tf/files/64c41206277c409e5ee5ee8f386eba88/aidoru.zip?token=eyJ1c2VyX2lkIjo3MDIsInRlYW1faWQiOjQ4NywiZmlsZV9pZCI6NDB9.ZnJe-A.7-v1WIFJqTbpd6xf4VcFpEK4Uy0)

Description:
> ### Phase Connect is full of seiso idols!
>
>There's a hidden flag on Jelly's page, but the creator hasn't made her page public yet. Can you find a way to access her page and capture the flag?
# 

The page has 6 images, 1 of which links to a 404 page. Using Inspect Element, we can see that each of the remaining 5 images have filenames based on the character and a link to a directory `/covers/` then a 32 character hexidecimal string.

For example, the image in the top left is `/static/images/rie.jpg` and links to `/covers/41895503f71f59ce931bd3590c577b3c`. This 32 character hexidecimal string is the length of an MD5 checksum, and sure enough, the MD5 checksum of `rie` is `41895503f71f59ce931bd3590c577b3c`.

The image on the bottom left links to a 404 page. The filename is `/static/images/jelly.jpg` so it should link to `/covers/{the MD5 checksum for jelly}`. This would be `/covers/328356824c8487cf314aa350d11ae145`.

When we visit this link, we get the flag as a youtube video embed with src `https://www.youtube.com/embed/jellyCTF{u_r_the_p3rfect_ultimate_IDOR}?autoplay=;start=`, which gives us the flag when we use Inspect Element.

Flag: `jellyCTF{u_r_the_p3rfect_ultimate_IDOR}`
