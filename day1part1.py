maxcal = 0
while True:
  exiting = 0 
  thiscal = 0
  while True:
    a = input("")
    if a == "exit":
      exiting = 1
      break
    try:
      thiscal += int(a)
    except:
      break
  if thiscal > maxcal:
    maxcal = thiscal
  if exiting == 1:
    break
print(maxcal)
