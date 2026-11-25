import sys
src=open('big.py').read().split('seed=int(sys.argv[1])')[0];exec(src)
seed,idx=int(sys.argv[1]),int(sys.argv[2]);rng=random.Random(seed)
for i in range(idx):
    k=rng.choice([5,6,7]);H,M=make(k,rng)
print('k',k,'тайные множители',sorted(M));print('высоты',H);print('правила',all_rules(H))
