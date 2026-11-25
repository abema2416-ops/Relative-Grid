import sys;sys.argv=['x','куб 2x2x2']
exec(open('b3.py').read().split("name=sys.argv[1]")[0])
def path(T,star,maxd=4):
    T=norm(frozenset(T),set())[0];N=len(T);B=[max(c[k] for c in T)+1 for k in range(3)]
    start=norm(frozenset({(0,0,0)}),set());par={start:None};fr=[start]
    for d in range(maxd+1):
        for st in fr:
            if st[0]==T:
                out=[];s=st
                while s:out.append(par[s][1] if par[s] else 'точка');s=par[s][0] if par[s] else None
                return list(reversed(out))
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
                            if key in par:continue
                            ax=''.join('xyz'[i] for i in axes)
                            par[key]=((c,g),f"зона {len(Z)} кл. → {'α*' if len(axes)>1 else 'α'} по {ax} ×{f}; стало {sorted(nc)}");nf.append(key)
        fr=nf
for n in ['ступени 2x2 высоты 1,2,2,3','Г 3D: 2x2x2 + выступ']:
    print(n);[print('  ',s) for s in path(S[n],False)]
