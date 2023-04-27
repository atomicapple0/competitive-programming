#include <bits/stdc++.h>
#include <algorithm>  
#include <string>  
#include <iostream>  
  
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int T, A, B, C;
int Memo[100000000];

int hash(int a, int b, int c) {
    if (b > c)
        swap(b, c)
    if (a > b)
        swap(a, b)
    return a + 
}

int main() {
    scanf("%d", &n);
    int sum = 0;

    string s = "abc";  
    sort(s.begin(), s.end());  
    do {  
        cout << s << '\n';  
    } while(next_permutation(s.begin(), s.end()));  
      
    printf("%d", sum);
    return 0;
}
