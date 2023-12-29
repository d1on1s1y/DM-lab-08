from colorama import Fore
BNF = "<E>::=(<E>)|<E>+<E>|<E>*<E>|<V>|<C>"
var1= "<V>::=x|y"
var2= "<C>::=1|2"
print(BNF + ", " + var1 + ", " + var2)
def typeProd(STRarray):
    res = []
    array = STRarray.replace("::=", "|").replace("<", "").replace(">", "").split("|")
    for el in array[1:len(array)]:
        res.append(array[0]+" -> "+el)
    print(", ".join(res))
typeProd(BNF)
typeProd(var1)
typeProd(var2)

print(Fore.RED + "Ланцюжок: " + Fore.GREEN + "x+(x+1+2*x)")
print(Fore.LIGHTGREEN_EX + "                   E             ")
print("                /  |  \              ")
print("               /   +   \             ")
print("              E         E            ")
print("              |      /  |  \         ")
print("              V     (   E   )        ")
print("              |         |            ")
print("              x         |            ")
print("                     /  +  \         ")
print("                    /       \        ")
print("                  / E \   / E \     ")
print("                 E  |  E E  |  E    ")
print("                 |  +  | |  *  |    ")
print("                 V     C V     C    ")
print("                 |     | |     |    ")
print("                 x     1 x     2    ")
print("                                     ")
typeProd("x+x*(x+2)")






