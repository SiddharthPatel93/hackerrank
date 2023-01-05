def palindromeIndex(s):
    print(s)
    lastindex = len(s) -1
    for i in range(0,len(s)):
        if i == lastindex:
            return -1
        if lastindex - i == 1:
            if s[i]==s[lastindex]:
                return -1
            else:
                return i
        if s[i] == s[lastindex]:
            #remove both ends
            lastindex-=1
            continue
            #try removing the last letter if first and 2nd last letter match
        if s[i]==s[lastindex -1]:
                newstring = s[i:lastindex]
                val = palindromeIndex(newstring)
                if val == -1:
                    return lastindex
        if s[i+1]==s[lastindex]:
                newstring2= s[i+1:lastindex+1]
                val = palindromeIndex(newstring2)
                if val ==-1:
                    return i
        else:
            return -1
                
                



print(palindromeIndex(s='quyjjdcgsvvsgcdjjyq'))
#print(palindromeIndex(s='yjjdcgsvvsgcdjjy')) #1
print(palindromeIndex(s='hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh'))
print(palindromeIndex(s='wcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnw'))
print(palindromeIndex(s='fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf'))
print(palindromeIndex(s='cggc'))
print(palindromeIndex(s='bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb'))
print(palindromeIndex(s='pcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcp'))
print(palindromeIndex(s='fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf'))
print(palindromeIndex(s='isappmunmnldmkttkmdlnmnumppasi'))
print(palindromeIndex(s='mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm'))
print(palindromeIndex(s='bvlqpixvvxipqlvb'))
print(palindromeIndex(s='tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt'))
print(palindromeIndex(s='olmevkasccsakvemlo'))
print(palindromeIndex(s='lhrxvssvxrhl'))
print(palindromeIndex(s='prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp'))
print(palindromeIndex(s='oalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlao'))
print(palindromeIndex(s='kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk'))