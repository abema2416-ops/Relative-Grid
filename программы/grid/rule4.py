exec(open('rmin.py').read().split('tests=')[0]); import random
exec(open('rule3.py').read().split('random.seed')[0].split('import random',1)[1])
def rule4(H):  # common-factor peeling: take the divisor shared by most heights (ties: the largest), divide them
    V=[h for h in set(H) if h>1];M=[]
    while any(v>1 for v in V):
        best=None
        for d in range(2,max(V)+1):
            cnt=sum(1 for v in V if v%d==0)
            if cnt and (best is None or (cnt,d)>best):best=(cnt,d)
        d=best[1];M.append(d);V=[v//d if v%d==0 else v for v in V]
    return len(M)
random.seed(1);N=1000;r3=r4=both=0;under=0;ex=[]
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a=rmin(H);b=rule3(H);c=rule4(H)
    r3+=(b==a);r4+=(c==a);both+=(min(b,c)==a);under+=(c<a)
    if c!=a:ex.append((sorted(H),a,b,c))
print('rule3 exact',r3,'rule4 exact',r4,'best of both',both,'rule4 under',under)
print(ex[:8])
for H in [{6,10,15,30},{12,18},{2,3,6,12},{2,4},{2,3,4}]:print(sorted(H),rmin(H),rule3(H),rule4(H))
