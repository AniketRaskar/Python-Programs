name = "Aniket Raskar"
# indexing starts from 0 (space is also calculated)

name1=name.lower() #conversion to lower case permenantly but in variable name1

print(name.upper()) #conversion to upper case but not perment 
print(name1)

print(name.find('R'))  #finds the index of String or letter in '' but if not present then return -1
print(name.find('Raskar'))

print(name.replace("Aniket",("AniketShet"))) #replaces the characters or word
print(name.replace('a',('p')))  #replaces the letter a in string with p


print('T'in name)  #returns true if present also it cheaks case sensitivity
print('n' in name)
print('Datt' in name)  #cheaks that string present in string


