print("Conditional Statements - Exercise 3")
ss = input("Enter Score:")
try:
    fs = float(ss)
except:
    print("Error Message")
    quit()
if fs >= 1 :
    print("Error Message")
elif fs >= 0.9 :
    print("A")
elif fs >= 0.8 :
    print("B")
elif fs >= 0.7 :
    print("C")
elif fs >= 0.6 :
    print("D")
elif fs < 0.6 :
    print("F")


print()
