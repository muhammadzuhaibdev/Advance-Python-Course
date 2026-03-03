print("print before the function")
def Add(a, b):
    print("a ->", a, "b ->", b )
    num1 = 10
    num2 = 20
    result = num1 + num2 + a + b
    print(result)
Add(10,30)
print("print After the function")    
Add(100,200)