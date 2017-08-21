
def checkMax (lists ):
    isMaxlen = max(len(x) for x in lists)
    for list in lists:
        if len(list) == isMaxlen:
            return list

msg = input('Enter you massage: ')
lists = msg.split(" ")

word = checkMax( lists )


print("result is "+word)