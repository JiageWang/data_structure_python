def strstr(s, t):
    """
    时间复杂度：O(m+n)
    """
    m, n = len(s), len(t)
    table = prefix_table(t)
    i, j = 0, 0
    ll = []
    while i < m:
        if s[i] == t[j]:
            if j == n - 1:
                return i-j
            else:
                i += 1
                j += 1
        else:
            j = table[j]
            if j == -1:
                i += 1
                j += 1
    return ll


def prefix_table(t):
    """
    模式串：A, B, A, B, C, A, B, A, A
    字串                          最长前后缀
    字串0：                        =>-1
    字串1： A                      => 0
    字串2： A, B                   => 0
    字串3： A, B, A                => 1
    字串4： A, B, A, B             => 2
    字串5： A, B, A, B, C          => 0
    字串6： A, B, A, B, C, A       => 1
    字串7： A, B, A, B, C, A, B    => 2
    字串8： A, B, A, B, C, A, B, A => 3
    复杂度：O(n)
    """
    n = len(t)
    prefix = [0] * n  # 最长前缀表
    prefix[0] = -1  # 首位设为-1
    _len = 0
    i = 2
    while i < n:
        if t[i - 1] == t[_len]:  # 比较的是字串，需-1
            # 匹配成功最长前后缀增加1
            _len += 1
            prefix[i] = _len
            i += 1
        elif _len > 0:
            # 匹配失败并且之前最长前后缀不为0 ==>   继续匹配当前字符
            _len = prefix[_len - 1]
        else:
            # 匹配失败并且之前最长前后缀为0   ==>   跳到下一个字符
            i += 1

    return prefix


print(prefix_table('aabaabaaa'))
print(prefix_table('ababcabaa'))
print(strstr('adfsasdfa', 'fa'))
