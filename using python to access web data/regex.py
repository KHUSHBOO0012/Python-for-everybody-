# 1. Import regex
import re

f = open('regex_sum_108125.txt', 'r')
total = 0

for line in f:
    numbers = map(int, re.findall('[0-9]+', line))
    total += sum(numbers)
print (total)