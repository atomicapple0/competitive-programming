#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

char C[100];
char T[100];

int main() {
    scanf("%s\n%s", C, T);
    if (C[0] == T[0]) {
        printf("%s\n", C);
    } else {
        printf("Undecided\n");
    }
    return 0;
}
