def spl(s):
    if len(s)%2 == 0:
        return [s[:len(s)//2], s[len(s)//2:]]
    return [s[:len(s)//2 + 1], s[len(s)//2+1:]]
def get_str(s1, s2):
    s = spl(s1)
    ss = spl(s2)
    return s[0] + ss[0] + s[1] + ss[1]
    
print(get_str("abced", "joseph"))