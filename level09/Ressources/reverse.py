reverse_str = ""
token_bytes = b"\x66\x34\x6b\x6d\x6d\x36\x70\x7c\x3d\x82\x7f\x70\x82\x6e\x83\x82\x44\x42\x83\x44\x75\x7b\x7f\x8c\x89"

index = 0
for i in token_bytes:
    reverse_str += chr(i - index)
    index += 1
print(f'orignal: {reverse_str}')

