"""Кент НОД (идея автора): НОД всех пар высот → самые частые общие куски — первые действия;
затем остатки высот снова раскладываются так же; простые, которые ни с чем не идут, — отдельные действия."""
import json, math, time, sys
from collections import Counter
def cover(h,blocks):
    """можно ли собрать h из части blocks (каждый блок не больше раза) — перебор только среди делителей h"""
    ds=sorted([b for b in blocks if h%b==0],reverse=True)
    def go(r,i):
        if r==1: return True
        for j in range(i,len(ds)):
            if r%ds[j]==0 and math.gcd(ds[j],r//ds[j])==1 and go(r//ds[j],j+1): return True
        return False
    return go(h,0)
def gcd_kent(H):
    H=sorted(set(H)); chosen=[]
    rest={h:h for h in H}                       # что осталось собрать у каждой высоты
    while True:
        todo=[r for r in rest.values() if r>1]
        if not todo: break
        C=Counter()
        for i in range(len(todo)):
            for j in range(i+1,len(todo)):
                g=math.gcd(todo[i],todo[j])
                if g>1: C[g]+=1
        if not C: chosen+= [r for r in set(todo)]; break     # общего нет — остатки идут отдельными действиями
        g,cnt=C.most_common(1)[0]
        if cnt<1: chosen+= list(set(todo)); break
        chosen.append(g)
        for h in rest:
            if rest[h]%g==0 and math.gcd(g,rest[h]//g)==1: rest[h]//=g
    chosen=sorted(set(chosen))
    ok=all(cover(h,chosen) for h in H)
    return chosen,ok
if __name__=="__main__":
    d=json.load(open('hell.json')); H=d['H']; secret=set(d['M_secret'])
    t=time.time(); M,ok=gcd_kent(H)
    print(f"кент НОД: множителей {len(M)}, собирают все высоты: {ok}, за {time.time()-t:.1f} с")
    print(f"из них тайных: {len(set(M)&secret)} из {len(secret)}")
