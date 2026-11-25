# Гладкие фигуры с наложенной сеткой: сетка — это плоскости x, y, z = const, которые режут фигуру.
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'figure.dpi': 160})
INK = '#35322d'; OUT = './'
BLUE, RED, GREEN, YEL, VIO = '#8dbdeb', '#f0a184', '#a6d8a0', '#f3d774', '#b9acef'
ELEV, AZIM = 26, -56

def view_vec(elev, azim):
    e, a = np.radians(elev), np.radians(azim); return np.array([np.cos(e)*np.cos(a), np.cos(e)*np.sin(a), np.sin(e)])

def surf(ax, P, h, base, cell=None, tint=None, tintcol=YEL, elev=ELEV, azim=AZIM, lw=1.0):
    """P = (X,Y,Z) сетка точек поверхности; cell = координаты, по которым режет сетка (по умолчанию сами X,Y,Z);
    tint = булев массив вершин, которые входят в отмеченную зону."""
    X, Y, Z = P; C = cell if cell is not None else P
    idx = [np.floor(c / h + 1e-9) for c in C]
    line = np.zeros((X.shape[0]-1, X.shape[1]-1), bool)
    for I in idx:
        a, b, c, d = I[:-1, :-1], I[1:, :-1], I[:-1, 1:], I[1:, 1:]
        line |= (a != b) | (a != c) | (a != d)
    du = [np.gradient(A, axis=0) for A in P]; dv = [np.gradient(A, axis=1) for A in P]
    n = np.cross(np.stack(du, -1), np.stack(dv, -1)); n /= (np.linalg.norm(n, axis=-1, keepdims=True) + 1e-12)
    v = view_vec(elev, azim); s = n @ v; n = n * np.sign(s)[..., None]
    L = view_vec(elev + 28, azim - 35); lam = np.clip(n @ L, 0, 1)
    shade = (0.50 + 0.50 * lam)[:-1, :-1]
    col = np.zeros(line.shape + (4,)); col[..., 3] = 1
    b = np.array(to_rgb(base)); col[..., :3] = b[None, None, :] * shade[..., None]
    if tint is not None:
        t = tint[:-1, :-1]; col[t, :3] = np.array(to_rgb(tintcol))[None, :] * shade[t][:, None]
    col[line, :3] = np.array(to_rgb(INK))
    ax.plot_surface(X, Y, Z, facecolors=col, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)
    ax.view_init(elev=elev, azim=azim); ax.set_axis_off()

def frame(ax, r, zr=None, xr=None, zoom=1.32):
    xr = xr or r; zr = zr or r; ax.set_xlim(-xr, xr); ax.set_ylim(-r, r); ax.set_zlim(-zr, zr); ax.set_box_aspect((xr / r, 1, zr / r), zoom=zoom)

N = 260
def sphere(R=1.0):
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, N), np.linspace(0, np.pi, N), indexing='ij')
    return R*np.cos(u)*np.sin(v), R*np.sin(u)*np.sin(v), R*np.cos(v)
def torus(R=0.68, r=0.30, kz=1.0):
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, N), np.linspace(0, 2*np.pi, N), indexing='ij')
    return (R + r*np.cos(v))*np.cos(u), (R + r*np.cos(v))*np.sin(u), kz*r*np.sin(v)
def capsule(R=0.42, Lh=0.55):
    u, t = np.meshgrid(np.linspace(0, 2*np.pi, N), np.linspace(0, 1, N), indexing='ij')
    ang = np.where(t < 0.3, t/0.3*np.pi/2, np.where(t > 0.7, np.pi/2 + (t-0.7)/0.3*np.pi/2, np.pi/2))
    ax_ = np.where(t < 0.3, Lh, np.where(t > 0.7, -Lh, Lh - (t-0.3)/0.4*2*Lh)) + R*np.cos(ang)
    rad = R*np.sin(ang); return ax_, rad*np.cos(u), rad*np.sin(u)
def cube_faces(a=0.8):
    s = np.linspace(-a, a, 140); A, B = np.meshgrid(s, s, indexing='ij'); o = np.full_like(A, a)
    return [(A, B, o), (o, A, B), (A, -o, B)]            # три грани, обращённые к зрителю
def ball_with_hole(R=1.0, kz=0.5, a=0.34):
    # тело вращения: стенка тоннеля (цилиндр радиуса a) + наружная часть сплющенного шара
    zc = kz*np.sqrt(R*R - a*a); t = np.linspace(0, 1, N); rho = np.empty(N); z = np.empty(N)
    m = t < 0.22; rho[m] = a; z[m] = -zc + (t[m]/0.22)*2*zc
    th0 = np.arcsin(a/R); th = th0 + (t[~m]-0.22)/0.78*(np.pi - 2*th0); rho[~m] = R*np.sin(th); z[~m] = kz*R*np.cos(th)
    u = np.linspace(0, 2*np.pi, N); U, RHO = np.meshgrid(u, rho, indexing='ij'); _, ZZ = np.meshgrid(u, z, indexing='ij')
    return RHO*np.cos(U), RHO*np.sin(U), ZZ

