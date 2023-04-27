#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1
#define log(fmt,...) do { if (DEBUG) { printf("[%s():%d] " fmt "\n", __FUNCTION__, __LINE__, ##__VA_ARGS__); } } while (0)

int B, I;
vector<tuple<int,int,int,int>> boxes;
vector<tuple<int,int,int,int>> items;
vector<int> temp(3,0);
int a, b, c;

int main() {
    scanf("%d", &B);
    for (int i=0; i<B; i++) {
        scanf("%d %d %d", &a, &b, &c);
        temp[0] = a; temp[1] = b; temp[2] = c;
        sort(temp.begin(), temp.end());
        boxes.push_back(make_tuple(a*b*c, temp[0], temp[1], temp[2]));
    }
    scanf("%d", &I);
    sort(boxes.begin(), boxes.begin());
    for (int i=0; i<I; i++) {
        scanf("%d %d %d", &a, &b, &c);
        temp[0] = a; temp[1] = b; temp[2] = c;
        sort(temp.begin(), temp.end());
        bool flag = false;
        for (int b=0; b<B; b++) {
            if (get<1>(boxes[b]) >= temp[0] && get<2>(boxes[b]) >= temp[1] && get<3>(boxes[b]) >= temp[2]) {
                printf("%d\n", get<0>(boxes[b]));
                flag = true;
                break;
            }
        }
        if (!flag) {
            printf("Item does not fit.\n");
        }
    }
    // printf("lmao %d\n", B);
    return 0;
}
