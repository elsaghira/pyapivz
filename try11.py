#!/usr/bin/python3

while True:
    try:
        print("lets try")
        x = int(input("what us the value of x? "))
        y = int(input("what is the valueof y? "))
        print("the value of x/y is:", x/y)
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    except ValueError:
        print("You seem to be giving us a non numeric")
    except Exception as err:
        print(err)
