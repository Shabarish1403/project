import csv

data = csv.reader(open('/home/shabarish/Desktop/data.csv'))
table = list(data)
print(table)

l = len(table)
table1 = table[0]
i=1
while i<l:
    table1+=table[i]
    i+=1
print(table1)

if len(table1) == len(set(table1)):
    print('No Duplicates found')
else:
    print('Duplicates found')

table2 = set(table1)
print(table2)

with open('/home/shabarish/Desktop/text.txt','w') as f:
    f.write('\n'.join(table2))
