# Check bd mobile number is valid or not

import re

mobileNumberInput = input("Enter mobile number: ")
# mobileNumberInput = '01745090164'
regexPattern = '[0-9]{3}[0-9]{8}'

pattern = re.fullmatch(regexPattern, mobileNumberInput)

if pattern:
    print(pattern.group())
else:
    print('Nope')
