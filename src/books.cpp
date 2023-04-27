#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, t;
int x;
static int A[100000];

int main() {
    scanf("%d %d", &n, &t);
    for (int i=0; i<n; i++) {
        scanf("%d", &x);
        A[i] = x;
    }
    int best = 0;
    int rangesum = 0;
    int r = 0;
    for (int l=0; l<n; l++) {
        while (r < n && rangesum <= t) {
            if (rangesum <= t) best = max(best, r-l);
            rangesum += A[r];
            r++;
        }
        if (rangesum <= t) best = max(best, r-l);
        // printf("%d %d %d %d\n", l, r, rangesum, A[r]);
        rangesum -= A[l];
    }
    printf("%d\n", best);
    
    return 0;
}
