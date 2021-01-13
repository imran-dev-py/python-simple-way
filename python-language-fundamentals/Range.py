# range is represents a sequence of number, it is immutable

r = range(10) # 0 ... 9
print(r) # range(0, 10)
print(type(r)) # range

for i in range(5):
    print(i, end='|')

print()

r = range(20, 5, -5)
print(r[0:2]) # range(20, 10, -5)
print(r[0]) # 20
print(r[1]) # 15