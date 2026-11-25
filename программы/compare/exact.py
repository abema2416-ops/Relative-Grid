import random
def comp(X,f):
    a=min(X); return frozenset(a+(c-a)//f for c in X)
rnd=random.Random(5); bad1=bad2=0; tests=0
for _ in range(3000):
    L=rnd.randint(2,13); f=rnd.randint(2,4)
    cells=frozenset(c for c in range(L) if rnd.random()<.5)
    if not cells: continue
    res=comp(cells,f); a=min(cells)
    # формула: блоки позиций зоны [0,L) относительно якоря a
    blocks={}
    for c in range(a,L): blocks.setdefault((c-a)//f,[]).append(c)
    nonempty={(c-a)//f for c in cells}
    form=1
    for b in nonempty:
        z=len(blocks[b]); form*= 2**(z-1) if b==0 else 2**z-1
    same_anchor=sum(1 for m in range(1,1<<L) if min(c for c in range(L) if m>>c&1)==a and comp(frozenset(c for c in range(L) if m>>c&1),f)==res)
    anyanchor=sum(1 for m in range(1,1<<L) if comp(frozenset(c for c in range(L) if m>>c&1),f)==res)
    tests+=1
    if form!=same_anchor: bad1+=1
    if form!=anyanchor: bad2+=1
print("тестов",tests,"формула≠(тот же якорь):",bad1,"формула≠(любой якорь):",bad2)
