students = ["ram","shyam","kishan","radha","radhika"]

##loop and break condition till perticular name
for i in students : 
    if i == "radha":
        break
    print(i)

teachers = ["Don","Varpe","Kshama","Apsunge"]
#loop and continue condition 
#consider the case if array not contains name kishan
for i in teachers :
    if i == "Varpe":
        continue
    print(i)