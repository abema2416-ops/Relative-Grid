import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':12})
BG='#ffffff'; C1='#3b6fb6'; C2='#e0a23a'; C3='#5aa36a'; C4='#c8463c'; GH='#d9d9d9'
def ax3(fig,pos,title,el=22,az=-58):
    a=fig.add_subplot(pos,projection='3d');a.set_title(title);a.set_axis_off();a.view_init(el,az);a.set_box_aspect(None);return a
def vox(a,filled,col,alpha=1.0,ec='#333333'):
    a.voxels(filled,facecolors=col,edgecolor=ec,linewidth=.4,alpha=alpha)
def eq(a,n):
    a.set_xlim(0,n);a.set_ylim(0,n);a.set_zlim(0,n)
def save(fig,name):
    fig.savefig(name,dpi=130,bbox_inches='tight',facecolor=BG);plt.close(fig)

# 1 ---------- hedgehog
fig=plt.figure(figsize=(13,4.2))
fig.suptitle('Задача 1. Ёжик: 2n − 1 действий α',fontsize=14,y=1.02)
steps=[('Шаг 1: α по x',[(0,1,1),(1,1,1),(2,1,1)]),('Шаг 2: α вверх по y',[(1,2,1)]),('Шаг 3: α вниз по y',[(1,0,1)]),
       ('Шаг 4: α по +z',[(1,1,2)]),('Шаг 5: α по −z',[(1,1,0)])]
cols=[C1,C2,C3,C4,'#8a5bb5']
for i in range(5):
    a=ax3(fig,151+i,steps[i][0]);F=np.zeros((3,3,3),bool);FC=np.empty((3,3,3),object)
    for j in range(i+1):
        for c in steps[j][1]:F[c]=True;FC[c]=cols[j]
    vox(a,F,FC);eq(a,3)
save(fig,'p1.png')

# 2 ---------- holey cube (9^3 model of 101^3)
n=9;F=np.ones((n,n,n),bool)
for x in range(1,n-1,2):
    for y in range(1,n-1,2):F[x,y,:]=False
fig=plt.figure(figsize=(12,5.2))
fig.suptitle('Задача 2. Дыры через одну ячейку (модель 9 × 9 × 9: 16 дыр; у куба 101³ их 2500)',fontsize=13)
a=ax3(fig,121,'Вид сбоку: сквозные столбики',el=35,az=-50);vox(a,F,'#b9c9e3',ec='#4a5f80');eq(a,n)
b=fig.add_subplot(122);b.set_title('Вид сверху: каждый квадрат 2 × 2 держит ≤ 1 дыру')
top=np.ones((n,n));
for x in range(1,n-1,2):
    for y in range(1,n-1,2):top[y,x]=0
b.imshow(top,cmap=matplotlib.colors.ListedColormap(['#ffffff','#b9c9e3']),extent=(0,n,0,n),origin='lower')
for k in range(n+1):b.axhline(k,color='#4a5f80',lw=.5);b.axvline(k,color='#4a5f80',lw=.5)
for k in range(1,n-1,2):
    for m in range(1,n-1,2):b.add_patch(plt.Rectangle((k-.0,m-.0),2,2,fill=False,ec=C4,lw=1.6) if k<n-2 and m<n-2 else plt.Rectangle((k,m),1,1,fill=False,ec=C4,lw=1.6))
b.set_xticks([]);b.set_yticks([]);b.set_aspect('equal')
save(fig,'p2.png')

# 3 ---------- order matters
def box(sx,sy,sz,lost=None,N=6):
    F=np.zeros((N,4,4),bool);F[:sx,:sy,:sz]=True;FC=np.empty(F.shape,object);FC[F]='#b9c9e3'
    if lost:
        G=np.zeros_like(F);G[:lost[0],:lost[1],lost[2]:lost[3]]=True;FC[G]=C4
    return F,FC
fig=plt.figure(figsize=(13,7.6))
fig.suptitle('Задача 3. Сначала сжимай, потом растягивай',fontsize=14)
rows=[('Путь А (потеря 72 бита)',[(4,4,4,None,'Начало: 64'),(6,4,4,(6,4,1,4),'α по x: 96, красные исчезнут'),(6,4,1,None,'α по z: 24 (−72)')]),
      ('Путь Б (потеря 48 бит)',[(4,4,4,(4,4,1,4),'Начало: 64, красные исчезнут'),(4,4,1,None,'α по z: 16 (−48)'),(6,4,1,None,'α по x: 24 (+8)')])]
