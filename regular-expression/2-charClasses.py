import re

match = re.finditer('[abc]', 'a789@bk9z')  # a or b or c match
match = re.finditer('[^abc]', 'a789@bk9z')  # except abc
match = re.finditer('[a-z]', 'a789@bk9z')  # a to z any char

for m in match:
    print(m.group())

# Predefined char classes ==>
# \s ==> special character
# \S ==> except special character
# \W ==> except alpha numeric character only spacial character [^a-zA-Z0-9]
# \w ==> any alpha numeric char [a-zA-Z0-9]
# . ==> any character
# \d ==> any digit [0-9] or \d
# \D ==> except any digit (alphabet + special chars)

print()
matchPattern = re.finditer(r'\w', 'a7b @k9z')
for match in matchPattern:
    print(match.group())
