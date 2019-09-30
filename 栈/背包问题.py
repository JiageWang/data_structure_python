def knap_rec(weight, wlist, n):
    # 重量为0，说明问题有解
    if weight == 0:
        return True
    # 重量小于0，或是重量大于0但是n小于0说明无解
    elif weight < 0 or (weight > 0 and n < 1):
        return False
    # 不取n，判断是否有解
    elif knap_rec(weight, wlist, n - 1):
        return True
    # 取n，判断是否有解
    elif knap_rec(weight - wlist[n-1], wlist, n - 1):
        return True
    else:
        return False


print(knap_rec(7, [1, 2, 3, 5, 6], 5))
