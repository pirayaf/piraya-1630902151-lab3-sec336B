#Ex 2 Reverst Stack
array1 = []
array2 = []
print("Pushing in to Array1")
array1.append("A")
print(array1)
array1.append("B")
print(array1)
array1.append("C")
print(array1)
array1.append("D")
print(array1)
array1.append("E")
print(array1)
array1.append("F")
print(array1)

#First in last out (FILO)
print("Pushing in to Array2")
array2.append(array1.pop())
print(array2)
array2.append(array1.pop())
print(array2)
array2.append(array1.pop())
print(array2)
array2.append(array1.pop())
print(array2)
array2.append(array1.pop())
print(array2)
array2.append(array1.pop())
print(array2)

#First in first out (FIFO)
print("Pushing in to Array1")
array1.append(array2.pop(0))
print(array1)
array1.append(array2.pop(0))
print(array1)
array1.append(array2.pop(0))
print(array1)
array1.append(array2.pop(0))
print(array1)
array1.append(array2.pop(0))
print(array1)
array1.append(array2.pop(0))
print(array1)




