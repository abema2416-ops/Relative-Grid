s=open('gsim.cpp',encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
rep("struct Res { long long cost; int acts, bits; vector<string> path; };","struct Res { long long cost; int acts, bits, pairs; vector<string> path; };")
rep("Res solve(St src, St dst, long long wA, long long wB, bool anyZ) {","Res solve(St src, St dst, long long wA, long long wB, bool anyZ, long long wP = 0) {")
rep("unordered_map<St, pair<int,int>, Hs> ab;","unordered_map<St, pair<int,int>, Hs> ab; unordered_map<St, int, Hs> pr_;")
rep("dist[src] = 0; ab[src] = {0, 0};","dist[src] = 0; ab[src] = {0, 0}; pr_[src] = 0;")
rep("Res r{d, ab[u].first, ab[u].second, {}};","Res r{d, ab[u].first, ab[u].second, pr_[u], {}};")
rep("auto relax = [&](St v, int bits, string how) { v = canon(v); long long nd = d + wA + wB * bits;","auto relax = [&](St v, int bits, string how, int pairs = 0) { v = canon(v); long long nd = d + wA + wB * bits + wP * pairs;")
rep("ab[v] = {ab[u].first + 1, ab[u].second + bits};","ab[v] = {ab[u].first + 1, ab[u].second + bits}; pr_[v] = pr_[u] + pairs;")
rep('if (cr) relax({c, g | cr}, 0, "склеить все трещины");','if (cr) relax({c, g | cr}, 0, "склеить " + to_string(__builtin_popcountll(cr)) + " пар", __builtin_popcountll(cr));')
rep("  return {-1, -1, -1, {}};","  return {-1, -1, -1, -1, {}};")
i=s.index("  vector<pair<string, vector<string>>> T;"); j=s.index("  St one{1, 0};")
s=s[:i]+'''  vector<pair<string, vector<string>>> T;
  T.push_back({"кольцо 3×3", {"###", "#.#", "###"}});
  if (W >= 4) T.push_back({"толстое кольцо 4×3 (q>0)", {"####", "#.##", "####"}});
  if (W >= 4) T.push_back({"сплошной 4×3 (q>0, дыр нет)", {"####", "####", "####"}});
'''+s[j:]
rep("    for (int from = 0; from < 2; from++) {","    for (int from = 0; from < 1; from++) {")
rep("      Res A = solve(src, dst, 1000, 1, anyZ), B = solve(src, dst, 1, 1000, anyZ);","      Res A = solve(src, dst, 1000, 1, anyZ), B = solve(src, dst, 1, 1000, anyZ), C = solve(src, dst, 1, 1000000, anyZ, 1000);")
rep('      printf("      путь с наименьшими действиями: "); for (auto &p : A.path) printf("%s; ", p.c_str()); printf("\\n");',
    '      printf("      путь с наименьшими действиями: "); for (auto &p : A.path) printf("%s; ", p.c_str()); printf("\\n");\n      printf("      без потерь, меньше всего склеенных пар: %d пар, %d д.: ", C.pairs, C.acts); for (auto &p : C.path) printf("%s; ", p.c_str()); printf("\\n");')
open('gsim.cpp','w',encoding='utf8').write(s)
