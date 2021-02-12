# Regular Expression ==> Reprsent a group of strings according to particular pattern

# Application areas of Regular Expression ==>
# 1) Validations
# 2) Pattern matching
# 3) Translators like compilers, assembler, interpreters
# 4) Develop digital circuits
# 5) communication protocols TCP/IP

# re module contains some methods :-
# 1) compile() ==> convert pattern into regex obj
# 2) finditer() ==> return an iterator object

import re

pattern = re.compile('Python')
print(type(pattern))  # re.pattern

match = pattern.finditer('Learning Python is very easy')
print(match) # <callable_iterator object at 0x01B32D30>

# we can call 3 methods now
# start() -> return start index
# end() -> return end+1 index
# group() -> return full match

for m in match:
    print(m.group())
