# Solution

You search for the flag in the entire system once by doing this command you will find the flag under the group and user flag00

```sh
find / -type f -group flag00 2> /dev/null
```

this will output only two file

```sh
/usr/sbin/john
/rofs/usr/sbin/john
```

both of them contains the same value inside

```sh
cdiiddwpgswtgt
```

this is a caesar cipher (ROT 11) which will give you nottoohardhere, now with that we can use this to login as flag00

```sh
level00@SnowCrash:/usr/sbin$ su flag00
Password: 
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```
