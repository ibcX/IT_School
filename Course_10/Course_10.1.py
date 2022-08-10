

score = 10

def function_one():
    global score
    score += 20
    return score

print(function_one())
print(score)

def test_function(command_one, *args):
    print(type(args))
    print(args)
    print(command_one)


test_function("Razvan", "Test", "Hello")


def shopping_list(**kwargs):
    print(type(kwargs))
    print(kwargs)

shopping_list(bannana=20, apple=10, cherry=25)

# factorial

def factorial(number):
    if number ==0:
        return 1
    return number * factorial(number -1)

print("\n", factorial(5))


