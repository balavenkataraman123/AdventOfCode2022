prlist = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
prsum = 0
while True:   
    a = input("")
    if a == "exit":
        break
    fstr = a[:int(len(a)/2)]
    sstr = a[int(len(a)/2):]
    for i in set(list(fstr)):
        if i in set(list(sstr)):
            prsum += (prlist.index(i) + 1)
print(prsum)