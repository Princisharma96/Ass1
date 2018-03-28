
# -------------------------------------------------------------------------------------------------
# Code Till Module 4
# -------------------------------------------------------------------------------------------------

# import  is used take  details from spy_details file
from spy_details import Spy, friends
from spy_details import spy_1

# list of default status
STATUS_MESSAGES = ['My name is Princi.', 'I love Python', 'Location: New Delhi']


# add_friend() function is use to add frinds
def add_friend():
    # using class user in spy_details
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name
    new_friend.name = input("Please add your friend's name: ")

    # user name validation.
    if len(new_friend.name) > 0:
        if len(new_friend.name) > 20:
            print("Your name length is big.")
    else:
        print("Name should be not empty or length is less then 20 char.")
        return add_friend()

    new_friend.salutation = input("What to call Mr. or Ms.?: ")

    # user salutation validation
    if len(new_friend.salutation) > 0:
        if len(new_friend.salutation) > 5:
            print("Your salutation is too big.")
    else:
        print("Salutation empty or check length")
        return add_friend()

    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of the friend
    new_friend.age = int(input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print("Age should be in between 12 to 50")
        return add_friend()

    #ask for rating of friend, using float
    new_friend.rating = float(input("Spy rating? "))

    if new_friend.rating > 0.0:
        True
    else:
        print("Ratting should be more than 0.0")
        return add_friend()

    # add friend if all conditions check
    friends.append(new_friend)
    print('Friend Added!')
    # check total no of friends in a list.
    return len(friends)


# add_status() function is use to add status like in whatsapp
def add_status(current_status_message):
    if current_status_message !=None:
        print("your current status is:"+current_status_message)
    else:
        print("you don't have any current messeage")
    question=input("do you want to select status from old status? y/n")
    # if user want to add new status
    # then append new_status to STATUS_MESSAGE
    if question.upper()=="N":
        new_status=input("enter your new status ")
        if len(new_status)>0:
            STATUS_MESSAGES.append(new_status)
            return(new_status)
        else:
            print("invalid new status need to be enter ")
    # if user want to select from STATUS_MESSAGE
    elif question.upper()=="Y":
        # showing all old status
        for i in range(len(STATUS_MESSAGES)):
            print(str(i)+"."+STATUS_MESSAGES[i])
        message_selection=int(input("\n choose from above status"))
        # if user enter more than the no of  status in STATUS MESSAGE
        if len(STATUS_MESSAGES)>message_selection:
            update_status_message=STATUS_MESSAGES[message_selection]
        else:
            print("selected message is not in older status ")
        return update_status_message


#start_chat function inorder to show the menu to the user so that the user can select the desired function he wants to perform
def start_chat(spy_name, spy_age, spy_rating):
    current_status_messesge = None
    print("your current status is " + str(current_status_messesge))
    continue_option = "Y"
    while (continue_option == 'Y' or continue_option == 'y'):

        menu_option = int(input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        # displaying menu for user.
        while (menu_option<=6):
            if menu_option == 1:
                print("You choose update the status ")

                current_status_messesge = str(add_status(current_status_messesge))
                # calls the add_status_message from the add_status file
                print("Your selected status is:" +current_status_messesge) #Displays the status chosen or entered by the spy
                break
            elif menu_option == 2:
                print("Adding a friend initiated......")
                # add a new friend
                number_of_friends = add_friend()
                print('You have %d friends' % number_of_friends) #prints the number of friends
                break
            elif menu_option == 3:
                print("Send a secret message initiated......")
                break
            elif menu_option == 4:
                print("Read a secret message initiated......")
                break
            elif menu_option == 5:
                print("Reading chat from user")
                break
            elif menu_option ==6:
                print("Exiting now.....")
                exit()
        continue_option = input("Would you like to perform another operation (Y/N)")
    print("Thank you for your time")


spy_is_online = False  # status of the spy
user_option = input(
    "Would you like to continue as "+spy_1.salutation+" "+spy_1.name +" or create your own(Y/N)")  # type of user
# -------------------------------------------------------------------------------------------------
# for creating new user
# -------------------------------------------------------------------------------------------------
if user_option == 'N' or user_option == 'n' :
    spy_name = input("Welcome to SpyChat, you must tell me your Spyname first:")
    if len(spy_name) > 0: # to calculate the length of the string
        print('Welcome ' + spy_name + ' Glad to have you with us.')
        spy_salutation = input("What should I call you Mr. or Ms. ?")
        print(
            'Alright ' + spy_salutation + '.' + spy_name + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(input('What is your age? '))  # age of the spy
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(input('What is your spy rating? '))
        if spy_rating > 4.5:
            print('Great Ace!')
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
        print('Sorry you are not of the correct age to become a spy.')  # entered age is not between 12 and 50
    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your spy rating is " + str(
            spy_rating))  # float value to string value
    spy_is_online = True
    print('Changing the status of spy from offline to online ' + str(
        spy_is_online))  # bool value to string value for concatenation
    start_chat(spy_name, spy_age, spy_rating)  # calling menu option
# -----------------------------------------------------------------------------------------------------------------------
# for continuing as a default user
# -----------------------------------------------------------------------------------------------------------------------
elif user_option == 'Y' or user_option == 'y':

    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_1.salutation + '.' + spy_1.name + ", Your spy rating is " + str(spy_1.rating))  # float value to string value
    spy_is_online = True

    start_chat(spy_1.name, spy_1.age, spy_1.rating)  # calling menu option
else:
    print("Please select default user or create a new one.")
