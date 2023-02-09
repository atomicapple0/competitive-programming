#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, v, x;

int main() {
    scanf("%d %d", &n, &v);
    int curr = 0;
    int cost = 0;
    for (int i=1; i<=n; i++) {
        if (curr < n-i) {
            int need = n-i - curr;
            int can_buy = v - curr;
            int buy = min(need, can_buy);
            curr += buy;
            cost += buy * i;
        }
        log("%d %d\n", curr, cost);
        curr--;
    }
    printf("%d", cost);
    return 0;
}
