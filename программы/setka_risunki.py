import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'figure.dpi': 160})
INK = '#35322d'; OUT = './'  # папка, куда сохранять рисунки
COL = {'blue': '#7fb3e6', 'red': '#ee9a7a', 'green': '#9fd39a', 'yellow': '#f2d36b', 'violet': '#b3a5ec', 'grey': '#cfcfca'}

def vox(ax, filled, color, title=None, elev=24, azim=-58):
    ax.voxels(filled, facecolors=color, edgecolor=INK, linewidth=0.35, shade=True)
    ax.set_box_aspect(filled.shape); ax.set_axis_off(); ax.view_init(elev=elev, azim=azim)
    if title: ax.set_title(title, fontsize=11, color=INK, pad=0)

def grid_idx(n):
    c = (np.arange(n) + 0.5) / n * 2 - 1
    return np.meshgrid(c, c, c, indexing='ij')

def ball(n): x, y, z = grid_idx(n); return x**2 + y**2 + z**2 <= 1
def torus(n, R=0.66, r=0.3):
    x, y, z = grid_idx(n); return (np.sqrt(x**2 + y**2) - R)**2 + z**2 <= r**2
def flat(a, k):  # срез по высоте, чтобы фигура была плоской
    n = a.shape[2]; return a[:, :, n//2 - k:n//2 + k]
def spinner(n):
    x, y, z = grid_idx(n); body = np.zeros_like(x, bool); holes = np.zeros_like(x, bool)
    body |= x**2 + y**2 <= 0.30**2; holes |= x**2 + y**2 <= 0.13**2
    for k in range(3):
        a = np.pi/2 + k*2*np.pi/3; cx, cy = 0.62*np.cos(a), 0.62*np.sin(a)
        body |= (x-cx)**2 + (y-cy)**2 <= 0.34**2; holes |= (x-cx)**2 + (y-cy)**2 <= 0.17**2
        t = np.clip((x*np.cos(a) + y*np.sin(a))/0.62, 0, 1); body |= (x - t*cx)**2 + (y - t*cy)**2 <= 0.20**2
    return (body & ~holes) & (np.abs(z) <= 0.16)
def two_hole(n):
    x, y, z = grid_idx(n); b = (np.abs(x) <= 0.95) & (np.abs(y) <= 0.55) & (np.abs(z) <= 0.22)
    h = ((x+0.45)**2 + y**2 <= 0.26**2) | ((x-0.45)**2 + y**2 <= 0.26**2); return b & ~h

# Рис. 1. Шар на трёх уровнях
fig = plt.figure(figsize=(10, 3.9))
for i, n in enumerate([4, 8, 16]):
    ax = fig.add_subplot(1, 3, i+1, projection='3d'); b = ball(n)
    vox(ax, b, COL['blue'], f'уровень n = {n}\n{int(b.sum())} ячеек')
fig.suptitle('Рис. 1. Один и тот же шар, записанный на трёх уровнях сетки', color=INK, y=0.99)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 1 — шар на трёх уровнях.png', bbox_inches='tight'); plt.close(fig)

# Рис. 2. Разные фигуры под сеткой
fig = plt.figure(figsize=(10, 7.6))
items = [(np.ones((6, 6, 6), bool), COL['yellow'], 'куб, дыр нет'),
         (torus(18)[:, :, 5:13], COL['red'], 'тор, одна дыра'),
         (two_hole(20)[:, 4:16, 7:13], COL['green'], 'пластина с двумя дырами'),
         (spinner(26)[:, :, 10:16], COL['violet'], 'спиннер, четыре дыры')]
for i, (a, c, t) in enumerate(items):
    ax = fig.add_subplot(2, 2, i+1, projection='3d'); vox(ax, a, c, f'{t}\n{int(a.sum())} ячеек', elev=38)
fig.suptitle('Рис. 2. Сетку можно наложить на любую фигуру', color=INK, y=0.98)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 2 — разные фигуры.png', bbox_inches='tight'); plt.close(fig)

# 2D-помощники
def cells(ax, rows, color=COL['blue'], mark=None, title=None, w=None, h=None):
    H = len(rows); W = max(len(r) for r in rows); w = w or W; h = h or H
    for yy in range(h):
        for xx in range(w):
            ax.add_patch(Rectangle((xx, h-1-yy), 1, 1, fill=False, ec='#c9c3b6', lw=0.6))
    for yy, r in enumerate(rows):
        for xx, ch in enumerate(r):
            if ch in '#*':
                ax.add_patch(Rectangle((xx, h-1-yy), 1, 1, fc=(COL['yellow'] if ch == '*' else color), ec=INK, lw=1.3))
    ax.set_xlim(-0.15, w+0.15); ax.set_ylim(-0.15, h+0.15); ax.set_aspect('equal'); ax.axis('off')
    if title: ax.set_title(title, fontsize=10.5, color=INK)

# Рис. 3. Действие α
fig, axs = plt.subplots(1, 3, figsize=(10, 2.9))
cells(axs[0], ['......', '.**...', '.##...', '......'], title='до: отмечена группа (жёлтая)')
cells(axs[1], ['......', '.****.', '.##...', '......'], title='α: растянуть вдвое вправо\nлевая сторона закреплена, +2 ячейки')
cells(axs[2], ['......', '.*....', '.##...', '......'], title='α: сжать вдвое\n−1 ячейка, 1 бит потери')
fig.suptitle('Рис. 3. Действие α: одна группа, одно направление, закреплённая сторона', color=INK, y=1.02)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 3 — действие альфа.png', bbox_inches='tight'); plt.close(fig)

# Рис. 4. Куб за три действия
fig = plt.figure(figsize=(10, 3.2))
for i, (shape, t) in enumerate([((1, 1, 1), 'точка\n0 действий'), ((4, 1, 1), 'ряд\n1 действие'), ((4, 4, 1), 'слой\n2 действия'), ((4, 4, 4), 'куб\n3 действия')]):
    ax = fig.add_subplot(1, 4, i+1, projection='3d'); a = np.zeros((4, 4, 4), bool); a[:shape[0], :shape[1], :shape[2]] = True; vox(ax, a, COL['yellow'], t); ax.set_xlim(0, 4); ax.set_ylim(0, 4); ax.set_zlim(0, 4)
fig.suptitle('Рис. 4. Утверждение 12: куб разряда k строится ровно за k действий', color=INK, y=1.0)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 4 — куб за три действия.png', bbox_inches='tight'); plt.close(fig)

# Рис. 5. Кольцо растёт вокруг дыры
steps = [['*..', '...', '...'], ['#**', '...', '...'], ['###', '*..', '*..'], ['###', '#.*', '#.*'], ['###', '#.#', '#*#']]
fig, axs = plt.subplots(1, 5, figsize=(10, 2.5))
for i, s in enumerate(steps): cells(axs[i], s, title=f'шаг {i}')
fig.suptitle('Рис. 5. Утверждение 13: кольцо растёт одними растяжениями, дыру не пробивают (новые ячейки жёлтые)', color=INK, y=1.03, fontsize=10.5)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 5 — кольцо растёт.png', bbox_inches='tight'); plt.close(fig)

# Рис. 6. Цена дыры
fig, axs = plt.subplots(1, 3, figsize=(10, 3.0), gridspec_kw={'wspace': 0.75})
cells(axs[0], ['####', '####', '####', '####'], title='сплошной квадрат')
cells(axs[1], ['####', '#..#', '#..#', '####'], title='квадрат с дырой 2×2')
cells(axs[2], ['####', '#**#', '#**#', '####'], title='дыра закрыта')
for a, b, txt in [(axs[0], axs[1], 'пробить:\n4 бита'), (axs[1], axs[2], 'закрыть:\n0 бит')]:
    fig.add_artist(FancyArrowPatch((a.get_position().x1 + 0.005, 0.47), (b.get_position().x0 - 0.005, 0.47), transform=fig.transFigure, arrowstyle='->', mutation_scale=16, color=INK, lw=1.4))
    fig.text((a.get_position().x1 + b.get_position().x0)/2, 0.56, txt, ha='center', color='#b3402f', fontsize=10)
fig.suptitle('Рис. 6. Утверждение 15: убрать ячейки дорого, вернуть бесплатно', color=INK, y=1.08)
fig.savefig(OUT + 'Сетка — рис. 6 — цена дыры.png', bbox_inches='tight'); plt.close(fig)

# Рис. 7. Лесенка
fig, axs = plt.subplots(1, 4, figsize=(10, 2.9))
for ax, n in zip(axs, [2, 4, 8, 16]):
    xs, ys = [0], [0]
    for k in range(n): xs += [(k+1)/n, (k+1)/n]; ys += [k/n, (k+1)/n]
    ax.plot([0, 1], [0, 1], color='#b3402f', lw=1.2, ls='--'); ax.plot(xs, ys, color=INK, lw=1.6)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(f'n = {n}\nдлина лесенки 2', fontsize=10.5, color=INK)
fig.suptitle('Рис. 7. Лесенка подходит к диагонали (длина 1,41), но её длина остаётся 2:\nфигура имеет предел, а её длина к длине предела не сходится', color=INK, y=1.12, fontsize=10.5)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 7 — лесенка.png', bbox_inches='tight'); plt.close(fig)

# Рис. 8. Предел через округление
fig = plt.figure(figsize=(10, 3.6))
def coarse(n, m=4):
    b = ball(n).astype(float); k = n // m; return b.reshape(m, k, m, k, m, k).mean(axis=(1, 3, 5)) >= 0.5
for i, n in enumerate([4, 8, 16, 32]):
    ax = fig.add_subplot(1, 4, i+1, projection='3d'); c = coarse(n); vox(ax, c, COL['green'], f'шар уровня {n},\nокруглённый до 4×4×4\n{int(c.sum())} ячеек')
fig.suptitle('Рис. 8. Определение предела: грубая картинка перестаёт меняться', color=INK, y=1.02)
fig.tight_layout(); fig.savefig(OUT + 'Сетка — рис. 8 — предел через округление.png', bbox_inches='tight'); plt.close(fig)
print('ok')
