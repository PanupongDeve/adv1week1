

list = [0,0,0,0,0]
result = 0

def getList ( list ):
    for i in range(5):
        list[i] = int(input("Enter list["+str(i)+"]: "))
    return list
def sumpos( list ):
    result = 0
    for x in list:
        if x < 0 :
            continue       
        elif x ==0:
            continue
        else:
            result += x
    return result

list = getList( list )
print(list)
result = sumpos( list )
print(result)