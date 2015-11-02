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

  int N;
  cin >> N;

  int A[N];
  int B[N];
  REP(i, N) cin >> A[i];
  REP(i, N) cin >> B[i];

  int IDXS[N];
  REP(i, N) IDXS[i] = i;

  int sum = 0;
  int win = 0;
  do {
      int twin = 0;
      REP(i, N) {
          if(A[IDXS[i]] > B[i]) twin++;
      }
      if(twin > (N - twin)) win++;
      sum++;
  } while( next_permutation(IDXS, IDXS+N) );

  cout << (double) win / sum << endl;
  return 0;
}
