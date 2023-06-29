#while:
if True:
  print('se ejecutó')

stop = False
while stop:
  print('hasta el fin')
  stop = True

counter = 0
while counter < 10:
  print('counter:', counter)
  counter += 1

counter2 = 0
while counter2 < 10:
  counter2 +=1
  if counter2 == 8:
    break
  print(counter2)

counter3 = 0
while counter3 < 20:
  counter3 += 1
  if counter3 < 15:
    continue
  print(counter3) #while counter3 <15 no execute


  