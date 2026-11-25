from structrule import *
from seed import cover
def keylock(H,beam=8,K=10):
    """author's 'ключ и замок': take a key (small part used by the most heights), divide it out,
    look for the next key in what is left (the residuals), ... until the last part (the lock) closes the list;
    try several keys at each step (beam) and compare the finished sets (сравнение)."""
    H=sorted(set(H));best=None;states=[[]]
    for depth in range(len(H)+1):
        new=[]
        for M in states:
            R=[h for h in H if not can_build(h,M)]
            if not R:
                S=prune(M,H,lambda d:d)
                if best is None or len(S)<len(best):best=S
                continue
            res=[h//cover(h,M) for h in R]
            C=Counter()
            for r in set(res):
                for d in divisors(r):
                    if d>1:C[d]+=res.count(r)
            cands=sorted(C,key=lambda d:(-C[d],-d))[:K]+sorted(set(res))[:3]
            for d in dict.fromkeys(cands):new.append(M+[d])
        if not new:break
        def score(M):
            b=sum(can_build(h,M) for h in H);return (b,sum(math.log(cover(h,M)) for h in H),-len(M))
        new.sort(key=score,reverse=True);states=new[:beam]
        if best is not None and min(len(s) for s in states)>=len(best):break
    return best
if __name__=="__main__":
    F=json.load(open('last3.json'))
    for f in F:
        t=time.time();S=keylock(f['H']);print('тварина: ответ',f['k'],'ключ-замок',len(S),sorted(S),'тайные',f['M'],round(time.time()-t,1),'с',flush=True)
    d=json.load(open('boss.json'));t=time.time();S=keylock(d['H']);print('босс: ключ-замок',len(S),round(time.time()-t),'с',flush=True)
