height=float(input("enter height in m:"))
weight=float(input("enter width in kg:"))
Bmi=weight/height**2

if(Bmi <18.5):
    print(f"Your bmi is {Bmi} , You are underweight")
elif(Bmi>18.5 and Bmi <25):
     print(f"Your bmi is {Bmi} , You are normal weight")
elif(Bmi>25 and Bmi <30):
     print(f"Your bmi is {Bmi} , You are overweight")
elif(Bmi>30 and Bmi <35):
     print(f"Your bmi is {Bmi} , You are obese")  
else:
     print(f"Your bmi is {Bmi} , You are clinically obese")

