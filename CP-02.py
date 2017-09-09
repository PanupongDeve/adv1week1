msg = 'Once upone the time'
cutmsg = msg[3:10]
result = msg+' {arrow} '.format(arrow= '=>')+cutmsg
print(result)