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

  int x1, y1;
  int x2, y2;

  cin >> x1 >> y1;
  cin >> x2 >> y2;
  x2 = -x2;

  // y - y1 = ((y2 - y1) / (x2 - x1)) * (x - x1)
  // y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
  // need intercept -> ((y2 - y1) / (x2 - x1)) * (-x1) + y1
  cout << ((double)(y2 - y1) / (x2 - x1)) * (-x1) + y1 << endl;

  return 0;
}
