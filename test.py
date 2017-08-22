
lists = [None]*3
i = 0
f = open('test.txt')
for line in f:
    lists[i] = line.strip('\n')
    i += 1
f.close()

newLists = sorted(lists)
print(newLists)

f = open('updateTest.txt','w')
for list in newLists:
    f.write(list+"\n")
f.close()


    