#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

vector<tuple<string,string>> same;
vector<tuple<string,string>> different;


int X,Y,G;
string a,b,c;
char buffer[1000];

unordered_map<string, int> dict;

int main() {
    scanf("%d", &X);
    for (int x=0; x<X; x++) {
        scanf("%s", buffer); a = buffer;
        scanf("%s", buffer); b = buffer;
        same.push_back(make_tuple(a,b));
    }
    scanf("%d", &Y);

    for (int y=0; y<Y; y++) {
        scanf("%s", buffer); a = buffer;
        scanf("%s", buffer); b = buffer;
        different.push_back(make_tuple(a,b));
    }
    
    scanf("%d", &G);
    for (int g=0; g<G; g++) {
        scanf("%s", buffer); a = buffer;
        scanf("%s", buffer); b = buffer;
        scanf("%s", buffer); c = buffer;
        dict[a] = g;
        dict[b] = g;
        dict[c] = g;
    }

    int count = 0;
    for (int x=0; x<X; x++) {
        a = get<0>(same[x]);
        b = get<1>(same[x]);
        if (dict[a] != dict[b]) {
            count++;
        }
    }
    for (int y=0; y<Y; y++) {
        a = get<0>(different[y]);
        b = get<1>(different[y]);
        if (dict[a] == dict[b]) {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}
