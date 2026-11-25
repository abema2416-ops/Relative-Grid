from lib import *
def pf(n):
    r={};p=2
    while p*p<=n:
        while n%p==0:r[p]=r.get(p,0)+1;n//=p
        p+=1
    if n>1:r[n]=r.get(n,0)+1
    return r
def primes_rule(H):  # all heights from common prime factors, each prime as many times as its largest power
    mx={}
    for h in set(H):
        if h>1:
            for p,e in pf(h).items():mx[p]=max(mx.get(p,0),e)
    return sum(mx.values())
random.seed(1);N=1000;e=b2=un=0;ex=[]
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a=rmin(H);x=rule3(H);y=primes_rule(H);m=min(x,y)
    e+=(m==a);un+=(m<a)
    if m!=a:ex.append((sorted(H),a,x,y))
print('min(separately, primes) exact',e,'of',N,'under',un);print(ex[:6])
