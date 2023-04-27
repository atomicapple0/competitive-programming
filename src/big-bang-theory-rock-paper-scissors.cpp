#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, na, nb, x;

int NA[1000];
int NB[1000];

int A[5][5] = {
    {0,-1,1,1,-1},
    {1,0,-1,1,-1},
    {-1,1,0,-1,1},
    {-1,-1,1,0,1},
    {1,1,-1,-1,0},
};

int main() {
    scanf("%d %d %d", &n, &na, &nb);
    int sum = 0;
    for (int i=0; i<na; i++) {
        scanf("%d", &x);
        NA[i] = x;
    }
    for (int i=0; i<nb; i++) {
        scanf("%d", &x);
        NB[i] = x;
    }
    int fa = 0;
    int fb = 0;
    for (int i=0; i<n; i++) {
        int a = i % na;
        int b = i % nb;
        int r = A[NA[a]][NB[b]];
        log(" %d %d   %d %d -> %d", a,b, NA[a], NB[b], r);
        if (r == 1) {
            fa++;
        } else if (r == -1) {
            fb++;
        }
    }
    printf("%d %d", fa, fb);
    return 0;
}
