#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int count;
int N, C;
int x;
unordered_map<int, int> dict;

int main() {
    scanf("%d %d", &N, &C);
    for (int c=0; c<C; c++) {
        scanf("%d", &x);
        dict[x]++;
    }

    



    printf("%d", count);
    return 0;
}
