#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { prllf("[%s():%lld] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)
template <class T>
void prll_v(vector<T> &v) { if (DEBUG) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; } }
const ll INF=2e5+10;
typedef vector<ll> vi;
typedef vector<tuple<ll,ll>> vii;
typedef vector<vi> vvi;
typedef map<ll,ll> mii;
long big = 5e6;
ll T, N, M;
vvi G(big);
vi D(big, -1);
vi V(big);

// void bfs() {
//     queue<ll> q;
//     q.push(0);
//     D[0] = 0;
//     V[0] = 1;
//     while (!q.empty()) {
//         ll u = q.front();
//         q.pop();
//         for (auto v : G[u]) {
//             if (V[v]) continue;
//             V[v] = 1;
//             D[v] = D[u] + 1;
//             q.push(v);
//         }
//     }
//     return;
// }
ll modified = 0;
vi Memo(big, -1);
ll dfs(ll prev, ll curr) {
    // if (Memo[prev] != -1) return Memo[u];

    // V[prev] = 1;
    // modified++;
    Memo[curr] = 0;
    if (curr != 0 && G[curr].size() == 1) {
        Memo[curr] += 1;
    }
    for (auto v : G[curr]) {
        if (v != prev) {
            Memo[curr] += dfs(curr, v);
        }
    }
    // log("dfs(%lld) = %lld\n", u, Memo[curr]);
    return Memo[curr];
}

void solve() {
    scanf("%lld", &N);
    for (ll i = 0; i < N; i++) {
        G[i].clear();
        D[i] = -1;
        V[i] = 0;
        Memo[i] = -1;
    }
    for (ll i = 0; i < N-1; i++) {
        ll u, v;
        scanf("%lld %lld", &u, &v);
        u--; v--;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    scanf("%lld", &M);
    dfs(-1, 0);
    // for (ll i = 0; i < N; i++) {
    //     prllf("%i :", i);
    //     for (auto x : G[i]) {
    //         prllf("%lld ", x);
    //     }
    //     prllf("\n");
    // }
    // for (ll i = 0; i < N; i++) {
    //     prllf("| %lld ", D[i]);
    // }
    // log("ok");
    for (ll i = 0; i < M; i++) {
        ll u, v;
        scanf("%lld %lld", &u, &v);
        u--; v--;

        // ll scoreu;
        // if (Memo[u] != -1) {
        //     scoreu = Memo[u];
        // } else {
        //     for (ll i = 0; i < N; i++) {
        //         V[i] = 0;
        //     }
        //     scoreu = dfs(u);
        // }
        
        // ll scorev;
        // if (Memo[v] != -1) {
        //     scorev = Memo[v];
        // } else {
        //     for (ll i = 0; i < N; i++) {
        //         V[i] = 0;
        //     }
        //     scorev = dfs(v);
        // }
        printf("%lld\n", Memo[u] * Memo[v]);
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    scanf("%lld", &T);
    while (T--) {
        solve();
    }
    return 0;
}
