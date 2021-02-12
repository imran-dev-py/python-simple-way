# process of collecting data from web page called web scraping

# web scraping with regex
import urllib.request
import re

websites = ['http://google.com', 'http://yahoo.com']

for website in websites:
    print('Searching..', website)

    url = urllib.request.urlopen(website)
    readUrl = url.read()  # by default it's bytes class
    webTitle = re.findall('<title>.*</title>', str(readUrl), re.IGNORECASE)
    print(webTitle[0])

print(len('919945600000'))
