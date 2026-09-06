x = 5
y = x + 2
print(y)

name = """Alice"""
# name[0] = 'a'
language = "Python"
print(language[0:6:2])
print("Reverse: " + language[::-1])
print(language[2:])

'''
multi-line comment using
docstrings
'''
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


def add(a, b):
    """This function adds two numbers"""
    return a + b


print(add(36, 32))
