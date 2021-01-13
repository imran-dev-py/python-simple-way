# bytes data types are useful when deal with binary data [images, files]
# bytes value range is 0 to 255, more than 255 is ValueError
# immutable

l = list(range(10, 50, 10))
b = bytes(l)
print(b)
print(type(b)) # bytes
print(b[0]) # 10
print(b[2:]) # b'\x1e('

[print(x) for x in b]

# byteArray
# byteArray value range is 0 to 255, more than 255 is ValueError
# mutable

ll = list(range(10, 50, 10))
b = bytearray(ll)
print(type(b)) # bytearray
print(b)
print(b[-1])
print(b[2:])
b[0] = 00
[print(x) for x in b]
