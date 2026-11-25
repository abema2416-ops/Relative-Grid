from lib import *
exec(open('rule6.py').read().split('random.seed')[0].replace('from lib import *',''))
src=open('rule7.py').read();i=src.index('def rule7');exec(src[i:src.index('random.seed',i)])
src=open('rule8.py').read();i=src.index('def common_divs');exec(src[i:src.index('random.seed',i)])
def allbest(H):return min(rule3(H),primes_rule(H),rule7(H),greedy(H))
for seed,N,hi in [(1,1000,40),(7,2000,40)]:
    random.seed(seed);ex=un=0;bad=[]
    for _ in range(N):
        H=set(random.sample(range(2,hi+1),random.randint(2,6)))
        a=rmin(H);b=allbest(H);ex+=(a==b);un+=(b<a)
        if a!=b:bad.append((sorted(H),a,b))
    print(f'seed {seed}: all rules together exact {ex} of {N}, under {un}');print(bad[:5])
