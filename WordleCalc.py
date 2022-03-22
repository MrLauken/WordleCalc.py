import enchant 
d = enchant.Dict("en_US")
Liste = ["Q","S","U","O","D","F","H", "J", "L", "Z", "X", "V"]
Ord = "SLO"
for x in Liste:
    for y in Liste:
        test= str(str(Ord) + str(x) + str(y))
        if d.check(test):
            print(test)