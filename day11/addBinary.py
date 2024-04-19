def addBinary(self, a, b):
    s= []
    a_index = len(a) - 1
    b_index = len(b) - 1
    carry = 0
    while a_index >= 0 or b_index >= 0 or carry == 1:
        if (a_index >= 0):
            carry += int(a[a_index])
            a_index -= 1
        if (b_index >= 0):
            carry += int(b[b_index])
            b_index -= 1
        s.append(str(carry % 2))
        carry = carry // 2
    return "".join(s[::-1])