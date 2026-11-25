// Счётчик со склейками для «Относительной сетки», плоский случай.
// Состояние: клетки (маска) + склейки (маска стыков по сторонам). Касание без склейки — трещина.
// Действия: растянуть, сжать (группа = зона ∩ клетки), σ (убрать зону), β (склеить все текущие трещины).
// Биты = число исчезнувших клеток (правило автора: одна клетка — один бит).
// Растяжение и сжатие, рвущие склейку, недопустимы (П5). Формы считаются с точностью до сдвига.
// Сборка: g++ -O2 -std=c++17 gsim.cpp -o gsim ; запуск: ./gsim W H zones(any|box)
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
int W, H, M, NE; vector<pair<int,int>> EDGES; map<pair<int,int>,int> EID;
inline int id(int x, int y) { return x + W * y; }
struct St { u64 c, g; bool operator==(const St &o) const { return c == o.c && g == o.g; } };
struct Hs { size_t operator()(const St &s) const { return s.c * 1000003ULL ^ s.g; } };
int eid(int a, int b) { if (a > b) swap(a, b); auto it = EID.find({a, b}); return it == EID.end() ? -1 : it->second; }
St canon(St s) {
  int mnx = 99, mny = 99; for (int i = 0; i < M; i++) if (s.c >> i & 1) { mnx = min(mnx, i % W); mny = min(mny, i / W); }
  if (!mnx && !mny) return s;
  St r{0, 0}; for (int i = 0; i < M; i++) if (s.c >> i & 1) r.c |= 1ULL << id(i % W - mnx, i / W - mny);
  for (int e = 0; e < NE; e++) if (s.g >> e & 1) { int a = EDGES[e].first, b = EDGES[e].second; r.g |= 1ULL << eid(id(a % W - mnx, a / W - mny), id(b % W - mnx, b / W - mny)); }
  return r;
}
u64 contacts(u64 c) { u64 m = 0; for (int e = 0; e < NE; e++) if ((c >> EDGES[e].first & 1) && (c >> EDGES[e].second & 1)) m |= 1ULL << e; return m; }
int holes(St s) { // b1 = компоненты − клетки + склейки − q
  int F = __builtin_popcountll(s.c), E = __builtin_popcountll(s.g), q = 0;
  vector<int> p(M); iota(p.begin(), p.end(), 0); function<int(int)> f = [&](int x) { return p[x] == x ? x : p[x] = f(p[x]); };
  for (int e = 0; e < NE; e++) if (s.g >> e & 1) p[f(EDGES[e].first)] = f(EDGES[e].second);
  set<int> comp; for (int i = 0; i < M; i++) if (s.c >> i & 1) comp.insert(f(i));
  for (int y = 0; y + 1 < H; y++) for (int x = 0; x + 1 < W; x++) { int a = id(x, y), b = id(x + 1, y), c = id(x, y + 1), d = id(x + 1, y + 1);
    int es[4] = {eid(a, b), eid(a, c), eid(b, d), eid(c, d)}; bool ok = true; for (int k = 0; k < 4; k++) ok &= (s.g >> es[k] & 1); if (ok) q++; }
  return (int)comp.size() - F + E - q;
}
// применение растяжения/сжатия; возвращает false, если недопустимо
bool alpha(St s, u64 G, int axis, int sd, int f, bool stretch, St &out, int &lost) {
  int a = INT_MAX; for (int i = 0; i < M; i++) if (G >> i & 1) { int ci = axis ? i / W : i % W; a = min(a, sd * ci); }
  u64 rest = s.c & ~G; map<int, vector<int>> img; u64 nc = 0; lost = 0;
  for (int i = 0; i < M; i++) if (G >> i & 1) {
    int x = i % W, y = i / W, ci = axis ? y : x, t = sd * ci - a;
    vector<int> out;
    if (stretch) { for (int j = 0; j < f; j++) { int p = sd * (a + f * t + j); int nx = axis ? x : p, ny = axis ? p : y; if (nx < 0 || ny < 0 || nx >= W || ny >= H) return false; out.push_back(id(nx, ny)); } }
    else { int p = sd * (a + t / f); int nx = axis ? x : p, ny = axis ? p : y; out.push_back(id(nx, ny)); }
    for (int o : out) { if (rest >> o & 1) return false; nc |= 1ULL << o; }
    img[i] = out;
  }
  if (!stretch) lost = __builtin_popcountll(G) - __builtin_popcountll(nc);
  u64 ng = 0;
  if (stretch) for (auto &kv : img) for (size_t k = 0; k + 1 < kv.second.size(); k++) ng |= 1ULL << eid(kv.second[k], kv.second[k + 1]);
  auto adj = [&](int p, int q) { return abs(p % W - q % W) + abs(p / W - q / W) == 1; };
  for (int e = 0; e < NE; e++) if (s.g >> e & 1) {
    int p = EDGES[e].first, q = EDGES[e].second; vector<int> P = img.count(p) ? img[p] : vector<int>{p}, Q = img.count(q) ? img[q] : vector<int>{q};
    bool any = false, same = false;
    for (int x : P) for (int y : Q) { if (x == y) same = true; else if (adj(x, y)) { ng |= 1ULL << eid(x, y); any = true; } }
    if (!any && !same) return false; // склейка порвалась
  }
  out = {rest | nc, ng & contacts(rest | nc)}; return true;
}
vector<u64> zonesFor(u64 c, bool anyZ) {
  vector<u64> z;
  if (anyZ) { vector<int> cs; for (int i = 0; i < M; i++) if (c >> i & 1) cs.push_back(i); int n = cs.size();
    for (int m = 1; m < (1 << n); m++) { u64 g = 0; for (int k = 0; k < n; k++) if (m >> k & 1) g |= 1ULL << cs[k]; z.push_back(g); } }
  else { set<u64> seen; for (int y0 = 0; y0 < H; y0++) for (int y1 = y0; y1 < H; y1++) for (int x0 = 0; x0 < W; x0++) for (int x1 = x0; x1 < W; x1++) {
      u64 g = 0; for (int y = y0; y <= y1; y++) for (int x = x0; x <= x1; x++) g |= 1ULL << id(x, y); g &= c; if (g && seen.insert(g).second) z.push_back(g); } }
  return z;
}
struct Res { long long cost; int acts, bits, pairs; vector<string> path; };
// Дейкстра с весом wA*действия + wB*биты
Res solve(St src, St dst, long long wA, long long wB, bool anyZ, long long wP = 0) {
  src = canon(src); dst = canon(dst);
  unordered_map<St, long long, Hs> dist; unordered_map<St, pair<St, string>, Hs> par; unordered_map<St, pair<int,int>, Hs> ab; unordered_map<St, int, Hs> pr_;
  typedef tuple<long long, u64, u64> T; priority_queue<T, vector<T>, greater<T>> pq;
  dist[src] = 0; ab[src] = {0, 0}; pr_[src] = 0; pq.push({0, src.c, src.g});
  while (!pq.empty()) {
    auto [d, c, g] = pq.top(); pq.pop(); St u{c, g}; if (d > dist[u]) continue;
    if (u == dst) { Res r{d, ab[u].first, ab[u].second, pr_[u], {}}; St v = u; while (!(v == src)) { auto &pr = par[v]; r.path.push_back(pr.second); v = pr.first; } reverse(r.path.begin(), r.path.end()); return r; }
    auto relax = [&](St v, int bits, string how, int pairs = 0) { v = canon(v); long long nd = d + wA + wB * bits + wP * pairs; auto it = dist.find(v);
      if (it == dist.end() || nd < it->second) { dist[v] = nd; par[v] = {u, how}; ab[v] = {ab[u].first + 1, ab[u].second + bits}; pr_[v] = pr_[u] + pairs; pq.push({nd, v.c, v.g}); } };
    // сдвиги, чтобы было место расти в отрицательную сторону
    vector<St> shifts{u};
    int mxx = 0, mxy = 0; for (int i = 0; i < M; i++) if (c >> i & 1) { mxx = max(mxx, i % W); mxy = max(mxy, i / W); }
    for (int dx = 0; dx + mxx < W; dx++) for (int dy = 0; dy + mxy < H; dy++) { if (!dx && !dy) continue; St s{0, 0};
      for (int i = 0; i < M; i++) if (c >> i & 1) s.c |= 1ULL << id(i % W + dx, i / W + dy);
      for (int e = 0; e < NE; e++) if (g >> e & 1) { int a = EDGES[e].first, b = EDGES[e].second; s.g |= 1ULL << eid(id(a % W + dx, a / W + dy), id(b % W + dx, b / W + dy)); }
      shifts.push_back(s); }
    for (St s : shifts) {
      for (u64 G : zonesFor(s.c, anyZ)) {
        for (int axis = 0; axis < 2; axis++) for (int sd = -1; sd <= 1; sd += 2) for (int f = 2; f <= (axis ? H : W); f++) for (int st = 0; st < 2; st++) {
          St o; int lost; if (alpha(s, G, axis, sd, f, st, o, lost) && !(canon(o) == canon(s))) relax(o, lost, string(st ? "растянуть" : "сжать") + " ×" + to_string(f));
        }
        u64 left = s.c & ~G; if (left) relax({left, s.g & contacts(left)}, __builtin_popcountll(G), "убрать " + to_string(__builtin_popcountll(G)) + " кл.");
      }
    }
    u64 cr = contacts(c) & ~g; if (cr) relax({c, g | cr}, 0, "склеить " + to_string(__builtin_popcountll(cr)) + " пар", __builtin_popcountll(cr));
  }
  return {-1, -1, -1, -1, {}};
}
St shape(vector<string> rows) { St s{0, 0}; for (int y = 0; y < (int)rows.size(); y++) for (int x = 0; x < (int)rows[y].size(); x++) if (rows[y][x] == '#') s.c |= 1ULL << id(x, y); s.g = contacts(s.c); return s; }

