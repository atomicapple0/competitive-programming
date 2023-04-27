#include <bits/stdc++.h>
using namespace std;

#define DEBUG 0
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

char ch;
int n, m, pt, cnt;

typedef struct letter {
    int pt;
    int cnt;
    int idx;
    int used;
} letter_t;

letter_t L[1000];
map<char,letter> M;

int main() {
    scanf("%d\n", &n);
    log("n is %d", n);
    for (int i=0; i<n; i++) {
        scanf("%c %d %d\n", &ch, &pt, &cnt);
        log(" | %c %d %d |", ch, pt, cnt);
        M.insert({ch,{pt, cnt, 0, 0}});
    }
    scanf("%d", &m);
    int best = 0;
    char word[1000000];
    log("m is %d", m);
    for (int i=0; i<m; i++) {
        scanf("%s\n", word);
        int j=0;
        int ok=1;
        int score=0;
        log("new word!\n");
        while (word[j] != '\0') {
            ch = word[j];
            log("%c", word[j]);
            if (M[ch].idx != i) {
                M[ch].idx = i;
                M[ch].used = 0;
            }
            M[ch].used++;
            if (M[ch].used > M[ch].cnt) {
                ok=0;
                break;
            }
            score += M[ch].pt;
            j++;
        }
        if (ok) {
            log("ok and %d\n", score);
            best = max(best,score);
        }
    }
    printf("%d\n", best);
    return 0;
}