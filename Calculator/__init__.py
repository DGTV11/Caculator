def cmdLS():
  print('''SqrRt(outprint) -- returns the square root of a number by N dimensions (outprint can only be 1 or 0!)
  \nONEoutofZERO -- tells you the value of 1/0''')

def SqrRt(outprint):
  N = int(input('What is your number of dimensions?'))
  C = int(input('What is the squared output (NO FLOAT NUMBERS!!)?'))
  Out = C / N
  if outprint == 1:
    print('Ans: %s'%Out)
  else:
    return Out

def ONEoutofZERO():
  print('Since 0/0 is the only fraction for 0, 1/0 isn\'t \nreal because it surpassed 0/0 (Which IS the only fraction of 0!) \nbut it can be defined as infinity')

