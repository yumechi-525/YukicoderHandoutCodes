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
#define DDEBUG(x,y) cout<<#x<<": "<<x<<", "<<#y<<": "<<y<<endl
#define ll long long
#define ull unsigned long long
#define MOD 1000000007

int alphacount[26];
/* 
0 A
1 B
2 C
3 D
4 E
5 F
6 G
7 H
8 I
9 J
10 K
11 L
12 M
13 N
14 O
15 P
16 Q
17 R
18 S
19 T
20 U
21 V
22 W
23 X
24 Y
25 Z
*/

/*
helloworld
-> lとoのみ考える
*/
int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.precision(16);

	REP(i, 26)
		cin >> alphacount[i];

	ll res = 1;

	res *= alphacount[7]; // h
	res *= alphacount[4]; // e
	res *= alphacount[22]; // w
	res *= alphacount[17]; // r
	res *= alphacount[3]; // d

	ll omax = 1;
	FOR(i, 1, alphacount[14]) {
		omax = max(omax, (ll)i * (alphacount[14] - i));
	}
	if(alphacount[14] < 2) omax = 0;

	ll lmax = 1;
	FOR(i, 1, alphacount[11]-1) {
		int temp = (alphacount[11] - i) * (alphacount[11] - i - 1) / 2;
		lmax = max(lmax, (ll)i * temp);
	}
	if(alphacount[11] < 3) lmax = 0;

	// cout << "**RESULT**" << endl;
	res *= omax * lmax;
	cout << res << endl;
}
