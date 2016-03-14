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

	int h, w, n;
	cin >> h >> w >> n;
	
	deque<pair<char, int> > ope(n);
	REP(i, n) {
		int j;
		char c;
		cin >> c >> j;
		ope.push_front(mp(c, j));
	}
	
	int th = 0, tw = 0;
	REP(i, n) {
		auto p = ope.front();
		ope.pop_front(); // pop_front() は void 型
		if(p.first == NULL && p.second == 0) break; // null check

		if(p.first == 'R' && p.second == th) {
			tw = (tw == 0 ? w - 1 : tw - 1);
		} else if (p.first == 'C' && p.second == tw) {
			th = (th == 0 ? h - 1 : th - 1);
		}
	}

	cout << ((th+tw) % 2 == 1 ? "black" : "white") << endl;
}
