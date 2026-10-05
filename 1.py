#Exception handling
try:
    num=int(input("Enter a number:"))
    print(10/num)
except ValueError:
    print("invalid input.plese enter a valid number")
except ZeroDivisionError:
    print("number cannot be zero")
except Exception as e:
    print("an error occured:", e)
else:
    print("success")
finally:
    print("Execution completed")

#file handling with exception
try:
    file=open("data.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("exception occur:",e)
else:
    print("success")
finally:
    print("execution completed")