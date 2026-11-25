import time, random, itertools, sys
sys.setrecursionlimit(10000)
exec(open('h.py').read().split("random.seed(1)")[0])
def sponge(n):
    # «губка»: случайные тоннели и пузыри в кубе n×n×n
    O={c for c in itertools.product(range(n),repeat=3)}
    rnd=random.Random(n)
    for _ in range(n//2):  # сквозные тоннели
        ax=rnd.randrange(3); a,b=rnd.randrange(1,n-1),rnd.randrange(1,n-1)
        for t in range(n):
            c=[0,0,0]; o=[i for i in range(3) if i!=ax]; c[ax]=t;c[o[0]]=a;c[o[1]]=b; O.discard(tuple(c))
    for _ in range(n//3):  # пузыри
        c=tuple(rnd.randrange(2,n-2) for _ in range(3)); O.discard(c)
    return O
print("ребро | кубиков | наш способ: ответ, сек | классика (матрицы): ответ, сек")
for n in (6,10,14,18,22):
    O=sponge(n)
    t=time.time(); f=formula(O,n); tf=time.time()-t
    if n<=18:
        t=time.time(); h=homology(O); th=time.time()-t; hs=f"{h}, {th:.2f}"
    else: hs="не дождались (слишком долго)"
    print(n,"|",len(O),"|",f,f"{tf:.2f}","|",hs, flush=True)
