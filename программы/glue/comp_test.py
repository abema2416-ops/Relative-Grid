exec(open('glue.py').read().split("random.seed(7)")[0])
def compress(cells, glue, Z, axis, s, f):
    G = [c for c in cells if c in Z]
    if not G: return None
    a = min(s*c[axis] for c in G); img = {}
    for c in G:
        t = s*c[axis] - a; p = list(c); p[axis] = s*(a + t//f); img[c] = tuple(p)
    rest = cells - set(G); new = set(img.values())
    if new & rest: return None
    merged = len(G) - len(new)
    def adj(p, q): return abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1
    ng = set()
    for (p, q) in glue:
        P, Q = img.get(p, p), img.get(q, q)
        if P == Q: continue
        if not adj(P, Q): return None
        ng.add(norm(P, Q))
    return rest | new, ng, merged
random.seed(3); W = 8; tested = bad = 0
for trial in range(4000):
    cells = {(4, 4)}; glue = set()
    for step in range(16):
        r = random.random()
        if r < 0.55:
            pool = list(cells); Z = set(random.sample(pool, random.randint(1, min(4, len(pool)))))
            q = stretch(cells, glue, Z, random.randrange(2), random.choice([1, -1]), random.choice([2, 3]))
            if q and all(0 <= x < W and 0 <= y < W for x, y in q[0]): cells, glue = q
        elif r < 0.8:
            cand = [norm(p, q) for p in cells for q in cells if p < q and abs(p[0]-q[0]) + abs(p[1]-q[1]) == 1 and norm(p, q) not in glue]
            if cand: glue = glue | {random.choice(cand)}
        else:
            pool = list(cells); Z = set(random.sample(pool, random.randint(1, min(5, len(pool)))))
            q = compress(cells, glue, Z, random.randrange(2), random.choice([1, -1]), random.choice([2, 3]))
            if q and q[2] == 0:
                h0 = holes_true(cells, glue); cells, glue = q[0], q[1]; tested += 1
                if holes_true(cells, glue) != h0: bad += 1
print('сжатий без слияния:', tested, 'из них изменили число дыр:', bad)
