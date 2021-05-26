dang={
    '1':'yak.wav','2':'du.wav','3':'se.wav','4':'char.wav','5':'pench.wav','6':'shash.wav','7':'haft.wav','8':'hasht.wav',
    '9':'no.wav','10':'da.wav','11':'yazda.wav','12':'dwazda.wav','13':'sezda.wav','14':'charda.wav','15':'pazda.wav',
    '16':'shazda.wav','17':'havda.wav','18':'hajda.wav','19':'nozda.wav','20':'bist.wav','30':'si.wav','40':'chl.wav',
    '50':'penjy.wav','60':'shest.wav','70':'hafte.wav','80':'hashte.wav','90':'nohat.wav','100':'sad.wav',
    '1000':'hzar.wav','1000000':'mlyon.wav','w':'wu.wav'
}

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
    playsound(dang['1'])
    playsound(dang['1000000'])
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
    playsound(dang[i])
resAll