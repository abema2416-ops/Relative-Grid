"""Кент скачков (идея автора: точки «номер — высота», считаем повторяющиеся скачки).
Скачок — частное двух высот b/a (если делится). Самые частые скачки — кандидаты в множители.
Берём k самых частых (k от нижней границы вверх, плюс небольшой перебор среди топа) и проверяем,
собираются ли все высоты. Если k = нижней границе — ответ точный."""
import json, math, time, itertools, sys, random
from collections import Counter
def builds(H,M):
    P={1}
    for m in M: P|={x*m for x in P}
    return all(h in P for h in H)
def jumps(H,lb,extra=3,deadline=None):
    H=sorted(set(h for h in H if h>1))
    C=Counter(b//a for a in H for b in H if b>a and b%a==0)
    for h in H: C[h]+=1          # сама высота — тоже скачок от «нуля»
    top=[d for d,_ in C.most_common()]
    for k in range(lb, len(H)+1):
        pool=top[:k+extra]
        for M in itertools.combinations(pool,k):
            if deadline and time.time()>deadline: return None
            if builds(H,M): return k,sorted(M)
    return None
if __name__=="__main__":
    exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
    for name,f in [('гигабосс','boss.json'),('контрпример','fails_7.json')]:
        d=json.load(open(f)); d=d if isinstance(d,dict) else d[0]; H=d['H']
        lb=max(rank(H),math.ceil(math.log2(len(set(H))+1)))
        t=time.time(); r=jumps(H,lb,3,time.time()+60)
        print(f"{name}: нижняя граница {lb}, кент скачков: {r[0] if r else None} {'(= граница, ТОЧНО)' if r and r[0]==lb else ''} за {time.time()-t:.2f} с; множители {r[1] if r else ''}",flush=True)
