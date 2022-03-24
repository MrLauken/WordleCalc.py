import sys
import enchant 
import random
import time

def DO_something():
    return None

emptystring= ""
d = enchant.Dict("en_US")
Liste = ["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","v","W", "X", "Y", "Z"]
ordliste=[]
ekstraliste=[]
teller=0
for x in range(1,6):
    yes_NO= input("\n Do you know letter nr. " + str(x) +". in the word? (y/n): ")
    if yes_NO== "y" or yes_NO=="Y":
        ordliste.append(str(input("\n Please write letter: ")).upper())
        teller+=1
    elif yes_NO== "n" or yes_NO=="N":
        ordliste.append(None)
    else:
        for x in range(0,16):
            print("\n ERROR: Invalid input, script will autoterminate in 15 seconds")
            time.sleep(1)
        sys.exit()

yes_NO=str(input("Are there any letters of unknown placement? (y/n): ")).upper()

if yes_NO=="Y":
    ekstrabok = str(input("Please write letter/letters: (E.G POERTY) ").upper())
    for x in ekstrabok:
        ekstraliste.append(x)
else:
        for x in range(0,16):
            print("\n ERROR: Invalid input, script will autoterminate in 15 seconds")
            time.sleep(1)
        sys.exit()


excluded_letters = input("\n Write all excluded letters if there are any: (E.G ADEFIQTOP) ")
for x in str(excluded_letters.upper()):
    for y in Liste:
        if x==y:
            Liste.remove(y)
p=0
z=0
q=0
ordliste1=[]
ekstraliste1=[]
godkjenteord = []
Sigma= True
teller=5-teller

for x in ordliste:
    ordliste1.append(x)


while p<=100 and z<=150000:
    aight=1
    if len(ekstraliste)>>0:
        for x in ekstraliste:
            ekstraliste1.append(x)
    for x in ordliste:
        if x== None:
            if teller == 0 or len(ekstraliste1)==0:
                ordliste1[q] = Liste[random.randint(0,len(Liste)-1)]
                aight+=1
            elif teller == aight:
                ordliste1[q]= ekstraliste[random.randint(0,len(ekstraliste)-1)]
                ekstraliste1.remove(ordliste1[q])
                aight+=1
            else: 
                randa =(teller-len(ekstraliste))*100/(teller) 
                check = random.randint(0,100)
                if check>=int(randa):
                    ordliste1[q] = Liste[random.randint(0,len(Liste)-1)]
                    aight+=1
                else:
                    ordliste1[q]= ekstraliste[random.randint(0,len(ekstraliste)-1)]
                    ekstraliste1.remove(ordliste1[q])
                    aight+=1

                
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
else:
    print("The great search for words terminated correctly due to runtime. This limitation might have caused certain words to escape, although this is fairly unlikely ")

print("Script will autoterminate in 60 seconds")
time.sleep(60)

    