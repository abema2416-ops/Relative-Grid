import random, sys
from collections import deque
# 2D/3D cells as tuples; gluings as frozenset pairs (side only). P3 + P5.
def stretch(cells, glue, G, ax, s, f):
    a=min(s*c[ax] for c in G)
    rest=cells-G; img={}; new=set(rest); ng=set()
    for c in G:
        t=s*c[ax]-a; lst=[]
        for j in range(f):
            p=list(c); p[ax]=s*(a+f*t+j); p=tuple(p)
            if p in rest: return None
            lst.append(p)
        img[c]=lst
        for j in range(1,f): ng.add(frozenset((lst[j-1],lst[j])))
        new|=set(lst)
    for c in rest: img[c]=[c]
    for g in glue:
        A,B=tuple(g); ok=False
        for u in img[A]:
            for w in img[B]:
                if sum(abs(x-y) for x,y in zip(u,w))==1: ng.add(frozenset((u,w))); ok=True
        if not ok: return None
    return frozenset(new), frozenset(ng)
def norm(cells):
    m=[min(c[k] for c in cells) for k in range(len(next(iter(cells))))]
    return frozenset(tuple(c[k]-m[k] for k in range(len(m))) for c in cells)
def seg_steps(cells, glue, dim, fmax):
    out=[]
    for ax in range(dim):
        lines={}
        for c in cells:
            key=c[:ax]+c[ax+1:]; lines.setdefault(key,[]).append(c[ax])
        segs=[]
        for key,v in lines.items():
            v.sort(); cur=[v[0]]
            for q in v[1:]:
                if q==cur[-1]+1: cur.append(q)
                else: segs.append((key,cur)); cur=[q]
            segs.append((key,cur))
        def cell(key,q): return key[:ax]+(q,)+key[ax:]
        for s in (1,-1):
            for kind in (0,1):
                groups={}
                for key,v in segs:
                    k= (v[0] if s==1 else v[-1]) if kind==0 else (v[-1] if s==1 else v[0])
                    groups.setdefault(k,[]).append((key,v))
                for k,g in groups.items():
                    if len(g)>12: continue
                    for m in range(1,1<<len(g)):
                        G=set()
                        for b in range(len(g)):
                            if m>>b&1:
                                key,v=g[b]
                                if kind==0: G|={cell(key,q) for q in v}
                                else: G.add(cell(key, v[-1] if s==1 else v[0]))
                        for f in range(2,fmax+1):
                            r=stretch(cells,glue,frozenset(G),ax,s,f)
                            if r: out.append(r)
    return out
def lseg(target, dim, maxd, fmax):
    t=norm(target)
    start=(frozenset({(0,)*dim}),frozenset())
    if norm(start[0])==t: return 0
    fr=[start]; seen={(norm(start[0]),)}
    for d in range(1,maxd+1):
        nf=[]
        for c,g in fr:
            for nc,ngl in seg_steps(c,g,dim,fmax):
                n=norm(nc)
                if n==t: return d
                # prune: must fit target frame
                ext=[max(x[k] for x in n)+1 for k in range(dim)]
                text=[max(x[k] for x in t)+1 for k in range(dim)]
                if any(e>te for e,te in zip(ext,text)): continue
                if len(nc)>len(t): continue
                key=(n,)
                if key in seen: continue
                seen.add(key); nf.append((nc,ngl))
        fr=nf
    return None
random.seed(int(sys.argv[1])); dim=int(sys.argv[2]); L=int(sys.argv[3]); N=int(sys.argv[4]); maxcells=int(sys.argv[5])
found=0; tested=0
for it in range(N):
    cells=frozenset({(0,)*dim}); glue=frozenset(); chain=[]
    ok=True
    for step in range(L):
        for tries in range(50):
            k=random.randint(1,len(cells)); G=frozenset(random.sample(sorted(cells),k))
            ax=random.randrange(dim); s=random.choice((1,-1)); f=random.choice((2,2,3))
            r=stretch(cells,glue,G,ax,s,f)
            if r and len(r[0])<=maxcells: cells,glue=r; chain.append((sorted(G),ax,s,f)); break
        else: ok=False; break
    if not ok: continue
    tested+=1
    d=lseg(cells,dim,L,4)
    if d is None:
        found+=1
        print("CANDIDATE", sorted(norm(cells)), chain, flush=True)
print("tested",tested,"candidates",found)
