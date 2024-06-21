
def solve(eqs_a, mod):
    eqs = eqs_a
    for i in range(len(eqs)):
        factor = (-pow(eqs[i][i], -1, mod)) % mod
        eqs[i] = [(j*factor) % mod for j in eqs[i]]
        for j in range(i+1, len(eqs)):
            factor = eqs[j][i]
            eqs[j] = [(eqs[j][k]+(factor*eqs[i][k])) % mod for k in range(len(eqs[j]))]
    eqs.append(1)
    for i in range(len(eqs)-2, -1, -1):
        first = eqs[i][i+1:]
        second = eqs[i+1:]
        thing = 0
        for j in range(len(first)):
            thing += first[j]*second[j]
        thing %= mod
        eqs[i] = thing
    return eqs

# tests
test = [[4, 1, 3, 0], [4, 4, 1, 0], [2, 4, 3, 1]]
assert solve(test, 5) == [1, 2, 3, 1]

# actual stuff
awascii32 = 'awjelyhosiumpcntbdfgr.,!{}_/;CTF'
slotIndices = [[10992, 30978, 12520], [30983,  7390,   481], [25974, 26744,  9122]]
slotSpins = [[ 19,  22,  19], [ 32,  27,  29], [347, 349, 353]]
mod = 32768

# need to be careful because 22 and 32 are even and can't be inverse modulo mod 2^15
things = []
for i in slotIndices:
    a = [j[0] for j in slotSpins]
    a.append(i[0])
    b = [j[1] for j in slotSpins]
    b.append(i[1])
    c = [j[2] for j in slotSpins]
    c.append(i[2])
    things.append(solve([a, b, c], mod))
values = []
for i in things:
    for j in range(3):
        z = i[j]
        for k in range(3):
            values.append(z % 32)
            z >>= 5
print(''.join([awascii32[i] for i in values]))
