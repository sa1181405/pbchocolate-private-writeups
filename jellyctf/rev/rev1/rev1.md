# rev1
Writeup author: **lolmenow**

Point count: 304pts

Difficulty: easy

Provided files: rev1

Description: you'll want some kind of disassembler e.g. ghidra, ida, binary ninja, radare2
# 

Before opening this in a disassembler, lets runs ome basic checks on this file.

Using linux's `file` command we can see some basic properties. 

```
rev1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6b0f8a7e759927a3b24ed052ceab1f82a5bbad6d, for GNU/Linux 3.2.0, with debug_info, not stripped
```

This binary executable is not stripped, meaning we can see function names and debugging symbols. This is perfect as it makes it easier to reverse.

Lets open it up in a disassembler! I personally use ida, but any work!

Once the binary has been decompiled, we see two important functions. `main()` and `get_key()`

main()

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int key; // ebx
  int i; // eax
  char v6[72]; // [rsp+0h] [rbp-48h] BYREF

  if ( argc <= 1 )
  {
    __printf_chk(1LL, "%s%s%s", "usage: ", *argv, " flag\n");
    return 2;
  }
  else
  {
    key = get_key();
    if ( !strcmp(argv[1], "hint") )
    {
      puts("use secure secret value of the princess' age\n");
    }
    else
    {
      for ( i = 0; i <= 36; ++i )
        v6[i] = aCEerMTzxIaKxMx[i] + key;
      key = strcmp(v6, argv[1]);
      if ( key )
      {
        puts("Flag incorrect.");
        return 1;
      }
      else
      {
        puts("Flag correct!");
      }
    }
  }
  return key;
}
```

get_key()

```
__int64 __fastcall get_key()
{
  return 7LL;
}
```

Interestingly, the key value is always returned as `7`

What is most important is these few lines:

```
for ( i = 0; i <= 36; ++i )
        v6[i] = aCEerMTzxIaKxMx[i] + key;
```

What this does is that it iterates over the first 37 characters of the array aCEerMTzxIaKxMx. It then Adds the key value (7) to each character and stores the result in the v6 buffer.

We can view the array `aCEerMTzxIaKxMx`, which is `c^eer<M?tZX<*Ia,kX?*MX_)kX:Xik*g<,..v`

This most likely is a rotation cipher of some kind with the key `7`

I used dcodes caeser cipher [decoder](https://www.dcode.fr/caesar-cipher) and inputted the string above. I then used the key of 7 and told it to rotate the entire string using the **ascii** table.

Here were my settings:

![image](https://github.com/sa1181405/pbchocolate-private-writeups/assets/170969470/1bf47e49-d23f-45e7-96e5-a20d86f7c09f)

Clicking decrypt gives us the flag!

Final flag: `jellyCTF{a_C1Ph3r_F1T_f0r_A_pr1nC355}`



