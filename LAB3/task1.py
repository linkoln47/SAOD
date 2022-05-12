def func_prefix(s: str) -> list:
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l:
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]:
        elif i:         # i > 0
            i = P[i - 1]
        else:           # i == 0
            P[j] = 0
            j += 1
    return P
def kmp(text: str, sub: str) -> list:
    sub_len = len(sub)
    text_len = len(text)
    print(text_len, sub_len)
    if not text_len or sub_len > text_len:
        return []
    P = func_prefix(sub)
    print(">>>", P)
    entries = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        # text[i] 1= sub[j]
        elif j:     # j > 0
            j = P[j-1]
        else:
            i += 1
    return entries
if __name__ == '__main__':
    s = input("введите строку: ")
    sub = input("введите подстроку: ")
    Q = input("Различать регистр?(да\нет): ")
    if Q == "нет":
        s = s.lower()
        sub = sub.lower()
    P = kmp(s, sub)
    print(P)
    for i in P:
        print(s[i:i + len(sub)])