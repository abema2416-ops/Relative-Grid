import sys
from pipe import *
F=json.load(open('fails_21.json'))+json.load(open('fails_22.json'))
for i in map(int,sys.argv[1:]):
    f=F[i];t=time.time();b=method_v2(f['H']);print(f['M'],'ответ',f['k'],'v1',f['v1'],'v2',b,round(time.time()-t),'c',flush=True)
