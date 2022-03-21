def cpllatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3*number+1


try:
    number = int(input("Enter a number"))
except ValueError:
    print("Invalid input, enter a number.")

number = cpllatz(number)
print(number)
while number != 1:
    number = cpllatz(number)
    print(number)



