# phase_coffee_2
Writeup author: **lolmenow**

Point count: 487pts

Difficulty: medium

Provided files: phase_coffee_2.zip

Description: Surely all the bugs have been fixed...
# 

Following the same steps as the first edition of this challenge, lets take a look at the source code. Fortunately, the C source file is provided. 

```
#include <stdio.h>
#include <stdlib.h>

// Surely there won't be any more bugs
int main(int argc, char **argv) {
    int coin_balance = 100;
    int con = 0;

    while (con == 0){
        printf("\nWelcome to the Phase Connect coffee shop v2.0\n");
        printf("We sell coffee! \n");
        printf("Please buy our coffee... \n");
        printf("or else... \n");

        printf("1. Check Account Balance\n");
        printf("2. Purchase Coffee\n");
        printf("3. Exit\n");

        printf("Enter a menu selection \n");
        fflush(stdin);

        int menu;
        scanf("%d", &menu);

        if(menu == 1)
        {
            printf("\n\nCurrent account balance: %d \n\n", coin_balance);
        }
        else if (menu == 2)
        {
            printf("\n\nCurrently on sale\n");
            printf("1. Chisaka Airi Inspired - $35 each\n");
            printf("2. Rie Himemiya Inspired - $35 each\n");
            printf("3. Jelly Hoshiumi Inspired (Limited Edition) - $1,000,000 each\n");
            printf("Please make a selection: ");

            int choice;
            fflush(stdin);
            scanf("%d", &choice);

            if (choice == 1 | choice == 2)
            {
                printf("\nEnter desired quantity: ");

                int quantity = 0;
                fflush(stdin);
                scanf("%d", &quantity);
                printf("\n");

                if (quantity > 0)
                {
                    int total_cost = 35 * quantity;
                    int coin_balance_after_purchase = coin_balance - total_cost;

                    printf("Current balance: %d\n", coin_balance);
                    printf("Total cost: %d\n", total_cost);
                    printf("Balance after purchase: %d\n", coin_balance_after_purchase);

                    if (coin_balance_after_purchase < 0)
                    {
                        printf("Insufficient funds to purchase! Please try again!\n\n");
                    }
                    else
                    {
                        coin_balance = coin_balance_after_purchase;
                        printf("%d coffees purchased! Your coffee is being packaged and will be delivered in 2028!\n\n", quantity);
                        printf("Current balance: %d\n", coin_balance);
                    }
                }
                else
                {
                    // Stupid bugs... Fixed negative coffee quantity input validation
                    printf("Invalid coffee quantity\n");
                }
            }
            else if (choice == 3)
            {
                printf("You have chosen the deluxe, premium, limited edition seiso idol princess Jelly Hoshiumi inspired coffee.\n");
                printf("This coffee costs $1,000,000. Press 1 to confirm purchase: ");

                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);

                if (bid == 1)
                {
                    if (coin_balance >= 1000000)
                    {
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("Flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        break;
                    }
                    else
                    {
                        printf("Insufficient funds to purchase! Please try again!\n\n");
                    }
                }
            }
        }
        else
        {
            con = 1;
        }
    }
    return 0;
}
```

With the last vulnerability in mind, lets see if its similar to this problem.

And this time, we have an integer underflow vulnerability!

```
int total_cost = 35 * quantity;
int coin_balance_after_purchase = coin_balance - total_cost;
```

The `coin_balance_after_purchase` could underflow if `total_cost` is greater than `coin_balance`. In C, if you subtract a larger int from a smaller one, the result wraps around and becomes a very large positive number.

But, what exactly do we have to input so it can wrap around and become a very large positive number? Simply putting in the integer limit number from the first edition of this challenge won't work. 

In this case, we would need to input a very large quantity that, when multiplied by 35, causes an integer overflow resulting in a negative `total_cost`. This negative `total_cost` would then, when subtracted from `coin_balance`, effectively add to it, giving us a high balance.

Simple arithmetic math can help us find the value. 

`2147483647 / 35 + 1 = 61356676`

Lets try inputting `61356676`

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/5982705d-063e-45d5-82bb-e0a71aeb311c)

Hmmm, that does not seem to work.

Lets try it with a slightly higher number so we can be sure it wraps around. Lets try `61356680`

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/4f555b63-f113-49fc-8a36-74b4887e0b7a)

It successfully underflowed and now we have a high balance! We can now buy the "flag" coffee.

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/9bd882fe-b6ff-460b-8691-b594832e7fad)

There is our flag!

Final flag: `jellyCTF{dud3_y0u_m1ss3d_4n0th3r_bug}`


