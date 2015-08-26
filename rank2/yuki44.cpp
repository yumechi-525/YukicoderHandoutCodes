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
#define MOD (10 ** 9 + 7)

ll dp[60];

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int N;
  cin >> N;

  dp[0] = 1;
  for(int i = 0; i < N; i++) {
      for(int j = 1; j < 3; j++) {
          dp[i+j] += dp[i];
      }
  }

  cout << dp[N] << endl;
}
