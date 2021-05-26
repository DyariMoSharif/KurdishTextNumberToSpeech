def thno(nav):
    naved=str(nav)
    res=[]
    if naved[1]!='1':
        if naved[0]!='0':
            res.append(naved[0])
            res.append('100')
            res.append('w')
        if naved[1]!='0':
            res.append(str(int(naved[1])*10))
            res.append('w')
        if naved[2]!='0':
            res.append(naved[2])
        else:
            res.pop()
            
    if naved[1]=='1':
        if naved[0]!='0':
            res.append(naved[0])
            res.append('100')
            res.append('w')
        if naved[1:3]!='0':
            res.append(str(int(naved[1:3])))
    return res

from playsound import playsound
entered=572037
if entered<1000000:
    entered=format(entered, '6d').replace(' ','0')
elif entered==1000000:
    playsound('1')
    playsound('1000000')
else:
    print('Tikaye, jimareke nabêt le yek milion ziyatir bêt')
    quit()

entered=str(entered)
resAll=[]
resAll+=thno(entered[0:3])
resAll+=['1000','w']
resAll+=thno(entered[3:6])
resAll
for i in resAll:
    outLoud=i+'.wav'
    playsound(outLoud)
resAll