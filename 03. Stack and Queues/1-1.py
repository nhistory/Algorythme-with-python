class Kstack:
  def __init__(self,arrayQuantity,arraySize):
    self.arrayQuantity = arrayQuantity
    self.arraySize = arraySize
    self.stackSize = int(self.arraySize/self.arrayQuantity)

    self.arr = [0]*self.arraySize
    self.top = [-1]*self.arrayQuantity

  def isEmpty(self, stackNumber):
    return self.arr[stackNumber*self.stackSize] == 0

  def isFull(self, stackNumber):
    return self.arr[(stackNumber+1)*self.stackSize-1] != 0

  def push(self, data, stackNumber):
    if self.isFull(stackNumber):
      print("stack overflow")
      return

    self.top[stackNumber] = self.top[stackNumber] + 1
    self.arr[self.stackSize*stackNumber+self.top[stackNumber]] = data

  def pop(self, stackNumber):
    if self.isEmpty(stackNumber):
      return None

    print(f'Popped element from stack {stackNumber} is {self.arr[self.stackSize*stackNumber+self.top[stackNumber]]}')
    self.arr[self.stackSize*stackNumber+self.top[stackNumber]] = 0
    self.top[stackNumber] = self.top[stackNumber] - 1
  

kstack = Kstack(3,15)

# # isEmpty()
# print(kstack.isEmpty(0))
# print(kstack.isEmpty(1))
# print(kstack.isEmpty(2))

# push()
kstack.push(10,0)
kstack.push(11,1)
kstack.push(21,1)
kstack.push(31,1)
kstack.push(12,2)
print(kstack.isEmpty(0))
print(kstack.isEmpty(1))
print(kstack.isEmpty(2))
print(kstack.arr)

# isFull()
kstack.push(20,0)
kstack.push(30,0)
kstack.push(40,0)
kstack.push(50,0)
kstack.push(60,0)
kstack.push(70,0)
print(kstack.arr)

kstack.pop(0)
print(kstack.arr)
kstack.pop(0)
print(kstack.arr)

