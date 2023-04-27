#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int a;

int main() {
    scanf("%d", &a);
    int ans = 0;
    for (int bins=a/5; bins<=a/4; bins++) {
        int balls = a - 4*bins;
        log("bins=%d balls=%d", bins, balls);
        if (balls <= bins) {
            ans += 1;
        }
    }
    printf("%d\n", ans);
    return 0;
}
