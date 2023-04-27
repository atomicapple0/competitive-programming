#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, t;
int x;
static int A[100000];

static int goal;
static int idx;
int bsearch(int lo, int hi, int (*f)(int)) {
  /* We know that f() is a monotonic function, namely that 
     if i < j then f(i) <= f(j)

     The goal is to find the smallest index i in the range [0,1000000]
     such that f(i) = 1.  If there is no index in that range with f(i)=1
     then return -1.
  */

  int m;
  if (f(hi) == 0) return -1;
  if (f(lo) == 1) return lo;
  /* Induction hypothesis at start of loop: 
     lo < hi and f(lo) = 0, f(hi) = 1 */
  while(lo + 1 < hi) {
    m = lo + (hi-lo)/2;
    /* alternative is (lo+hi)/2, but possible overflow */
    if (f(m) == 0) lo = m; else hi = m;
  }
  return hi;
}

int main() {
    scanf("%d %d", &n, &t);
    log("n=%d t=%d", n, t);
    int sum = 0;
    for (int i=0; i<n; i++) {
        scanf("%d", &x);
        sum += x;
        A[i] = sum;
        log("i=%d x=%d sum=%d", i, x, sum);
    }
    // for (int j=0; j<n; j++) {
    //     int jj = 3 + j;
    //     if (jj > n-1) {
    //         log("%d",A[jj % (n)] + A[n]);
    //     } else {
    //         log("%d", A[jj]);
    //     }
    // }
    int best = 0;
    for (int i=0; i<n; i++) {
        // binsearch right
        idx = i;
        int score = bsearch(0, n-1, [](int j) { 
            int jj = idx + j;
            int a_i = A[jj];
            if (jj < n) {
                a_i = A[jj] - A[idx];
            } else {
                a_i = A[n] - A[idx] + A[jj % (n)];
            }
            return a_i < t ? 0 : 1; 
        });
        log("i=%d A[i]=%d A[n]=%d goal=%d score=%d hmm=%d", i, A[i], A[n], goal, score, (score+i) % (n));
        if (score == -1) score = n;
        best = max(best, score);
    }
    printf("%d", best);
    return 0;
}
