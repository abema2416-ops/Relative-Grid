// Быстрая версия: 3D, α с любыми зонами + П3 + П5 (склейки), против правила отрезков.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long u64;
int X,Y,Z,MAXD,MD,NC;
struct Key{u64 a,b,c,d; bool operator==(const Key&o)const{return a==o.a&&b==o.b&&c==o.c&&d==o.d;}};
struct KH{size_t operator()(const Key&k)const{return k.a*0x9E3779B97F4A7C15ULL ^ (k.b+0x632BE59BD9B4E019ULL)*31 ^ k.c*1000003 ^ k.d*7919;}};
struct St{ int n; int x[64],y[64],z[64]; int ng; short ga[200],gb[200]; };
inline int cid(int x,int y,int z){return x+X*(y+Y*z);}
// нормализация, проверка размера, ключ
bool finish(St&s, Key&k){
  int mnx=1e9,mny=1e9,mnz=1e9,mxx=-1e9,mxy=-1e9,mxz=-1e9;
  for(int i=0;i<s.n;i++){mnx=min(mnx,s.x[i]);mny=min(mny,s.y[i]);mnz=min(mnz,s.z[i]);mxx=max(mxx,s.x[i]);mxy=max(mxy,s.y[i]);mxz=max(mxz,s.z[i]);}
  if(mxx-mnx+1>X||mxy-mny+1>Y||mxz-mnz+1>Z) return false;
  u64 m=0; for(int i=0;i<s.n;i++){s.x[i]-=mnx;s.y[i]-=mny;s.z[i]-=mnz; m|=1ULL<<cid(s.x[i],s.y[i],s.z[i]);}
  k={m,0,0,0};
  for(int e=0;e<s.ng;e++){ int A=s.ga[e],B=s.gb[e];
    int ax=s.x[A],ay=s.y[A],az=s.z[A],bx=s.x[B],by=s.y[B],bz=s.z[B];
    if(ax+ay+az>bx+by+bz){swap(ax,bx);swap(ay,by);swap(az,bz);}
    int dir= bx!=ax?0:(by!=ay?1:2); int idx=cid(ax,ay,az)*3+dir;
    if(idx<64) k.b|=1ULL<<idx; else if(idx<128) k.c|=1ULL<<(idx-64); else k.d|=1ULL<<(idx-128); }
  return true; }
static int occ[40][40][40]; static int stamp=0;
const int OFF=12;
bool stretch(const St&s,const vector<int>&G,int ax,int sg,int f,St&o){
  stamp++; static int inG[64]; static int gs=0; gs++;
  for(int i:G) inG[i]=gs;
  int a=INT_MAX; for(int i:G){int c= ax==0?s.x[i]:ax==1?s.y[i]:s.z[i]; a=min(a,sg*c);}
  for(int i=0;i<s.n;i++) if(inG[i]!=gs) occ[s.x[i]+OFF][s.y[i]+OFF][s.z[i]+OFF]=stamp;
  o.n=0; static int first[64]; int cnt[64];
  for(int i=0;i<s.n;i++) if(inG[i]!=gs){ first[i]=o.n; cnt[i]=1; o.x[o.n]=s.x[i];o.y[o.n]=s.y[i];o.z[o.n]=s.z[i];o.n++; }
  o.ng=0;
  for(int i:G){ int c= ax==0?s.x[i]:ax==1?s.y[i]:s.z[i]; int t=sg*c-a; first[i]=o.n; cnt[i]=f;
    for(int j=0;j<f;j++){ int p=sg*(a+f*t+j); int nx=s.x[i],ny=s.y[i],nz=s.z[i]; if(ax==0)nx=p; else if(ax==1)ny=p; else nz=p;
      if(nx+OFF<0||ny+OFF<0||nz+OFF<0||nx+OFF>=40||ny+OFF>=40||nz+OFF>=40) return false;
      if(occ[nx+OFF][ny+OFF][nz+OFF]==stamp) return false;
      if(o.n>=64) return false; o.x[o.n]=nx;o.y[o.n]=ny;o.z[o.n]=nz;
      if(j>0){ if(o.ng>=200) return false; o.ga[o.ng]=o.n-1; o.gb[o.ng]=o.n; o.ng++; }
      o.n++; } }
  for(int e=0;e<s.ng;e++){ int A=s.ga[e],B=s.gb[e]; bool ok=false;
    for(int u=first[A];u<first[A]+cnt[A];u++) for(int w=first[B];w<first[B]+cnt[B];w++){
      if(abs(o.x[u]-o.x[w])+abs(o.y[u]-o.y[w])+abs(o.z[u]-o.z[w])==1){ if(o.ng>=200) return false; o.ga[o.ng]=u;o.gb[o.ng]=w;o.ng++; ok=true; } }
    if(!ok) return false; }
  // убрать повторы склеек
  vector<pair<int,int>> v; for(int e=0;e<o.ng;e++) v.push_back({min(o.ga[e],o.gb[e]),max(o.ga[e],o.gb[e])}); sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()),v.end());
  o.ng=v.size(); for(int e=0;e<o.ng;e++){o.ga[e]=v[e].first;o.gb[e]=v[e].second;}
  return true; }
