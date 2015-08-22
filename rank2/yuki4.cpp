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

int dp[10500];

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int N;
  cin >> N;

  int A[N];
  int sum = 0;
  REP(i, N) {
      cin >> A[i];
      sum += A[i];
  }

  sort(A, A+N);
  if(sum % 2 == 1) {
      cout << "impossible" << endl;
      return 0;
  }

  dp[0] = 1;
  REP(i, N) {
      RREP(j, 10000) {
          if(dp[j]) {
              dp[j + A[i]] = 1;
          }
      }
  }

  cout << (dp[sum/2] ? "possible" : "impossible") << endl;
  return 0;
}
