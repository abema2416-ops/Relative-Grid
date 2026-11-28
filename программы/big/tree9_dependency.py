from fractions import Fraction
import itertools, subprocess, math
P=[2,3,5,7,11,13,17,19,23,29,31,37]
H=[110,299,1218,4030,4070,17670,48433,787930,6697405,10068366,10818885,49560797]
A=[[Fraction(1 if h%p==0 else 0) for p in P] for h in H]
# зависимость между строками: c·A = 0  (ищем ядро транспонированной таблицы)
n=len(H); M=[[A[i][j] for i in range(n)] for j in range(len(P))]  # столбцы = высоты
rows=[r[:] for r in M]; piv=[]; r=0
for c in range(n):
    p=next((i for i in range(r,len(rows)) if rows[i][c]!=0),None)
    if p is None: continue
    rows[r],rows[p]=rows[p],rows[r]; rows[r]=[x/rows[r][c] for x in rows[r]]
    for i in range(len(rows)):
        if i!=r and rows[i][c]!=0:
            k=rows[i][c]; rows[i]=[x-k*y for x,y in zip(rows[i],rows[r])]
    piv.append(c); r+=1
free=[c for c in range(n) if c not in piv]
print("свободных столбцов (зависимостей):",len(free))
f=free[0]; v=[Fraction(0)]*n; v[f]=Fraction(1)
for i,c in enumerate(piv): v[c]=-rows[i][f]
supp=[i for i in range(n) if v[i]!=0]
print("зависимость:", " + ".join(f"({v[i]})·{H[i]}" for i in supp), "= 0 (в показателях)")
print("в зависимости участвует высот:",len(supp))
# проверка: может ли группа высот из зависимости собраться меньшим числом множителей
T=[H[i] for i in supp]; ps=sorted({p for h in T for p in P if h%p==0})
m=[sum(1<<ps.index(p) for p in P if h%p==0) for h in T]
out=subprocess.run(['./core_exact_bin','600',str(len(T)-1),str(len(T)-1)],input=f"{len(T)} {len(ps)}\n"+" ".join(map(str,m)),capture_output=True,text=True).stdout
print("группа:",T); print("решатель для группы (нужно", len(T)-1, "множителей):", out.strip())
