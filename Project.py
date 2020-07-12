import csv
from functools import reduce

data = csv.reader(open('/home/shabarish/Desktop/data.csv'))
table = list(data)
print(table)

table1 = reduce(lambda x,y:x+y,table)
print(table1)

if len(table1) == len(set(table1)):
    print('No Duplicates found')
else:
    print('Duplicates found')

table2 = set(table1)
print(table2)

with open('/home/shabarish/Desktop/text.txt','w') as f:
    f.write('\n'.join(table2))
