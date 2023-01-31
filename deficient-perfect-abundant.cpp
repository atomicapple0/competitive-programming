#include <bits/stdc++.h>
using namespace std;

int n, x;

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &x);
        int sum = 0;
        for (int j=1; j<=((int)sqrt(x)); j++) {
            if (x%j == 0) {
                sum += j;
                if (j != x/j && j != 1) {
                    sum += x/j;
                }
            }
        }
        if (sum == x) {
            printf("%d is a perfect number.\n", x);
        } else if (sum < x) {
            printf("%d is a deficient number.\n", x);
        } else {
            printf("%d is an abundant number.\n", x);
        }
    }
    return 0;
}
