# given email is valid or not

import re
emailId = input('Enter email id ')
regexPattern = r'[a-z0-9_\.]+[@][a-z]+[.][a-z]+'
patternMatch = re.findall(regexPattern, emailId, re.IGNORECASE)
print(patternMatch)
