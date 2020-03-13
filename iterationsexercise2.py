print("Iterations - Exercise 2")
num = 0
tot = 0.0
numb = list()
while True :
    sval = input("Enter a number: ")

    try:
        fval = float(sval)
        numb.append(sval)
        num = num + 1
        tot = tot + fval
        maxi = max(numb)
        mini = min(numb)
    except:
        if sval == "done" :
            break
        else:
            print("Invalid Input")


print("Total",tot)
print("Number",num)
print("Maximum:", maxi)
print("Minimum:", mini)
