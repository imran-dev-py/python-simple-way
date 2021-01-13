# Fundamental data types are :=
# str, int, float, complex, bool

# once we create an object we can't perform any changes in that object. If we're trying to perform any 
# changes, with these changes a new object will be created.
# All fundamental data types are immutable

x = 10 # object will be created and point to x
print(id(x)) # 169...728
x = x + 1 # new object will be created and point to x
print(id(x)) # 169...744

x = 50
y = x
print(id(x)) # ...368
print(id(y)) # ...368

x += 5
print(id(x)) # ...448
print(id(y)) # ...368

a = b = c = 10 # abc point to same object, so only one object will be created with 3 ref variables
print(id(a), id(b), id(c)) # ...104 ...104 ...104

# advantage of reuseable object is memory utilization and performance speed

a = 5+2j
b = 5+2j
# complex number is immutable but not share same object. but remaining data types share same object 
# if content is same.. look above
print(a is b) # False

a = 11+0j
b = a
print(a is b) # True

print('hello' is 'hello') # True
print(10 is 10) # True
print(10.6 is 10.6) # True
print(False is False) # True
print(2+8j is 2+8j) # False