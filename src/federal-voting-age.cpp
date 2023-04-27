#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int MONTH = 2;
int YEAR = 2007;
int DAY = 27;
int n, year, month, day;

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d %d %d", &year, &month, &day);
        log("year=%d month=%d day=%d", year, month, day);
        bool old = false;
        if (year + 18 < YEAR) {
            old = true;
            log("a");
        } else if (year + 18 == YEAR) {
            if (month < MONTH) {
                log("b");
                old = true;
            } else if (month == MONTH) {
                if (day <= DAY) {
                    log("c");
                    old = true;
                }
            }
        }
        if (old) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    return 0;
}
