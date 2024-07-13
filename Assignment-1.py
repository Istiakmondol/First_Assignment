#1. Data Types and Variables

#Task-1
age = 25
salary = 100.5
name = "Md. Istiak Mondol"
employed = False

#Task-2
print("age: ",type(age))
print("salary: ",type(salary))
print("name: ",type(name))
print("employed: ",type(employed))

#Task-3
print("addition: ",age+salary)
print("Subtraction: ",age-salary)
print("Multiplication ",age*salary)
print("Division: ",salary/age)
print("Remainder: ",salary%age)

#2. Control Flow (if/else)

#Task-1
x=int(input("Enter a number: "))

#Task-2
if(x%2==0):
    print(f"{x} is Even")
else:
    print(f"{x} is Odd")
    
# 3. Strings and Manipulation

#Task-1
var="My Name is Khan and i'm not a terrorist"

#Task-2

# 2.1 Convert the sentence to uppercase and lowercase.
var0= var
var= var.upper()
print(f"Upper Case: {var}")
var= var.lower()
print(f"Lower Case: {var}")

# 2.2 Split the sentence into a list of words.
var= var.split(" ")
print(var)

# 2.3 Find the length of the sentence.
print(f"The length of the string is : {len(var0)}")

# 2.4 Replace a specific word in the sentence with another word.
var0 = var0.replace("terrorist","'Actor'")
print(var0)

#Loops (for/while)

#Task-1
numbers = [1,2,3,4,5,6,7,8,9,10]
print("Each Number Multiplied by 2 in the list: ")
for i in numbers:
    print(i*2)

#Task-2
i=1
sum=0
while(i<=10):
    sum+= i
    i+= 1
print(f"Sum of numbers: {sum}")

# 5. Lists and List Comprehensions

#Task-1
fruits = ['Mango', 'Banana', 'Lichi', 'papaya']

#Task-2
len_of_fruits = [len(i) for i in fruits]
print(len_of_fruits)

#Task-3
fruits.append('cherry')
print(f"After appending a new fruit: {fruits}")

#Task-4
sorted_fruits= sorted(fruits, key=str.lower)
print(f"After sorting: {sorted_fruits}")

# 6. Dictionaries

#Task-1
book={"title": "War and Peace",
      "author": "Tolstoy",
      "year": 1869
      }

#Task-2
print(f"Book Title: {book['title']}")
print(f"Book Author: {book['author']}")
print(f"Book Year: {book['year']}")

#Task-3
book["genre"] = "historical chronicle"

#Task-4
for i, j in book.items():
    print(f"{i}: {j}")


