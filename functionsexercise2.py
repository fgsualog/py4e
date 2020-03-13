print("Functions - Exercise 2")
def computegrade(score):
#print("In computegrade", score)
    if score >= 1 :
        print("Error Message")
    elif score >= 0.9 :
        print("A")
    elif score >= 0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    elif score < 0.6 :
        print("F")

ss = input("Enter Score:")
try:
    fs = float(ss)
except:
    print("Error Message")
    quit()

xs = computegrade(fs)
print()
