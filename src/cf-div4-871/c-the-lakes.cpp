#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)
template <class T>
void print_v(vector<T> &v) { if (DEBUG) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; } }
const int INF=2e5+10;
typedef vector<int> vi;
typedef vector<tuple<int,int>> vii;
typedef vector<vi> vvi;
typedef map<int,int> mii;


int T;

int A[1100][1100];
int V[1100][1100];

int w,h;

int dfs(int i, int j) {
    // printf("dfs(%d,%d)\n", i, j);
    if (i < 0 || i >= h || j < 0 || j>= w) {
        return 0;
    }
    if (V[i][j]) {
        return 0;
    }
    V[i][j] = 1;
    if (A[i][j] == 0) {
        return 0;
    }
    return A[i][j] + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1);

}

void solve() {
    scanf("%d %d", &h, &w);
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            scanf("%d", &A[i][j]);
            V[i][j] = 0;
        }
    }
    int best = 0;
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            best = max(best, dfs(i,j));
        }
    }
    printf("%d\n", best);
}

int main() {
    scanf("%d", &T);
    while (T--) {
        solve();
    }
    return 0;
}
