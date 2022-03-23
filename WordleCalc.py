import enchant 
import random
emptystring= ""
d = enchant.Dict("en_US")
Liste = ["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","v","W", "X", "Y", "Z"]
ordliste=[]
for x in range(1,6):
    yes_NO= input("\n Do you know letter nr. " + str(x) +". in the word? (y/n): ")
    if yes_NO== "y" or yes_NO=="Y":
        ordliste.append(input("\n Please write letter: "))
    elif yes_NO== "n" or yes_NO=="N":
        ordliste.append(None)
    else:
        print("\n Invalid input")
        x=x-1

excluded_letters = input("\n Write all excluded letters if there are any: (E.G ADEFIQTOP)")
for x in str(excluded_letters.isupper()):
    for y in Liste:
        if x==y:
            Liste.remove(y)
p=0
z=0
q=0
ordliste1=[]
godkjenteord = []
Sigma= True
for x in ordliste:
    ordliste1.append(x)

while p<=100 and z<=100000:
    for x in ordliste:
        if x== None:
            ordliste1[q] = Liste[random.randint(0,len(Liste)-1)]
        q+=1
    q=0
    strin = "".join(ordliste1)    
    

    if d.check(strin):
        for x in godkjenteord:
            if x==strin:
                Sigma = False
                break
        if Sigma == True:
            godkjenteord.append(strin)
            print(strin)
            p+=1
        Sigma=True
    z+=1

if p>=100:
    print("Program ended early due to too many possible words")           
    