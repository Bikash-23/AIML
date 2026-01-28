# if,elif,else

# age  = 15
# if age>= 18:
#     print('You can vote')
#     print('you can drive')
# else:
#     print("you can't vote")

# color = input("Enter color:")

# if color == "red":
#     print("Stop")
# elif color == "green":
#     print("Go")
# elif color == 'yellow':
#     print("Look")
# else:
#     print("Error")

# --------------Match-case---------------------
color = input("Enter color:")
match color:
    case "red":
        print("Stop!")
    case "green":
        print("GO!")
    case "yellow":
        print("Look!")
    case _: #defult
        print("Error")

# username = input("Enter User Name: ")
# password = input("Enter Password: ")

# if(username == "admin" and password == "pass"):
#     print("Succesfully login..")
# elif(username != "admin" and password == "pass"):
#     print("Wrong username!")
# elif(username == "admin" and password != "pass"):
#     print("Wrong password!")
# else:
#     print("wrong username and password")


# -------------------Nesting--------------------

# username = input("Enter User Name: ")
# password = input("Enter Password: ")

# if(username == "admin" and password == "pass"):
#     print("Succesfully login..")
# else:
#     if(username != "admin"):
#         print("Wrong Username!")
#     else:
#         print("Wrong Password!")
