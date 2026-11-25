from gold import *
import json
def rule_half(H,width=0.12):
    # author: "medium golden big mode" — the part used by about half of the heights (50/50), and among those the biggest
    C=counts(H);N=len(H)
    cand=[d for d in C if abs(C[d]/N-0.5)<=width]
    cand.sort(key=lambda d:(-d))            # biggest first among the "half" parts
    M=[]
    for d in cand:
        if any(d%m==0 or m%d==0 for m in M):continue   # a new independent part, not a multiple of a taken one
        M.append(d)
        if all(can_build(h,M) for h in H):break
    for h in sorted(H):
        if not can_build(h,M):M.append(h)
    return prune(M,H,lambda d:(abs(C.get(d,0)/N-0.5),-d))
if __name__=="__main__":
    d=json.load(open('boss.json'));H=d['H'];t=time.time()
    for w in (0.08,0.12,0.18):
        S=rule_half(H,w);print('ширина',w,'ответ',len(S),sorted(S),round(time.time()-t),'с',flush=True)
    print('тайные',d['M'])
    C=counts(H);print('частоты тайных, %:',{m:round(100*C[m]/len(H)) for m in d['M']})
