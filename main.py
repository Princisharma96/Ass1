
# -------------------------------------------------------------------------------------------------
# Code for lecture 1 of Spychat dated 19th March 2018
# -------------------------------------------------------------------------------------------------
# print('Welcome to Spy Chat')
# print('Let\'s get started')
# spy_name = input("What is your spy name?") #to store the name of the spy
# print('Welcome '+spy_name+'. How are you?')
# # to check the datatype of the entered spy name
# type(spy_name)
# spy_salutation = input("What should I call you Mr. or Ms. ?") #salutation for the spyname
# print('Alright '+spy_salutation+'.'+spy_name+' I\'d like to know a little bit more about you...')

# -------------------------------------------------------------------------------------------------
# Code for lecture 2 of Spy Chat dated 21st March 2018
# -------------------------------------------------------------------------------------------------
from spy_details import spy_rating,spy_age,spy_salutation,spy_name


# list of default status
STATUS_MESSAGES = ['My name is Princi.', 'I love Python', 'Location: New Delhi']


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


def start_chat(spy_name, spy_age, spy_rating):  # currently not using the parameters
    current_status_messesge = None
    print("your current status is " + str(current_status_messesge))
    continue_option = "Y"
    while (continue_option == 'Y' or continue_option == 'y'):

        menu_option = int(input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        while (menu_option<=6):
            if menu_option == 1:
                print("You choose update the status ")

                current_status_messesge = str(add_status(current_status_messesge))
                # calls the add_status_message from the add_status file
                print("Your selected status is:" +current_status_messesge) #Displays the status chosen or entered by the spy
                break
            elif menu_option == 2:
                print("Adding a friend initiated......")
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
    "Would you like to continue as "+spy_salutation+" "+spy_name +" or create your own(Y/N)")  # type of user
# -------------------------------------------------------------------------------------------------
# for creating new user
# -------------------------------------------------------------------------------------------------
if user_option == 'N' or user_option == 'n' :
    spy_name = input("Welcome to SpyChat, you must tell me you Spyname first:")
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
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your sp rating is " + str(
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
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name + ", Your sp rating is " + str(spy_rating))  # float value to string value
    spy_is_online = True

    start_chat(spy_name, spy_age, spy_rating)  # calling menu option
else:
    print("Please select default user or create a new one.")
