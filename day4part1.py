inputs = []

while True:   
    a = input("")
    if a == "exit":
        break
    inputs.append(a)


ans = 0
for a in inputs:
    [r1, r2] = [k.split("-") for k in a.split(",")]

    if int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[1]):
        ans += 1
    elif int(r1[0]) >= int(r2[0]) and int(r1[1]) <= int(r2[1]):
        ans += 1   
print(ans)