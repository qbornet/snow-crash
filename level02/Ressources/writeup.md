# Solution

So this one is pretty straigh forward once we loged in we see a level02.pcap, 
which is a capture of packet that could be used by application such as wireshark

By importing this capture file and following the tcp stream we can see that the client is sending a password   

which look like this in wireshark:
```sh
ft_wandr...NDRel.L0L
```

each dot is the representation of the char **0x7f** which is back **DEL**. 
So to find the password for flag02 we need to replace the letter by the number of dot preceding those said letter

which will give us the password **ft_waNDReL0L**

so now we can login and get the flag !

```sh
level02@SnowCrash:~$ su flag02
Password: 
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq1
```
