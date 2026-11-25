# check: does alpha* (2 axes, same f, product image) keep the number of holes d in 2D (n=2), with P3 and P5?
import random, itertools, numpy as np
def adj(p,q):return abs(p[0]-q[0])+abs(p[1]-q[1])==1
def act(O,S,G,axes,signs,f):
    a={i:min(s*c[i] for c in G) for i,s in zip(axes,signs)};img={}
    for c in G:
        rng=[]
        for i,s in zip(axes,signs):
            t=s*c[i]-a[i];rng.append([(i,s*(a[i]+f*t+j)) for j in range(f)])
        out=[]
        for combo in itertools.product(*rng):
            q=list(c)
            for i,v in combo:q[i]=v
            out.append(tuple(q))
        img[c]=out
    rest=O-G;new=set(x for v in img.values() for x in v)
    if new&rest or len(new)!=sum(len(v) for v in img.values()):return None
    S2=set()
    for v in img.values():
        for p in v:
            for q in v:
                if adj(p,q):S2.add(frozenset((p,q)))
    for e in S:
        p,q=tuple(e);P=img.get(p,[p]);Q=img.get(q,[q]);pr=[frozenset((x,y)) for x in P for y in Q if adj(x,y)]
        if not pr:return None
        S2|=set(pr)
    return rest|new,S2
def betti1(O,S):
    # complex K: squares, glued along glued sides only (16(a)); compute b1 = dim H1 over Q via ranks
    O=list(O);idx={c:i for i,c in enumerate(O)}
    # vertices/edges of separate squares, then identify via union-find for glued sides
    parent={}
    def f(x):
        while parent.setdefault(x,x)!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def un(a,b):parent[f(a)]=f(b)
    corners=lambda c:[(c[0],c[1]),(c[0]+1,c[1]),(c[0]+1,c[1]+1),(c[0],c[1]+1)]
    sides=lambda c:[((c[0],c[1]),(c[0]+1,c[1])),((c[0]+1,c[1]),(c[0]+1,c[1]+1)),((c[0],c[1]+1),(c[0]+1,c[1]+1)),((c[0],c[1]),(c[0],c[1]+1))]
    for e in S:
        a,b=tuple(e)
        common=set(corners(a))&set(corners(b))
        for pt in common:un(('v',a,pt),('v',b,pt))
        sa=[s for s in sides(a) if set(s)==common][0]
        un(('e',a,sa),('e',b,sa))
    V={};E={};
    for c in O:
        for pt in corners(c):V.setdefault(f(('v',c,pt)),None)
        for s in sides(c):E.setdefault(f(('e',c,s)),(f(('v',c,s[0])),f(('v',c,s[1]))))
    vi={v:i for i,v in enumerate(V)};ei={e:i for i,e in enumerate(E)}
    d1=np.zeros((len(V),len(E)))
    for e,(u,w) in E.items():
        d1[vi[u],ei[e]]-=1;d1[vi[w],ei[e]]+=1
    d2=np.zeros((len(E),len(O)))
    for c in O:
        s=sides(c);sg=[1,1,-1,-1]
        for side,g in zip(s,sg):d2[ei[f(('e',c,side))],idx[c]]+=g
    r1=np.linalg.matrix_rank(d1) if len(E) else 0;r2=np.linalg.matrix_rank(d2)
    return len(E)-r1-r2
rng=random.Random(1);tests=0;changed=0;mixed=0
for trial in range(4000):
    O={(0,0)};S=set()
    for step in range(rng.randint(2,7)):
        cl=list(O);G=set(rng.sample(cl,rng.randint(1,len(cl))))
        kind=rng.random()
        if kind<.4:
            r=act(O,S,G,(rng.randint(0,1),),(rng.choice((1,-1)),),rng.randint(2,3))
        elif kind<.8:
            r=act(O,S,G,(0,1),(rng.choice((1,-1)),rng.choice((1,-1))),rng.randint(2,3))
            if r:
                d0=betti1(O,S);d1_=betti1(*r);tests+=1
                if d0!=d1_:changed+=1;print('CHANGED',sorted(O),d0,d1_)
        else:
            cont=[frozenset((p,q)) for p in O for q in O if p<q and adj(p,q) and frozenset((p,q)) not in S]
            if cont:S=S|set(rng.sample(cont,rng.randint(1,len(cont))));r=None
            else:r=None
        if r:O,S=r
print('alpha* tests',tests,'d changed',changed)
