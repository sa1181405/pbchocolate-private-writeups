# is_jelly_stuck
Writeup author: **7000x887143**

Point count: 961pts

Difficulty: medium

Provided files: `clues.txt` `upload_me_to_google_drive_if_you_want.xlsx` `grid.png`

Description: Man, I don't know anything about computers or hacking. Let's just relax with an easy crossword puzzle...
# 

This was mostly an osint challenge, you can take a look at all the crossword answers below.

**ACROSS**

1	Ancient "rose-red city"
`PETRA (ancient city in Jordan)`

6	Running off current
`ELECTRIC (electric current)`

9	Statute
`LAW`

12	Remi, Airi, Shiina, Rie, Erina, Panko
`ALIASES (https://phase-connect.com/phase-02-alias/)`

13	Sci-fi star knight circa 1977
`JEDI (Star Wars)`

14	New Phase branch, maybe
`ES`

15	Minivan alternative, abbr.
`SUV`

16	Lists files in the current directory
`LS (https://en.wikipedia.org/wiki/Ls)`

17	Jelly is
`FLATASABREAD`

22	Jelly is also a
`DORK`

23	This, backwards
`FTCYLLEJ (JellyCTF backwards)`

24	Roman blackjack?
`XXI (21 in Roman numerals)`

**DOWN**

1	Basic projectile and legume
`PEA (pea shooter)`

2	Letter, Jelly only takes
`ELL (taking the L)`

3	Last name of developer, released a free beta on itch.io needed to solve this challenge

`TEIKARI (https://hempuli.itch.io/baba-is-you-level-editor-beta)`

4	Color TV pioneer
`RCA (https://en.wikipedia.org/wiki/RCA)`

5	Between ports
`ATSEA (what ships are, between ports)`

7	... to ay resects
`RESSF (press F to pay respects, remove all P's)`

8	... you?
`IS (baba is you)`

9	Yellow, left-to-right top-to-bottom, code
`LEVEL (the 8 cells form a baba is you level code)`

10	Commonly blocked
`AD (adblockers)`

11	Dorian Gray creator
`WILDE (Oscar Wilde)`

13	Court panel
`JURY`

15	Co. that purchased AT&T in 2005
`SBC (https://www.nbcnews.com/id/wbna6887107)`

17	Package delivery co. ticker symbol
`FDX (FedEx)`

18	Smoked salmon for breakfast
`LOX (https://en.wikipedia.org/wiki/Lox)`

19	Killing your teammate, abbr.
`TK (teamkill)`

20	What's that noise? Did someone __ me?
`AT (@)`

21	Yankovic

`AL ("Weird Al" Yankovic)`

## Flag construction
*"The flag is complete gibberish, but you'll know it when you're optimal!"*

The crossword is the same shape as the Baba is You level given in `9 DOWN`. Following the optimal (shortest) solution, the player character passes through cells that spell the flag out (see `crosswordpath.mp4` in this directory, video by taodragon who found this!).

Once following that path in your grid, you get the flag!

Final flag: `jellyctf{krodflakarkt_k__aliases_c_led_ls}`
