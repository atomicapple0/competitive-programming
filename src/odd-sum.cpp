#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int n, x, e, o;
int e_x, o_x;
int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &x);
        int ee = e + x;
        int oo = o + x;
        if (e_x) {
            if (ee % 2 == 0) {
                e = max(e,ee);
            } else {
                o = max(o,ee);
            }
        } else {
            if (x % 2 == 0 && o_x && oo % 2 == 0) {
                e = max(x, oo);
                e_x = 1;
            } else if (o_x && oo % 2 == 0) {
                e = oo;
                e_x = 1;
            } else if (x % 2 == 0) {
                e = x;
                e_x = 1;
            }
        }
        if (o_x) {
            if (oo % 2 == 0) {
                e = max(e,oo);
            } else {
                o = max(o,oo);
            }
        } else {
            if (x % 2 != 0 && e_x && ee % 2 != 0) {
                o = max(x, ee);
                o_x = 1;
            } else if (e_x && ee % 2 != 0) {
                o = ee;
                o_x = 1;
            } else if (x % 2 != 0) {
                o = x;
                o_x = 1;
            }
        }
        if (x % 2 == 0) {
            e = max(e,x);
        } else {
            o = max(o,x);
        }
        log("%d %d %d %d", e, o, ee, oo);
    }
    printf("%d\n",o);
    return 0;
}