unordered_map<u64,int> run(bool rule){
  unordered_map<u64,int> best; unordered_set<Key,KH> seen; St s0; s0.n=1; s0.x[0]=s0.y[0]=s0.z[0]=0; s0.ng=0; Key k0; finish(s0,k0); seen.insert(k0); best[k0.a]=0;
  vector<St> fr={s0}; vector<int> G; G.reserve(64);
  for(int d=1;d<=MAXD;d++){ vector<St> nf; long tried=0;
    for(auto&s:fr){ int n=s.n;
      for(int ax=0;ax<3;ax++) for(int sg=-1;sg<=1;sg+=2){
        auto tryZone=[&](const vector<int>&Gz){ for(int f=2;f<=MD;f++){ St o; tried++; if(!stretch(s,Gz,ax,sg,f,o)) continue; Key k; if(!finish(o,k)) continue; if(d==MAXD){ if(!best.count(k.a)) best[k.a]=d; } else if(seen.insert(k).second){ nf.push_back(o); if(!best.count(k.a)) best[k.a]=d; } } };
        if(!rule){ if(n>18) continue; for(u64 sub=1;sub<(1ULL<<n);sub++){ G.clear(); for(int i=0;i<n;i++) if(sub>>i&1) G.push_back(i); tryZone(G);} }
        else { // отрезки вдоль оси ax
          map<pair<int,int>,vector<pair<int,int>>> L;
          for(int i=0;i<n;i++){ int c[3]={s.x[i],s.y[i],s.z[i]}; L[{c[(ax+1)%3],c[(ax+2)%3]}].push_back({c[ax],i}); }
          vector<vector<int>> segs; vector<int> segLine; vector<int> lo,hi; int li=0;
          for(auto&[kk,v]:L){ sort(v.begin(),v.end()); vector<int> cur={v[0].second}; int l0=v[0].first,pr=v[0].first;
            for(size_t j=1;j<v.size();j++){ if(v[j].first!=pr+1){segs.push_back(cur);segLine.push_back(li);lo.push_back(l0);hi.push_back(pr);cur.clear();l0=v[j].first;} cur.push_back(v[j].second); pr=v[j].first;}
            segs.push_back(cur);segLine.push_back(li);lo.push_back(l0);hi.push_back(pr); li++; }
          for(int kind=0;kind<2;kind++){ map<int,vector<int>> groups;
            for(int i=0;i<(int)segs.size();i++){ int key= kind==0?(sg==1?lo[i]:hi[i]):(sg==1?hi[i]:lo[i]); groups[key].push_back(i);}
            for(auto&[key,g]:groups){ int k=g.size(); if(k>16) continue;
              for(u64 sub=1;sub<(1ULL<<k);sub++){ G.clear(); u64 lm=0; bool dup=false; // строки: не больше одного отрезка
                set<int> ls; for(int i=0;i<k;i++) if(sub>>i&1){ int si=g[i]; if(!ls.insert(segLine[si]).second){dup=true;break;}
                  if(kind==0) for(int c:segs[si]) G.push_back(c); else G.push_back(sg==1? (s.x[0],segs[si].back()) : segs[si].front()); }
                if(!dup) tryZone(G); } } } } } }
    fr.swap(nf); fprintf(stderr,"%s: глубина %d, состояний %zu, фигур всего %zu, растяжений %ld\n",rule?"правило":"перебор",d,fr.size(),best.size(),tried); }
  return best; }
int main(int c,char**v){ X=atoi(v[1]);Y=atoi(v[2]);Z=atoi(v[3]);MAXD=atoi(v[4]); MD=max(X,max(Y,Z)); NC=X*Y*Z; if(NC>64) return 1;
  auto T=run(false); auto R=run(true); long eq=0,fast=0,miss=0,less=0,extra=0;
  for(auto&[m,d]:T){ auto it=R.find(m); if(it==R.end()){miss++;continue;} if(it->second==d) eq++; else if(it->second>d) fast++; else less++; }
  for(auto&[m,d]:R) if(!T.count(m)) extra++;
  printf("поле %dx%dx%d, цепочки до %d: фигур %zu; совпало %ld; перебор быстрее %ld; правило не нашло %ld; правило обещает меньше %ld; лишних %ld\n",X,Y,Z,MAXD,T.size(),eq,fast,miss,less,extra); fflush(stdout); }
