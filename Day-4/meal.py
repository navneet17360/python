import random
names_list=input("enter name seperated by commas:\n")
names_list=names_list.split(", ")
print(names_list)

number=len(names_list)
print(number)
random_number=random.randint(0,number-1)
print(random_number)
person_who_will_pay=names_list[random_number]

print(f"{person_who_will_pay} is going to buy meal today")
# import random
# names_list=input("enter name seperated by commas:\n")
# names_list=names_list.split(", ")
# person_who_will_pay=random.choice(names_list)
# print(f"{person_who_will_pay} is going to buy meal today")
