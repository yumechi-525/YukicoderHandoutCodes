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
#define INF 1<<29
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define _DEBUG(x) cout<<#x<<": "<<x<<endl
#define _DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n, k;
	cin >> n >> k;

	ll ans = 0;
	vector<int> list;
	REP(i, n) list.pb(i + 1);

	ll limit = 1;
	REP(i, n) limit *= 2;

	FOR(i, 1, limit-1) {
		vector<int> l1 = {};
		vector<int> l2 = {};
		int bitnum = i;
		REP(j, n) {
			((bitnum & 1) == 1 ? l1 : l2).pb(list[j]);
			bitnum >>= 1;
		}
		sort(l1.begin(), l1.end());
		sort(l2.begin(), l2.end());

		// if(l1.size() == 0 || l2.size() == 0) continue;

		int l1max = *max_element(l1.begin(), l1.end());
		int l2min = *min_element(l2.begin(), l2.end());
		if(l1max > l2min && l1[0] == k) ans++;
	}
#if DEBUG
	cout << "** RESULT **" << endl; // debug
#endif
	cout << ans << endl;
}
