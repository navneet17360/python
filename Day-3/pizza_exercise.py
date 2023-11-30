# # #small pizza=15
# # medium pizza=20
# # large pizza=25    --
# # pepperoni for small pizza =2
# # pepperoni for medium or large pizza=3 --
# # extra cheese for any size pizza=1

# output format 
# your final bill is: $28

print("Welcome to Python Pizza Deliveries")
size=input("Enter Size:")
add_pepperoni=input("Do you want pepperoni? yes or no:")
extra_cheese=input("Do you want extra cheese? yes or no:")
bill=0

if(size=="S"):
    bill+=15
elif(size=="M"):
    bill+=20
else:
    bill+=25

if(add_pepperoni=="Y"):
    if(size=="S"):
        bill+=2
    else:
        bill+=3
if(extra_cheese=="Y"):
    bill+=1
    

print(f"your final Bill is ${bill} ")
    
    
    
    
    


