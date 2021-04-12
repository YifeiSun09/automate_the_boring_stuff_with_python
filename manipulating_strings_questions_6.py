tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]
#empty dictionary for sorting the data
newTable={0:[],1:[],2:[],3:[]}
#iterate through each list tableData
for i in tableData:
    for j in range(len(i)):
        #put each item of tableData into newTable by index
        newTable[j].append(i[j])

longest=0
for k,v in newTable.items():
    length=len(''.join(v))
    if length>longest:
        longest=length
for k,v in newTable.items():
    print(' '*(longest-len(''.join(v)))+' '.join(v))