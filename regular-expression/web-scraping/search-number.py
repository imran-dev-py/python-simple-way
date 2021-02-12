# find the phone number from redbus.in website

import re
import urllib.request

openUrl = urllib.request.urlopen(
    "https://www.redbus.in/info/contactus")
readUrl = openUrl.read()

phoneNumbers = re.findall(
    r'[+][1-9]{4}\s[0-9]{4}\s[0-9]{2}', str(readUrl))

print(phoneNumbers)