int main(int argc, char **argv) {
  setvbuf(stdout, nullptr, _IOLBF, 0);
  // argv: name W H row1 row2 ...   (field = shape bounding box + 1 margin handled by W,H)
  string name=argv[1]; W=atoi(argv[2]); H=atoi(argv[3]); M=W*H; bool anyZ=true;
  for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) { if (x + 1 < W) { EID[{id(x, y), id(x + 1, y)}] = EDGES.size(); EDGES.push_back({id(x, y), id(x + 1, y)}); }
    if (y + 1 < H) { EID[{id(x, y), id(x, y + 1)}] = EDGES.size(); EDGES.push_back({id(x, y), id(x, y + 1)}); } }
  NE = EDGES.size();
  vector<string> rows; for (int k=4;k<argc;k++) rows.push_back(argv[k]);
  St dst=shape(rows); St one{1,0}; int hd=holes(dst);
  Res A = solve(one, dst, 1000, 1, anyZ);            // fewest actions (bits allowed)
  Res C = solve(one, dst, 1, 1000000, anyZ, 0);       // no bit loss, then fewest actions
  printf("%s|holes %d|min actions %d (bits %d)|lossless min actions %d|", name.c_str(), hd, A.acts, A.bits, C.bits==0?C.acts:-1);
  for (auto &p : C.path) printf("%s; ", p.c_str()); printf("\n");
}
