# Question-1
# part-1
# f = open("Python\\OperationOnFile\\names.txt","w")
# f.write("raja\nkavi\nkhan\nraj\nravi")

# part-2
# with open("Python\\OperationOnFile\\names.txt","r")as f:
#     print(f.read())
# f.close()

# Question-2 
# part-1
# f = open("Python\\OperationOnFile\\log.txt","w")
# f.write("Hello!")
# part-2
# f = open("Python\\OperationOnFile\\log.txt","a")
# f.write("\nProgram run succefully")
# f.close()

# Question-3
# list = [5,10,15,20,25]
# list = [val for val in list if val>=15]
# print(list)

# Question-5
# import json
# part-1
# city = {
#     "Mumbai" : "12M",
#     "Delhi":"10M",
#     "Kolkata":"15M"
# }
# part-2
# f = open("Python\\OperationOnFile\\cities.json","x")
# part-3
# with open("Python\\OperationOnFile\\cities.json","w") as f:
#     json.dump(city,f,indent=3,sort_keys=True)
# part-4
# with open("Python\\OperationOnFile\\cities.json","r") as f:
#     data= json.load(f)
#     print(data)
# part-5
# new_city = input("Enter new city:")
# new_population = input("Enter Population:")
# city[new_city] = new_population
# with open("Python\\OperationOnFile\\cities.json","w") as f:
#     json.dump(city,f,indent=4)

# Question-5
# try: 
#     f = open("Python\\OperationOnFile\\names.txt","r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("file does not exist!")
# else:
#     print("Open!")
# finally:
#     print("Code done!")