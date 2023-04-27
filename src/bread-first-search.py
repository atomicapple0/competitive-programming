from collections import defaultdict

def main():
    N,M = map(int, input().strip().split(" "))
    arr = [N+1 for _ in range(N)]
    adj = defaultdict(set)
    for i in range(M):
        u,v = map(int, input().strip().split(" "))
        adj[u-1].add(v-1)

    i = 1
    curr_dist = 1
    prev_dist = 0
    prev_idx = 0

    edges = []
    n_edges = 0
    for v in adj[0]:
        arr[v] = min(curr_dist,arr[v])

    cnt = defaultdict(int)

    # print(arr)
    arr[0] = 0
    for i in range(1,N):
        if arr[i] == N+1:
            # add edge from prev_idx to i
            arr[i] = curr_dist
            edges.append((prev_idx, i))
            n_edges += 1
        elif arr[i] == curr_dist:
            # noop
            pass
        elif arr[i] == curr_dist + 1:
            cccc = 0
            for j in range(i+1,N):
                if arr[j] > curr_dist:
                    break
                if arr[j] == curr_dist:
                    cccc += 1

            if cccc == 0:
                prev_dist = curr_dist
                curr_dist = curr_dist + 1
                prev_idx = i
            else:
                edges.append((prev_idx, i))
                n_edges += 1
                
        elif arr[i] < curr_dist:
            # add edge from prev_idx to i
            edges.append((prev_idx, i))
            n_edges += 1
        else:
            print("wtf")
            import pdb; pdb.set_trace()
        
        for v in adj[i]:
            arr[v] = min(curr_dist+1,arr[v])
        arr[i] = curr_dist
    #     print(arr)

    # print(edges)
    print(n_edges)
                
main()