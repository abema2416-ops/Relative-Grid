from bigmode import *
def rule_peel(H):
    # author: take the number (<= the largest divisor) that divides the most heights; among those, the largest; divide it out; repeat
    rem={h:h for h in H};M=[]
    while any(v>1 for v in rem.values()):
        C=Counter()
        for v in set(x for x in rem.values() if x>1):
            pass
        C=Counter()
        for h,v in rem.items():
            if v>1:
                for d in divisors(v):
                    if d>1:C[d]+=1
        d=max(C,key=lambda d:(C[d],d))
        M.append(d)
        for h in rem:
            if rem[h]%d==0 and rem[h]>1:rem[h]//=d
    M=prune(M,H,lambda d:d)
    return improve(H,M)
if __name__=="__main__":
    from why import H as H1
    S=rule_peel(H1);print(len(S),sorted(S))
