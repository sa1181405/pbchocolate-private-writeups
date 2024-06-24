# the_brewing_secrets
Writeup author: **taodragon_**

Point count: 927pts

Difficulty: hard

Provided:
`the_brewing_secrets.zip`
`nc chals.jellyc.tf 6000`

Description:
> Rumour has it Sakana stores the secret recipes for Phase Connect's coffee blends in his ~~garage~~ 'super secure laboratory'. Can you hack your way in?
#

The code checks the passcode in an interesting way.
```
int runChallenge(int passcodeLength)
{
    int EXTRA_ALLOWANCE = passcodeLength;
    int bitmask = (1 << passcodeLength) - 1;
    int maxTimeout = bitmask;
    int passCode = random() & bitmask;

    printf("WARNING: System will timeout after %d entries\n", maxTimeout + EXTRA_ALLOWANCE);
    printf("Enter %d-digit binary passcode  \n", passcodeLength);

    int timeout = 0;
    int userInput = 0;

    char received;

    while (timeout < maxTimeout + EXTRA_ALLOWANCE)
    {
        scanf(" %c", &received);

        // optimisation with bit shift
        userInput = bitmask & (userInput << 1 | (received != '0'));
        if (userInput == passCode)
        {
            return 1;
        }

        if (timeout % passcodeLength == (passcodeLength - 1))
        {
            printf("Passcode incorrect. Try again!\n");
        }

        timeout++;
    }

    printf("Timeout exceeded\n");

    return 0;
}
```

`runChallenge` is called with `passcodeLength` as 6. Note that the procedure returns 1 if the last 6 inputs are the password. This means that we can effectively brute force the password by sending a string containing every possible 6 digit combination of `"1"` and `"0"`.
This is documented at https://github.com/samyk/opensesame.

Script: `sol.py`

This gives us the string `000000100001100010100011100100101100110100111101010111011011111100000`, which unlocks every time.

Flag: `jellyCTF{mad3_w1th_99_percent_l0v3_and_1_percent_sad_g1rl_t3ars}`

