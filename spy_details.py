#############INFORMATION OF A DEFAULT USER#####

print("For Default user")
spy_name = input("What's your name?")
# checking length of the name
if len(spy_name) > 0:
    # asking for spy salutation
    spy_salutation = input("What would you like us to call you (Mr., Ms. or Mrs.) ?")
    # welcoming spy
    print("Welcome to the spy chat " + spy_salutation + " " + spy_name)
    print("Alright " + spy_salutation + " " + spy_name + " I'd like to know a little bit more about you...")
    # checking spy age
    spy_age = int(input("What's your age?"))
    if spy_age > 12 and spy_age < 50:
        # checking spy rating
        spy_rating = float(input("What is your spy rating?"))
        if spy_rating > 4.5:
            print("Outstanding!")
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print("Amazing!")
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print("You can surely improve!")
        else:
            print("Don't Worry! We'll help you!")
        # if spy is online
        spy_is_online = True
        # welcome with details
        print("Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
            spy_rating) + " Proud to have you onboard")
    # age is not eligible
    else:
        print("You are not ready to be a spy yet!")
# name not provided
else:
    print("Please provide us with your name first!")
# valid entry