# Solution

So when trying to find the first file for flag00 i discovered that /etc/passwd which is the file that store user information (login shell, home, login name, password, ect...)
one passowrd that was encrypted but visible was for flag01

```sh
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```

so from this i remember the name of where the first flag00 was hidden which is john, which is technically a binary for bruteforcing encrypted data but here it was a simple text file,
so i decided to use john to find the password with a known wordlist name rockyou.txt

```sh
john --wordlist=rockyou.txt passwd
```
here is the result of john

```sh
Created directory: /home/qbornet/.john
Warning: detected hash type "descrypt", but the string is also recognized as "descrypt-opencl"
Use the "--format=descrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 AVX])
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
abcdefg          (?)
1g 0:00:00:00 DONE (2024-09-13 18:55) 50.00g/s 3276Kp/s 3276Kc/s 3276KC/s 123456..mooner
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

giving use the decrypted password for flag01 which is: **abcdefg**


from that we can connect to flag01
```sh
level01@SnowCrash:~$ su flag01
Password: 
Don't forget to launch getflag !
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
```
