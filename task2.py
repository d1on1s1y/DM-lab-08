from colorama import Fore, Style
def task_b(arr):

    # useful array
    array_helping = []
    array_param = [[], [], []]
    array_exit = []
    param = ""

    # remove spaces
    arr = arr.replace(" ", "")

    # array_helping
    for _ in range(0, len(arr)):
        if arr[_] == "," or arr[_] == "}":
            array_helping.append(param)
            param = ""
            continue
        param += arr[_]

    # array_param
    for _ in range(0, len(array_helping)):
        if array_helping[_][0] == "S":
            for i in range(0, len(array_helping[_])):
                if array_helping[_][i] == '>':
                    for j in range(i, len(array_helping[_])):
                        param += array_helping[_][j]
                    array_param[0].append(param.replace(">", ""))
                    param = ""
                    break

        if array_helping[_][0] == "B":
            for i in range(0, len(array_helping[_])):
                if array_helping[_][i] == '>':
                    for j in range(i, len(array_helping[_])):
                        param += array_helping[_][j]
                    array_param[1].append(param.replace(">", ""))
                    param = ""
                    break

        if array_helping[_][0] == "A":
            for i in range(0, len(array_helping[_])):
                if array_helping[_][i] == '>':
                    for j in range(i, len(array_helping[_])):
                        param += array_helping[_][j]
                    array_param[2].append(param.replace(">", ""))
                    param = ""
                    break

    # array_exit
    for i in range(0, len(array_param[0])):
        for j in range(0, len(array_param[0][i])):

            if array_param[0][i][j] == "A":
                for k in range(0, len(array_param[1])):
                    param = array_param[0][i]
                    param = param.replace("A", array_param[1][k])
                    param = param.replace("S", "")
                    array_exit.append(param.replace("A", ""))
                break

            if array_param[0][i][j] == "B":
                for k in range(0, len(array_param[1])):
                    param = array_param[0][i]
                    param = param.replace("B", array_param[1][k])
                    param = param.replace("S", "")
                    array_exit.append(param.replace("B", ""))
                break

            if array_param[0][i][j] == "S":
                for k in range(0, len(array_param[0])):
                    param = array_param[0][i]
                    param = param.replace("S", array_param[0][k])
                    param = param.replace("B", "")
                    array_exit.append(param.replace("S", ""))
                break

    print(array_exit)

print(Fore.GREEN + "b. P = {S->0B, B->1B, B->0}")
multiple = "S->0B, B->1B, B->0}"
task_b(multiple)
print(Style.BRIGHT + Fore.RED + "2. Регулярна тип 3")
print("3. S0 = S1 | 0 = S0 | S0 = B | 1 = B")
print()
print("              S                 ")
print("         (0)/   \(1)            ")
print("          S1     S2             ")
print("      (0)/  \(1)                ")
print("       S3    S4                 ")
print("")
print(Style.BRIGHT + Fore.GREEN + "|----------------------------|")
print("|        |          f        |")
print("|        |-------------------|")
print("|  Стан  |        Вхід       |")
print("|        |-------------------|")
print("|--------|    0    |    1    |")
print("|--------|-------------------|")
print("|   S0   |    S0   |    S0   |")
print("|--------|-------------------|")
print("|   S1   |    S0   |    S1   |")
print("|--------|-------------------|")
print()
