print("welcome to password generator!!!!!")
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p''q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','[',']','/','|']
numbers_need = int(input("how many numbers do you need? "))
letters_need = int(input('how many letters do you need?  '))
symbols_need = int(input("how many symbols do you need? "))
import random
password_list =[]
for char in range(0,letters_need):
    password_list.append(random.choice(letters))
for char in range(0,numbers_need):
    password_list.append(random.choice(numbers))
for char in range(0,symbols_need):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is:{password}")
print("welcome to password generator!!!!!")
numbers = ['1','2','3','4','5','6','7','8','9','0']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p''q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','[',']','/','|']
numbers_need = int(input("how many numbers do you need? "))
letters_need = int(input('how many letters do you need?  '))
symbols_need = int(input("how many symbols do you need? "))
import random
password_list =[]
for char in range(0,letters_need):
    password_list.append(random.choice(letters))
for char in range(0,numbers_need):
    password_list.append(random.choice(numbers))
for char in range(0,symbols_need):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is:{password}")
