import os
# Function 
def readFile(filename):
    lists = []
    i = 0
    f = open( filename+'.txt')
    for line in f:
        lists.append(line.strip('\n'))
        i += 1
    f.close()
    return lists
def writeFile(lists):
    for list in lists:
        details = []
        tmp = list.split("=")
        id = tmp[0]
        msg1 = 'id='+id
        details.append(msg1)
        group = tmp[1]
        msg2 = 'group='+group
        details.append(msg2)
        os.mkdir(id)
        f = open( id+'/work.conf','w')
        print()
        for detail in details:
            f.write(detail+"\n")
    f.close()
    
# Main
student = readFile('student')
writeFile(student)
print("Succes!!!")