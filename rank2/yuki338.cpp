#include <iostream>
#include <cstdio>
#include <cmath>
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
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int yp, np;
	cin >> yp >> np;

	auto calcp = [=](int f, int s){return (int)(100.0 * f / s + 0.5 + 1e-6);};
	if(!yp || !np) {
		cout << 1 << endl;
		return 0;
	}
	int res = 1;
	while(true) {
		FOR(i, 1, res) {
			int ta = res - i;
			int tb = i;
			if(yp == calcp(ta, res) && np == calcp(tb, res)) {
				cout << res << endl;
				goto exit;
			}
		}
		res++;
	}

exit:
	return 0;
}
