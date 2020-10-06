#loop
#while loop

number = int(input("Enter Integer: "))

k = 1
while k <= number:
    if k%2==0:
        print(f"{k} is an Even number. ")
    else:
        print(f"{k} is an Odd number. ")
    k+=1