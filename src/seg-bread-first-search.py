from collections import defaultdict

def main():
    N,M = map(int, input().strip().split(" "))
    arr = [i for i in range(N+1)]
    adj = defaultdict(set)
    for i in range(M):
        u,v = map(int, input().strip().split(" "))
        u,v = min(u,v), max(u,v)
        arr[u] = max(arr[u],v)
        adj[u].add(v)
    print(arr)

    
                
main()