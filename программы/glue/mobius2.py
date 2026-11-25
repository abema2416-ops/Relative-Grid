# Поиск ленты Мёбиуса из единичных квадратов сетки Z^3: цикл квадратов, соседние в цикле склеены по общей стороне.
import itertools, sys
def sq_verts(b, ax):  # квадрат: угол b, оси ax=(u,w); вершины по кругу
    u, w = ax; e = lambda i: tuple(1 if k == i else 0 for k in range(3))
    add = lambda p, q: tuple(x+y for x, y in zip(p, q))
    return [b, add(b, e(u)), add(add(b, e(u)), e(w)), add(b, e(w))]
def edges(v): return [frozenset((v[i], v[(i+1) % 4])) for i in range(4)]
def squares_with_edge(E):
    p, q = sorted(E); d = [q[i]-p[i] for i in range(3)].index(1); res = []
    for o in range(3):
        if o == d: continue
        for sgn in (0, -1):
            b = list(p); b[o] += sgn; ax = tuple(sorted((d, o))); res.append((tuple(b), ax))
    return res
def analyse(cyc):
    n = len(cyc); V = {s: sq_verts(*s) for s in cyc}
    glue = [(cyc[i], cyc[(i+1) % n]) for i in range(n)]
    gE = {}
    for a, b in glue:
        E = set(edges(V[a])) & set(edges(V[b])); 
        if len(E) != 1: return None
        gE[(a, b)] = E.pop()
    # каждая сторона склеена не более одного раза
    if len(set(gE.values())) != n: return None
    allE = {}
    for s in cyc:
        for E in edges(V[s]): allE[E] = allE.get(E, 0) + 1
    if any(c > 1 and E not in set(gE.values()) for E, c in allE.items()): return None
    if any(c > 2 for c in allE.values()): return None
    # вершины комплекса: по точкам решётки, компоненты квадратов, связанных склеенными сторонами через точку
    pts = {}
    for s in cyc:
        for p in V[s]: pts.setdefault(p, []).append(s)
    Vn = 0
    for p, ss in pts.items():
        par = {s: s for s in ss}
        def f(x):
            while par[x] != x: x = par[x]
            return x
        deg = {s: 0 for s in ss}; ecount = 0
        for (a, b), E in gE.items():
            if p in E: par[f(a)] = f(b); deg[a] += 1; deg[b] += 1; ecount += 1
        comps = {f(s) for s in ss}; Vn += len(comps)
        if len(comps) != 1: return None   # вложение: в каждой точке один кусок
        # поверхность: каждая компонента — путь или цикл (степени <= 2) — у цикла по одной точке это ок
        if any(v > 2 for v in deg.values()): return None
    F = n; Ecnt = 4*n - n; chi = Vn - Ecnt + F
    # ориентируемость: переносим ориентацию по циклу
    orient = {cyc[0]: V[cyc[0]]}
    def dir_edges(vs): return {(vs[i], vs[(i+1) % 4]) for i in range(4)}
    for i in range(n):
        a, b = cyc[i], cyc[(i+1) % n]; E = tuple(gE[(a, b)])
        da = dir_edges(orient[a]); 
        x, y = E if (E[0], E[1]) in da else (E[1], E[0])
        vb = V[b]; ob = vb if (y, x) in dir_edges(vb) else vb[::-1]
        if i == n-1:
            return chi, (ob == orient[b] or set(dir_edges(ob)) == set(dir_edges(orient[b])))
        orient[b] = ob
best = None
start = ((0, 0, 0), (0, 1))
L = int(sys.argv[1])
def dfs(path, used):
    global best
    if best: return
    cur = path[-1]; 
    for E in edges(sq_verts(*cur)):
        for nb in squares_with_edge(E):
            if nb == cur: continue
            if len(path) >= 4 and nb == path[0] and len(path) == L:
                r = analyse(path)
                if r and r[0] == 0 and not r[1]: best = list(path); return
            if nb in used or len(path) >= L: continue
            if any(abs(c) > 2 for c in nb[0]): continue
            used.add(nb); path.append(nb); dfs(path, used); path.pop(); used.discard(nb)
dfs([start], {start})
print('длина', L, ':', best)
