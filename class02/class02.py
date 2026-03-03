#  username = "Zuhaib"
# message = f"Hello {username}"

# Operator
# 1) Arithmetic Operators (+, -, *, /, %, **, //)
# num1 = 10
# num2 = 5
# result = num1 / num2
# result = num1 - num2
# result = num2 + num1 * 10 + num2 + num1 * 20 / 4
# result = num1 // 3

# 2) Assignment Operators (=, +=, -=, *=, /= ,%= , **=, //)
# num1 = 10
# num1 += 10
# num1 = num1 + 10
# num1 -= 10
# num1 *= 5
# num1 /= 5
# num1 //= 5
# num1 **= 3
# num1 %= 20
# print(num1)
 

# 3) Comparison Operators (==, !=, < , >, <=, >=)
# num1 = 10 
# num2 = 20 
# BODMAS
# result = (num1 + 10) * 30 / 6 + 4 != num2 + 20 / 4 + 2 % 5 + 4 ** 5
# result = num1 % 4 + 10 / 4 + False + .5 + (2 ** 3) + True * 1 * 2   
# print(result)

# 4) Logical Operators (and , or, not)
# num1 = 10
# num2 = 20
# result = num1 >= 20 + num2 and num1 + 10 + True >= num2 or num2 + 1 == 20 + True + 1 * 10 % 3
# result = not(True or not(20 + num2 >= 50 or 10 + 30 + num1 % 4 == 30))
# result = not((20 + num1 % num2) ** 3 + 10 and (num2 % 12) + 10 // 2 * 3 + True >= num1 + 20 or (20 % 3) + 10 and True)
# print(result)

# and cases
# T T => T
# T F => F
# F T => F
# F F => F

# or cases
# T T => T
# F T => T
# T F => T
# F F => F

# Membership Operartor
userName = "Zuhaib"
value = "z"

result = value in userName
print(result)

# Identity Operartor
userName = "Zuhaib"
value = "Zuhaib"

result = value is not userName
print(result)