for r,(name,st) in enumerate(rows):
    for c,(sx,sy,sz,lost,t) in enumerate(st):
        a=ax3(fig,int(f'23{r*3+c+1}'),(name+'\n' if c==0 else '\n')+t);F,FC=box(sx,sy,sz,lost);vox(a,F,FC);a.set_xlim(0,6);a.set_ylim(0,6);a.set_zlim(0,6)
save(fig,'p3.png')

# 4 ---------- euler count
fig,a=plt.subplots(figsize=(6.6,6.6))
S=[(x,y) for x in range(7) for y in range(7) if not (x%2==1 and y%2==1)]
for x,y in S:a.add_patch(plt.Rectangle((x,y),1,1,fc='#b9c9e3',ec='#4a5f80',lw=.8))
for x in (1,3,5):
    for y in (1,3,5):a.add_patch(plt.Rectangle((x,y),1,1,fc='white',ec=C4,lw=2))
V=set();[V.update([(x,y),(x+1,y),(x,y+1),(x+1,y+1)]) for x,y in S]
a.scatter(*zip(*V),s=12,c='#1f2d44',zorder=3)
a.set_xlim(-.3,7.3);a.set_ylim(-1.6,7.3);a.set_aspect('equal');a.axis('off')
a.set_title('Задача 4. Дыры считаем без глаз',fontsize=14)
a.text(3.5,-.9,'Точек В = 64   Отрезков Р = 112   Ячеек Г = 40\nВ − Р + Г = −8   →   дыр = 1 − (−8) = 9',ha='center',fontsize=12)
save(fig,'p4.png')

# 5 ---------- 3^3 -> 1
fig=plt.figure(figsize=(13,4.4))
fig.suptitle('Задача 5. Сжали 27 ячеек в 1: потеряно 26 бит → 2²⁶ = 67 108 864 вариантов прошлого',fontsize=13,y=1.02)
seq=[((3,3,3),'Куб 3 × 3 × 3 (27)'),((1,3,3),'α по x: 9 (−18)'),((1,1,3),'α по y: 3 (−6)'),((1,1,1),'α по z: 1 (−2)')]
for i,(s,t) in enumerate(seq):
    a=ax3(fig,141+i,t);F=np.zeros((3,3,3),bool);F[:s[0],:s[1],:s[2]]=True;G=np.ones((3,3,3),bool)&~F
    FC=np.empty(F.shape,object);FC[F]='#b9c9e3';FC[G]='#eeeeee'
    a.voxels(F|G,facecolors=FC,edgecolor='#999999',linewidth=.3,alpha=.55);a.voxels(F,facecolors='#3b6fb6',edgecolor='#222',linewidth=.5);eq(a,3)
save(fig,'p5.png')

# 6 ---------- dimension tower
import itertools
def proj(v):  # project n-dim vertex to 2D
    n=len(v);ang=[np.pi*k/ max(n,1) +0.25 for k in range(n)];sc=[1/(1+0.18*k) for k in range(n)]
    return np.array([sum(v[k]*np.cos(ang[k])*sc[k] for k in range(n)),sum(v[k]*np.sin(ang[k])*sc[k] for k in range(n))])
fig,axs=plt.subplots(1,5,figsize=(15,3.8))
fig.suptitle('Задача 6. Каждое новое измерение: копия + β по каждой вершине (1, 2, 4, 8, … , 512 → всего 1023)',fontsize=13,y=1.03)
names=['0D → 1D\n1 склейка','1D → 2D\n2 склейки','2D → 3D\n4 склейки','3D → 4D\n8 склеек','4D → 5D\n16 склеек']
for d in range(1,6):
    a=axs[d-1];vs=list(itertools.product([0,1],repeat=d));P={v:proj(v) for v in vs}
    for v in vs:
        for k in range(d):
            if v[k]==0:
                w=list(v);w[k]=1;w=tuple(w);new=(k==d-1)
                a.plot(*zip(P[v],P[w]),color=C4 if new else '#4a5f80',lw=1.6 if new else 1,ls='--' if new else '-')
    a.scatter(*zip(*P.values()),s=14,c='#1f2d44',zorder=3);a.set_title(names[d-1]);a.set_aspect('equal');a.axis('off')
fig.text(.5,-.04,'Красный пунктир — новые склейки β. У 10-мерного куба: 1024 вершины, 5120 рёбер, 11 520 квадратов, 15 360 кубов.',ha='center',fontsize=11)
save(fig,'p6.png')

