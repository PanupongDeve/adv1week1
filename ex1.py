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


def getMoney(lists):
    money = []
    for list in lists:
        tmp = list.split(":")
        money.append(int(tmp[1]))
    money = sorted(money)
    money.reverse()     
    return money
def sumMoney(lists):
    result = 0
    for list in lists:
        result += list
    return result
def showDetail(lists,money):
    for list in lists:
        print(list)
    message = '\nSum Money :' +'{result}'.format(result = money)
    print(message)

# Main
lists = readFile("employee")
lists = getMoney(lists)
money = sumMoney(lists)
showDetail(lists,money)
