def swap_case(s):
    ans=[]
    for i in s:
        if i==i.upper():
            ans.append(i.lower())
        elif i==i.lower():
            ans.append(i.upper())
        else:
            ans.append(i)
    return "".join(ans)
