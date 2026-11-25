import math, itertools
# объём шара радиуса 1: наша сетка уровня N (θ = 1/2, доля по 8³ точкам) против формулы 4/3·π
exact=4/3*math.pi
for N in (4,8,16,32):
    h=1/N; cnt=0; k=6
    for i,j,l in itertools.product(range(-N,N),repeat=3):
        inside=0
        for a,b,c in itertools.product(range(k),repeat=3):
            x=(i+(a+.5)/k)*h; y=(j+(b+.5)/k)*h; z=(l+(c+.5)/k)*h
            inside+= x*x+y*y+z*z<=1
        if inside*2>=k**3: cnt+=1
    v=cnt*h**3
    print(f"N={N}: клеток {cnt}, объём {v:.4f}, ошибка {abs(v-exact)/exact*100:.2f}%")
print("формула:",round(exact,6))
