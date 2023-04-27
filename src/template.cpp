#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, x;

int main() {
    scanf("%d", &n);
    int sum = 0;
    for (int i=0; i<n; i++) {
        scanf("%d", &x);
        log("x=%d", x);
        sum += x;
    }
    printf("%d", sum);
    return 0;
}
