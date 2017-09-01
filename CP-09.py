
# Function 
def readFile(lists,filename):
    i = 0
    f = open( filename+'.txt')
    for line in f:
        lists[i] = line.strip('\n')
        i += 1
    f.close()
    return lists

def writeFile(lists,filename):
    f = open( filename+'.txt','w')
    for list in lists:
        f.write(list+"\n")
    f.close()

# main
lists = [None]*3
newLists = readFile(lists,'test')
newLists = sorted(newLists)
print(newLists)
writeFile(newLists,'updateTest')




    