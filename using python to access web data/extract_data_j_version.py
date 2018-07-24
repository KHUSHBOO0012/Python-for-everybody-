
import requests

url = raw_input("Enter json URL: ")
counts = []

file = requests.get(url)
data = file.json()
comments = data["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))