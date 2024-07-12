# QUEUE IMPLEMENTATION
# DO NOT MODIFY

class Queue(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.queue = list

#     def get_list(self):
#         return self.queue

    def size(self):
        return len(self.queue)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def tail(self):
        return self.queue[-1]

    def deq(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enq(self, data=None):
        self.queue.append(data)

    def print(self):
        print(self.queue)

    def __str__(self):
        return self.queue.__str__()

    def __repr__(self):
        return self.queue.__repr__()

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.queue == other.queue
        return False

# def main():
#     q = Queue()
#     q.print()
#     print("Is empty?", q.is_empty())
#     for i in range(1, 7):
#         q.enq(i)
#     print("Front:   ", q.front())
#     print("Deq:     ", q.deq())
#     q.print()
#     print("Is empty?", q.is_empty())

# # Don't run main on import
# if __name__ == "__main__":
#     main()

class Stack(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.stack = list

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, data=None):
        self.stack.append(data)

    def print(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack.__str__()

    def __repr__(self):
        return self.stack.__repr__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.stack == other.stack
        return False


def flip(stack):
  newStack = Stack()
  while not stack.is_empty():
    newStack.push(stack.pop())
  return newStack

# flip(Stack([1,2,3,4])).print()


def count_uniq(queue):
  uniques = 0
  
  while not queue.is_empty():
    # Can also write while !queue.is_empty()
    lastValue = queue.deq()
    if lastValue != queue.front():
      uniques += 1
  return uniques

# print(count_uniq(Queue( [1,1,1,2,2,4,4,4,6] )))
# print(count_uniq(Queue( [3,0,4,4,4,7,7,5,5,5,5] )))
# print(count_uniq(Queue( [ ] )))


def p2i(queue):
  # Use Stacks to solve this problem
  newS = Stack()
  finalString = ""

  while not queue.is_empty():
    # Pull each item out of the queue one at a time
    testChar = queue.deq()

    if type(testChar) == int:
      # If it's a #, add it to the stack
      newS.push(testChar)
    else:
      # If it's not a number, pull the last 2 numbers and build the string
      rChar = newS.pop()
      lChar = newS.pop()
      finalString = str(lChar) + " " + testChar + " " + str(rChar)
      # Push the string into the stack
      newS.push(finalString)

  return finalString

# print(p2i(Queue( [1, 2, "+"] )))
# print(p2i(Queue( [5, 4, "*", 7, "+"] )))
# print(p2i(Queue( [2, 3, "*", 8, 5, "*", "+"] )))


def matcher(str):
  # Define the chars to match against
  rbraces = ["[", "{", "("]
  lbraces = ["]", "}", ")"]

  isMatch = False
  newS = Stack()

  # Put all chars into a Queue
  newQ = Queue()
  for i in str:
    newQ.enq(i)
  
  while not newQ.is_empty():
    testChar = newQ.deq()

    if testChar in rbraces:
      newS.push(rbraces.index(testChar))
    elif testChar in lbraces:
      test = lbraces.index(testChar)
      if  test == newS.pop():
         isMatch = True
    else:
      isMatch = True
  return isMatch

print(matcher("[()]"))
print(matcher("[("))
print(matcher("hello"))