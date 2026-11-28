import sys, time, math
P=[2,3,5,7,11,13,17,19,23,29,31,37]
def table(H):
    ps=sorted({p for h in H for p in P if h%p==0})
    return ps,[[1 if h%p==0 else 0 for p in ps] for h in H]
def fooling(H,limit=120):
    ps,A=table(H); cells=[(i,j) for i in range(len(H)) for j in range(len(ps)) if A[i][j]]
    n=len(cells)
    # «дурачат» друг друга: в одном прямоугольнике быть не могут
    adj=[0]*n
    for a in range(n):
        for b in range(a+1,n):
            (i1,j1),(i2,j2)=cells[a],cells[b]
            if i1==i2 and j1==j2: continue
            if not A[i1][j2] or not A[i2][j1]:
                adj[a]|=1<<b; adj[b]|=1<<a
    best=[0]; t=time.time()
    def popc(x): return bin(x).count('1')
    def expand(R,P_):
        if time.time()-t>limit: raise TimeoutError
        if P_==0:
            best[0]=max(best[0],R); return
        if R+popc(P_)<=best[0]: return
        while P_:
            if R+popc(P_)<=best[0]: return
            v=P_.bit_length()-1; P_&=~(1<<v)
            expand(R+1,P_&adj[v])
    try: expand(0,(1<<n)-1); return best[0],True
    except TimeoutError: return best[0],False
if __name__=="__main__":
    tests={'задача 9 (ответ 11 или 12?)':[110,299,1218,4030,4070,17670,48433,787930,6697405,10068366,10818885,49560797],
           '9 высот (ответ 8)':[11,357,1463,2618,3705,4485,7293,8211,34034],
           '8 высот (ответ 7)':[130,143,357,2210,6783,8645,440895,881790]}
    for name,H in tests.items():
        t=time.time(); fb,done=fooling(H,float(sys.argv[1]))
        print(f"{name}: клеток-«обманщиков» {fb} ({'точно' if done else 'не меньше'}), за {time.time()-t:.1f} с",flush=True)
