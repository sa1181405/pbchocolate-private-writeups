Touch Grass

Point count: 150pts

Provided files: N/A

Description: ARIA has ordered you to touch grass. Now you actually have to do it. Make up for all the times you havent touched it.


Since there is no source provided, we have to start pentesting.

I made an account to check things out.

![image](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/8fff33ed-108b-4280-b048-3f6b92d8e64e)

Hmmm we need 100000 pieces of grass?

Lets check out the page source.


![image(1)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/0585bc20-24aa-4716-81e8-613eb39069f0)

Okay, we see that we can go to /api/click with a POST request to get a click

![image(2)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/c68ee34e-53c0-4629-8567-35a46d7f2e70)

Hmmm okay, content type/json should fix this.

![image(3)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/7226d95b-da14-4be1-8be2-b3402ee43efe)


Nevermind, lets supply it with our /register json data.

![image(4)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/a7f415ff-71ff-4ae7-a7ef-e3789f8be687)

Oh an Admin API?


At this point, I tried bruteforcing and trying to find the admin API. This did absolutely nothing until someone from the discord server says to "check how users are made".

So, I go back to the registration page and I notice something.

![image(5)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/6be1ece7-bad0-4b11-a104-520d4d63995a)

Registration.js! This should be interesting.

```
$(document).ready(function() {
    $('#register_button').on('click', register);
    console.log("ready");
});

const register = async() => {
    $('#register_button').prop('disabled', true);

    // prepare alert
    let card = $("#resp-msg");
    card.attr("class", "alert alert-info");
    card.text("Sending registration...");
    card.show();

    // validate
    let username = $("#username").val();
    let first_name = $("#first_name").val();
    let last_name = $("#last_name").val();
    let password = $("#password").val();

    await fetch(`/api/register`, {
        // copy from the /admin/api/register endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username: username, first_name: first_name, last_name: last_name, password: password}),
        })
        .then((response) => response.json()
            .then((resp) => {
                card.attr("class", "alert alert-danger");
                if (response.status == 200) {
                    card.attr("class", "alert alert-info");
                    card.text(resp.message);
                    card.show();
                    window.location = "/dashboard";
                }
                card.text(resp.message);
                card.show();
            }))
        .catch((error) => {
            card.text(error);
            card.attr("class", "alert alert-danger");
            card.show();
        });

        $('#register_button').prop('disabled', false);
}
```

There it is! Our admin API! We can now make accounts with the status of admin. Lets make one.


![image(6)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/8481b79b-1f2f-4248-a3fd-e85f3688441f)



Seems to work. Now that we know the admin api, we can assume the click endpoint would be on /api/admin/click since we are an "admin" account.

![image(8)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/76606170-5d7f-4d6d-bce9-5b4428e9d76c)

Missing count parameter? No problem, lets add it! We know we need 100000 for the flag 

![image(7)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/0570f19e-a76d-4d91-9cb9-0f121879ed16)

The parameters might be getting in our away. Lets try only our user and count parameter, as the other fields were only necessary for registration.

![image(9)](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/d7ce0787-7292-40ae-aac6-3da2a529d069)

Count updated! Lets check the dashboard.

![ezgif-2-873430a4b0](https://github.com/sa1181405/pbchocolate-private-writeup-making/assets/170969470/ea4da15f-ac7a-4df3-bd1a-01a7dc49a44a)

There it is! Our flag!

Final flag: `SIVBGR{T0uch_1t}`
