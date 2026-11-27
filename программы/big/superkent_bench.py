import sys, random, time, math
sys.argv=[sys.argv[0]]+sys.argv[1:]
exec(open('/tmp/claude-0/-home-claude/70a5592c-c34c-5075-ac31-210cdddf20fb/scratchpad/superkent.py').read().split("H=json.load")[0])
src=open('pipe.py').read().split('if __name__')[0]; exec(src)
rng=random.Random(5)
for k in [5,6,7,8,9]:
    ts=[];bad=0;to=0
    for i in range(8):
        H,M=sparse_make(k,rng) if k<=6 else make2(k,rng,[2,3,5,7,11,13],2,3)
        t=time.time()
        try:
            r,res,nodes=solve(H,len(set(H)),t+60)
            ts.append(time.time()-t); bad+= (r>k)
        except TimeoutError: to+=1
    print(f"k={k}: решено {len(ts)}/8, среднее {sum(ts)/max(1,len(ts)):.2f} с, макс {max(ts) if ts else 0:.2f} с, не успел за 60 с: {to}",flush=True)
