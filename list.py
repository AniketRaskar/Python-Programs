marks  = [95,98,97]
print(marks)
print(marks[0])
#print(marks[3])  //out of bounds eception
# if we give index negative then it gets count from last index
print(marks[-1])
print(marks[0:2])  #gives element at index 0 & 1
print(marks[-3:-1]) #gives elemet from index -3 to -1 ie. 0 to 3

#by for loop displaying all elements
for elements in marks:
    print(elements)

marks.append(99)  #adds the marks at the end of array
print(marks)

marks.insert(0,80)  #adds the marks at the start of the array
print(marks)

print(99 in marks)  #returns true if present in array else false
print(len(marks))  #gives the length of array