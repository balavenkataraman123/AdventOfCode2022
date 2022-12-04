prlist = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
prsum = 0
while True:   
    a = input("")
    if a == "exit":
        break
    b = input("")
    c = input("")

    for i in set(list(a)):
        if i in set(list(b)):
            if i in set(list(c)):
                prsum += (prlist.index(i) + 1)
print(prsum)