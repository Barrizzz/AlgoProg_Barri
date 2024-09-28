def main():
    print("What do you want to do?\nFind the union of two lists (input 1)\nTuple and strings stuff (input 2)")
    option = input("Input here: ")

    match option:
        case "1":
            myListA = collectList("Set A")
            myListB = collectList("Set B")

            unifyLists(myListA, myListB)

        case "2":
            collectTupnstrings()

        case _:
            print("Stop being stupid")

def unifyLists(A,B):
    C = list(set(A).union(set(B)))
    C.sort()
    print(C)

def tupnstrings(tuple,string):
    stringList = list(string)
    finalResult = []

    for i in range(len(tuple)):
        result = stringList[i] * tuple[i]
        finalResult.append(result)

    return(''.join(finalResult))

def collectList(list_name):
    collectedList = []

    while True:
        value = input(f"Input {list_name} (type 'stop' when done): ")
        if value.lower() == "stop":
            break
        collectedList.append(value)
    return collectedList

def collectTupnstrings():
    collectedTuple = []

    while True:
        tup = input("Input tuple (type 'stop' when done): ")
        if tup.lower() == "stop":
            finalTup = tuple(map(int, collectedTuple))
            break
        collectedTuple.append(tup)

    print(finalTup)
    finalString = input(f"Please input a string with {len(finalTup)} characters: ")

    if len(finalString) != len(finalTup):
        print("Why you so stupid!")
    else:
        print(tupnstrings(finalTup,finalString))

main()