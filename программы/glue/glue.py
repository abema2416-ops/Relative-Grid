# Плоская сетка со склейками. Объект: клетки + склеенные стыки (пары соседей по стороне).
# Число дыр считаем независимо, по настоящему клеточному комплексу: квадраты, у которых
# склеенные стороны отождествлены. b1 = компоненты - χ  (b2 = 0 для поверхности с краем).
import random, itertools
def norm(p, q): return (p, q) if p < q else (q, p)
def holes_true(cells, glue):
    # строим комплекс: у каждой клетки 4 угла и 4 стороны; склейка отождествляет общую сторону и её два угла
    par = {}
    def f(x):
        while par.setdefault(x, x) != x: par[x] = par[par[x]]; x = par[x]
        return x
    def u(a, b): par[f(a)] = f(b)
    def corner(c, dx, dy): return ('v', c, dx, dy)
    def side(c, k): return ('e', c, k)
    for c in cells:
        for dx in (0, 1):
            for dy in (0, 1): f(corner(c, dx, dy))
        for k in range(4): f(side(c, k))
    for (a, b) in glue:
        (ax, ay), (bx, by) = a, b
        if bx == ax + 1:   # b справа от a: правая сторона a (k=1) = левая сторона b (k=3)
            u(side(a, 1), side(b, 3)); u(corner(a, 1, 0), corner(b, 0, 0)); u(corner(a, 1, 1), corner(b, 0, 1))
        else:              # b выше a: верхняя сторона a (k=2) = нижняя b (k=0)
            u(side(a, 2), side(b, 0)); u(corner(a, 0, 1), corner(b, 0, 0)); u(corner(a, 1, 1), corner(b, 1, 0))
    V = len({f(x) for x in par if x[0] == 'v'}); E = len({f(x) for x in par if x[0] == 'e'}); F = len(cells)
    # компоненты связности комплекса = компоненты клеток по склейкам
    p2 = {c: c for c in cells}
    def g(x):
        while p2[x] != x: p2[x] = p2[p2[x]]; x = p2[x]
        return x
    for a, b in glue: p2[g(a)] = g(b)
    comps = len({g(c) for c in cells})
    return comps - (V - E + F)
def holes_formula(cells, glue):
    Q = 0
    for (x, y) in cells:
        q = [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
        if all(c in cells for c in q):
            need = [norm(q[0], q[1]), norm(q[0], q[2]), norm(q[1], q[3]), norm(q[2], q[3])]
            if all(e in glue for e in need): Q += 1
    p2 = {c: c for c in cells}
    def g(x):
        while p2[x] != x: p2[x] = p2[p2[x]]; x = p2[x]
        return x
    for a, b in glue: p2[g(a)] = g(b)
    comps = len({g(c) for c in cells})
    return comps - len(cells) + len(glue) - Q
def stretch(cells, glue, Z, axis, s, f):
    """Растяжение по правилам 1.7 + склейки: образ клетки — f клеток подряд, склеенных между собой;
    склейка c–c' переходит в склейки между соседними образами. Если склейка рвётся — действие недопустимо."""
    G = [c for c in cells if c in Z]
    if not G: return None
    a = min(s*c[axis] for c in G)
    def img(c):
        t = s*c[axis] - a; out = []
        for j in range(f):
            p = list(c); p[axis] = s*(a + f*t + j); out.append(tuple(p))
        return out
    Gs = set(G); rest = cells - Gs
    newc = {c: img(c) for c in G}
    allnew = set(x for v in newc.values() for x in v)
    if allnew & rest: return None
    ng = set()
    for c in G:
        for k in range(f - 1): ng.add(norm(newc[c][k], newc[c][k+1]))
    def adj(p, q): return abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1
    for (p, q) in glue:
        P = newc.get(p, [p]); Qd = newc.get(q, [q])
        pairs = [norm(x, y) for x in P for y in Qd if adj(x, y)]
        if not pairs: return None          # склейка порвалась
        ng.update(pairs)
    return (rest | allnew), ng
random.seed(7); W = 7; bad_formula = bad_stretch = bad_glue = 0; n_st = n_gl = 0
for trial in range(3000):
    cells = {(3, 3)}; glue = set()
    for step in range(14):
        if random.random() < 0.65:
            pool = list(cells); k = random.randint(1, min(4, len(pool)))
            Z = set(random.sample(pool, k)); r = stretch(cells, glue, Z, random.randrange(2), random.choice([1, -1]), random.choice([2, 2, 3]))
            if r is None or any(not (0 <= x < W and 0 <= y < W) for x, y in r[0]): continue
            h0 = holes_true(cells, glue); cells, glue = r; h1 = holes_true(cells, glue); n_st += 1
            if h1 != h0: bad_stretch += 1
        else:
            cand = [norm(p, q) for p in cells for q in cells if p < q and abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1 and norm(p, q) not in glue]
            if not cand: continue
            e = random.choice(cand); h0 = holes_true(cells, glue); glue = glue | {e}; h1 = holes_true(cells, glue); n_gl += 1
            if not (h1 - h0 in (0, 1)): bad_glue += 1
        if holes_true(cells, glue) != holes_formula(cells, glue): bad_formula += 1
print('растяжений:', n_st, 'из них изменили число дыр:', bad_stretch)
print('склеек:', n_gl, 'из них изменили число дыр не на 0 и не на +1:', bad_glue)
print('расхождений формулы b1 = компоненты − клетки + склейки − Q с честным подсчётом:', bad_formula)
# пример: кольцо 3x3
ring = {(x, y) for x in range(3) for y in range(3)} - {(1, 1)}
tree = {norm((0,0),(1,0)), norm((1,0),(2,0)), norm((2,0),(2,1)), norm((2,1),(2,2)), norm((2,2),(1,2)), norm((1,2),(0,2)), norm((0,2),(0,1))}
print('кольцо без последней склейки: дыр', holes_true(ring, tree), '; с ней:', holes_true(ring, tree | {norm((0,1),(0,0))}))
