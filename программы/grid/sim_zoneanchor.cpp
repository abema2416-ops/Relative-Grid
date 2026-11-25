// Счётчик для «Относительной сетки», черновик 0.1.
// Перебирает все конфигурации ячеек в коробке W×H×D и все действия α (растянуть, сжать), σ (уничтожить) по зонам.
// Считает: длину построения (число действий) и потерянную информацию (log2 числа прообразов, Утверждение 2).
// Сборка: g++ -O2 -mbmi2 -std=c++17 sim.cpp -o sim
// Запуск: ./sim W H D zonemode   (zonemode: box | slab | any)
#include <bits/stdc++.h>
#include <immintrin.h>
using namespace std;
typedef uint32_t u32;

int W, H, D, M; u32 NS;
int DIM[3];
inline int idx(int x, int y, int z) { return x + W * (y + H * z); }
void xyz(int i, int c[3]) { c[0] = i % W; c[1] = (i / W) % H; c[2] = i / (W * H); }

vector<u32> canon;
u32 shiftMask(u32 s, int dx, int dy, int dz) {            // сдвиг без проверки
  u32 r = 0; for (int i = 0; i < M; i++) if (s >> i & 1) { int c[3]; xyz(i, c); r |= 1u << idx(c[0] + dx, c[1] + dy, c[2] + dz); } return r;
}
void bbox(u32 s, int mn[3], int mx[3]) { for (int a = 0; a < 3; a++) { mn[a] = 99; mx[a] = -1; } for (int i = 0; i < M; i++) if (s >> i & 1) { int c[3]; xyz(i, c); for (int a = 0; a < 3; a++) { mn[a] = min(mn[a], c[a]); mx[a] = max(mx[a], c[a]); } } }
vector<u32> placements(u32 cs) {                          // все положения формы в коробке
  int mn[3], mx[3]; bbox(cs, mn, mx); vector<u32> r;
  for (int dz = 0; mx[2] + dz < D; dz++) for (int dy = 0; mx[1] + dy < H; dy++) for (int dx = 0; mx[0] + dx < W; dx++) r.push_back(shiftMask(cs, dx, dy, dz));
  return r;
}
bool connected(u32 s, bool anyContact) {
  if (!s) return false; u32 seen = s & (~s + 1), fr = seen;
  while (fr) { int i = __builtin_ctz(fr); fr &= fr - 1; int c[3]; xyz(i, c);
    for (int dz = -1; dz <= 1; dz++) for (int dy = -1; dy <= 1; dy++) for (int dx = -1; dx <= 1; dx++) {
      int man = abs(dx) + abs(dy) + abs(dz); if (!man) continue; if (!anyContact && man != 1) continue;
      int x = c[0] + dx, y = c[1] + dy, z = c[2] + dz; if (x < 0 || y < 0 || z < 0 || x >= W || y >= H || z >= D) continue;
      u32 b = 1u << idx(x, y, z); if ((s & b) && !(seen & b)) { seen |= b; fr |= b; } } }
  return seen == s;
}

enum { STRETCH = 0, COMPRESS = 1, UNSTRETCH = 2, SIGMA = 3 };
const u32 BAD = 0xFFFFFFFFu;
struct Action { int type, axis, dir, f; u32 zm; vector<u32> img, raw; vector<uint16_t> cnt; /* cnt[S] = число прообразов результата */ };
vector<Action> acts;

