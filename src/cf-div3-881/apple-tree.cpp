#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)
template <class T>
void print_v(vector<T> &v) { if (DEBUG) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; } }
const int INF=2e5+10;
typedef vector<int> vi;
typedef vector<tuple<int,int>> vii;
typedef vector<vi> vvi;
typedef map<int,int> mii;

long big = 5e6;
int T, N, M;
vvi G(big);
vi D(big, -1);
vi V(big);

void bfs() {
    queue<int> q;
    q.push(0);
    D[0] = 0;
    V[0] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto v : G[u]) {
            if (V[v]) continue;
            V[v] = 1;
            D[v] = D[u] + 1;
            q.push(v);
        }
    }
    return;
}
int modified = 0;
vi Memo(big, -1);
int dfs(int u) {
    if (Memo[u] != -1) return Memo[u];

    V[u] = 1;
    modified++;
    int ans = 0;
    if (u != 0 && G[u].size() == 1) {
        ans = 1;
    }
    for (auto v : G[u]) {
        if (D[v] > D[u]) {
            if (!V[v]) {
                ans += dfs(v);
            }
        }
    }
    Memo[u] = ans;
    log("dfs(%d) = %d\n", u, ans);
    return ans;
}

void solve() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        G[i].clear();
        D[i] = -1;
        V[i] = 0;
        Memo[i] = -1;
    }
    for (int i = 0; i < N-1; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    scanf("%d", &M);
    bfs();
    // for (int i = 0; i < N; i++) {
    //     printf("%i :", i);
    //     for (auto x : G[i]) {
    //         printf("%d ", x);
    //     }
    //     printf("\n");
    // }
    // for (int i = 0; i < N; i++) {
    //     printf("| %d ", D[i]);
    // }
    // log("ok");
    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--;

        int scoreu;
        if (Memo[u] != -1) {
            scoreu = Memo[u];
        } else {
            for (int i = 0; i < N; i++) {
                V[i] = 0;
            }
            scoreu = dfs(u);
        }
        
        int scorev;
        if (Memo[v] != -1) {
            scorev = Memo[v];
        } else {
            for (int i = 0; i < N; i++) {
                V[i] = 0;
            }
            scorev = dfs(v);
        }
        printf("%d\n", scoreu * scorev);
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    scanf("%d", &T);
    while (T--) {
        solve();
    }
    return 0;
}
