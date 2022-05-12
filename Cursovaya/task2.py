for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    maxSmb = 'z' if 97 + k > 122 else chr(97 + k)
    smb = 'a'
    lastSmb = 'a'
    for elm in s:
        if ord(elm) > ord(maxSmb):
            lastSmb = elm
            break
        if ord(smb) < ord(elm):
            smb = elm

    for ordSmb in range(ord(smb), ord('a'), -1):
        s = s.replace(chr(ordSmb), 'a')
        k -= 1

    newSmb = 97 if ord(lastSmb) - k < 97 else ord(lastSmb) - k
    for ordSmb in range(ord(lastSmb), newSmb, -1):
        s = s.replace(chr(ordSmb), chr(newSmb))

    print(s)