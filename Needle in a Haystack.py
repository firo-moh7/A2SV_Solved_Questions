
T = int(input())
for _ in range(T):
    s = input().strip()
    t = input().strip()

    from collections import Counter

    cnt_t = Counter(t)
    cnt_s = Counter(s)

    # Check feasibility
    possible = True
    for ch in cnt_s:
        if cnt_s[ch] > cnt_t[ch]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue

    # Remove s characters from t
    for ch in s:
        cnt_t[ch] -= 1

    # Build remaining characters string
    remaining = []
    for ch in sorted(cnt_t.keys()):
        remaining.append(ch * cnt_t[ch])
    remaining = ''.join(remaining)

    first = s[0]

    # Option 1: put chars == first before s
   
    if s < "".join(sorted(s)):
        i = 0
        while i < len(remaining) and remaining[i] <= first:
            i += 1
    else:
        # Option 2: put chars == first after s
        i = 0
        while i < len(remaining) and remaining[i] < first:
            i += 1
    res = remaining[:i] + s + remaining[i:]

    # Print best
    print(res)


