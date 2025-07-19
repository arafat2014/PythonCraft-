def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
print(f"{number} is {check_even_odd(number)}.")
