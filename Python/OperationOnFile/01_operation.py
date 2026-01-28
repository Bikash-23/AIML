# Open,Read & Close 
# f = open("Python\OperationOnFile\sample.txt","r")
# f = open("Python\OperationOnFile\sample.txt","w")

# data = f.read()
# print(data)
# f.close()

# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()

# f.write("Text to convert \nthe complete data")
# f.close()

with open("Python\OperationOnFile\sample.txt","r") as f:
        print(len(f.read()))