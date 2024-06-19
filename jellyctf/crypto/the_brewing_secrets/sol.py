def open_sesame(n):
    a = ['0' for i in range(n)]
    #FIFO stack
    b = []
    while len(b) < 2**n:
        if ''.join(a[-6:]) in b:
            while a.pop() == '1':
                b.remove(''.join(a[-6:]))
            a.append('1')
        else:
            b.append(''.join(a[-6:]))
            a.append('0')
    return ''.join(a[:-1])

print(open_sesame(6))
