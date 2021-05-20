import matplotlib.pyplot as plt
graph = []
temp = []
num = []
def growthfactor():
    ans = 0
    a = 0
    b = 1
    while True:
        div = int(input("Enter how many days:"))
        if div == 0 or div == 1:
            print("Try Again but not with 1 or 0")
            continue
        else:
            break
    for i in range(div):
        while True:
            try:
                number = int(input("Day{}:".format(str(i+1))))
            except ValueError:
                print("Give a valid number!!")
                continue
            else:
                break
        num.append(number)
    for a in range(div-1):
        ans += num[b] / num[a]
        a+=1
        b+=1
    result = ans/(div-1)
    lval = num[div-1]
    return result, lval
def nextcases(growth = 0, lc = 0):
    if growth == 0:
        growth = float(input("Growth Factor:"))
    if lc == 0:
        lc = int(input("Latest Case:"))
    days = int(input("How many days to calculate:"))
    for day in range(days):
        lc *= growth
        inte = int(lc)
        print("Day{}:{}".format(day+1, inte))
        graph.append(inte)
        temp.append(day)
    plt.plot(temp, graph)
    plt.show()
def real():
    choice = input("What do you wanna choose:")
    if choice == "1":
        print("Your GrowthFactor and LastCase is",growthfactor())
        input()
    elif choice == "2":
        nextcases()
    elif choice == "3":
        result, lval = growthfactor()
        print("Your GrowthFactor is {}".format(result))
        nextcases(result, lval)
    elif choice == "4":
        print("ThankYou!")
    else:
        print("Sorry thats not a choise\n1)GrowthFactor 2)PredictCases 3)Both 4)Exit")
        real()
if __name__ == "__main__":
    print("\t\t\t\t\t\tWelcome\n\t\tType the number to choose 1)GrowthFactor 2)PredictCases 3)Both 4)Exit")
    real()
