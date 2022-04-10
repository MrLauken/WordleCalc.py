import sys
import enchant 
import random
import time

def DO_something():
    return None

emptystring= ""
d = enchant.Dict("en_US")
Liste = ["A","B","C","D","E","F","G","H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","v","W", "X", "Y", "Z"]
ekstraliste = [None, None, None, None, None]
ordliste=[]
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

yes_NO=str(input("\n Are there any letters of unknown placement? (y/n): ")).upper()
k=1
if yes_NO=="Y":
    while yes_NO == "Y" and k<<6 :
        ekstrabok = str(input("\n Please write the " + str(k) + ". letter of unknown placement: ")).upper()
        plassering = input("\n Where can the letter still be placed in the word? : (e.g 1345)  ")
        for x in plassering: 
            if ekstraliste[int(x)-1]!= None:
                ekstraliste[int(x)-1] = str(ekstraliste[int(x)-1]) + str(ekstrabok)
            else:
                ekstraliste[int(x)-1] =  ekstrabok
        yes_NO=str(input("\n Are there any more letters of unknown placement? (y/n): ")).upper()
        k+=1
elif yes_NO=="N":
    print()
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
l = 0
ordliste1=[]
ekstraliste1=[]
godkjenteord = []
Sigma= True
teller+=k-1
for x in ordliste:
    ordliste1.append(x)

while p<=100 and z<=150000:
    aight=1
    ekstraliste1=[]
    s=0
    for x in ekstraliste:
        ekstraliste1.append(x)
        if x != None:
            s+=1
    for x in ordliste:
        if x== None:
            if ekstraliste[q]!=None and ekstraliste1[q]!="":
                sjanse = random.randint(0,len(ekstraliste1[q])+1)
                #print(int(teller+l), sjanse,ekstraliste1, ekstraliste1[q], "print 1")
                if sjanse>=1 or teller+l>=5: 
                    p = 0
                    sjanse = random.randint(0,int(len(ekstraliste1[q]))-1)   
                    for x in ekstraliste1[q]:
                        
                        #print(sjanse, p, x)
                        if sjanse == p:
                            #print(x, "Print 2")
                            ordliste1[q] = x
                            tall = 0
                            streng = ""
                            for w in ekstraliste1:
                                streng = str(w)
                                if w!= None:
                                    for y in w:
                                        if y == x:
                                            streng = streng.replace(x, "")
                                ekstraliste1[tall] = streng
                                streng = ""
                                tall+=1 
                            break
                        p+=1
                        
                else: 
                    ordliste1[q] = Liste[random.randint(0,len(Liste)-1)]
                    l+=1
                    #print(ordliste1[q], "print 3")
            else: 
                ordliste1[q] = Liste[random.randint(0,len(Liste)-1)]
                l+=1
                #print(ordliste1[q], "print 4")
                
        q+=1
    q=0
    #print(ordliste1, "print 5")
    strin = "".join(ordliste1)    
    l=0


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
    print("\nProgram ended early due to too many possible words")         
else:
    print("\nThe great search for words terminated correctly due to runtime. This limitation might have caused certain words to escape, although this is fairly unlikely ")

print("\nScript will autoterminate in 60 seconds")
time.sleep(60)

    