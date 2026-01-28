# try,except,else,finally 

try:
    x = int(input("Enter Num:"))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by 0 is not allowed!")
except ValueError:
    print("Invalid Input!")
else:
    print(f"Ans: {ans}")
finally:
    print("End of Program!")