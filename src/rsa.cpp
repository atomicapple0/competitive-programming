#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

#define M 10000000
int n;
int A[M];

int main() {
    scanf("%d", &n);
    
    for (int i=2; i<M; i++) {
        if (A[i] == 0) {
            // printf("prime: %d\n", i);
            for (int j=2*i; j<M; j+=i) {
                A[j] = 1;
            }
        }
    }

    for (int i=M-1; i>0; i--) {
        if (A[i] == 0 && n%i == 0) {
            printf("%d\n", i);
            return 0;
        }
    }

    return 0;
}
