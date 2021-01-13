# print() without args, its return newline

a, b, c = 10, 20, 30
print('Values are:', a, b, c) # Values are: 10 20 30
print('Values are:', a, b, c, sep='|') # Values are:|10|20|30

# print multiple values in a single line
print('hello', end='')
print('durga', end='')
print('soft')

print('Hello', 'Rena', sep=',', end=' <3') # Hello,Rena <3
print()

print(10, 20, 30, sep=':', end='***')
print(40, 50, 60, sep=':')
print(70, 80, sep='**', end='$$')
print(90,100) 
# 10:20:30***40:50:60
# 70**80$$90 100

# difference between below code
print('durga', 'software') # two str will be printed separated by space durga software
print('durga'+'software') # concatenation will be happended and convert it single str 'durgasoftware'