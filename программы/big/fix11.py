from dfs import *
F=json.load(open('dfsfails_41.json'))+json.load(open('dfsfails_42.json'))
ok=0;rest=[]
for f in F:
    H=f['H'];c=[f['got']]
    for fn in (lambda H:diff_rule(H),lambda H:diff_roots_rule(H),lambda H:diff_dfs(H,top=80,tlimit=60)):
        S=fn(H)
        if S:c.append(len(S))
    if min(c)!=f['k']:
        b,_=ensemble(H);c.append(b)
    ok+=min(c)==f['k']
    if min(c)!=f['k']:rest.append(f);print('осталась',f['M'],len(H),f['k'],min(c),flush=True)
print('из',len(F),'исправлено',ok)
json.dump(rest,open('rest.json','w'))
