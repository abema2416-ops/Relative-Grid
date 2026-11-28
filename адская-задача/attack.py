import sys, json, math, time
sys.path.append('/home/claude/relative-grid/программы/big')
import os
d=json.load(open('/tmp/hell/hell.json')); H=d['H']; secret=d['M_secret']
os.chdir('/home/claude/relative-grid/программы/big')
exec(open('rank_bound.py').read().split("# 1) старый")[0].replace("exec(open('superkent.py').read().split(\"H=json.load\")[0])",""))
from jumps import jumps
from giga2 import guided
from collections import Counter
t=time.time(); rk=rank(H); lg=math.ceil(math.log2(len(H)+1)); lb=max(rk,lg)
fs=[fac(h) for h in H]; ps={p for f in fs for p in f}
print(f"нижняя граница: ранг {rk}, логарифм {lg} → {lb};  верхняя: min(высот {len(H)}, полос {len(ps)}) = {min(len(H),len(ps))};  тайный ответ ≤ {len(secret)}  ({time.time()-t:.1f} с)",flush=True)
C=Counter(b//a for a in H for b in H if b>a and b%a==0)
print(f"скачков (одна высота делит другую): {sum(C.values())}",flush=True)
t=time.time(); r=jumps(H,lb,3,time.time()+60); print(f"кент скачков: {r[0] if r else 'не нашёл'} ({time.time()-t:.0f} с)",flush=True)
t=time.time()
try:
    g=guided(H,len(secret),time.time()+120,lb,C); print(f"суперкент по графику: {g[0] if g else 'нет'} ({time.time()-t:.0f} с)")
except TimeoutError: print(f"суперкент по графику: не успел за 120 с")
