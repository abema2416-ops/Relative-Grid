// Exact BFS for l_cell (stretches with P3,P5 + beta- "remove all glues") in a W x H box.
#include <bits/stdc++.h>
using namespace std;
int W,H;
struct S{vector<pair<int,int>> c; set<pair<pair<int,int>,pair<int,int>>> g;};
typedef pair<vector<pair<int,int>>, vector<pair<pair<int,int>,pair<int,int>>>> Key;
Key norm(vector<pair<int,int>> c, set<pair<pair<int,int>,pair<int,int>>> g, bool &ok){
  int mx=INT_MAX,my=INT_MAX,Mx=INT_MIN,My=INT_MIN;
  for(auto&p:c){mx=min(mx,p.first);my=min(my,p.second);Mx=max(Mx,p.first);My=max(My,p.second);}
  ok = (Mx-mx<W && My-my<H);
  for(auto&p:c){p.first-=mx;p.second-=my;}
  sort(c.begin(),c.end());
  vector<pair<pair<int,int>,pair<int,int>>> gg;
  for(auto e:g){auto a=e.first,b=e.second;a.first-=mx;a.second-=my;b.first-=mx;b.second-=my;if(b<a)swap(a,b);gg.push_back({a,b});}
  sort(gg.begin(),gg.end());
  return {c,gg};
}
bool adj(pair<int,int>a,pair<int,int>b){return abs(a.first-b.first)+abs(a.second-b.second)==1;}
int main(int argc,char**argv){
  W=atoi(argv[1]);H=atoi(argv[2]);int D=atoi(argv[3]);
  map<Key,int> dist; vector<Key> fr;
  bool ok; Key st=norm({{0,0}},{},ok); dist[st]=0; fr.push_back(st);
  for(int d=1; d<=D; d++){
    vector<Key> nf;
    for(auto &k:fr){
      auto &c=k.first; int n=c.size();
      set<pair<int,int>> cs(c.begin(),c.end());
      // beta- all
      if(!k.second.empty()){ Key nk=norm(c,{},ok); if(!dist.count(nk)){dist[nk]=d;nf.push_back(nk);} }
      for(unsigned m=1;m<(1u<<n);m++){
        vector<pair<int,int>> G,R; for(int i=0;i<n;i++) (m>>i&1?G:R).push_back(c[i]);
        set<pair<int,int>> Rs(R.begin(),R.end());
        for(int ax=0;ax<2;ax++) for(int s=-1;s<=1;s+=2){
          int a=INT_MAX; for(auto&p:G){int v=s*(ax?p.second:p.first); a=min(a,v);}
          int lim = ax?H:W;
          for(int f=2; f<=lim; f++){
            map<pair<int,int>,vector<pair<int,int>>> img; bool bad=false; vector<pair<int,int>> nc=R;
            set<pair<pair<int,int>,pair<int,int>>> ng;
            for(auto&p:G){int t=s*(ax?p.second:p.first)-a; vector<pair<int,int>> L;
              for(int j=0;j<f;j++){int q=s*(a+f*t+j); pair<int,int> P= ax? make_pair(p.first,q):make_pair(q,p.second);
                if(Rs.count(P)){bad=true;break;} L.push_back(P);} if(bad)break;
              for(size_t j=0;j+1<L.size();j++) ng.insert({L[j],L[j+1]});
              for(auto&P:L) nc.push_back(P); img[p]=L;}
            if(bad) continue;
            for(auto&e:k.second){ auto P = img.count(e.first)?img[e.first]:vector<pair<int,int>>{e.first};
              auto Q = img.count(e.second)?img[e.second]:vector<pair<int,int>>{e.second}; bool any=false;
              for(auto&x:P)for(auto&y:Q) if(adj(x,y)){ng.insert({min(x,y),max(x,y)});any=true;}
              if(!any){bad=true;break;} }
            if(bad) continue;
            Key nk=norm(nc,ng,ok); if(!ok) continue;
            if(!dist.count(nk)){dist[nk]=d;nf.push_back(nk);}
          }
        }
      }
    }
    fr=nf; fprintf(stderr,"depth %d: %zu new\n",d,nf.size());
  }
  // output min depth per cell set that is a relief with full base row of width W
  map<vector<int>,int> best;
  for(auto&kv:dist){ auto&c=kv.first.first; vector<int> h(W,0); bool okr=true;
    set<pair<int,int>> cs(c.begin(),c.end());
    for(int x=0;x<W;x++){ int y=0; while(cs.count({x,y}))y++; h[x]=y; if(y==0) okr=false;}
    if(!okr) continue; int tot=0; for(int x:h) tot+=x; if(tot!=(int)c.size()) continue;
    if(!best.count(h)||best[h]>kv.second) best[h]=kv.second; }
  for(auto&kv:best){ for(int x:kv.first) printf("%d ",x); printf(": %d\n",kv.second);}
}
