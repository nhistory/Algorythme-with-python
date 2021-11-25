class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.tops = [-1]
        self.topIndex = 0
        if capacity < 1:
            raise NameError("Can't have stacks of that height")
        else:
            self.capacity = capacity

    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])
            self.tops[-1] += 1
        else:
            filteredTops = [i for i, value in enumerate(self.tops) if value < self.capacity - 1]
            if filteredTops == []:
                self.topIndex = 0
            else:
                self.topIndex = filteredTops[0]
            if len(self.stacks[self.topIndex]) < self.capacity:
                self.stacks[self.topIndex].append(item)
                self.tops[self.topIndex] += 1
            else:
                if len(self.stacks[-1]) >= self.capacity:
                    self.stacks.append([item])
                    self.tops.append(0)
                else:
                    self.stacks[-1].append(item)
                    self.tops[-1] += 1

    def pop(self):
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        else:
            popped_data = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popped_data

    def popAt(self, index):
        if self.stacks == []:
            raise NameError("Can't pop an empty stack")
        elif index+1 > len(self.stacks):
            raise NameError("Index is out of range")
        else:
            popped_data = self.stacks[index][-1]
            if len(self.stacks[index]) == 1:
                self.tops[index] -= 1
                del self.stacks[index]
            elif len(self.stacks) == index+1:
                self.tops[index] -= 1
                del self.stacks[-1][-1]
            else:
                self.tops[index] -= 1
                self.topIndex = index
                del self.stacks[index][-1]
            return popped_data

x = SetOfStacks(3)
x.push(1)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(2)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(3)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(4)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(5)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(6)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(7)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(8)
print(x.stacks)
print(x.tops)
print(x.topIndex)

# x.pop()
# print(x.stacks)
# x.pop()
# print(x.stacks)
# x.pop()
# print(x.stacks)

x.popAt(1)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.popAt(1)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.popAt(0)
print(x.stacks)
print(x.tops)
print(x.topIndex)

x.push(20)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(30)
print(x.stacks)
print(x.tops)
print(x.topIndex)
x.push(40)
print(x.stacks)
print(x.tops)
print(x.topIndex)