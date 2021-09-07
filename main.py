# Password Generator Project
import random as rand


def EasyPass(charNum, sympNum, nNum, chars, nums, symbol):
    passW = []
    for i in range(charNum):
        randNum = rand.randint(0, len(chars) - 1)
        passW.append(chars[randNum])
    for i in range(sympNum):
        randNum = rand.randint(0, len(symbol) - 1)
        passW.append(symbol[randNum])
    for i in range(nNum):
        randNum = rand.randint(0, len(nums) - 1)
        passW.append(nums[randNum])
    return passW


def HardPass(charNum, sympNum, nNum, chars, nums, symbol):
    randPass = EasyPass(charNum, sympNum, nNum, chars, nums, symbol)
    rand.shuffle(randPass)
    print(randPass)
    return randPass


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("Easy password\n")
password = EasyPass(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols)
print(password)
strPass = "".join(password)
print(strPass)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("\n \nHard password\n")
password = HardPass(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols)
strHardPass = "".join(password)
print(strHardPass)