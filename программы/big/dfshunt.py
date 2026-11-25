from dfs import *
import sys
rng=random.Random(int(sys.argv[1]));t=time.time();n=ok=0;fails=[]
while time.time()-t<float(sys.argv[2]):
    k=rng.choice([5,6,7]);H,M=(sparse_make(k,rng) if rng.random()<.5 else make2(k,rng,*rng.choice([([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3)])))
    S=diff_dfs(H,tlimit=20);d=len(S) if S else 99;n+=1;ok+=d==k
    if d!=k:fails.append({'M':sorted(M),'H':H,'k':k,'got':d});print('ТВАРИНА',sorted(M),len(H),k,d,flush=True)
    if n%20000==0:print('...',n,ok,flush=True)
json.dump(fails,open(f'dfsfails_{sys.argv[1]}.json','w'))
print('задач',n,'точно',ok,flush=True)
