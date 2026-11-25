from bigmode import *
rng=random.Random(6)
configs=[([2,3,5,7],3,3),([2,3,5,7,11],2,3),([2,3,5],4,3),([2,3,5,7,11,13],2,2)]
while True:
    pool,maxe,maxp=rng.choice(configs);k=rng.choice([5,6])
    H,M=make2(k,rng,pool,maxe,maxp)
    if sorted(M)==[4,18,1000,5000,25000]:break
if __name__=="__main__": print('высоты',H)
C=counts(H) if __name__=="__main__" else None
if __name__=="__main__":
  for n,s in SC.items():
      S=rule_bigmode(H,s);print(n,'до замены',sorted(S),'после',sorted(improve(H,S)))
if __name__=="__main__": print('частоты тайных:',{m:C.get(m,0) for m in [4,18,1000,5000,25000]})
if __name__=="__main__": top=sorted([d for d in C if C[d]>=2],reverse=True)[:12];print('самые крупные моды',[(d,C[d]) for d in top])