# 7 ---------- tube
def cyl(a,x0,r,L=1,col=C1,n=24):
    t=np.linspace(0,2*np.pi,n);x=np.array([x0,x0+L]);T,X=np.meshgrid(t,x)
    a.plot_surface(X,r*np.cos(T),r*np.sin(T),color=col,alpha=.85,linewidth=0,shade=True)
fig=plt.figure(figsize=(13,4.8))
fig.suptitle('Задача 7. Труба: диаметр звена k^(−3/4)',fontsize=14)
a=ax3(fig,121,'Первые 14 звеньев',el=18,az=-75)
for k in range(1,15):cyl(a,k-1,k**-0.75/2,col=plt.cm.Blues(0.35+0.6*k/14))
a.set_xlim(0,14);a.set_ylim(-3,3);a.set_zlim(-3,3);a.set_box_aspect((14,6,6))
b=fig.add_subplot(122);K=np.arange(1,3001)
b.plot(K,np.cumsum(np.pi/4*K**-1.5),color=C1,lw=2,label='объём (останавливается у ≈ 2,05)')
b.plot(K,np.cumsum(np.pi*K**-0.75),color=C4,lw=2,label='площадь (растёт без конца)')
b.axhline(2.0518,color=C1,ls=':',lw=1);b.set_xscale('log');b.set_yscale('log');b.set_xlabel('число звеньев');b.legend(frameon=False);b.spines[['top','right']].set_visible(False)
save(fig,'p7.png')

# 8 ---------- horn
fig=plt.figure(figsize=(12,5))
a=ax3(fig,111,'Задача 8. Рог из цилиндров радиуса 1/k: объём π³/6 ≈ 5,168, площадь бесконечна',el=20,az=-70)
for k in range(1,26):cyl(a,k-1,1/k,col=plt.cm.Oranges(0.85-0.5*k/25),n=36)
a.set_xlim(0,25);a.set_ylim(-1,1);a.set_zlim(-1,1);a.set_box_aspect((25,2.2,2.2))
save(fig,'p8.png')

# 9 ---------- staircase + voxel sphere
fig=plt.figure(figsize=(14,4.6))
fig.suptitle('Задача 9. Лесенка всегда длиной 2, хотя прилипает к диагонали √2 ≈ 1,414',fontsize=13,y=1.02)
for i,n in enumerate([2,4,16]):
    a=fig.add_subplot(1,4,i+1);xs=[0];ys=[0]
    for k in range(n):xs+=[(k+1)/n,(k+1)/n];ys+=[k/n,(k+1)/n]
    a.plot([0,1],[0,1],color='#999',ls='--');a.plot(xs,ys,color=C4,lw=2);a.set_aspect('equal');a.set_xticks([]);a.set_yticks([]);a.set_title(f'n = {n}: длина 2')
m=14;g=(np.indices((m,m,m))+.5-m/2);S=(g**2).sum(0)<(m/2)**2
a=fig.add_subplot(144,projection='3d');a.voxels(S,facecolors='#b9c9e3',edgecolor='#4a5f80',linewidth=.2);a.set_axis_off();a.set_title('Шар по граням ячеек:\n6πr² вместо 4πr²')
save(fig,'p9.png')

# 10 ---------- flatten
fig=plt.figure(figsize=(13,4.8))
fig.suptitle('Задача 10. Сплющили кубик: биты → ∞, объём → 1',fontsize=14)
n=6;a=ax3(fig,131,'Куб на сетке 1/n (n = 6): 216 ячеек');F=np.ones((n,n,n),bool);FC=np.empty(F.shape,object);FC[:]='#b9c9e3';FC[:,:,1:]=C4;vox(a,F,FC,ec='#333');eq(a,n)
a=ax3(fig,132,'После α по z: 36 ячеек (−180 бит)');F=np.zeros((n,n,n),bool);F[:,:,0]=True;vox(a,F,'#3b6fb6');eq(a,n)
b=fig.add_subplot(133);N=np.arange(1,1001)
b.plot(N,N**3-N**2,color=C4,lw=2,label='потеря бит n³ − n²');b.set_yscale('log');b.set_xscale('log');b.set_xlabel('n (мелкость сетки)')
b2=b.twinx();b2.plot(N,1-1/N,color=C1,lw=2,label='потеря объёма 1 − 1/n');b2.set_ylim(0,1.1)
b.set_ylabel('бит',color=C4);b2.set_ylabel('объём',color=C1);b.set_title('n = 1000: 999 000 000 бит, объём 0,999')
save(fig,'p10.png')
print('ok')
