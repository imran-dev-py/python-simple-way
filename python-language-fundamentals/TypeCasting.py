# int()
print(int(True)) # 1
print(int(False)) # 0
print(int(.5)) # 0
# print(int('g')) ValueError
# print(int('10.0')) ValueError
print(int(0xFace)) # 64206
# print(int(2+5j)) TypeError
print(int('10')) # 10

# float()
print(float(10)) # 10.0
print(float(0b1111)) # 15.0
print(float(0o456)) # 302.0
print(float(False)) # 0.0
print(float(True)) # 1.0
print(float(0xFace)) # 64206.0
print(float('10')) # 10.0
print(float(100.5)) # 100.5
print(float('100.0')) # 100.0
# print(float(20+5j)) TypeError

# complex()
print(complex(200)) # 20+0j
print(complex(20.5)) # 20.5+0j
print(complex(0b1111)) # 15+0j
print(complex(True)) # 1+0j

print(complex('10'))
print(complex('10.5')) # 10.5+0j

print(complex(10, 20)) # 10+20j
print(complex(25.5, 45)) # 20.5+45j
# print(complex('10', '20')) TypeError
# print(complex('10', 20)) TypeError
# print(complex(10, '50')) TypeError

# bool()
print(bool('')) # False
print(bool(12)) # True
print(bool(2+8j)) # True
print(bool(0+0j)) # False
print(bool(1+0j)) # True
print(bool(0xFade)) # True
print(bool('string')) # True
print(bool(0.1)) # True
print(bool(0.0)) # False
print(bool('False')) # True

# str()
print(str(0b1111)) # '15'
print(str(115)) # '115'
print(str(0.5)) # '0.5'
print(str(5+2j)) # '5+2j'
print(str(True)) # 'True'