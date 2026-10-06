maths=int(input("enter the marks of maths : "))
computer=int(input("enter the marks of computer : "))
chemistry=int(input("enter the marks of chemistry :"))
literature=int(input("enter the marks of literature :"))
physics=int(input("enter the marks of physics :"))

sum=(maths+computer+chemistry+literature+physics)
print("The sum of the marks is : ",sum)

percentage=(sum/500)*100
print("Your percentage is : ",percentage)