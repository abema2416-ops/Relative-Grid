exec(open('chk.py').read().split('rng=random.Random(1)')[0])
def full_squares(O,S):
    out=[]
    for (x,y) in O:
        sq=[(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
        if all(c in O for c in sq):
            st=[frozenset((sq[0],sq[1])),frozenset((sq[0],sq[2])),frozenset((sq[1],sq[3])),frozenset((sq[2],sq[3]))]
            if all(e in S for e in st):out.append(sq)
    return out
rng=random.Random(5);adm=0;withmixed=0
for trial in range(6000):
    O={(0,0)};S=set()
    for step in range(rng.randint(2,7)):
        cl=list(O);G=set(rng.sample(cl,rng.randint(1,len(cl))))
        k=rng.random()
        if k<.5:r=act(O,S,G,(rng.randint(0,1),),(rng.choice((1,-1)),),rng.randint(2,3))
        elif k<.85:
            mixedsq=[sq for sq in full_squares(O,S) if 0<sum(c in G for c in sq)<4]
            r=act(O,S,G,(0,1),(rng.choice((1,-1)),rng.choice((1,-1))),rng.randint(2,3))
            if r:
                adm+=1
                if mixedsq:withmixed+=1
        else:
            cont=[frozenset((p,q)) for p in O for q in O if p<q and adj(p,q) and frozenset((p,q)) not in S]
            S=S|set(rng.sample(cont,rng.randint(1,len(cont)))) if cont else S;r=None
        if r:O,S=r
print('admissible alpha*',adm,'with mixed full squares',withmixed)
