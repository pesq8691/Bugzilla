import urllib
import re
import json

# insert any Bugzilla url here and run
# the results are pushed out to a text file named Output.txt
# we need to make this script able to accept data sent from the js file
# it should also be able to send back the ID's as an array or a json obj
url = 'https://bugzilla.mozilla.org/buglist.cgi?resolution=---&resolution=WORKSFORME&resolution=INCOMPLETE&resolution=SUPPORT&query_format=advanced&bug_status=REOPENED&bug_status=RESOLVED&component=Collector%20Extension&component=Compatibility%20Tools&product=addons.mozilla.org%20Graveyard'
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


