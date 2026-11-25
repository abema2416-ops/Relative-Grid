# Формула Пика на наших клетках: площадь = I + B/2 + h − 1 (h — число дыр), для объектов без касаний «уголком».
import random, itertools
def check(O):
    pts={}
    for (x,y) in O:
        for dx,dy in ((0,0),(1,0),(0,1),(1,1)): pts[(x+dx,y+dy)]=pts.get((x+dx,y+dy),0)+1
    # точка внутри, если все 4 клетки вокруг заняты
    I=sum(1 for p,k in pts.items() if k==4); B=sum(1 for p,k in pts.items() if k<4)
    # «уголок»: в точке две клетки по диагонали без двух других
    pinch=any(((p[0]-1,p[1]-1) in O)==((p[0],p[1]) in O) and ((p[0]-1,p[1]) in O)==((p[0],p[1]-1) in O) and ((p[0]-1,p[1]-1) in O)!=((p[0]-1,p[1]) in O) for p in pts)
    # дыры: компоненты пустых клеток (по сторонам) внутри рамки, не касающиеся края
    xs=[c[0] for c in O]; ys=[c[1] for c in O]
    box=[(x,y) for x in range(min(xs)-1,max(xs)+2) for y in range(min(ys)-1,max(ys)+2)]
    empty={c for c in box if c not in O}; seen=set(); comps=0
    for s in empty:
        if s in seen: continue
        comps+=1; st=[s]; seen.add(s)
        while st:
            u=st.pop()
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                v=(u[0]+d[0],u[1]+d[1])
                if v in empty and v not in seen: seen.add(v); st.append(v)
    h=comps-1
    return pinch, len(O), I+B/2+h-1
def connected(O):
    s=next(iter(O)); seen={s}; st=[s]
    while st:
        u=st.pop()
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            v=(u[0]+d[0],u[1]+d[1])
            if v in O and v not in seen: seen.add(v); st.append(v)
    return len(seen)==len(O)
rnd=random.Random(2); ok=bad=skip=0
for _ in range(20000):
    n=rnd.randint(3,7); O={(x,y) for x in range(n) for y in range(n) if rnd.random()<.7}
    if not O or not connected(O): continue
    pinch,area,pick=check(O)
    if pinch: skip+=1; continue
    if area==pick: ok+=1
    else: bad+=1
print("совпало",ok,"не совпало",bad,"пропущено (касание уголком)",skip)
