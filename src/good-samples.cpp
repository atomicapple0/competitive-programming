#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

long long N, M, K;
vector<long long> X(1000000);

int main() {
    scanf("%lld %lld %lld", &N, &M, &K);
    M = min(M,N);
    long long rem = K;
    long long m;
    for (m=0; m<M; m++) {
        long long diff = N-m;
        if (rem >= diff) {
            rem -= diff;
        } else {
            break;
        }
    }

    log("m=%lld rem=%lld", m, rem);

    if (m==0 || (rem>0 && m==M)) {
        printf("-1\n");
        return 0;
    }

    for (long long i=0; i<N; i++) {
        X[i] = i % M + 1;
    }
    for (long long i=rem+m; i<N; i++) {
        log("X[%lld] (%lld) = X[%lld] (%lld)", i, X[i], i-m, X[i-m]);
        X[i] = X[i-m];
    }
    rem = 0;
    m = m+1;
    if (m < M) {
        for (long long i=rem+m; i<N; i++) {
            log("X[%lld] (%lld) = X[%lld] (%lld)", i, X[i], i-m, X[i-m]);
            X[i] = X[i-m];
        }
    }

    for (long long i=0; i<N-1; i++) {
        printf("%lld ", X[i]);
    }
    printf("%lld\n", X[N-1]);
    
    return 0;
}
