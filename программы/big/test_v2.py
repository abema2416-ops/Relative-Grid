from pipe import *
F=json.load(open('fails_21.json'))+json.load(open('fails_22.json'))
ok=0
for f in F:
    t=time.time();b=method_v2(f['H']);ok+=b==f['k'];print(f['M'],'ответ',f['k'],'v1',f['v1'],'v2',b,round(time.time()-t),'c',flush=True)
print('v2 fixed',ok,'of',len(F))
