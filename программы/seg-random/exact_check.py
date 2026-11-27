import sys, itertools
sys.setrecursionlimit(10000)
exec(open('rnd.py').read().split("random.seed")[0])
def full_steps(cells,glue,dim,fmax):
    cl=sorted(cells); out=[]
    for k in range(1,len(cl)+1):
        for G in itertools.combinations(cl,k):
            G=frozenset(G)
            for ax in range(dim):
                for s in (1,-1):
                    for f in range(2,fmax+1):
                        r=stretch(cells,glue,G,ax,s,f)
                        if r: out.append(r)
    return out
def bfs(target,dim,maxd,stepfn):
    t=norm(target); text=[max(x[k] for x in t)+1 for k in range(dim)]; fmax=max(text)
    start=(frozenset({(0,)*dim}),frozenset()); fr=[start]; seen=set()
    def key(c,g):
        m=[min(x[k] for x in c) for k in range(dim)]
        sh=lambda x: tuple(x[k]-m[k] for k in range(dim))
        return (frozenset(map(sh,c)), frozenset(frozenset(map(sh,p)) for p in g))
    seen.add(key(*start))
    for d in range(1,maxd+1):
        nf=[]
        for c,g in fr:
            for nc,ng in stepfn(c,g,dim,fmax):
                n=norm(nc)
                if n==t: return d
                ext=[max(x[k] for x in n)+1 for k in range(dim)]
                if any(e>te for e,te in zip(ext,text)) or len(nc)>len(t): continue
                kk=key(nc,ng)
                if kk in seen: continue
                seen.add(kk); nf.append((nc,ng))
        fr=nf
    return None
T=[eval(x) for x in sys.argv[1:]]
for tgt in T:
    tgt=set(tgt)
    a=bfs(tgt,2,4,full_steps); b=bfs(tgt,2,5,seg_steps)
    print("cells",len(tgt),"l_alpha",a,"l_seg",b,flush=True)
