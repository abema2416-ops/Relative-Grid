// Точный решатель R для бесквадратных высот (нормальный базис), высоты — битовые маски простых.
// Ветвление по «самой узкой» несобранной высоте; следующий блок — непустое подмножество её остатка.
#include <bits/stdc++.h>
using namespace std;
int n,U; vector<int> F; long long nodes=0; chrono::steady_clock::time_point T0; double LIM;
vector<int> B;
unordered_set<string> memo; int curK;
// множество масок, собираемых из непересекающихся блоков внутри f
void reach(int f, vector<int>& out){
    vector<char> seen(1<<U,0); vector<int> st={0}; seen[0]=1;
    for(size_t i=0;i<st.size();i++){int m=st[i];
        for(int b:B) if((b&f)==b && !(b&m)){int nm=m|b; if(!seen[nm]){seen[nm]=1; st.push_back(nm);}}}
    out=st;
}
bool dfs(int k){
    nodes++;
    { vector<int> sb=B; sort(sb.begin(),sb.end()); string key((char*)sb.data(),sb.size()*sizeof(int)); if(memo.count(key)) return false; memo.insert(key); }
    if((nodes&4095)==0 && chrono::duration<double>(chrono::steady_clock::now()-T0).count()>LIM) throw 1;
    int bestf=-1; size_t bestc=SIZE_MAX; vector<int> bestR;
    int unbuilt=0;
    for(int f:F){ vector<int> r; reach(f,r);
        bool ok=false; for(int m:r) if(m==f){ok=true;break;}
        if(ok) continue; unbuilt++;
        // варианты остатка
        set<int> rem; for(int m:r) rem.insert(f&~m);
        size_t c=0; for(int R:rem) c+=(1u<<__builtin_popcount(R))-1;
        if(c<bestc){bestc=c;bestf=f;bestR.assign(rem.begin(),rem.end());}
    }
    if(!unbuilt) return true;
    if((int)B.size()==k) return false;
    int r=k-B.size(); if(unbuilt > (1LL<<r)-1 + 0 && r<20 && unbuilt > ((1LL<<r)-1)*(long long)(1<<min(20,(int)B.size()))) return false;
    set<int> tried;
    for(int R:bestR) for(int s=R;s;s=(s-1)&R){ if(tried.count(s)) continue; tried.insert(s);
        B.push_back(s); if(dfs(k)) return true; B.pop_back(); }
    return false;
}
int main(int argc,char**argv){
    LIM=atof(argv[1]); int lo=atoi(argv[2]), hi=atoi(argv[3]);
    cin>>n>>U; F.resize(n); for(auto&x:F)cin>>x;
    T0=chrono::steady_clock::now();
    for(int k=lo;k<=hi;k++){ B.clear(); memo.clear();
        try{ if(dfs(k)){ printf("R = %d (точно: для k < %d решения нет), узлов %lld, %.1f с\nблоки:",k,k,nodes,chrono::duration<double>(chrono::steady_clock::now()-T0).count()); for(int b:B) printf(" %d",b); printf("\n"); return 0;} 
             else printf("k = %d: решения нет (доказано), узлов %lld\n",k,nodes); fflush(stdout);}
        catch(int){ printf("k = %d: не успел за %.0f с\n",k,LIM); return 0;}
    }
}
