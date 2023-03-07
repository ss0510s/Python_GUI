# with open('ipp.csv', 'r') as fp:
#     lines = fp.readlines()
#     lines.pop(0)
#     print(lines)
#     for line in lines:
#         # print(line.rstrip('\n').split(',')[2])
#         if(int(line.rstrip('\n').split(',')[1]) <= 16):
#             print(line.rstrip('\n').split(',')[2])

import csv

with open('ipp.csv','r') as fp:
    freader = csv.reader(fp)
    header = next(freader)
    for rows in freader:
        print(rows[2])