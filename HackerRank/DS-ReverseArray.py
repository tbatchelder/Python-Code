def reverseArray(a):
  # Apprently you CAN'T assign this to a variable - it just changes the original list sent
  a.reverse()
  return a

print(reverseArray([1,4,3,2]))
print([1,4,3,2])