void buildActions(const string &mode) {
  vector<u32> zones;
  if (mode == "any") { for (u32 z = 1; z < NS; z++) zones.push_back(z); }
  else for (int z0 = 0; z0 < D; z0++) for (int z1 = z0; z1 < D; z1++) for (int y0 = 0; y0 < H; y0++) for (int y1 = y0; y1 < H; y1++) for (int x0 = 0; x0 < W; x0++) for (int x1 = x0; x1 < W; x1++) {
    if (mode == "slab") { int full = (x0 == 0 && x1 == W - 1) + (y0 == 0 && y1 == H - 1) + (z0 == 0 && z1 == D - 1); if (full < 2) continue; }
    u32 m = 0; for (int z = z0; z <= z1; z++) for (int y = y0; y <= y1; y++) for (int x = x0; x <= x1; x++) m |= 1u << idx(x, y, z); zones.push_back(m);
  }
  for (u32 zm : zones) {
    int n = __builtin_popcount(zm); vector<int> zc; for (int i = 0; i < M; i++) if (zm >> i & 1) zc.push_back(i);
    int mn[3], mx[3]; bbox(zm, mn, mx);
    { Action A; A.type = SIGMA; A.axis = A.dir = A.f = 0; A.zm = zm; A.img.assign(1u << n, 0); A.img[0] = BAD; A.raw.assign(1u << n, 0); acts.push_back(A); }
    for (int axis = 0; axis < 3; axis++) { if (DIM[axis] < 2) continue;
      for (int dir = -1; dir <= 1; dir += 2) for (int f = 2; f <= DIM[axis]; f++) for (int type = STRETCH; type <= UNSTRETCH; type++) {
        Action A; A.type = type; A.axis = axis; A.dir = dir; A.f = f; A.zm = zm; A.img.assign(1u << n, BAD); A.raw.assign(1u << n, BAD); A.raw[0] = 0; bool anyValid = false;
        for (u32 p = 1; p < (1u << n); p++) {
          u32 full = _pdep_u32(p, zm), im = 0; bool ok = true;
          for (int k = 0; k < n && ok; k++) if (p >> k & 1) {
            int c[3]; xyz(zc[k], c); int off = dir > 0 ? c[axis] - mn[axis] : mx[axis] - c[axis];
            if (type == STRETCH) { for (int j = 0; j < f; j++) { int o = f * off + j, pos = dir > 0 ? mn[axis] + o : mx[axis] - o; if (pos < 0 || pos >= DIM[axis]) { ok = false; break; } int cc[3] = { c[0], c[1], c[2] }; cc[axis] = pos; im |= 1u << idx(cc[0], cc[1], cc[2]); } }
            else {
              if (type == UNSTRETCH) { for (int j = 0; j < f; j++) { int o = f * (off / f) + j, pos = dir > 0 ? mn[axis] + o : mx[axis] - o; if (pos < 0 || pos >= DIM[axis]) { ok = false; break; } int cc[3] = { c[0], c[1], c[2] }; cc[axis] = pos; if (!(full >> idx(cc[0], cc[1], cc[2]) & 1)) { ok = false; break; } } if (!ok) break; }
              int o = off / f, pos = dir > 0 ? mn[axis] + o : mx[axis] - o; int cc[3] = { c[0], c[1], c[2] }; cc[axis] = pos; im |= 1u << idx(cc[0], cc[1], cc[2]);
            }
          }
          if (ok) A.raw[p] = im; if (ok && im != full) { A.img[p] = im; anyValid = true; }
        }
        if (anyValid) acts.push_back(A);
      }
    }
  }
}
inline u32 applyAct(const Action &A, u32 S) {               // BAD, если действие неприменимо
  u32 p = _pext_u32(S, A.zm); u32 im = A.img[p]; if (im == BAD) return BAD; u32 rest = S & ~A.zm; if (im & rest) return BAD; u32 T = rest | im; if (!T || T == S) return BAD; return T;
}
// Число прообразов считается по всем конфигурациям, к которым действие применимо, включая те, где оно ничего не меняет
// (пустая зона, сжатие без изменения). Так «обратимость по одному результату» понимается в Утверждении 2.
bool TOTAL = true;
void countPreimages() {
  vector<u32> c(NS);
  for (auto &A : acts) { A.cnt.assign(NS, 0); vector<u32> res(NS, BAD);
    for (u32 S = 1; S < NS; S++) { u32 T;
      if (TOTAL) { u32 r = A.raw[_pext_u32(S, A.zm)], rest = S & ~A.zm; T = (r == BAD || (r & rest)) ? BAD : (rest | r); }
      else T = applyAct(A, S);
      res[S] = T; if (T != BAD) c[T]++; }
    for (u32 S = 1; S < NS; S++) if (res[S] != BAD) A.cnt[S] = (uint16_t)min<u32>(65535, c[res[S]]);
    for (u32 S = 1; S < NS; S++) if (res[S] != BAD) c[res[S]] = 0;
  }
}
// metric: 0 = шаги (все действия), 1 = шаги только растяжением, 2 = биты (строгое чтение: растянуть, сжать, σ), 3 = биты с точным обратным растяжением
vector<double> dijkstra(u32 src, int metric, vector<u32> *parent = nullptr, vector<int> *pact = nullptr) {
  vector<double> dist(NS, 1e18); dist[src] = 0; if (parent) { parent->assign(NS, 0); pact->assign(NS, -1); }
  priority_queue<pair<double, u32>, vector<pair<double, u32>>, greater<>> pq; pq.push({ 0, src });
  while (!pq.empty()) { auto [d, u] = pq.top(); pq.pop(); if (d > dist[u] + 1e-12) continue;
    for (u32 S : placements(u)) for (size_t ai = 0; ai < acts.size(); ai++) { const Action &A = acts[ai];
      if (metric == 1 && A.type != STRETCH) continue; if ((metric == 0 || metric == 2 || metric == 4) && A.type == UNSTRETCH) continue;
      u32 T = applyAct(A, S); if (T == BAD) continue; u32 v = canon[T];
      double w = metric <= 1 ? 1.0 : metric == 4 ? (double)__builtin_popcount(S ^ T) : log2((double)A.cnt[S]); if (dist[u] + w < dist[v] - 1e-12) { dist[v] = dist[u] + w; if (parent) { (*parent)[v] = u; (*pact)[v] = (int)ai; } pq.push({ dist[v], v }); } }
  }
  return dist;
}
string draw(u32 s) { string r; for (int z = 0; z < D; z++) { for (int y = 0; y < H; y++) { for (int x = 0; x < W; x++) r += (s >> idx(x, y, z) & 1) ? '#' : '.'; r += ' '; } if (z + 1 < D) r += "| "; } return r; }
u32 parse(const vector<string> &rows) { u32 m = 0; for (size_t y = 0; y < rows.size(); y++) for (size_t x = 0; x < rows[y].size(); x++) if (rows[y][x] == '#') m |= 1u << idx((int)x, (int)y, 0); return canon[m]; }
const char *TN[] = { "растянуть", "сжать", "обратно", "сигма" };

