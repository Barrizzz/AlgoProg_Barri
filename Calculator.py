print(f"WELCOME TO THE BEST CALCULATOR EVER IF YOU THINK THIS SUCK THEN U SUCK\n If you are done please input (=)")

allNum = []

number = eval(input("Please input numbers: "))
sign = input("Input what operation you want ( + | - | * | / ): ")
allNum.append(number)
allNum.append(sign)

while sign != '=':
    number = input("Please input numbers: ")
    allNum.append(number)

    sign = input("Input what operation you want ( + | - | * | / ): ")
    allNum.append(sign)

allNum.pop()
finalStr = "".join(map(str, allNum))

print(eval(finalStr))


   
    
