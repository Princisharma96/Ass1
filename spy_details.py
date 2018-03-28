#------------------------------------------------------------------------------------
#  The Spy_details.py file is meant for a Default user and shall be imported when the
# user is given the option to continue as a default user or create a new spy user.
#------------------------------------------------------------------------------------


class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None

spy_1=Spy('Princi Sharma','Ms',20,4.3)

friend_one=Spy('Princi','Ms',20,4.1)
friend_two=Spy('Ujjwal','Mr',22,4.0)
friend_three=Spy('Vivek','Mr',21,4.5)

friends=[friend_one,friend_two,friend_three]