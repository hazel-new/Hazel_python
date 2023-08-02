# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    fist_number = input("\nFirst number: ")
    if fist_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(fist_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)