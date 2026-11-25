from bigmode import *
def find(Mt,seed=6):
    rng=random.Random(seed)
    configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
    while True:
        pool,maxe,maxp=rng.choice(configs);k=rng.choice([5,6]);H,M=make2(k,rng,pool,maxe,maxp)
        if sorted(M)==Mt:return H
def peel(H,score):
    rem={h:h for h in H};M=[]
    while any(v>1 for v in rem.values()):
        C=Counter()
        for h,v in rem.items():
            if v>1:
                for d in divisors(v):
                    if d>1:C[d]+=1
        d=max(C,key=lambda d:score(C[d],d));M.append(d)
        for h in rem:
            if rem[h]>1 and rem[h]%d==0:rem[h]//=d
    return improve(H,prune(M,H,lambda d:d))
def greedy_gold(H,score):
    C=counts(H);cand=sorted([d for d in C if C[d]>=2],key=lambda d:score(C[d],d),reverse=True);M=[];nb=0
    for d in cand:
        T=M+[d];b=sum(can_build(h,T) for h in H)
        if b>nb:M=T;nb=b
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return improve(H,prune(M,H,lambda d:(C.get(d,0),d)))
S={'частота×log(величина)':lambda c,d:c*math.log(d),'частота²×log':lambda c,d:c*c*math.log(d),'частота×величина':lambda c,d:c*d,'частота×корень':lambda c,d:c*d**.5}
if __name__=="__main__":
  cases={'4,18,1000,5000,25000':find([4,18,1000,5000,25000]),'6,216,540,3125,10000,16875':find([6,216,540,3125,10000,16875])}
  for nm,H in cases.items():
      print(nm, {k:(len(peel(H,f)),len(greedy_gold(H,f))) for k,f in S.items()},flush=True)
