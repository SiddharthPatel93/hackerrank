def superDigit(n, k):
    intval = int(n)
    total=0
    if intval<10:
        return intval
    else:
        res = [int(x) for x in str(n)]

        for x in res:
            total+=x
        total=total*k
        if total >10:
            stotal=str(total)
            return superDigit(stotal,1)
        else:
            return total

print(superDigit(148,3))
print(superDigit(9875,4))
print(superDigit(123,3))