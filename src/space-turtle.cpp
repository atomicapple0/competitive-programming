#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

struct pt {
    int x;
    int y;
};

int tx, ty, ttm;
int sx, sy, sm;
vector<pt> S;
vector<pt> T;

int delta;
char lr;

int main() {
    scanf("%d %d %d", &sx, &sy, &sm);
    for (int i=0; i<sm; i++) {
        scanf("%d %c", &delta, &lr);
        for (int j=0; j<abs(delta); j++) {
            if (lr == 'X') {
                sx += delta > 0 ? 1 : -1;
            } else {
                sy += delta > 0 ? 1 : -1;
            }
            S.push_back({sx, sy});
            log(" %d %d\n", sx, sy);
        }
    }
    scanf("%d %d %d", &tx, &ty, &ttm);
    for (int i=0; i<ttm; i++) {
        scanf("%d %c", &delta, &lr);
        for (int j=0; j<abs(delta); j++) {
            if (lr == 'X') {
                tx += delta > 0 ? 1 : -1;
            } else {
                ty += delta > 0 ? 1 : -1;
            }
            T.push_back({tx, ty});
            log(" %d %d", tx, ty);
        }
    }

    double close = 1e20;
    for (size_t i = 0; i < (S.size() * T.size()); i++) {
        int ii = i % S.size();
        int jj = i % T.size();
        double dist = hypot(S[ii].x - T[jj].x, S[ii].y - T[jj].y);
        // printf("%ld %.2lf\n", i, dist);
        close = min(close, dist);
    }
    printf("%.2lf\n", close);
    return 0;
}
