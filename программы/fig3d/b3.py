# 3D lossless minimal construction: alpha (1 axis) and optionally alpha* (2 axes, same coefficient, product), any zones,
# P3 (no collisions), P5 (glue transfer, no tearing); one beta at the end if cracks remain.
import sys, itertools
def norm(cells,glue):
    m=[min(c[k] for c in cells) for k in range(3)]
    sh=lambda c:(c[0]-m[0],c[1]-m[1],c[2]-m[2])
    return frozenset(map(sh,cells)),frozenset(frozenset(map(sh,e)) for e in glue)
def adj(p,q):return sum(abs(a-b) for a,b in zip(p,q))==1
def contacts(cells):
    r=set()
    for p in cells:
        for k in range(3):
            q=list(p);q[k]+=1;q=tuple(q)
            if q in cells:r.add(frozenset((p,q)))
    return r
def act(cells,glue,Z,axes,signs,f):
    a={i:min(s*c[i] for c in Z) for i,s in zip(axes,signs)}
    img={}
    for c in Z:
        ranges=[]
        for i,s in zip(axes,signs):
            t=s*c[i]-a[i];ranges.append([(i,s*(a[i]+f*t+j)) for j in range(f)])
        lst=[]
        for combo in itertools.product(*ranges):
            q=list(c)
            for i,v in combo:q[i]=v
            lst.append(tuple(q))
        img[c]=lst
    rest=cells-Z;new=set(x for v in img.values() for x in v)
    if new&rest:return None
    ng=set()
    for v in img.values():
        sv=set(v)
        for p in v:
            for q in v:
                if adj(p,q):ng.add(frozenset((p,q)))
    for e in glue:
        p,q=tuple(e);P=img.get(p,[p]);Q=img.get(q,[q]);ok=False
        for x in P:
            for y in Q:
                if adj(x,y):ng.add(frozenset((x,y)));ok=True
        if not ok:return None
    return rest|new,ng
def solve(T,star,maxd=7):
    T=norm(frozenset(T),set())[0];N=len(T);B=[max(c[k] for c in T)+1 for k in range(3)]
    start=norm(frozenset({(0,0,0)}),set());seen={start};fr=[start];best=None
    for d in range(maxd+1):
        for c,g in fr:
            if c==T:
                tot=d+(1 if contacts(c)-set(g) else 0)
                best=tot if best is None else min(best,tot)
        if best is not None and best<=d+1:return best
        nf=[]
        for c,g in fr:
            cl=list(c)
            for k in range(1,len(cl)+1):
                for Z in itertools.combinations(cl,k):
                    Z=frozenset(Z)
                    opts=[((i,),(s,)) for i in range(3) for s in (1,-1)]
                    if star:opts+=[((i,j),(s,t)) for i in range(3) for j in range(i+1,3) for s in (1,-1) for t in (1,-1)]
                    for axes,signs in opts:
                        for f in range(2,max(B[i] for i in axes)+1):
                            if any(f>B[i] for i in axes):continue
                            r=act(c,g,Z,axes,signs,f)
                            if not r:continue
                            nc,ng=norm(*r)
                            if len(nc)>N or any(max(x[k] for x in nc)>=B[k] for k in range(3)):continue
                            key=(nc,ng)
                            if key in seen:continue
                            seen.add(key);nf.append(key)
        fr=nf
        if not fr:break
    return best
def box(a,b,c):return {(x,y,z) for x in range(a) for y in range(b) for z in range(c)}
S={
 'куб 2x2x2':box(2,2,2),
 'брусок 3x2x1':box(3,2,1),
 'брусок 3x3x2 ':None,
 'ёжик 3D (7 клеток)':{(1,1,1),(0,1,1),(2,1,1),(1,0,1),(1,2,1),(1,1,0),(1,1,2)},
 'кольцо 3x3 (плоское)':box(3,3,1)-{(1,1,0)},
 'Г 3D: 2x2x2 + выступ':box(2,2,2)|{(2,0,0)},
 'ступени 2x2 высоты 1,2,2,3':{(0,0,0),(1,0,0),(0,1,0),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(1,1,2)},
 'П 3D (арка 3x1x2 с дыркой)':{(0,0,0),(2,0,0),(0,0,1),(1,0,1),(2,0,1)},
}
name=sys.argv[1];T=S[name]
print(name,'| только α:',solve(T,False),'| α и α*:',solve(T,True),flush=True)
