val = int(input("Enter the number"))

if val == 0:
    print("Enter the valid number, Zero is not included")
elif val == 1:
    print("1 is not considered as a prime number")
elif val >1:
    for i in range(2,int(val//2)+1):
        if val%i==0:
            print("It is a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("You entered a invalid one")
