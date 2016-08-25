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
#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n, l;
	cin >> n >> l;

	int nummax = l / (n - 1) + 1;
	if(nummax < 2) {
		cout << 0 << endl;
		return 0;
	}

	bool primes[nummax];
	primes[0] = false;
	primes[1] = false;
	FOR(i, 2, nummax) primes[i] = true;

	FOR(i, 2, nummax) {
		if(primes[i]) {
			for(int j = i * 2; j < nummax; j += i) {
				primes[j] = false;
			}
		}
	}

	long ans = 0;
	REP(i, nummax) {
		if(primes[i]) {
			int t = (l + 1) - (n - 1) * i;
			if(t <= 0) break;
			ans += t;
		}
	}

	cout << ans << endl;
	return 0;
}
