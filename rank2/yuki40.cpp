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
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define RFOR(i, a, b) for (int i = (b)-1; i >= (a); i--)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define RREP(i, n) for (int i = (n)-1; i >= 0; i--)
#define INF 1 << 30
#define ALEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
#define MP make_pair
#define mp make_pair
#define pb push_back
#define PB push_back
#define DEBUG(x) cout << #x << ": " << x << endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int main() {
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int d;
  cin >> d;

  int array[d + 1];
  REP(i, d + 1) cin >> array[i];

  RFOR(i, 3, d + 1) {
    if (array[i] != 0) {
      array[i - 2] += array[i];
      array[i] = 0;
    }
  }

  int digit = 0;
  RFOR(i, 0, 3) {
    if (array[i] != 0) {
      digit = i;
      break;
    }
  }

  cout << digit << endl;
  if (digit == 2) {
    cout << array[0] << " " << array[1] << " " << array[2] << endl;
  } else if (digit == 1) {
    cout << array[0] << " " << array[1] << endl;
  } else {
    cout << array[0] << endl;
  }

  return 0;
}
