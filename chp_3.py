def cpllatz(number):
    if number%2==0:
        print(number//2)
    else:
        print(3*number+1)

number=int(input("Enter a number"))
cpllatz(number)

x=cpllatz(number)

while number > 1:
    number -= 1
    

    print(number)
