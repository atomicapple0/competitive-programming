#include <bits/stdc++.h>
#include <vector>

using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int m, n;
vector<int> X(100000);
vector<int> Y(100000);

int main() {
    scanf("%d", &m);
    for (int mm=0; mm<m; mm++) {
        scanf("%d", &n);
        log("%d", n);
        for (int i=0; i<n; i++) {
            scanf("%d", &X[i]);
        }
        for (int i=0; i<n; i++) {
            scanf("%d", &Y[i]);
        }
        int best = 0;
        int x = n-1;
        for (int y=n-1; y>=0; y--) {
            while (x>0 && Y[y]>=X[x-1]) {
                x--;
            }
            log("x=%d y=%d Y[y]=%d X[x]=%d", x, y, Y[y], X[x]);
            if (Y[y]>=X[x]) {
                best = max(best, y-x);
            }
        }
        printf("The maximum distance is %d\n", best);
    }
    return 0;
}
