#Lists
c =['Joe','Mary','Paul']
c[1] = 'JoeMary'
c.append('Loul')


for x in c:
    print(x)

#Dictionary
info = {'John':[30,'Attard'], 'Mary':32,'Paul':40}
print (info['John'])
info ['Isaac'] = 31
print (info['Isaac'])
print(info.keys())
print('Isaac' in info)

# Selection

age = 23

if (age >= 18):
    print('I can vote')
    if (age>22):
        print('I am over 22 as well')
else:
    print('I cannot vote')

# Multiple condition
#val = int(input("Enter your Choice: "))
val = 2

if(val==1):
    print('Margherita')
elif (val==2):
    print('Napoloitana')
elif (val==3):
    print('Capricciosa')
else:
    print('No selection')

# compound boolean expression

age = 12
has_insurance = True

if age >= 18 and has_insurance:
    print('You can drive')
else:
    print('You cannot drive')

number0fAlevel = 1
age = 22

if age>=25 or number0fAlevel >=2:
    print('You are in')
else:
    print('Sorry you are not in')

#ternary operations

num_fish = 1
msg = 'You have fish' if num_fish > 0 else 'you have no fish'
print(msg)

num1 =1
## loops
while num1 < 5:
    print(num1)
    num1+=1 #count = count + 1

names=['Andreas', 'Joseph', 'Carl', 'Julian']

for x in names:
    print(x)

for x in range(5):
    print (x)

print('End')

for x in range(1,21,2):
    print (x)

print('End')

for x in range(20,1,-2):
    print (x)

print('End')

i=0
while True:
    print(i)
    i+=1
    if i > 10000:
        break

print('End')

cleaning_hour = 17
fishing_hour = 0

while fishing_hour <24:
    fishing_hour +=1
    if fishing_hour == cleaning_hour:
        continue
    print('Fishing for hour' + str(fishing_hour))
