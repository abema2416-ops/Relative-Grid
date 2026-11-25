# lossless minimal construction: stretches only (alpha, any zones, P3, P5 with glue transfer), then one beta at the end if cracks remain
import sys, itertools
def parse(rows):
    return frozenset((x,y) for y,r in enumerate(rows) for x,ch in enumerate(r) if ch=='#')
def norm(cells,glue):
    mx=min(x for x,y in cells);my=min(y for x,y in cells)
    c=frozenset((x-mx,y-my) for x,y in cells)
    g=frozenset(frozenset((a-mx,b-my) for a,b in e) for e in glue)
    return c,g
def adj(p,q):return abs(p[0]-q[0])+abs(p[1]-q[1])==1
def stretch(cells,glue,Z,axis,s,f):
    a=min(s*c[axis] for c in Z);img={}
    for c in Z:
        t=s*c[axis]-a;lst=[]
        for j in range(f):
            p=s*(a+f*t+j);lst.append((p,c[1]) if axis==0 else (c[0],p))
        img[c]=lst
    rest=cells-Z;new=set(x for v in img.values() for x in v)
    if new & rest:return None
    ng=set()
    for v in img.values():
        for p,q in zip(v,v[1:]):ng.add(frozenset((p,q)))
    for e in glue:
        p,q=tuple(e);P=img.get(p,[p]);Q=img.get(q,[q]);ok=False
        for x in P:
            for y in Q:
                if adj(x,y):ng.add(frozenset((x,y)));ok=True
        if not ok:return None
    return rest|new,ng
def contacts(cells):
    return {frozenset((p,(p[0]+1,p[1]))) for p in cells if (p[0]+1,p[1]) in cells}|{frozenset((p,(p[0],p[1]+1))) for p in cells if (p[0],p[1]+1) in cells}
def solve(rows,maxd=7):
    T=parse(rows);T=norm(T,set())[0];N=len(T);W=max(x for x,y in T)+1;H=max(y for x,y in T)+1
    start=norm(frozenset({(0,0)}),set());seen={start};frontier=[start]
    best=None
    for d in range(0,maxd+1):
        for c,g in frontier:
            if c==T:
                cr=len(contacts(c)-set(g))>0
                tot=d+(1 if cr else 0)
                if best is None or tot<best:best=tot
        if best is not None and best<=d+1:return best
        nf=[]
        for c,g in frontier:
            cl=list(c)
            for k in range(1,len(cl)+1):
                for Z in itertools.combinations(cl,k):
                    Z=frozenset(Z)
                    for axis in (0,1):
                        for s in (1,-1):
                            for f in range(2,(W if axis==0 else H)+1):
                                r=stretch(c,g,Z,axis,s,f)
                                if not r:continue
                                nc,ng=norm(*r)
                                if len(nc)>N:continue
                                if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H:continue
                                key=(nc,frozenset(ng))
                                if key in seen:continue
                                seen.add(key);nf.append(key)
        frontier=nf
        if not frontier:break
    return best
if __name__=='__main__':
    print(sys.argv[1],solve(sys.argv[2:]),flush=True)
