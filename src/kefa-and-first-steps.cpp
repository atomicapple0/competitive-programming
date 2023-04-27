#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

ll n, x;
int main() {
    scanf("%lld", &n);
    ll inc = 0;
    ll big = 0;
    ll last = 0;
    for (ll i=0; i<n; i++) {
        scanf("%lld", &x);
        log("%lld %lld %lld\n", last, big, inc);
        if (last <= x) {
            last = x;
            inc++;
        } else {
            last = x;
            big = max(big, inc);
            inc = 1;
        }
    }
    big = max(big, inc);
    printf("%lld\n",big);
    return 0;
}
