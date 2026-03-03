def Hide():
    print("Line 1")
    print("Line 2")
    print("Line 3")
    
# if 2 == 2:
#     print("if statement is true")
#     if 3 == 2:
#         print("nested if statement is true")
#         if 4 == 4:
#             print("nested nested if statement is true")
# elif 3 == 3:
#     print("elif statement is true")
# else:
#     print("if statement is false")


# write a program that take a number from the user and check if it is even or odd,
# if its even than check if it is greater than 50,
# if it is greater than 50 than add 10 to it and print the result, 
# if it is not greater than 50 than subtract 10 from it and print the result.abs

# userInput = int(input("Enter a number: "))
# if userInput % 2 == 0:
#     if userInput <= 50:
#         print(f"{userInput} is even number.")
#     else:
#         result = userInput + 10
#         print(f"Your Number {userInput} is even, so we can add 10 to this number. {result}")
# else:
#     if userInput < 50:
#         print(f"{userInput} is odd number.")
#     else:
#         result = userInput - 10
#         print(f"Your Number {userInput} is odd, so we can subtract 10 to this number. {result}")

# userInput = int(input("Enter a number: "))
# if userInput == 0:
#     print("Sunday")
# elif userInput == 1:
#     print("Monday")
# elif userInput == 2:
#     print("Tuesday")
# elif userInput == 3:
#     print("Wednesday")
# elif userInput == 4:
#     print("Thursday")
# elif userInput == 5:
#     print("Friday")
# elif userInput == 6:
#     print("Saturday")
# else:
#     print("Invalid input. Please enter a number between 0 and 6.")
    
# match userInput:
#     case 0:
#         print("Sunday")
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case _:
#         print("Invalid input. Please enter a number between 0 and 6.")





weekday = input("Enter a weekday: ")
match weekday:
    case "Sunday":
        print(0)
    case "Monday":
        print(1)
    case "Tuesday":
        print(2)
    case "Wednesday":
        print(3)
    case "Thursday":
        print(4)
    case "Friday":
        print(5)
    case "Saturday":
        print(6)
    case _:
        print("Invalid input. Please enter a valid weekday.")