#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <iterator>
using namespace std;

typedef long long ll;
typedef pair<ll,ll> point;

ll D=1000000007,fr[20000002]={0},f[20000002]={0};

ll sqr(ll x){ 
  return x*x; 
}
ll pw(ll a, ll n){
    ll res=1;
    while (n){
        if (n&1) res*=a;
        a*=a;
        a%=D;
        res%=D;
        n>>=1;
    }
    return res;
}
ll c(ll n, ll k){
    if (!fr[k]) fr[k]=pw(f[k],D-2);
    if (!fr[n-k]) fr[n-k]=pw(f[n-k],D-2);
    return ((f[n]*fr[k]%D)*fr[n-k])%D; 
}
ll paths_between_points(point p1, point p2){
    ll x1=p1.first,x2=p2.first,y1=p1.second,y2=p2.second;
    ll x=abs(x1-x2),y=abs(y1-y2);
    return c(x+y,y)%D;
}
ll paths_from_origin(point p){
    ll x=p.first,y=p.second;
    return c(x+y,x)%D;
}

int main()
{
    ll d7=10000000;
    f[0]=f[1]=1; 
    int k,n,m,a,b;
    for (int i=2;i<d7*2+2;i++) f[i]=f[i-1]*i%D;
    set<point>s;
    for (m=1;m<100000;m++){
        n=m+1;
        while (sqr(n*n-m*m)<=d7 && 4*sqr(m*n)<=d7){
            k=1;
            while (k*k*sqr(n*n-m*m)<=d7 && 4*sqr(k*n*m)<=d7){
                a=k*k*sqr(n*n-m*m);
                b=4*sqr(k*m*n);
                if (a>b) swap(a,b);
                s.insert(make_pair(a,b));
                s.insert(make_pair(b,a));
                k++;
            }
            n++;
        }
    }
    n=s.size();
    vector<point>points;
    ll ans[n+2];
    points.push_back(make_pair(0,0));
    for (auto it=s.begin();it!=s.end();it++) points.push_back(*it);
    points.push_back(make_pair(d7,d7));
//     cout<<n<<endl;
    auto it=s.begin();
    sort(points.begin(),points.end());
    for (int i=1;i<n+2;i++){
        ans[i]=paths_from_origin(points[i])%D;
        for (int j=0;j<i;j++){
            if (points[j].second>points[i].second) continue;
            ans[i]-=ans[j]*paths_between_points(points[j],points[i])%D;
        }
        while (ans[i]<0) ans[i]+=D;
    }
    cout << ans[n+1]%D << endl;
    return 0;
}
