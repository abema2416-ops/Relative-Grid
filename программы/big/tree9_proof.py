import itertools, subprocess, time
P=[2,3,5,7,11,13,17,19,23,29,31,37]
H=[110,299,1218,4030,4070,17670,48433,787930,6697405,10068366,10818885,49560797]
G=[110,1218,4030,4070,787930,6697405,10068366,10818885,49560797]
rest=[h for h in H if h not in G]
mask=lambda h: sum(1<<j for j,p in enumerate(P) if h%p==0)
allm=[mask(h) for h in H]; okall=True
for r in range(len(rest)+1):
    for extra in itertools.combinations(rest,r):
        T=G+list(extra); k=len(T)-1; t=time.time()
        inp=f"{len(T)} {len(P)}\n"+" ".join(str(mask(h)) for h in T)+f"\n{len(allm)} "+" ".join(map(str,allm))
        out=subprocess.run(['./core_shared','1500',str(k),str(k)],input=inp,capture_output=True,text=True).stdout.strip()
        print(f"группа из {len(T)} (+{list(extra)}): нужно ≤ {k} общих веток → {out} ({time.time()-t:.1f} с)",flush=True)
        if 'решения нет' not in out: okall=False
print("ДОКАЗАНО: R = 12" if okall else "не доказано")
