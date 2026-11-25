from lib import *
src=open('rule8.py').read();i=src.index('def common_divs');exec(src[i:src.index('def greedy',i)])
random.seed(7);N=2000;ok=0
for _ in range(N):
    H=set(random.sample(range(2,41),random.randint(2,6)));ok+=(rmin(H)==rmin_restricted(H))
print('G-D exact',ok,'of',N)
