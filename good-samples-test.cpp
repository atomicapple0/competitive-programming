#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int N, M, K;
vector<int> X(1000000);

int main() {
    
    for (int N=1; N<=16; N++) {
    for (int K=1; K<=100; K++) {
    
    M = 2;
    int rem = K;
    int m;
    for (m=0; m<M; m++) {
        int diff = N-m;
        if (rem >= diff) {
            rem -= diff;
        } else {
            break;
        }
    }


    if (m==0 || (rem>0 && m==M)) {
        log("N=%d K=%d m=%d rem=%d no solution", N, K, m, rem);
        continue;
    }
    log("N=%d K=%d m=%d rem=%d", N, K, m, rem);

    for (int i=0; i<N; i++) {
        X[i] = i % K + 1;
    }
    for (int i=rem+m; i<N; i++) {
        // log("X[%d] (%d) = X[%d] (%d)", i, X[i], i-m, X[i-m]);
        X[i] = X[i-m];
    }

    int count = N;
    for (int i=1; i<N; i++) {
        if (X[i] != X[i-1]) {
            count++;
        }
    }
    if (count != K) {
        printf("found one!! %d <> %d\n", count, K);
        for (int i=0; i<N; i++) {
            printf("%d ", X[i]);
        }
        printf("\n");
        return 0;
    }
    
    }
    }
    return 0;
}
