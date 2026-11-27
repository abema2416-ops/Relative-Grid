import itertools, sys
sys.path.insert(0,'../anyfig'); from bfs import stretch, norm
W,H=3,6; target=[3,2,4]
start=norm(frozenset({(0,0)}),set()); par={start:None}; fr=[start]
def relief(c):
    xs={x for x,y in c}
    if xs!=set(range(W)): return None
    h=[]
    for x in range(W):
        ys=sorted(y for xx,y in c if xx==x)
        if ys!=list(range(len(ys))): return None
        h.append(len(ys))
    return h
found=None
for d in range(1,4):
    nf=[]
    for st in fr:
        c,g=st; cl=list(c)
        for k in range(1,len(cl)+1):
            for Z in itertools.combinations(cl,k):
                Z=frozenset(Z)
                for axis in (0,1):
                    for s in (1,-1):
                        for f in range(2,(W if axis==0 else H)+1):
                            r=stretch(c,g,Z,axis,s,f)
                            if not r: continue
                            nc,ng=norm(*r)
                            if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H: continue
                            key=(nc,frozenset(ng))
                            if key in par: continue
                            par[key]=(st,sorted(Z),axis,s,f); nf.append(key)
                            if relief(nc)==target: found=key; break
                        if found: break
                    if found: break
                if found: break
            if found: break
        if found: break
    if found: break
    fr=nf
def show(c):
    rows=[]
    for y in range(H-1,-1,-1):
        rows.append("".join("█" if (x,y) in c else "·" for x in range(W)))
    return "\n".join(rows)
path=[];k=found
while par[k]: path.append((k,par[k][1:])); k=par[k][0]
for st,(Z,axis,s,f) in reversed(path):
    print("зона",Z,"ось","x" if axis==0 else "y","напр",s,"f",f); print(show(st[0])); print()
