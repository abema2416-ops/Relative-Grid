from roots import *
targets=[[2,9,16,20,25,2000,8100],[2,3,4,36,121,324,1323]]
found={};rng=random.Random(31)
while len(found)<2:
    k=rng.choice([5,6,7]);H,M=(sparse_make(k,rng) if rng.random()<.5 else make2(k,rng,*rng.choice([([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3)])))
    if sorted(M) in targets and tuple(sorted(M)) not in found:found[tuple(sorted(M))]=H
json.dump({str(list(k)):v for k,v in found.items()},open('last2.json','w'))
for M,H in found.items():
    Hs=sorted(set(H));Q=Counter()
    for a in Hs:
        for b in Hs:
            if a>b and a%b==0:Q[a//b]+=1
    for h in Hs:Q[h]+=1
    order=sorted(Q,key=lambda q:(-Q[q],-q))
    print('тайные',list(M),'высот',len(Hs),'| места тайных в списке остатков:',{m:(order.index(m)+1 if m in Q else None,Q.get(m,0)) for m in M})
