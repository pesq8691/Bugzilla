import urllib
import re

# insert any Bugzilla url here and run
# the results are pushed out to a text file named Output.txt

url = "https://bugzilla.mozilla.org/buglist.cgi?resolution=DUPLICATE&classification=Server%20Software&chfieldto=Now&query_format=advanced&chfieldfrom=2015-06-01&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&component=Consumer%20Pages&product=Marketplace";
url2 = 'https://bugzilla.mozilla.org/buglist.cgi?resolution=---&resolution=WORKSFORME&resolution=INCOMPLETE&resolution=SUPPORT&query_format=advanced&bug_status=REOPENED&bug_status=RESOLVED&component=Collector%20Extension&component=Compatibility%20Tools&product=addons.mozilla.org%20Graveyard'
htmlFile = urllib.urlopen(url)
htmlText = htmlFile.read()

data = htmlText.split('<a href="show_bug.cgi?id=')

text_file = open("Output.txt", "w")
item = 1;
for x in range(1, len(data)):
    myString = re.compile('([0-9]+)(">)([0-9]+)(</a>)')
    myObject =  myString.findall(data[x])
    if(len(myObject) > 0):
        print item, ' ', myObject[0][0]
        myItem = myObject[0][0] + ' '
        text_file.write(myItem)
        item += 1

text_file.close()


