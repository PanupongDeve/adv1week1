
def checklang( lists ):
    i = 0
    for list in lists:
        if len(list) < 3:
            del lists[i]
        i += 1
    return lists
msg = input('Enter you massage: ')
lists = msg.split(" ")

lists = checklang(lists)

lists = sorted(lists)

print(lists)