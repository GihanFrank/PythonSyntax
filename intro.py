# printing text on the screen
from audioop import reverse
import random
print('Gihan')

# indentation(Spacing)
if 5 < 2:
    # ther should be at least one space after the main statement.
    print('5 is greater')

    # Variables #
    # Variables #
x = 5
print(x, 3)
x = 'frank'
g = "gihan"
print(x+g)
# variable Casting
X, y, z = int(3), str(3), float(3)
print(X)  # varible names are case sensitive
print(x)
print(y)
print(z)
print(type(y))  # type of a variable
# unpacking
cars = ["bmw", "porsche", 'toyota', 'volvo']
a, b, c, d = cars
print(a, b, c, "5", d)  # concatination- commas or + can be used
# any variable created inside of a functions is local and can not be accessed from the outside.
# "global" keyward is used to create a globla variable inside of a function.
x = 3.6
y = 0.55
print(x+y)

# Numbers #
# Numbers #

print(random.uniform(1, 100))

# String #
# String #

a = 'Hellow,World'  # string are considered as arrays (many languages do that)
print(a)
print(a[3])

for y in 'banana':  # going through a for loop
    print(y)

    a = ' Gihan perera'  # lenth of a string
    print(len(a))
    print('er' in a)  # print a cirtain phrase or character in a text
    print(a[2:7])
    print(a[-7:-3])  # text sliceing using array number
    print(a.upper())
    print(a.lower())  # bult in methods
    print(a.strip())  # this removes the any spces at the beginign or at the end
    print(a.replace('p', 'P'))

# concatination
a, b, d, e, g, h = 'monkey', 'banana', 34, 'eats', 'days', 3
c = a+' '+b
# use numbers inside the {} to pass the argument orderly manner in f.format() method(see line 64)
f = a+' '+e+' '+'{1}'+' ' + b+' every '+'{0}'+' '+g
print(a+" "+b)
print(c)
print(f.format(h, d))  # nuber is put whreever the {} is present by order

print("my nick name is \"PODI\" at home")  # use \"" to produce "" in a text

# Boolean Values #
# Boolean Values #

print(10 > 9)

a = 200
b = 50
if a < b:
    print('b is greater')
else:
    print('\'A\' is greater')

    # Lists #

# lists are varialbes containing multiple items that can be represented by any data type
fruits = ['apple', 'banana', 'raspberry', 'blackberry',
          True, 55, 33, 'klm', 'delta', False, 69]
print(fruits[2])
fruits[2] = 'watermelon'
print(fruits[2], fruits[5], type(fruits[4]), type(fruits), fruits[-4:-2])
if 33 in fruits:
    print('not only fruits')
fruits.append('appended')  # add items to the end
fruits.insert(3, "avocado")  # add items to the spesific place
print(fruits, len(fruits))
fruits.remove(fruits[3])  # removeing items
fruits.pop(6)
fruits.clear()  # clear the list
print(fruits, len(fruits))
A=0
marks=[55,10,35,46,98,56,19,56,78,89,56,12,36,56]
for x in marks:  # for loop
    print(x)
print("ccccccccccccccccccccc")
for y in marks:
    A=y+A
print(A)

## list comprehension ##
failStudents=[x for x in marks if x<20]
print(failStudents)
marksLessThanTwenty=[]
for x in marks:
    if x<20:
     marksLessThanTwenty.append(x)
print(marksLessThanTwenty)
fruits = ['apple', 'banana', 'raspberry', 'blackberry']
fruits2=[x.upper() for x in fruits]
print(fruits2)
fruits3=[x if x !='raspberry' else 'orange' for x in fruits]
fruits4=[x if x=='raspberry' else 'mango' for x in fruits]
print(fruits3)
print(fruits4)
fruits5=fruits4
print('list end')
print(fruits5)
## sorting lists ##

fruits.sort()
print(fruits)
marks.sort(reverse=True)
print(marks)

                        # tuples#
                        # tuples #

thisTuple=('Gihan','Hiran','mahesha','gayan','Gihan',55,True) # tuples are ordered and unchangable and allow duplicate values
print(thisTuple)
x=len(thisTuple) # or ## print(len(thisTuple))
print(x)
print(type(thisTuple))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove(y[1])
thistuple = tuple(y)
print(thistuple)

##W3 school tuples while loop
