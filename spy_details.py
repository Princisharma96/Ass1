#------------------------------------------------------------------------------------
#  The Spy_details.py file is meant for a Default user and shall be imported when the
# user is given the option to continue as a default user or create a new spy user.
#------------------------------------------------------------------------------------

from datetime import datetime
import csv

# creating class
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None

# chats between spies
class ChatMessage:
        def __init__(self, spy_name, friend_name, time, message):
            self.spy_name = spy_name
            self.friend_name = friend_name
            self.time = time
            self.message = message


# define spy_name, age, rating)
spy_1=Spy('Princi Sharma','Ms',20,4.3)

# lists of friends
friends=[]
# list of chats
chats = []