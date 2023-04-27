#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

typedef long long ll;
ll t, n, x, a;
vector<int> A(100000);


int main() {
    scanf("%lld", &t);
    for (ll i=0; i<t; i++) {
        A.clear();
        scanf("%lld %lld", &n, &x);
        // log("%d %d", n, x);
        for (ll j=0; j<n; j++) {
            scanf("%lld", &a);
            A.push_back(a);
        }
        sort(A.begin(), A.end());
        ll sum = 0;
        ll prefix = 0;
        for (ll s=0; s<n; s++) {
            prefix += A[s];
            // if (x - prefix >= 0) {
            sum += max(0ll, (x - prefix) / (s+1) + 1);
            // }
        }
        printf("%lld\n", sum);
    }
    return 0;
}
