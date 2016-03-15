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

bool dp[10010];

vector<int> getPrime(int n) {
	vector<int> ret;

	// error check
	if(n <= 0) {
		cout << "can use this method negative number: getPrime " << n << endl;
		return ret;
	}

	FOR(i, 2, n) {
		bool flag = true;
		for(auto prime : ret) {
			if(i % prime == 0) {
				flag = false;
				break;
			}
		}

		if(flag) ret.pb(i);
	}

	return ret;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	int n;
	cin >> n;

	auto prime = getPrime(10000);

	dp[0] = dp[1] = true;
	REP(i, n+1) {
		for(auto j : prime) {
			if(i < j) break;
			if(!dp[i-j]) {
				dp[i] = true;
				break;
			}
		}
	}

	cout << (dp[n] ? "Win" : "Lose") << endl;
	return 0;
}
