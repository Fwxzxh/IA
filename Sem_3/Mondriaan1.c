#include <iostream.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
using namespace std;

int read() {
	int x = 0, f = 1; char c = getchar();
	while(!isdigit(c)){ if(c == '-') f = -1; c = getchar(); }
	while(isdigit(c)){ x = x * 10 + c - '0'; c = getchar(); }
	return x * f;
}

#define maxn 15
#define maxs 2048
#define LL long long

int n, m;
LL f[maxn][maxn][maxs];

int main() {
	while(1) {
		n = read(); m = read();
		if(!n && !m) break;

		memset(f, 0, sizeof(f));
		int all = (1 << m) - 1;
		f[1][1][all] = 1;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				for(int S = 0; S <= all; S++) if(f[i][j][S]) {
					if(S & 1) {
						if(j < m) f[i][j+1][S>>1] += f[i][j][S];
						else f[i+1][1][S>>1] += f[i][j][S];
					}
					if(!(S & 1)) {
						if(j < m) f[i][j+1][S>>1|(1<<m-1)] += f[i][j][S];
						else f[i+1][1][S>>1|(1<<m-1)] += f[i][j][S];
					}
					if(j > 1 && !(S >> m - 1 & 1) && (S & 1)) {
						if(j < m) f[i][j+1][S>>1|(1<<m-1)|(1<<m-2)] += f[i][j][S];
						else f[i+1][1][S>>1|(1<<m-1)|(1<<m-2)] += f[i][j][S];
					}
				}
		printf("%lld\n", f[n+1][1][all]);
	}
	return 0;
