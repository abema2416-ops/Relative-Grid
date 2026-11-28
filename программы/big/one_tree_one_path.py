"""Одно дерево — один путь (идея автора). Путь = один набор из k множителей-кандидатов.
Каждое «дерево» проверяет свой набор; деревья запускаются параллельно на всех ядрах."""
import itertools, math, time, sys, os
from multiprocessing import Pool
P=[2,3,5,7,11,13,17,19,23,29,31,37]
def cands(H):
    ps=[p for p in P if any(h%p==0 for h in H)]
    C=set()
    for h in H:
        f=[p for p in ps if h%p==0]
        for r in range(1,len(f)+1):
            for c in itertools.combinations(f,r): C.add(math.prod(c))
    return sorted(C)
def tree(args):                       # одно дерево = один путь
    H,M=args; S={1}
    for m in M: S|={x*m for x in S}
    return M if all(h in S for h in H) else None
def forest(H,k,limit):
    C=cands(H); n=math.comb(len(C),k); t=time.time(); done=0
    with Pool(os.cpu_count()) as pool:
        for r in pool.imap_unordered(tree,((H,M) for M in itertools.combinations(C,k)),chunksize=2000):
            done+=1
            if r: return r,n,done,time.time()-t
            if time.time()-t>limit: return None,n,done,time.time()-t
    return None,n,done,time.time()-t
if __name__=="__main__":
    tests=[("маленькая",[6,35,210,30],3),("5 высот",[30,42,55,66,105],4),
           ("8 высот (ответ 7)",[130,143,357,2210,6783,8645,440895,881790],7),
           ("задача 9 (12 высот, нужно 11)",[110,299,1218,4030,4070,17670,48433,787930,6697405,10068366,10818885,49560797],11)]
    for name,H,k in tests:
        r,n,done,dt=forest(H,k,60)
        speed=done/max(dt,1e-9)
        print(f"{name}: деревьев нужно {n:.3e}, проверено {done} за {dt:.1f} с "
              f"({speed:,.0f} деревьев/с) → {'найдено '+str(r) if r else 'не найдено'}; "
              f"на все деревья ушло бы ≈ {n/speed/3600/24/365:.2e} лет",flush=True)
