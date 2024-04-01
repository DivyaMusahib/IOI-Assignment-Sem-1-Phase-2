def check ():

  a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
  x = input("Please enter your password: ")

  if x == P1 or x == P2 or x == P3:
    print("Password cannot be the same as your previous passwords")
  
  if len(x) >= 10:
    a += 1
  if a == 0:
    print("Password does not contain the minimum 10 characters")  
    
  for i in range (len(x)):
    if x[i] == "!" or x[i] == "@" or x[i] == "#" or x[i] == "$" or x[i] == "%" or x[i] == "&" or x[i] == "*" :
      b += 1
  if b < 2:
    print("Password does not contain the minimum 2 special characters")
    
  for i in range (len(x)):
    if x[i]>="A" and x[i]<="Z":
       c += 1
  if c < 2:
    print("Password does not contain the minimum 2 capital letters")

  for i in range (len(x) - 4):
    if x[i] == x[i + 1] == x[i + 2] == x[i + 3]:
      d += 1
  if d != 0:
    print("Password should not contain same character consecutively 4 times")
 
  for i in range (len(x)):
    if x[i] >= "a" and x[i] <= "z":
      e += 1   
  if e < 2:
    print("Password does not contain the minimum 2 small letters")

  for i in range(len(x)):
    if (x[i] <= "9" and x[i] >= "1") or x[i] == 0:
      f += 1
  if f < 2:
    print("Password does not contain the minimum 2 digits")


  if b >= 2 and c >= 2 and e >= 2 and f >= 2 and a != 0 and d == 0 and x != P1 and x != P2 and x != P3 :
    print("Password has been set")
  else:
    check()



username = input("Please enter your username: ")
P1 = input("Previous password 1: ")
P2 = input("Previous password 2: ")
P3 = input("Previous password 3: ")
check()