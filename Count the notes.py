money=int(input("Enter a amount for widraw="))
note100=(money//100)
note50=(money%100)//50
note10=((money%100)%50)//10
print("The number of 100rs notes=",note100)
print("The number of 50rs notes=",note50)
print("The number of 10rs notes=",note10)