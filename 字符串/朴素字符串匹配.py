def strstr(s, t):
    """
    时间复杂度O(m*n)
    """
    pos = -1
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i+j] != t[j]:
                break
        else:
            pos = i
            break
    return pos


print(strstr('asdfasfd', 'sf'))

