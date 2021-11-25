class KStacks:
	
	def __init__(self, arrayQuantity, arraySize):
		self.arrayQuantity = arrayQuantity 
		self.arraySize = arraySize 

		self.arr = [0] * self.arraySize
		self.top = [-1] * self.arrayQuantity

		self.free = 0

		self.next = [i + 1 for i in range(self.arraySize)]
		self.next[self.arraySize - 1] = -1

	# Check whether given stack is empty.
	def isEmpty(self, stackNumber):
		return self.top[stackNumber] == -1

	# Check whether there is space left for
	# pushing new elements or not.
	def isFull(self):
		return self.free == -1

	# Push 'item' onto given stack number 'sn'.
	def push(self, item, stackNumber):
		if self.isFull():
			print("Stack Overflow")
			return

		insert_at = self.free
		self.free = self.next[self.free]
		self.arr[insert_at] = item
		self.next[insert_at] = self.top[stackNumber]
		self.top[stackNumber] = insert_at

	# Pop item from given stack number 'sn'.
	def pop(self, stackNumber):
		if self.isEmpty(stackNumber):
			return None

		top_of_stack = self.top[stackNumber]
		self.top[stackNumber] = self.next[self.top[stackNumber]]
		self.next[top_of_stack] = self.free
		self.free = top_of_stack
		return self.arr[top_of_stack]

	def printstack(self, stackNumber):
		top_index = self.top[stackNumber]
		while (top_index != -1):
			print(self.arr[top_index])
			top_index = self.next[top_index]

# Driver Code
if __name__ == "__main__":
	
	# Create 3 stacks using an
	# array of size 10.
	kstacks = KStacks(3, 15)

# Push some items onto stack number 2.
kstacks.push(15, 2)
kstacks.push(45, 2)

# Push some items onto stack number 1.
kstacks.push(17, 1)
kstacks.push(49, 1)
kstacks.push(39, 1)

# Push some items onto stack number 0.
kstacks.push(11, 0)
kstacks.push(9, 0)
kstacks.push(7, 0)

print(kstacks.arr)
print(kstacks.next)
print(kstacks.top)
print(kstacks.free)

print("Popped element from stack 2 is " +
          str(kstacks.pop(2)))
print("Popped element from stack 1 is " +
          str(kstacks.pop(1)))
print("Popped element from stack 0 is " +
          str(kstacks.pop(0)))

kstacks.printstack(0)

print(kstacks.isEmpty(0))
print(kstacks.arr)
print(kstacks.next)
print(kstacks.top)
print(kstacks.free)
