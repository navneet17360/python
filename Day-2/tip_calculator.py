# total_bill=int(input("total bill:"))
# number_of_persons=int(input("number of persons:"))
# rate_of_interest=int(input("rate of interest:"))

# new_total=total_bill+(total_bill*rate_of_interest)/100
# each_person_should_pay=new_total/number_of_persons
# print("Each person should pay",round(each_person_should_pay,2),"$")

print("Welcome to the tip calculator")
total_bill=(float(input("What was the total bill? $")))
rate_of_interest=(int(input("What percentage tip would you like to give? 10, 12, or 15?")))
number_of_persons=(int(input("How many people to split the bill?")))
new_total=total_bill+(total_bill*rate_of_interest)/100
each_person_should_pay=new_total/number_of_persons
print("Each person should pay",round(each_person_should_pay,2),"$")