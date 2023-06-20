#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)
template <class T>
void print_v(vector<T> &v) { if (DEBUG) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; } }

#define int long long
#define INF 5e6

typedef vector<int> vi;
typedef vector<tuple<int,int>> vii;
typedef vector<vi> vvi;
typedef map<int,int> mii;

// vi A(big, 0);
// vvi G(big);
int T;

void solve() {
    printf("solution");
    return;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    scanf("%lld", &T);
    while (T--) {
        solve();
    }
    return 0;
}
