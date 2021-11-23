sda = 0
whole = "+"
while sda != 2:
    while whole == "+" or "/" or "-" or "*":
        whole = input("Выберите действие: +,/,-,*: ") 
        break      
    a = float(input("Введите первое значение: "))
    b = float(input("Введите второе значение: "))
    if whole == "+":
        c = a + b
        print("Результат: " + str(c))
    elif whole == "/":
        c = a / b
        print("Результат: " + str(c))
    elif whole == "*":
        c = a * b
        print("Результат: " + str(c))
    elif whole == "-":
        c = a - b
        print("Результат: " +  str(c))
    else:
        print("Error")             
sda = int(input("Продолжим? : 1 - yes, 2 - no, :"))
           