# Declaring some variable

name = 'Joseph'
age = 34
print(age)
print(type(age))
print(type(name))

pi = 3.14159
print(type(pi))
complexNum = complex(2,3)
print(complexNum)
print(type(complexNum))

#some text variables now

document_code = 'p'
my_name = 'Joseph'
print(document_code)
print(my_name)
print(type(document_code))
print(type(my_name))
#g = input("Enter your name : ")
#print (g)

# Storing stings
str1 = 'Hello'
str2 = "hello"

str3 = """Helo this 
is my name"""

print(str1)
print(str2)
print(str3)

# concatenation

greeting = 'Good evening '
username = 'Jojo'

greeting_text = greeting + username
print ("{}{}".format(greeting,username))

is_raining = True

if(is_raining == True):
    print("Take umbrella")
else:
    print("Don't Need umbrella")
