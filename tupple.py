marks = (95,98,97,95,97,95,97) #tupples are immutable which cannot be edit agian whereas list and array can be edit so they are immutable, tupples are in square braket
#marks[0] =99  gives error
print(marks.index(97))   #gives the index
print(marks.count(97))   #returns the total count of given elements