exec(open('rmin.py').read().split('tests=')[0]); import random
def rule3(H):
    M=[]
    for h in sorted(set(x for x in H if x>1)):
        if h not in gen(M):M.append(h)
    return len(M)
random.seed(1);N=1000;ex=[];under=0
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)))
    a,b=rmin(H),rule3(H)
    if a!=b:ex.append((sorted(H),a,b))
    if b<a:under+=1
print('mismatch',len(ex),'of',N,'under',under);print(ex[:6])
for H in [{2,3,6,12},{6,10,15,30},{2,7,12,14,28}]:print(sorted(H),rmin(H),rule3(H))
