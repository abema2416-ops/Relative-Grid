# formal alpha from 1.7 (stretch), with glue transfer and rules P3, P5
def stretch(O,S,Z,i,s,f):
    G={c for c in O if c in Z}
    a=min(s*c[i] for c in G)
    img={}
    for c in G:
        t=s*c[i]-a
        img[c]=[tuple((s*(a+f*t+j)) if k==i else c[k] for k in range(len(c))) for j in range(f)]
    new=set(x for v in img.values() for x in v)
    rest=O-G
    assert not (new & rest),'P3 collision'
    im=lambda c: img.get(c,[c])
    adj=lambda p,q: sum(abs(x-y) for x,y in zip(p,q))==1
    S2=set()
    for v in img.values():   # cells of one image glued in a row
        for p,q in zip(v,v[1:]):S2.add(frozenset((p,q)))
    for e in S:
        c,d=tuple(e);pairs=[(p,q) for p in im(c) for q in im(d) if adj(p,q)]
        assert pairs,'P5 tear %s'%(e,)
        for p,q in pairs:S2.add(frozenset((p,q)))
    return rest|new,S2
O={(0,0)};S=set()
O,S=stretch(O,S,O,0,1,5)                      # 1: x, x5 -> 5 cells
O,S=stretch(O,S,{(2,0),(4,0)},1,1,2)          # 2: columns 3 and 5 up x2
O,S=stretch(O,S,{(0,0),(2,0),(2,1)},1,1,3)    # 3: columns 1 and 3 up x3
print([max(y for x,y in O if x==c)+1 for c in range(5)], len(O))
