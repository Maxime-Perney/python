import random
passwordLenght = input("Enter a number betwen 3-100 : ")
while int(passwordLenght) < 3 or int(passwordLenght) > 100:
    passwordLenght = input("Enter a number betwen 3-100")
password = ""
specialChara = ["!","@","#","$","%","?","&","*","(",")"]
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(int(passwordLenght)):
    selec = random.random()
    if selec > 0.8:
        password += str(random.choice(specialChara))
    elif selec > 0.5:
        password += str(random.choice(letter).upper())
    elif selec > 0.2:
        password += str(random.choice(letter))
    else:
        password += str(int(random.random() * 10))
print(password)
