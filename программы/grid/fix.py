exec(open('pics.py').read().split('# 1 ----------')[0])
# 2
n=9;F=np.ones((n,n,n),bool)
for x in range(1,n-1,2):
    for y in range(1,n-1,2):F[x,y,:]=False
fig=plt.figure(figsize=(12,5.2))
fig.suptitle('Задача 2. Дыры через одну ячейку (модель 9 × 9 × 9: 16 дыр; у куба 101³ их 2500)',fontsize=13)
a=ax3(fig,121,'Вид сбоку: сквозные столбики',el=35,az=-50);vox(a,F,'#b9c9e3',ec='#4a5f80');eq(a,n)
b=fig.add_subplot(122);b.set_title('Вид сверху: в каждом красном квадрате ≤ 1 дыры')
for x in range(n):
    for y in range(n):
        hole=(x%2==1 and y%2==1 and 0<x<n-1 and 0<y<n-1)
        b.add_patch(plt.Rectangle((x,y),1,1,fc='white' if hole else '#b9c9e3',ec='#4a5f80',lw=.5))
for x0 in range(1,n-1,2):
    for y0 in range(1,n-1,2):
        b.add_patch(plt.Rectangle((x0,y0),min(2,n-1-x0),min(2,n-1-y0),fill=False,ec=C4,lw=2))
b.set_xlim(0,n);b.set_ylim(0,n);b.set_xticks([]);b.set_yticks([]);b.set_aspect('equal')
save(fig,'p2.png')
# 7 side view
fig,(a,b)=plt.subplots(1,2,figsize=(13,4.6),gridspec_kw={'width_ratios':[1.3,1]})
fig.suptitle('Задача 7. Труба: диаметр звена k^(−3/4)',fontsize=14)
for k in range(1,21):
    d=k**-0.75;a.add_patch(plt.Rectangle((k-1,-d/2),1,d,fc=plt.cm.Blues(0.3+0.6*k/20),ec='#1f2d44',lw=.6))
a.set_xlim(-.3,20.3);a.set_ylim(-.7,.7);a.set_aspect('equal');a.set_title('Вид сбоку, первые 20 звеньев');a.set_yticks([]);a.set_xlabel('длина');a.spines[['top','right','left']].set_visible(False)
K=np.arange(1,3001)
b.plot(K,np.cumsum(np.pi/4*K**-1.5),color=C1,lw=2,label='объём (стоп у ≈ 2,05)')
b.plot(K,np.cumsum(np.pi*K**-0.75),color=C4,lw=2,label='площадь (растёт без конца)')
b.axhline(2.0518,color=C1,ls=':',lw=1);b.set_xscale('log');b.set_yscale('log');b.set_xlabel('число звеньев');b.legend(frameon=False);b.spines[['top','right']].set_visible(False)
save(fig,'p7.png')
# 8 horn
fig,a=plt.subplots(figsize=(13,4.6))
for k in range(1,31):
    r=1/k;a.add_patch(plt.Rectangle((k-1,-r),1,2*r,fc=plt.cm.Oranges(0.85-0.55*k/30),ec='#5a2e0e',lw=.6))
a.set_xlim(-.3,30.3);a.set_ylim(-1.15,1.15);a.set_aspect('equal');a.set_yticks([]);a.spines[['top','right','left']].set_visible(False);a.set_xlabel('длина')
a.set_title('Задача 8. Рог из цилиндров радиуса 1/k (вид сбоку)\nобъём π³/6 ≈ 5,168, площадь бесконечна',fontsize=13)
save(fig,'p8.png')