int main(int argc, char **argv) {
  W = atoi(argv[1]); H = atoi(argv[2]); D = atoi(argv[3]); string mode = argv[4]; if (argc > 5 && string(argv[5]) == "validonly") TOTAL = false; DIM[0] = W; DIM[1] = H; DIM[2] = D; M = W * H * D; NS = 1u << M;
  canon.assign(NS, 0); for (u32 s = 1; s < NS; s++) { int mn[3], mx[3]; bbox(s, mn, mx); canon[s] = shiftMask(s, -mn[0], -mn[1], -mn[2]); }
  setvbuf(stdout, nullptr, _IOLBF, 0); clock_t t0 = clock(); buildActions(mode); countPreimages(); fprintf(stderr, "подготовка %.1f c\n", double(clock() - t0) / CLOCKS_PER_SEC);
  size_t nst = 0, ncmp = 0, nsig = 0; int maxStretchCnt = 0; for (auto &A : acts) { if (A.type == STRETCH) { nst++; for (u32 S = 1; S < NS; S++) maxStretchCnt = max<int>(maxStretchCnt, A.cnt[S]); } else if (A.type == COMPRESS) ncmp++; else if (A.type == SIGMA) nsig++; }
  vector<u32> shapes; for (u32 s = 1; s < NS; s++) if (canon[s] == s) shapes.push_back(s);
  size_t nface = 0, nany = 0; for (u32 s : shapes) { if (connected(s, false)) nface++; if (connected(s, true)) nany++; }
  printf("=== коробка %dx%dx%d, зоны: %s, счёт прообразов: %s ===\n", W, H, D, mode.c_str(), TOTAL ? "по всем применимым" : "только где действие что-то меняет");
  printf("действий: растянуть %zu, сжать %zu, сигма %zu; форм (с точностью до сдвига): %zu, связных по граням: %zu, связных по любому касанию: %zu\n", nst, ncmp, nsig, shapes.size(), nface, nany);
  printf("наибольшее число прообразов у растяжения: %d\n", maxStretchCnt);
  u32 one = 1; vector<u32> par; vector<int> pa;
  auto steps = dijkstra(one, 0, &par, &pa); fprintf(stderr, "первый обход %.1f c\n", double(clock() - t0) / CLOCKS_PER_SEC); auto grow = dijkstra(one, 1), bitsR = dijkstra(one, 2), bitsE = dijkstra(one, 3); fprintf(stderr, "четыре обхода %.1f c\n", double(clock() - t0) / CLOCKS_PER_SEC);
  // гистограммы длины построения
  map<int, int> hAll, hFace, hAny, hGrow; int unreachable = 0, growFaceMiss = 0, growReach = 0; double maxBitsR = 0, maxBitsE = 0; int nzR = 0, nzE = 0;
  for (u32 s : shapes) { if (steps[s] > 1e17) { unreachable++; continue; } int k = (int)lround(steps[s]); hAll[k]++; bool fc = connected(s, false), ac = connected(s, true); if (fc) hFace[k]++; if (ac) hAny[k]++;
    if (grow[s] < 1e17) { growReach++; hGrow[(int)lround(grow[s])]++; } else if (fc) growFaceMiss++;
    maxBitsR = max(maxBitsR, bitsR[s]); maxBitsE = max(maxBitsE, bitsE[s]); if (bitsR[s] > 1e-9) nzR++; if (bitsE[s] > 1e-9) nzE++; }
  auto ph = [](const char *name, map<int, int> &h) { printf("%s:", name); for (auto &kv : h) printf("  %d шаг.: %d", kv.first, kv.second); printf("\n"); };
  printf("\n-- длина построения из одной ячейки --\n"); ph("все формы", hAll); ph("связные по граням", hFace); ph("связные по любому касанию", hAny);
  printf("недостижимых форм: %d\n", unreachable);
  ph("только растяжением (число шагов)", hGrow); printf("достижимо одним растяжением: %d форм; связных по граням, но недостижимых растяжением: %d\n", growReach, growFaceMiss);
  int mxs = hAny.empty() ? 0 : hAny.rbegin()->first; printf("самые длинные построения среди связных (%d шаг.), примеры:\n", mxs); int shown = 0;
  for (u32 s : shapes) if (connected(s, true) && (int)lround(steps[s]) == mxs && shown < 6) { printf("   %s\n", draw(s).c_str()); shown++; }
  printf("\n-- потерянная информация при построении из одной ячейки --\n");
  printf("строгое чтение (растянуть, сжать, сигма): форм с ненулевой ценой %d, наибольшая цена %.3f бит\n", nzR, maxBitsR);
  printf("с точным обратным растяжением: форм с ненулевой ценой %d, наибольшая цена %.3f бит\n", nzE, maxBitsE);
  // названные формы
  vector<pair<string, u32>> named;
  if (D == 1 && H == 1) { for (int L = 1; L <= W; L++) named.push_back({ "отрезок " + to_string(L), (1u << L) - 1 }); if (W >= 3) named.push_back({ "две ячейки с разрывом", canon[0b101] }); if (W >= 5) named.push_back({ "#.#.#", canon[0b10101] }); for (int h = 2; h + 2 <= W && h <= 5; h++) named.push_back({ "разрыв " + to_string(h), (u32)(1u | (1u << (h + 1))) }); }
  else if (D == 1) {
    named.push_back({ "ячейка", parse({ "#" }) }); named.push_back({ "пара", parse({ "##" }) }); named.push_back({ "ряд 3", parse({ "###" }) }); named.push_back({ "угол", parse({ "#.", "##" }) });
    named.push_back({ "диагональ 2", parse({ "#.", ".#" }) }); named.push_back({ "квадрат 2", parse({ "##", "##" }) });
    if (W >= 3 && H >= 3) { named.push_back({ "квадрат 3", parse({ "###", "###", "###" }) }); named.push_back({ "кольцо 3 (дыра 1)", parse({ "###", "#.#", "###" }) }); named.push_back({ "крест", parse({ ".#.", "###", ".#." }) }); named.push_back({ "шахматы 3", parse({ "#.#", ".#.", "#.#" }) }); named.push_back({ "буква С", parse({ "###", "#..", "###" }) }); }
    if (W >= 4 && H >= 4) { named.push_back({ "ряд 4", parse({ "####" }) }); named.push_back({ "квадрат 4", parse({ "####", "####", "####", "####" }) }); named.push_back({ "рамка 4 (дыра 2x2)", parse({ "####", "#..#", "#..#", "####" }) }); named.push_back({ "две дыры", parse({ "####", "#.##", "##.#", "####" }) }); named.push_back({ "шахматы 4", parse({ "#.#.", ".#.#", "#.#.", ".#.#" }) }); }
  } else {
    named.push_back({ "ячейка", 1 }); u32 full = NS - 1; named.push_back({ "полная коробка", full });
    u32 layer = 0; for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) layer |= 1u << idx(x, y, 0); named.push_back({ "один слой", layer });
    u32 col = 0; for (int z = 0; z < D; z++) col |= 1u << idx(0, 0, z); named.push_back({ "столбик", col });
    if (W >= 3 && H >= 3) { u32 tun = full; for (int z = 0; z < D; z++) tun &= ~(1u << idx(1, 1, z)); named.push_back({ "коробка со сквозной дырой", tun }); }
    named.push_back({ "коробка без угла", full & ~1u });
  }
  printf("\n-- названные формы: шаги из ячейки / только растяжением / рисунок и цепочка --\n");
  for (auto &nm : named) { u32 s = nm.second; printf("%-28s %s  шагов %d, растяжением %s\n", nm.first.c_str(), draw(s).c_str(), (int)lround(steps[s]), grow[s] < 1e17 ? to_string((int)lround(grow[s])).c_str() : "нельзя");
    vector<string> chain; u32 v = s; while (v != one && pa[v] >= 0) { const Action &A = acts[pa[v]]; char b[200]; snprintf(b, 200, "%s(зона %d яч.%s%s)", TN[A.type], __builtin_popcount(A.zm), A.type == SIGMA ? "" : (string(", ось ") + "xyz"[A.axis] + (A.dir > 0 ? "+" : "-") + ", x" + to_string(A.f)).c_str(), ""); chain.push_back(string(b) + " -> " + draw(v)); v = par[v]; }
    for (int i = (int)chain.size() - 1; i >= 0; i--) printf("      %s\n", chain[i].c_str()); }
  printf("\n-- расстояния между названными формами: шаги (строка -> столбец) --\n      "); for (size_t j = 0; j < named.size(); j++) printf("%4zu", j + 1); printf("\n");
  if (getenv("NAMED")) { vector<pair<string, u32>> nn; string e = getenv("NAMED"); for (size_t i = 0; i < named.size(); i++) if (e.find("," + to_string(i + 1) + ",") != string::npos) nn.push_back(named[i]); named = nn; }
  vector<vector<double>> DS, DB;
  for (size_t i = 0; i < named.size(); i++) { DS.push_back(dijkstra(named[i].second, 0)); DB.push_back(dijkstra(named[i].second, 2)); }
  for (size_t i = 0; i < named.size(); i++) { printf("%4zu  ", i + 1); for (size_t j = 0; j < named.size(); j++) { double d = DS[i][named[j].second]; if (d > 1e17) printf("   -"); else printf("%4d", (int)lround(d)); } printf("   %s\n", named[i].first.c_str()); }
  printf("\n-- то же в битах потерянной информации (строгое чтение) --\n      "); for (size_t j = 0; j < named.size(); j++) printf("%6zu", j + 1); printf("\n");
  for (size_t i = 0; i < named.size(); i++) { printf("%4zu  ", i + 1); for (size_t j = 0; j < named.size(); j++) { double d = DB[i][named[j].second]; if (d > 1e17) printf("     -"); else printf("%6.2f", d); } printf("   %s\n", named[i].first.c_str()); }
  // несимметричность шагов по всем парам связных форм — только для малых коробок
  if (shapes.size() <= 600) { int asym = 0, pairs = 0, maxd = 0; u32 wa = 0, wb = 0; vector<vector<double>> all; for (u32 s : shapes) all.push_back(dijkstra(s, 0));
    for (size_t i = 0; i < shapes.size(); i++) for (size_t j = i + 1; j < shapes.size(); j++) { if (!connected(shapes[i], true) || !connected(shapes[j], true)) continue; int a = (int)lround(all[i][shapes[j]]), b = (int)lround(all[j][shapes[i]]); pairs++; if (a != b) asym++; if (max(a, b) > maxd) { maxd = max(a, b); wa = a >= b ? shapes[i] : shapes[j]; wb = a >= b ? shapes[j] : shapes[i]; } }
    printf("\n-- все пары связных форм --\nпар: %d, с разным числом шагов туда и обратно: %d, наибольшее расстояние: %d шаг. (%s -> %s)\n", pairs, asym, maxd, draw(wa).c_str(), draw(wb).c_str()); }
  if (shapes.size() <= 600) {
    // биты по всем парам: сравнение с формулой «число ячеек A минус наибольшее перекрытие A и B»
    auto overlap = [&](u32 A, u32 B) { int best = 0; vector<array<int,3>> ca, cb; for (int q = 0; q < M; q++) { int c[3]; xyz(q, c); if (A >> q & 1) ca.push_back({ c[0], c[1], c[2] }); if (B >> q & 1) cb.push_back({ c[0], c[1], c[2] }); }
      for (int dz = -D; dz <= D; dz++) for (int dy = -H; dy <= H; dy++) for (int dx = -W; dx <= W; dx++) { int k = 0; for (auto &p : ca) for (auto &r : cb) if (p[0] == r[0] + dx && p[1] == r[1] + dy && p[2] == r[2] + dz) k++; best = max(best, k); } return best; };
    long eq = 0, lt = 0, gt = 0, nonint = 0, tot = 0, asymB = 0; double maxB = 0; vector<vector<double>> allB, allE; for (u32 sh : shapes) { allB.push_back(dijkstra(sh, 2)); allE.push_back(dijkstra(sh, 3)); }
    long eqE = 0, ltE = 0, zeroE = 0;
    for (size_t i = 0; i < shapes.size(); i++) for (size_t j = 0; j < shapes.size(); j++) { if (i == j) continue; double b = allB[i][shapes[j]], e = allE[i][shapes[j]]; tot++; int fm = __builtin_popcount(shapes[i]) - overlap(shapes[i], shapes[j]);
      if (fabs(b - lround(b)) > 1e-6) nonint++; if (fabs(b - fm) < 1e-6) eq++; else if (b < fm) lt++; else gt++; maxB = max(maxB, b); if (j > i && fabs(b - allB[j][shapes[i]]) > 1e-6) asymB++;
      if (fabs(e - b) < 1e-6) eqE++; else if (e < b) ltE++; if (e < 1e-9) zeroE++; }
    printf("\n-- биты, все упорядоченные пары форм (%ld) --\nсовпало с формулой «ячейки A минус перекрытие»: %ld, меньше формулы: %ld, больше формулы: %ld; нецелых значений: %ld; наибольшая цена: %.2f; пар с разной ценой туда и обратно: %ld\n", tot, eq, lt, gt, nonint, maxB, asymB);
    printf("с точным обратным растяжением: цена та же в %ld парах, меньше в %ld, нулевая в %ld\n", eqE, ltE, zeroE);
    { long below = 0, same = 0, supOK = 0, supAll = 0; for (size_t i = 0; i < shapes.size(); i++) for (size_t j = 0; j < shapes.size(); j++) { if (i == j) continue; double b = allB[i][shapes[j]]; int df = __builtin_popcount(shapes[i]) - __builtin_popcount(shapes[j]); if (b < df - 1e-6) below++; if (fabs(b - max(0, df)) < 1e-6) same++;
        if ((shapes[i] & shapes[j]) == shapes[i]) { supAll++; if (b < 1e-9) supOK++; } }
      printf("цена меньше разности числа ячеек |A|-|B|: %ld пар; цена равна max(0,|A|-|B|): %ld пар; пар, где A лежит внутри B (в этом положении): %ld, из них с нулевой ценой: %ld\n", below, same, supAll, supOK); }
    { long tot4 = 0, eq4 = 0, gt4 = 0, lt4 = 0, as4 = 0; vector<vector<double>> allW; for (u32 sh : shapes) allW.push_back(dijkstra(sh, 4));
      auto symd = [&](u32 A, u32 B) { return __builtin_popcount(A) + __builtin_popcount(B) - 2 * overlap(A, B); };
      for (size_t i = 0; i < shapes.size(); i++) for (size_t j = 0; j < shapes.size(); j++) { if (i == j) continue; double w = allW[i][shapes[j]]; int f = symd(shapes[i], shapes[j]); tot4++; if (fabs(w - f) < 1e-6) eq4++; else if (w > f) gt4++; else lt4++; if (j > i && fabs(w - allW[j][shapes[i]]) > 1e-6) as4++; }
      printf("\n-- правило «1 бит за каждую изменённую ячейку» --\nпар %ld: цена равна наименьшему числу несовпадающих ячеек: %ld, больше: %ld, меньше: %ld; несимметричных пар: %ld\n", tot4, eq4, gt4, lt4, as4);
      int sh4 = 0; for (size_t i = 0; i < shapes.size() && sh4 < 3; i++) for (size_t j = 0; j < shapes.size() && sh4 < 3; j++) { if (i == j) continue; double w = allW[i][shapes[j]]; int f = symd(shapes[i], shapes[j]); if (w > f + 1e-6) { printf("   пример: %s -> %s : %.0f, несовпадающих ячеек %d\n", draw(shapes[i]).c_str(), draw(shapes[j]).c_str(), w, f); sh4++; } } }
    int shownLt = 0; for (size_t i = 0; i < shapes.size() && shownLt < 4; i++) for (size_t j = 0; j < shapes.size() && shownLt < 4; j++) { if (i == j) continue; double b = allB[i][shapes[j]]; int fm = __builtin_popcount(shapes[i]) - overlap(shapes[i], shapes[j]); if (fabs(b - fm) > 1e-6) { printf("   пример отклонения: %s -> %s : %.2f бит, формула %d\n", draw(shapes[i]).c_str(), draw(shapes[j]).c_str(), b, fm); shownLt++; } }
  }
  return 0;
}
