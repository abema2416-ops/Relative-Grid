from bigmode import *
def rule_maxmode(H):
    # largest common part for every group size: for each count c (from many heights to 2), the largest divisor shared by c heights
    C=counts(H);lev={}
    for d,c in C.items():
        if c>=2 and d>lev.get(c,1):lev[c]=d
    M=[]
    for c in sorted(lev,reverse=True):
        d=lev[c];T=M+[d]
        if not can_build(d,M) or sum(can_build(h,T) for h in H)>sum(can_build(h,M) for h in H):M=T
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return improve(H,prune(M,H,lambda d:(C.get(d,0),d)))
if __name__=="__main__":
    from why import H as H1
    print('4,18,1000...:',sorted(rule_maxmode(H1)),len(rule_maxmode(H1)))
