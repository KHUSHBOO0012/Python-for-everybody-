import urllib.request, urllib.parse, urllib.error, json

url = ' http://py4e-data.dr-chuck.net/comments_108130.json'


#extract data
data = urllib.request.urlopen(url).read()

#put the data into a dictionary
data_parsed = json.loads(data)

total = 0
for item in data_parsed['comments']:
    total += int(item['count'])

print ('Total: ', total)