lttrq = []
dstr = list(input())
lttrq += dstr[:4]
offsetend = 4
print(lttrq)
for i in list(dstr[4:]):
    if not i in lttrq:
        if len(list(set(lttrq))) == len(lttrq):
            break
    lttrq.append(i)
    lttrq.pop(0)
    offsetend += 1


print(offsetend)
            

