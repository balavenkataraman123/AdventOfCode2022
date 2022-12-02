score = 0
while True:
    a = input("")
    if a == "exit":
        break
    inp = a.split()
    firsts = ["A", "B", "C"]
    seconds = ["X", "Y", "Z"]
    points = [
        [0+3,0+1,0+2],
        [3+1,3+2,3+3],
        [6+2,6+3,6+1]
    ]
    e = inp[0]
    y = inp[1]
    score += points[seconds.index(y)][firsts.index(e)]    
print(score)