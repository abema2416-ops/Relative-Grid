# Сквозные дыры и полости в 3D: формула против честного счёта гомологий (над GF(2)).
import random, itertools
def complex_of(O):
    V=set();E=set();F=set()
    for (x,y,z) in O:
        for d in itertools.product((0,1),repeat=3): V.add((x+d[0],y+d[1],z+d[2]))
        for ax in range(3):
            o=[a for a in range(3) if a!=ax]
            for d1 in (0,1):
                for d2 in (0,1):
                    b=[x,y,z]; b[o[0]]+=d1; b[o[1]]+=d2; E.add((tuple(b),ax))
            for d in (0,1):
                b=[x,y,z]; b[ax]+=d; F.add((tuple(b),ax))   # грань с нормалью ax
    return V,E,F
def comps(nodes,nb):
    nodes=set(nodes);seen=set();c=0
    for s in nodes:
        if s in seen: continue
        c+=1;st=[s];seen.add(s)
        while st:
            u=st.pop()
            for v in nb(u):
                if v in nodes and v not in seen: seen.add(v);st.append(v)
    return c
def formula(O,box):
    V,E,F=complex_of(O); chi=len(V)-len(E)+len(F)-len(O)
    b0=comps(O,lambda c:[(c[0]+a,c[1]+b,c[2]+d) for a,b,d in itertools.product((-1,0,1),repeat=3)])
    # полости: компоненты пустых клеток (по граням) внутри увеличенной коробки, не касающиеся её края
    lo=-1;hi=box
    empty=[c for c in itertools.product(range(lo,hi+1),repeat=3) if c not in O]
    nb=lambda c:[(c[0]+a,c[1]+b,c[2]+d) for a,b,d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
    cav=comps(empty,nb)-1
    return b0, b0+cav-chi, cav
def rank2(rows):
    # rows: list of int bitmasks; gaussian elimination over GF(2)
    piv={};r=0
    for v in rows:
        while v:
            h=v.bit_length()-1
            if h in piv: v^=piv[h]
            else: piv[h]=v;r+=1;break
    return r
def homology(O):
    V,E,F=complex_of(O); V=sorted(V);E=sorted(E);F=sorted(F);C=sorted(O)
    vi={v:i for i,v in enumerate(V)}; ei={e:i for i,e in enumerate(E)}; fi={f:i for i,f in enumerate(F)}
    d1=[]
    for (b,ax) in E:
        e=list(b);e[ax]+=1; d1.append((1<<vi[b])|(1<<vi[tuple(e)]))
    d2=[]
    for (b,ax) in F:
        o=[a for a in range(3) if a!=ax];m=0
        for k in range(2):
            for t in (0,1):
                p=list(b);p[o[1-k]]+=t; m|=1<<ei[(tuple(p),o[k])]
        d2.append(m)
    d3=[]
    for c in C:
        m=0
        for ax in range(3):
            for t in (0,1):
                p=list(c);p[ax]+=t;m|=1<<fi[(tuple(p),ax)]
        d3.append(m)
    r1,r2,r3=rank2(d1),rank2(d2),rank2(d3)
    b0=len(V)-r1; b1=len(E)-r1-r2; b2=len(F)-r2-r3
    return b0,b1,b2
random.seed(1); bad=0; n=0
for trial in range(1500):
    box=random.choice([3,4]); p=random.uniform(.3,.8)
    O={c for c in itertools.product(range(box),repeat=3) if random.random()<p}
    if not O: continue
    f=formula(O,box); h=homology(O); n+=1
    if (f[0],f[1],f[2])!=h: bad+=1; print("MISMATCH",f,h)
# известные фигуры
ring={(x,y,0) for x in range(3) for y in range(3)}-{(1,1,0)}
shell={c for c in itertools.product(range(3),repeat=3)}-{(1,1,1)}
print("кольцо:",formula(ring,3),homology(ring)," пузырь:",formula(shell,3),homology(shell))
print("проверено",n,"ошибок",bad)
