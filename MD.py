def subsets(nums):
    def backtrack(start, path):
        # Add the current path (subset) to the result
        result.append(path[:])
        
        # Iterate through the elements starting from 'start'
        for i in range(start, len(nums)):
            # Add the current element to the path
            path.append(nums[i])
            # Recursively generate subsets
            backtrack(i + 1, path)
            # Backtrack by removing the last element to explore other subsets
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Example usage:
input_array = [0]
result = subsets(input_array)
print(result)
#there is lesson
x=5
y="John"
print(type(x))
print(type(y))
str, int, float, complex=1j
list=["apple", "banana", "cherry"]
tuple=("apple", "banana", "cherry")
range=range(6)
dict={"name":"John", "age":36}
set={"apple", "banana", "cherry"}
frozenset({"apple", "banana", "cherry"})
bool=True
bytes=b"Hello"
bytearray(5)
memoryview(bytes(5))

#Type Conversion
x=1
y=2.8
z=1j

a = float(x)
b = int(y)
c = complex(x)

import random
print(random.randrange(1,10))

for x in "banana":
    print(x)

print(len(a))

txt="The best things in life are free!"
print("free" in txt)
if "free" in txt: #we can add not before in 
    print("Yes, 'free' is present.")

#slicing strings

b = "Hello, Word !"
print(b[2:5])
print(b[-5:-2])
print(a.upper())
print(a.lower())
print(a.strip())#removes whitespace returns "Hello, Word!"
print(a.replace("H", "J"))
print(a.split(","))
#Use the format() method to insert numbers into strings: (all theme name is string methods)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#ukazivaestsia poriadcovii nomer.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
#boolean values
"""Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

x=200
print(isinstance(x, int))
# +=	x += 3	x = x + 3
"""^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2"""
print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Looop list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension - Понимание
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [expression for item in iterable if condition == True]
newlist = [x for x in range(10)]

#sort 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
 
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """


for x in range(2, 30, 3): #Increment the sequence with 3 (default is 1):
  print(x)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

'''All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()