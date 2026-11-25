from bfs import *
def solve_path(rows,maxd=4):
    T=norm(parse(rows),set())[0];N=len(T);W=max(x for x,y in T)+1;H=max(y for x,y in T)+1
    start=norm(frozenset({(0,0)}),set());par={start:None};frontier=[start]
    def show(c):return ' '.join(''.join('#' if (x,y) in c else '.' for x in range(W)) for y in range(H))
    for d in range(maxd+1):
        for st in frontier:
            if st[0]==T:
                path=[];s=st
                while s:path.append(s);s=par[s][0] if par[s] else None
                for s in reversed(path):print(show(s[0]), '| трещин:',len(contacts(s[0])-set(s[1])))
                return
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
                                if len(nc)>N or max(x for x,y in nc)>=W or max(y for x,y in nc)>=H:continue
                                key=(nc,frozenset(ng))
                                if key in par:continue
                                par[key]=((c,g),);nf.append(key)
        frontier=nf
import sys
solve_path(["####","...#","##.#","####"]);print();solve_path(["#####","#.#.#","#####"])
