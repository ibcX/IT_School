
def my_function(a,b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError as error:
        print(f"Could not divide elements {error}")
    except TypeError as error:
        print(f"Type error {error}")
    else:
        print(result)

my_function(2,0)

