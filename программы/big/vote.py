from power import *
def method_sets(H):
    out={}
    out['настоящее использование']=rule_struct(H)
    out['ключ-замок']=keylock(H,8,10)
    p=power_rule(H)
    if p:out['степенной']=p
    out['большая мода']=improve(H,rule_bigmode(H,SC['крупнее*частота']))
    out['золотая середина']=greedy_gold(H,lambda c,d:c*math.log(d))
    return out
def vote_rule(H,maxk=8):
    """author: 'совпадения в совпадениях' — run the fast methods, take the parts they agree on, and search
    the smallest set only among the parts the methods produced"""
    sets=method_sets(H);V=Counter()
    for S in sets.values():
        for m in set(S):V[m]+=1
    pool=sorted(V,key=lambda m:(-V[m],-m))
    core=[m for m in pool if V[m]>=2]
    best=min(sets.values(),key=len)
    # exact search inside the pool (small), core parts tried first
    for k in range(math.ceil(math.log2(len(set(H))+1)),len(best)):
        for M in itertools.combinations(pool[:22],k):
            if all(can_build(h,M) for h in H):return list(M),sets,V
    return best,sets,V
if __name__=="__main__":
    rng=random.Random(2027)
    while True:
        k=rng.choice([5,6,7]);H,M=sparse_make(k,rng)
        if sorted(M)==[4,8,45,81,625,6075,8100]:break
    t=time.time();S,sets,V=vote_rule(H)
    print('новая тварина, ответ 7:',len(S),sorted(S),round(time.time()-t),'с')
    for n,x in sets.items():print('  ',n,len(x),sorted(x))
    print('  совпадения (сколько методов назвали):',{m:V[m] for m in sorted(V,key=lambda m:-V[m])[:12]})
