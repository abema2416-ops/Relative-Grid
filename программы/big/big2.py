import sys
src=open('swap.py').read().split("for seed,idx in")[0];exec(src)
def all_rules2(H):
    lb=math.ceil(math.log2(len(H)+1));r={}
    for name,f in [('по порядку',rule_small_first),('простые',rule_primes),('комбинации',lambda H:min(rule_combo(H),rule_combo(H,False)))]:
        r[name]=f(H)
        if min(r.values())==lb:return min(r.values()),r
    S=improve(H,solve_set(H));r['комбинации + проверка заменой']=len(S)
    if min(r.values())==lb:return min(r.values()),r
    r['частота']=rule_freq(H)
    if min(r.values())==lb:return min(r.values()),r
    r['моды']=min(rule_modes(H,k) for k in KEYS[:2])
    return min(r.values()),r
seed=int(sys.argv[1]);N=int(sys.argv[2]);rng=random.Random(seed);okc=0;t0=time.time()
for i in range(N):
    k=rng.choice([5,6,7]);H,M=make(k,rng)
    t=time.time();best,r=all_rules2(H);dt=time.time()-t;lb=math.ceil(math.log2(len(H)+1));okc+=best==k
    print(f"{i+1:3d}. высот {len(H):3d}, крупнейшая {max(H):.2e} ({len(str(max(H)))} цифр), ответ {k}; правила {best} {'✓' if best==k else '✗'} [{dt:.1f} c] {r}",flush=True)
print('ИТОГО',okc,'из',N,'за',round(time.time()-t0),'c',flush=True)
