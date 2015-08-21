#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <cmath>

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

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  string s;
  cin >> s;
  int upcount = 0, leftcount = 0;
  for(char c : s) {
      switch(c) {
          case 'N':
            upcount++;
            break;
          case 'S':
            upcount--;
            break;
          case 'W':
            leftcount++;
            break;
          case 'E':
            leftcount--;
            break;
      }
  }

  cout << sqrt(pow(upcount, 2.0) + pow(leftcount, 2.0)) << endl;

  return 0;
}
