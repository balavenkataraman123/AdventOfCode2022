callist = []
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
  callist.append(thiscal)
  if exiting == 1:
    break
callist.sort(reverse=True)
print(callist[0] + callist[1] + callist[2])
