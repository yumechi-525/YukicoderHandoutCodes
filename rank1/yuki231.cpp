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

    vector<int> list(n);
    vector<int> copylist(n);
    REP(i, n) {
        int g, d;
        cin >> g >> d;
        list[i] = g - d * 30000;
        copylist[i] = g - d * 30000;
    }

    sort(list.begin(), list.end());
    int last = list.at(n-1);
    if(last * 6 >= 3000000) {
        cout << "YES" << endl;
        REP(i, n) {
            if(last == copylist[i]) {
                REP(j, 6) {
                    cout << i+1 << endl;
                }
                break;
            }
        }
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