# Рис. 1. Шар и сетка трёх уровней
fig = plt.figure(figsize=(10, 3.9))
for i, n in enumerate([4, 8, 16]):
    ax = fig.add_subplot(1, 3, i+1, projection='3d'); surf(ax, sphere(), 2.0/n, BLUE); frame(ax, 0.82)
    ax.set_title(f'уровень n = {n}', fontsize=11, color=INK, pad=-4)
fig.suptitle('Рис. 1. Шар остаётся круглым; сетка только режет его на части. Чем выше уровень, тем мельче части', color=INK, y=0.98, fontsize=10.5)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 1 — шар и сетка.png', bbox_inches='tight'); plt.close(fig)

# Рис. 2. Разные фигуры
fig = plt.figure(figsize=(10, 7.4)); h = 0.2
ax = fig.add_subplot(2, 2, 1, projection='3d')
for F in cube_faces(): surf(ax, F, h, YEL)
frame(ax, 0.95); ax.set_title('куб', color=INK, pad=-4)
ax = fig.add_subplot(2, 2, 2, projection='3d'); surf(ax, sphere(), h, BLUE); frame(ax, 0.85); ax.set_title('шар', color=INK, pad=-4)
ax = fig.add_subplot(2, 2, 3, projection='3d'); surf(ax, torus(), h, RED, elev=48); frame(ax, 0.85, 0.5); ax.set_title('тор', color=INK, pad=-4)
ax = fig.add_subplot(2, 2, 4, projection='3d'); surf(ax, capsule(), h, GREEN); frame(ax, 0.85); ax.set_title('капсула («колбаска»)', color=INK, pad=-4)
fig.suptitle('Рис. 2. Сетку можно наложить на любую фигуру', color=INK, y=0.97)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 2 — разные фигуры.png', bbox_inches='tight'); plt.close(fig)

# Рис. 3. Действие α на шаре
fig = plt.figure(figsize=(11, 3.9)); h = 0.25
X, Y, Z = sphere(0.75); zone = X > 0
ax = fig.add_subplot(1, 3, 1, projection='3d'); surf(ax, (X, Y, Z), h, BLUE, tint=zone); frame(ax, 0.8, xr=1.2, zoom=1.5)
ax.set_title('до: отмечена зона (жёлтая)', fontsize=10.5, color=INK, pad=-4)
X2 = np.where(zone, 2*X, X)
ax = fig.add_subplot(1, 3, 2, projection='3d'); surf(ax, (X2 - 0.35, Y, Z), h, BLUE, cell=(X2, Y, Z), tint=zone); frame(ax, 0.8, xr=1.2, zoom=1.5)
ax.set_title('α: зона растянута вдвое вправо,\nсетка наложена заново — частей стало больше', fontsize=10.5, color=INK, pad=-4)
ax = fig.add_subplot(1, 3, 3, projection='3d'); surf(ax, (X2 - 0.35, Y, Z), h, BLUE, cell=(X, Y, Z), tint=zone); frame(ax, 0.8, xr=1.2, zoom=1.5)
ax.set_title('то же, но сетку не накладывали заново:\nчасти в зоне вытянулись', fontsize=10.5, color=INK, pad=-4)
fig.suptitle('Рис. 3. Действие α: зона, одно направление, закреплённая сторона (плоскость, где зона начинается)', color=INK, y=1.0, fontsize=10.5)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 3 — действие альфа.png', bbox_inches='tight'); plt.close(fig)

# Рис. 9. Шар -> сплющили -> пробили дыру -> тор
fig = plt.figure(figsize=(11, 3.7)); h = 0.25; E = 44
X, Y, Z = sphere(1.0)
ax = fig.add_subplot(1, 3, 1, projection='3d'); surf(ax, (X, Y, Z), h, BLUE, elev=E); frame(ax, 1.0); ax.set_title('шар', color=INK, pad=-4)
ax = fig.add_subplot(1, 3, 2, projection='3d'); surf(ax, (X, Y, Z*0.5), h, BLUE, elev=E); frame(ax, 1.0); ax.set_title('α: сжали вдвое по высоте\nгладкость осталась', fontsize=10.5, color=INK, pad=-4)
ax = fig.add_subplot(1, 3, 3, projection='3d'); surf(ax, ball_with_hole(), h, BLUE, elev=E); frame(ax, 1.0); ax.set_title('σ: убрали середину насквозь\nполучился тор', fontsize=10.5, color=INK, pad=-4)
fig.suptitle('Рис. 9. Пример автора: шар сплющивают и пробивают — выходит тор', color=INK, y=1.0)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 9 — из шара в тор.png', bbox_inches='tight'); plt.close(fig)
print('ok')
