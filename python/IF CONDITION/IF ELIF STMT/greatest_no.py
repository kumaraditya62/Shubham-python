num1=int(input("entre 1st no. :"))
num2=int(input("enter 2nd no. :"))
num3=int(input("enter 3rd no. :"))
if(num1>num2):
    if(num1>num3):
        print(num1,"is the greater no.")
    else:
        print(num3,"is the greatest no.")
elif(num2>num3):
 print(num2,"is the greatest no.")
else:
  print("the three no. are equal")