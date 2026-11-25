import sys
src=open('hunt.py').read().split("rng=random.Random(int(sys.argv[1]))")[0];exec(src)
def rule_bigmode(H,score):
    # author: always take the biggest part that several heights share (largest "mode"), even if it is made of smaller ones
    C=counts(H);cand=sorted([d for d in C if C[d]>=2],key=lambda d:score(d,C),reverse=True)
    M=[];nb=0
    for d in cand:
        T=M+[d];b=sum(can_build(h,T) for h in H)
        if b>nb:M=T;nb=b
        # a part that does not build anything yet is still kept if it divides many still-unbuilt heights
        elif sum(1 for h in H if h%d==0 and not can_build(h,M))>=3 and all(d%m for m in M if m>1):M=T
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:(d,))
SC={'крупнее':lambda d,C:d,'крупнее*частота':lambda d,C:C[d]*math.log(d),'частота, потом крупнее':lambda d,C:(C[d],d)}
def full(H):
    best,r=all_rules2(H)
    for n,s in SC.items():
        S=rule_bigmode(H,s);S=improve(H,S);r['бол. мода: '+n]=len(S)
    return min(r.values()),r
CE=[[2, 8, 16, 2058, 2744, 4802, 5145, 5488, 10290, 16464, 19208, 21952, 32928, 43904, 4941258, 10588410, 11294304, 12353145, 13176688, 14117880, 21176820, 24706290, 52706752, 79060128, 84707280, 169414560, 225886080, 13558811952, 25422772410, 27117623904, 29054597040, 33897029880, 50845544820, 67794059760, 216940991232, 232436776320, 406764358560, 139520174986080],
[9, 16, 144, 288, 625, 1250, 1500, 3375, 5625, 6750, 10000, 11250, 13500, 20000, 24000, 27000, 30375, 60750, 90000, 108000, 432000, 937500, 972000, 1875000, 2109375, 4218750, 5062500, 8437500, 10125000, 15000000, 18984375, 30000000, 37968750, 45562500, 67500000, 81000000, 91125000, 1458000000, 3164062500, 6328125000, 28476562500, 50625000000, 101250000000, 455625000000, 911250000000]]
if __name__=="__main__":
    for H in CE:
        print({n:len(improve(H,rule_bigmode(H,s))) for n,s in SC.items()})
