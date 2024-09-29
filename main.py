#1
def check_type(value):
    if type(value) == str:
        return type(value)
    elif type(value) == tuple:
        return type(value)
    return type(value)

list_1 = ['a', 'b', 'c', 'd', 'e']
list_1.append(['a', 'b4', 'c2', '3'])

tuple_1 = 2, 5, 43



print('String is', check_type(tuple_1))
print('String is', check_type(list_1))

#2
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))
print(number_1 + number_2)

#3
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

print("1. Normal")
print("2. Reverse")
menu = int(input("Choose an operation:"))

def counter():
    if menu == 1:
        for i in range(number_1, number_2):
            print(i + 1)
    elif menu == 2:
        for i in range(number_2, number_1 - 1, -1):
            print(i)

counter()


