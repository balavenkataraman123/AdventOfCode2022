lttrq = []
dstr = list(input())
lttrq += dstr[:14]
offsetend = 14
print(lttrq)
for i in list(dstr[14:]):
    if not i in lttrq:
        if len(list(set(lttrq))) == len(lttrq):
            break
    lttrq.append(i)
    lttrq.pop(0)
    offsetend += 1


print(offsetend)
            

