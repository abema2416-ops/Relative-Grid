# Можно ли без β₊, без σ и без сжатий со слиянием (но с β₋) дойти до целиком склеенной фигуры с дырой?
import sys, itertools
from collections import deque
W, H = int(sys.argv[1]), int(sys.argv[2]); CAP = int(sys.argv[3])
def norm(p, q): return (p, q) if p < q else (q, p)
def adj(p, q): return abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1
def inside(c): return 0 <= c[0] < W and 0 <= c[1] < H
def act(cells, glue, G, axis, s, f, kind):
    a = min(s*c[axis] for c in G); img = {}
    for c in G:
        t = s*c[axis] - a
        if kind == 'st':
            img[c] = []
            for j in range(f):
                p = list(c); p[axis] = s*(a + f*t + j); img[c].append(tuple(p))
        else:
            p = list(c); p[axis] = s*(a + t//f); img[c] = [tuple(p)]
    rest = cells - G; new = set(x for v in img.values() for x in v)
    if new & rest or not all(inside(x) for x in new): return None
    if kind == 'cm' and len(new) < len(G): return None      # слияние запрещено
    ng = set()
    for c, v in img.items():
        for x, y in zip(v, v[1:]): ng.add(norm(x, y))
    for (p, q) in glue:
        P, Q = img.get(p, [p]), img.get(q, [q]); ok = False
        for x in P:
            for y in Q:
                if adj(x, y): ng.add(norm(x, y)); ok = True
        if not ok: return None                              # П5: рвать склейки нельзя
    return frozenset(rest | new), frozenset(ng)
def d(cells, glue):
    par = {c: c for c in cells}
    def f(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for p, q in glue: par[f(p)] = f(q)
    comp = len({f(c) for c in cells})
    qq = 0
    for (x, y) in cells:
        sq = [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
        if all(c in cells for c in sq):
            if all(norm(sq[i], sq[j]) in glue for i, j in [(0,1),(0,2),(1,3),(2,3)]): qq += 1
    return comp - len(cells) + len(glue) - qq
def full(cells, glue):
    return all(norm(p, q) in glue for p in cells for q in cells if p < q and adj(p, q))
start = (frozenset({(0, 0)}), frozenset())
seen = {start}; Q = deque([start]); hits = []
while Q and len(seen) < CAP:
    cells, glue = Q.popleft(); cl = sorted(cells)
    succ = []
    for r in range(1, len(cl)+1):
        for G in itertools.combinations(cl, r):
            G = set(G)
            for axis in (0, 1):
                for s in (1, -1):
                    for f in (2, 3):
                        for kind in ('st', 'cm'):
                            v = act(cells, glue, G, axis, s, f, kind)
                            if v: succ.append(v)
    for g in glue: succ.append((cells, glue - {g}))       # β₋ по одной паре
    for v in succ:
        if v not in seen:
            seen.add(v); Q.append(v)
            if full(*v) and d(*v) >= 1: hits.append(v)
print('состояний:', len(seen), 'очередь пуста:', not Q, 'найдено целиком склеенных фигур с дырой:', len(hits))
for h in hits[:3]: print(sorted(h[0]))
