src=open('big2.py').read().split("seed=int(sys.argv[1])")[0];exec(src)
def improve2(H,M):
    C=counts(H);cand=sorted({d for d in C if C[d]>=2}|{math.gcd(a,b) for a,b in itertools.combinations(H,2)}-{1})
    M=list(M);changed=True
    while changed:
        changed=False
        for c1,c2 in itertools.combinations_with_replacement(cand,2):
            T=prune(M+[c1,c2],H,lambda d:(d in (c1,c2),C.get(d,0),d))
            if len(T)<len(M):M=T;changed=True;break
    return M
if __name__=="__main__":
 for H in [[2, 8, 16, 2058, 2744, 4802, 5145, 5488, 10290, 16464, 19208, 21952, 32928, 43904, 4941258, 10588410, 11294304, 12353145, 13176688, 14117880, 21176820, 24706290, 52706752, 79060128, 84707280, 169414560, 225886080, 13558811952, 25422772410, 27117623904, 29054597040, 33897029880, 50845544820, 67794059760, 216940991232, 232436776320, 406764358560, 139520174986080]]:
    S=improve(H,solve_set(H));t=time.time();S2=improve2(H,S);print(len(S),len(S2),sorted(S2),round(time.time()-t))
