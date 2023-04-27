def main():
    N = int(input().strip())

    for _ in range(N):
        M = int(input().strip())
        scores = []
        for i in range(M):
            inscore = input().strip()
            l,r = map(int,inscore.split("-"))
            scores.append((max(l,r),min(l,r)))
        scores.sort()
        matches = []
        for l,r in scores:
            ok = False
            for match in matches:
                ll,rr = match[-1]
                if l >= ll and r >= rr:
                    match.append((l,r))
                    ok = True
                    break
            if not ok:
                matches.append([(l,r)])
        print(len(matches))
        for match in matches:
            for l,r in match:
                print(f"{l}-{r}", end=" ")
            print()
main()