# just_win_lol
Point count: 908pts

Difficulty: hard

Provided files: `just_win_lol.zip`

Description 
> looks like that new Balatro game has already got some knockoffs. the RNG for this one sucks though - how are you ever meant to win?! reminder: do not bruteforce, you won't win
#

The goal is to get 5 of a kind for 5 draws out of 10.

Looking at `main.go`, we see that the handsa are generated with the `randHand` function that takes a rand object as a parameter. This function is used here:
```
		var timeNow = time.Now().UTC().Unix()
		var rand_time = rand.New(rand.NewSource(timeNow))
		hand := randHand(*rand_time)
```
The rand object has a seed of the current Unix timestamp. We can use this and the `isFiveOfAKind` function to test unix timestamps to see if they will give 5 of a kind.

We can therefore write a program in go that outputs the next 30 unix timestamps that will give a 5 of a kind by testing each subsequent timestamp.

By drawing at these specific times, we can get an arbitrary number of 5 of a kinds.

Program: sol.go

Flag: `jellyCTF{its_v3ry_stra1ghtf0rw4rd_s1mply_g3t_g00d_rng}`
