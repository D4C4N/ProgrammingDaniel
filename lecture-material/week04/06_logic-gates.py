def AND(a,b):
  if a == 1 and b == 1:
    return 1
  else:
    return 0

def OR(a,b):
  if a == 1 or b == 1:
    return 1
  else:
    return 0

def NOT(a):
  if a == 1:
    return 0
  else:
    return 1

def NAND(a,b):
  if a == 1 and b == 1:
    return 0
  else:
    return 1

def NOR(a,b):
  if a == 0 and b == 0:
    return 1
  else:
    return 0

def XOR(a,b):
  if a != b:
    return 1
  else:
    return 0
  
def XNOR(a,b):
  if a == b:
    return 1
  else:
    return 0

print("AND")
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
print("OR")
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))
print("NOT")
print(NOT(0))
print(NOT(1))
print("NAND")
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))
print("NOR")
print(NOR(0,0))
print(NOR(0,1))
print(NOR(1,0))
print(NOR(1,1))
print("XOR")
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))
print("XNOR")
print(XNOR(0,0))
print(XNOR(0,1))
print(XNOR(1,0))
print(XNOR(1,1))