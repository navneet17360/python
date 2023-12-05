# # # # # # # Convert String to List in Python
# # # # # # string to list of string


# # # # # # str=input('enter string:')
# # # # # # print(str.split())

# # # # # #string to list of characters

# # # # # str2=input("enter string2:")
# # # # # print(list(str2))


# # # # #List of Strings to List of Lists
# # # # str3=input("enter string3:")
# # # # print(str3)
# # # # str3=str3.split()


# # # # list1=(list(map(list,str3)))
# # # # print(list1)

# # # #CSV to list
# # # inp=input("enter CSV values")
# # # print(inp.split(','))

# # #A string consisting of Integers to a List of integers

# # list_of_integers=(input("enter numbers:"))
# # list_of_integers=list_of_integers.split()
# # print(list_of_integers)

# list_of_integers=(input("enter numbers:"))
# list_of_integers=list_of_integers.split()

# list2=list(map(int, list_of_integers))
# print(list2)