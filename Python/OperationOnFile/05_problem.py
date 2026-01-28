data = True
line = 1
word = "Python"
with open("Python\OperationOnFile\sample.txt","r") as f:
    while data:
       data  =f.readline()
       if(word in data):
          print(f"{word} found in line: {line}")
          break
      
       line+=1