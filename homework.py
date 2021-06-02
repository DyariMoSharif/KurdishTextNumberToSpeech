# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:41:54 2021

@author: Dyari M.shareef
"""


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
            if len(res)!=0:
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

entered=int(input()) #enter a number
#entered=3

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
if len(resAll)!=0:
    resAll+=['1000','w']
resAll+=thno(entered[3:6])
resAll

resAll[0]
if len(resAll)>4:
    if (resAll[1]=='100') & (resAll[0]=='1'):
        resAll[0]='none'
if len(resAll)>4:
    if (resAll[9]=='100')  & (resAll[8]=='1'):
        resAll[8]='none'

resAll = [i for i in resAll if i != 'none']

for i in resAll:
    outLoud=i+'.wav'
    playsound(outLoud)

resAll