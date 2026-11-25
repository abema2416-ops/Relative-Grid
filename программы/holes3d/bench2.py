import time,sys
exec(open('bench.py').read().split('print("ребро')[0])
n=int(sys.argv[1]); O=sponge(n)
t=time.time(); f=formula(O,n); tf=time.time()-t
print("наш",n,len(O),f,round(tf,2),flush=True)
if sys.argv[2]=='1':
    t=time.time(); h=homology(O); print("классика",n,h,round(time.time()-t,2),flush=True)
