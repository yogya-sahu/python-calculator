try:
    a = int(input("please enter your first number:"))

    b = int(input("please enter your second number:"))
    print("what kind of operation you want to perform . \npress + for addition\n press - for substracton\n press / for division\n press * for multiplication ")

    o = input("enter opertaion: ")
    match o:
        case "+":
            print(f"the result will be { a + b }")
             
        case "-":
            print(f"the result will be { a - b }")
             
        case "*":
            print(f"the result will be { a * b }")
             
        case "/":
            print(f"the result will be { a / b }")
             
        case default :
            print("invalid")
            
            
 
 
except Exception as e:
    print("please enter a vailed value of a and b")

