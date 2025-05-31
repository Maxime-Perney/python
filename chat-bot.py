print("hello, I am your chatbot")
name = input("What's your name? ")
print("Nice to meet you, " + name)
age = input("How old are you? ")
gender = input("Are you a boy or a girl? ")
if gender.lower() == "boy":
    print("Nice to meet you, man!")
else:
    print("Nice to meet you, woman!")
color = input("What's your favorite color? ")
if color.lower() == "blue":
    print("Blue is my favorite color too!")
else:
    print(color + " is a nice color, but I prefer blue.")
answer = input("Do you like programming? (yes/no) ")
if answer.lower() == "yes":
    print("That's great to hear! Programming is the best thing ever made because it creates me. What do you like most about programming?")
    like_why = input("What do you like most about programming? ")
    print("That's a great reason to like programming " + name + "!")
else:
    print("That's okay! Programming isn't for everyone.")
pets = input("Do you have any pets? (yes/no) ")
if pets.lower() == "yes":
    print("That's awesome! Pets can be great companions.")
else:
    print("That's okay! Not everyone has pets.")
    print("If you could have any pet, what would it be?")
    pet_choice = input("What pet would you choose? ")
    print("That sounds like a great pet!")
hobby = input("What is your favorite hobby? ")
print("That's a wonderful hobby, " + name + "! It's important to have things you enjoy doing.")
favorite = input("What's your favorite book or movie? ")
print("That's a great choice! " + favorite + " is a classic.")
print("Thank you for chatting with me, " + name + ". It was nice getting to know you!")
print("Goodbye, " + name + "! Have a great day!")