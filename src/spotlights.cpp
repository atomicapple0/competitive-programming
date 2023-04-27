#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

typedef vector<int> vi;
typedef vector<vi> vvi;

int n, m, x;
vvi A(1100, vi(1100));


int main() {
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            scanf("%d", &x);
            A[i][j] = x;
        }
    }
    int tot = 0;
    for (int i=0; i<n; i++) {
        int cnt = 0;
        int saw = 0;
        for (int j=0; j<m; j++) {
            if (A[i][j] == 0) {
                cnt++;
            } else {
                tot += cnt;
                log("%d %d %d", i, j, cnt);
                if (saw) {
                log("%d %d %d", i, j, cnt);
                    tot += cnt;
                }
                cnt = 0;
                saw = 1;
            }
        }
        if (saw) {
            tot += cnt;
        }
    }
    log("-----\n");
    for (int i=0; i<m; i++) {
        int cnt = 0;
        int saw = 0;
        for (int j=0; j<n; j++) {
            if (A[j][i] == 0) {
                cnt++;
            } else {
                log("%d %d %d", j, i, cnt);
                tot += cnt;
                if (saw) {
                log("%d %d %d", j, i, cnt);
                    tot += cnt;
                }
                cnt = 0;
                saw = 1;
            }
        }
        if (saw) {
            tot += cnt;
        }
    }
    printf("%d\n",tot);

    return 0;
}
