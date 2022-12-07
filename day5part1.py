stacks = [list(reversed(i)) for i in [ [],  list('JFCNDBW'), list("TSLQVZP"), list("TJGBZP"), list("CHBZJLTD"), list("SJBVG"), list("QSP"), list("NPMLFDVB"), list("RLDBFMSP"), list("RTDV")]]
#stacks = [list(reversed(i)) for i in [[], ["N", "Z"],["D","C","M"],["P"]]]
while True:
    inp = input("")
    if inp == "exit":

        break
    a = inp.split()
    n = int(a[1])
    s = int(a[3])
    e = int(a[5])
    for i in range(n):
        c = stacks[s][-1]
        stacks[s].pop()
        stacks[e].append(c)

for i in stacks[1:]:
    print(i[-1])

# LBLVVTVLP
