
def name( first, last, title='Khun'):
    msg = title+' '+first + ' ' + last
    return msg


msg = name('John', 'Doe', 'Mr.')
print(msg)

msg2 = name('SomChai','Dang')
print(msg2)