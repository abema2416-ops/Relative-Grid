# Do zones that take only PART of a column let a relief be built in fewer raises than ceil(log2 D)?
# BFS over shapes in a W x H box from one cell: alpha with any zone (subset of current cells), P3, P5 (glues tracked).
import itertools, math, sys
sys.path.insert(0,'../anyfig'); from bfs import stretch, norm, contacts
W,H=int(sys.argv[1]),int(sys.argv[2]);MAXD=int(sys.argv[3])
start=norm(frozenset({(0,0)}),set());depth={start[0]:0};seen={start};fr=[start]
for d in range(1,MAXD+1):
    nf=[]
    for c,g in fr:
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
                            if max(x for x,y in nc)>=W or max(y for x,y in nc)>=H:continue
                            key=(nc,frozenset(ng))
                            if key in seen:continue
                            seen.add(key);nf.append(key)
                            if nc not in depth:depth[nc]=d
    fr=nf;print('depth',d,'states',len(fr),flush=True)
# reliefs: every column a solid stack from y=0, all columns present, width >= 2
bad=0;checked=0
for c,d in depth.items():
    xs={x for x,y in c};w=max(xs)+1
    if xs!=set(range(w)):continue
    h=[0]*w;ok=True
    for x in range(w):
        ys=sorted(y for xx,y in c if xx==x)
        if ys!=list(range(len(ys))):ok=False;break
        h[x]=len(ys)
    if not ok or w<2:continue
    D=len(set(h));lb=1+math.ceil(math.log2(D)) if D>1 else 1   # 1 action for the row + raises
    checked+=1
    if d<lb:bad+=1;print('МЕНЬШЕ ГРАНИЦЫ',h,'действий',d,'граница',lb)
print('рельефов проверено',checked,'нарушений',bad)
