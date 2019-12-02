"""==> i = 1
while i <= 5:
    print("Fahad ", end="")
    j = 1
    while j <= 4:
        print("great ", end="")
        j = j+1
    i = i + 1
    print()
==> x = int(input("how many candies do you want? "))
i = 1
while i <= x:
    if x <= 7:
        print("candy")
    else:
        print("out of stock")
        break

    i += 1
==> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)

==> for i in range(4):
    x = 0
    while x < 4:
        print("# ", end="")
        x += 1
    print()


for i in range(4):
    for j in range(4-i):
        print("# ", end="")

    print()

class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.ic = self.InnerCalculator()

    def addition(self):
        a = self.value1 + self.value2
        print(a)
        print(self.ic.addition())

    def subtraction(self):
        return self.value1 - self.value2
    class InnerCalculator:
        def __init__(self):
            self.value3 = 6
            self.value4 = 8

        def addition(self):
            return self.value3 + self.value4


c1 = Calculator(5, 4)
c1.addition()
c2 = Calculator.InnerCalculator()

print(c2.addition())
# Duck Typing

class Mobile:
    def nokia(self, os):
        os.execute()

class SnapDragon:
    def execute(self):
        print("multiple shots")
        print("better speed")

anyObject = SnapDragon()

anyMobile = Mobile()
anyMobile.nokia(anyObject)

#Operator overloading
class Operators:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        n1 = self.m1 + self.m2
        n2 = other.m1 + other.m2
        print(n1)
        print(n2)
        return n1 + n2

    def __gt__(self, other):
        c1 = self.m1 + self.m2
        c2 = other.m1 + other.m2
        if c1 > c2:
            return True
        else:
            return False


s1 = Operators(9, 3)
s2 = Operators(17, 5)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
s3 = s1 + s2
print(s3)

f = open("H", "a")
f = open("H", "r")
f1 = open("hello", "w")
image2 = open("MyImage.jpg", "wb")

for data in f:
    f1.write(data)

image = open("IMG_5039_1.jpg", "rb")

for data1 in image: """