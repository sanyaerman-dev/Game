import random 

cor = 0

wr = 0 

while True:
    num1  = random.randint(1,10)
    num2  = random.randint(1,10)
    corans = num1 * num2
    userans = input(f"whart is {num1} * {num2}: ")

    if int(userans) == int(corans):
        print ("you got it right bravo")
        cor += 1
        print(f"you now have {cor } right and {wr} wrong ")
    else :
        print ("you got it wrong sorry")
        wr += 1
        print(f"you now have {cor } right and {wr} wrong ")