#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define INF 1<<30
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n = 0;
    cin >> n;
    int r = 0;

    REP(i, n) {
        int g, d;
        cin >> g >> d;
        r = g - d * 30000;
        if(r * 6 >= 3000000) {
            cout << "YES" << endl;
            REP(j, 6) {
                cout << i+1 << endl;
            }
            break;
        }
    }

    if(r * 6 < 3000000) {
        cout << "NO" << endl;
    }

    return 0;
}
