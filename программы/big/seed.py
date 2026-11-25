from half import *
def cover(h,M):
    reach={1}
    for m in M:
        if h%m:continue
        reach|={r*m for r in reach if h%(r*m)==0}
    return max(reach)
def total_cover(H,M):return sum(math.log(cover(h,M)) for h in H)
def grow(H,seed,cand):
    # author: start from one number, add the part that "covers" the most of all heights, repeat
    M=[seed];cur=total_cover(H,M);goal=sum(math.log(h) for h in H)
    while cur<goal-1e-9:
        best=None
        for d in cand:
            v=total_cover(H,M+[d])
            if v>cur+1e-9 and (best is None or (v,d)>best[0]):best=((v,d),d)
        if not best:break
        M.append(best[1]);cur=best[0][0]
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:d)
if __name__=="__main__":
    d=json.load(open('boss.json'));H=d['H'];C=counts(H);N=len(H)
    band=[x for x in C if 0.65<=C[x]/N<=0.97]
    cand=sorted(band,key=lambda x:-(C[x]*math.log(x)))[:150]
    print('кандидатов',len(cand),'(в полосе 65–97 %:',len(band),')',flush=True)
    t=time.time();best=None
    for i,s in enumerate(cand[:25]):
        S=grow(H,s,cand)
        if best is None or len(S)<len(best):best=S
        print(f'зерно {s}: {len(S)} действий; лучший пока {len(best)}  [{round(time.time()-t)} c]',flush=True)
        if len(best)==9:break
    print('ИТОГ',len(best),sorted(best),'тайные',d['M'])
