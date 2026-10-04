import math
import sys

print("Hello")

userName = "Foo"
userAge = 30
print("You are " + str(userAge))

print("10+20 =", 10+20)
print("10-20 =", 10-20)
print("10*20 =", 10*20)
print("3**2 = ", 3**2)
print("10 % 2 = ", 10 % 2)

print(math.floor(3.8)) #3
print(round(3.8)) #4
print(round(3.88, 1)) #3.9


a = 42
b = 'something'

try:
    print(a + b)
except TypeError as e:
    print("Error: ", e)

print("alma".upper())
print("LO" in "Hello".upper())
print("Decimal: %d, Float: %f, String: %s" % (12, 33.4, "something"))

# modern f-string
x = 42
print(f"x == {x}")

# list
players = [12, 31, 27, '48', 54]
print(players)
print(players[0])
print(players[-1])
print(players + [22, 67]) # array concat
print(len(players))

players.append(89)
print(len(players))
print(players[2:])

# tuple (is immutable)
players = (12, 31, 27, '48', 54)
try:
    players[2] = 'alma'
except TypeError as e:
    print("Cannot modify tuple: ", e)

try:
    del players[2]
except TypeError as e:
    print(e)

# list -> set (random order, no duplicates)
mylist = [8, 9, 2, 3, 5, 67]
myset = set(mylist)
print(mylist)
print(myset) # random order
print(sorted(mylist))

# dictionary
team = {
    91: "Ayers, Robert",
    12: "Bekham Jr,",
    3: "Brown, Josh",
    54: "Alina, Collins",
    21: "Landon, Coll"
}
print(len(team))
print(team[54])
print(team[91])
team[54] = "Chihiro"
print(team[54])

print(91 in team) # true 
print("Alina, Collins" in team) # false
print(team.keys())
print(team.values())

for (k, v) in team.items():
    print("Name: %s, #: %d" % (v, k))

if 91 in team:
    print("91 in team")
elif 12 in team:
    print("12 in team")
else:
    print("nobody in team")

# start, stop, step
for i in range(2, 10, 2):
    print(i)

i = 1
while i < 10:
    print(i, end=" ")
    i += 1
print()

# function
def isEven(num):
    if (num % 2) == 0:
        return True
    else:
        return False

for i in range(1, 10):
    if isEven(i):
        print("Num: " + str(i))

# multiple return values
def powers(x):
    return x**2, x**3, x**4
print(powers(2))

a, b, c = powers(2)
print(a, b, c)

# _ means I do not care about this valie
_, myval, _ = powers(2)
print(myval)

# lambda function
isEvenLambda = lambda num: (num % 2) == 0
for i in range(1, 10):
    if isEvenLambda(i):
        print(str(i))

print([x*x for x in range(10)])
print({x: x*x for x in range(5)}) #dictionary
print({x: x*x for x in range(5) if x != 2})
print(tuple(x*x for x in range(3)))

def fahrenheit(T):
    return ((9.0 / 5) * T + 32)

def celsius(T):
    return(5.0 / 9) * (T-32)

temps = (36.5, 37, 37.5, 38, 39)
tempsInF = list(map(fahrenheit, temps))
tempsInC = list(map(celsius, tempsInF))
print(tempsInF)
print(tempsInC)

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
oddNumbers1 = list(filter(lambda x: x % 2 == 1, fibonacci))
oddNumbers2 = list(filter(lambda x: x % 2, fibonacci)) # 1 = true
print(oddNumbers1)
print(oddNumbers2)

# files
with open("demofile.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

with open("demofile.txt", "r") as f:
    print(f.read())

with open("demofile.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("alma.txt", "w") as f:
    f.write("apple,banana,cherry\n")
    f.write("dog, cat\n")

with open("alma.txt", "r") as f:
    for line in f:
        print(line.strip().split(","))

# command line arguments
# python 01.py hello world
print(sys.argv[0])
if len(sys.argv) > 1:
    print(sys.argv[1])
if len(sys.argv) > 2:
    print(sys.argv[2])
else:
    print("nothing")

# classes
class Student:
    name = ''
    zhpoint = 0

    def __init__(self, _name, _point):
        self.name = _name
        self.zhpoint = _point
    
    def __str__(self):
        return f"{self.name}: {self.zhpoint}"
    
    def __repr__(self):
        return self.name + "(" + str(self.zhpoint) + ")"

def main():
    p = Student("Ford", 20)
    print(p) # uses str
    print([p]) # uses repr

    students = [
        Student("Arthur", 15),
        Student("Alina", 22)
    ]
    print(students) # uses repr

    for s in students:
        print(f"{s}") # uses str


# runs only when you execute this file directly
# not when another file does: import 01
if __name__ == "__main__":
    main()