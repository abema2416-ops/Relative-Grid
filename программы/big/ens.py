from keylock import *
from pipe import sparse_make, method_v1
def ensemble(H,k_lb=None):
    """all the author's methods together; the smallest answer wins (every answer is a real construction)"""
    lb=math.ceil(math.log2(len(set(H))+1));r={}
    r['настоящее использование']=len(rule_struct(H))
    if r['настоящее использование']==lb:return lb,r
    r['ключ-замок']=len(keylock(H,8,10))
    if min(r.values())==lb:return lb,r
    b,_=method_v1(H);r['прежние правила (порядок, простые, комбинации, частота, моды, большая мода, золотая середина)']=b
    if min(r.values())==lb:return lb,r
    r['ключ-замок, широкое сравнение']=len(keylock(H,80,30))
    return min(r.values()),r
if __name__=="__main__":
    F=json.load(open('last3.json'))
    for f in F:print('тварина',f['M'],'ответ',f['k'],'все вместе:',ensemble(f['H'])[0],flush=True)
    d=json.load(open('boss.json'));print('босс: все вместе',ensemble(d['H'])[0],flush=True)
    rng=random.Random(2027);t=time.time();n=ok=0;bad=[]
    while time.time()-t<700:
        k=rng.choice([5,6,7]);H,M=sparse_make(k,rng);b,_=ensemble(H);n+=1;ok+=b==k
        if b!=k:bad.append((sorted(M),len(H),k,b));print('ТВАРИНА',sorted(M),len(H),k,b,flush=True)
    print('НОВЫЕ ЗАДАЧИ:',n,'точно',ok,flush=True)
