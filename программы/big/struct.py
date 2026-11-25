from half import *
d=json.load(open('boss.json'));H=d['H'];S=set(H);N=len(H)
C=counts(H)
U={x:sum(1 for h in H if h%x==0 and (h//x in S)) for x in C if C[x]>=2}
top=sorted(U,key=lambda x:-U[x])[:20]
print('тайные:',{m:U.get(m,0) for m in d['M']})
print('лучшие по «настоящему использованию»:',[(x,U[x],'ТАЙНЫЙ' if x in d['M'] else '') for x in top])
