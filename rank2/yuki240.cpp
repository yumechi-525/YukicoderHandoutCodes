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

int mx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
int my[] = {-1, 1, -2, 2, -2, 2, -1, 1};

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
  cout.precision(16);

  int X, Y;
  cin >> X >> Y;

  queue< pair< pair<int, int>, int> > que;
  pair<int, int> p = mp(0, 0);
  que.push(mp(p, 0));
  while(!que.empty()) {
      pair<int, int> current = que.front().first;
      int count = que.front().second;
      que.pop();

      if(count >= 3) continue;
      REP(i, 8) {
          int nx = current.first + mx[i];
          int ny = current.second + my[i];
          if(nx == X && ny == Y) {
              cout << "YES" << endl;
              return 0;
          }

          if(count <= 2) {
              pair<int, int> nextpoint = mp(nx, ny);
              que.push(mp(nextpoint, count + 1));
          }
      }
  }

  cout << "NO" << endl;
  return 0;
}
