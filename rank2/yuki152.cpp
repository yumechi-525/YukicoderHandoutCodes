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

int gcd(int a, int b) {
    int c = 0;
    if(a > b) {
        int t = a;
        a = b;
        b = a;
    }
    while(a != 0) {
        c = a;
        a = b%a;
        b = c;
    }
    return b;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int THISMOD = 1000003;
  int L;
  cin >> L;

  int res = 0;
  FOR(i, 1, (int)(sqrt(L/4)) + 1) {
      FOR(j, i+1, (int)(sqrt(L/4)) + 1) {
          int a = j*j - i*i;
          int b = 2*i*j;
          int c = j*j + i*i;
          if(a * a + b * b != c * c) continue;
          if( a + b + c <= L/4 ) {
              // cout << "A: " << a << " B: " << b << " C: " << c << endl;
              if(gcd(gcd(a, b), c) == 1) res++;
          }
      }
  }

  cout << res % THISMOD << endl;
  return 0;
}
