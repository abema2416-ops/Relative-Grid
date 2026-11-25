exec(open('mode.py').read().split("H=[4,6,7,8,21,24]")[0])
import time
def everything(H):return min(min(mode_rule(H,f) for f in keys.values()),allbest(H),freq_rule(H))
random.seed(11);t=time.time();n=ok=0;bad=[]
while time.time()-t<1300:
    H=set(random.sample(range(2,61),random.randint(3,7)))
    a=rmin(H);b=everything(H);n+=1;ok+=a==b
    if a!=b:bad.append((sorted(H),b,a));print('BAD',sorted(H),b,a,flush=True)
    if b<a:print('UNDER!',H)
print('tested',n,'exact',ok,flush=True)
