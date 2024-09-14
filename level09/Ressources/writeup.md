# Solution

So we loged in and find the binary level09 and token, when we decompile the binary we find out,
that this binary increase the letter base on the index of the string so str[i] + i.

If we cat token we will see only the visible value char so we need to do `xxd -p | tr -d '0a'` to give the byte and remove \n

```sh
xxd -p token | tr -d '0a'
```

here is the string that we need to reverse.

```python
token_bytes = b"\x66\x34\x6b\x6d\x6d\x36\x70\x7c\x3d\x82\x7f\x70\x82\x6e\x83\x82\x44\x42\x83\x44\x75\x7b\x7f\x8c\x89"
```

so since to get this string we do str[i] + i we should do str[i] - i
here is the result from our script.

```python
reverse_str = ""
token_bytes = b"\x66\x34\x6b\x6d\x6d\x36\x70\x7c\x3d\x82\x7f\x70\x82\x6e\x83\x82\x44\x42\x83\x44\x75\x7b\x7f\x8c\x89"

index = 0
for i in token_bytes:
    reverse_str += chr(i - index)
    index += 1
print(f'orignal: {reverse_str}')
```

```sh
orignal: f3iji1ju5yuevaus41q1afiuq
```

now we can fetch the flag.

```sh
level09@SnowCrash:~$ su flag09
Password: 
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```
