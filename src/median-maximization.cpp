#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int t, n, s;

int ceil_div(int a, int b) {
    return (a + b - 1) / b;
}

int main() {
    scanf("%d", &t);
    int sum = 0;
    for (int i=0; i<t; i++) {
        scanf("%d %d", &n, &s);
        printf("%d\n", s / (n - ceil_div(n,2) + 1));
    }
    return 0;
}
