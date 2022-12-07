import copy
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
    
    tl = copy.deepcopy(stacks[s][-n:])
    stacks[s] = copy.deepcopy(stacks[s][:-n])
    stacks[e] += tl
    #print(stacks)   

for i in stacks[1:]:
    print(i[-1])

# LBLVVTVLP
