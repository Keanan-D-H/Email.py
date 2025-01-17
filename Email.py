#******* Email.py *************
# Keanan Hinchliffe 
"""


"""



class Email():
    """
    A class to represent an Email

Attributes
__________
has_been_read : bool
    a default of False to show the email is unread
address : str
    the email address of the incoming email
subject : str
    the subject_line of the email
content : str
    the content of the email
inbox : list
    holds multiple emails

Methods
_______
add_email (email)
    adds emails to the inbox list
get_email 
    makes the information of the email available
mark_as_read
    changes has_been_read to True

    """
    has_been_read = False

    def __init__(self, address, subject, content):

        self.address = address
        self.subject = subject
        self.content = content
        self.inbox = []


    def add_email(self,email):
        self.inbox.append(email)


    def get_email(self):
        return self.inbox
    

    def mark_as_read(self):
        self.has_been_read = True


def populate_inbox(): 
    """
    populate_inbox creates 3 Email objects and adds them to a list
    returns list of emails
    
    """
    email1 = Email("examp1@email.com","First", "Here we go!")
    email2 = Email ("2examp@2furious.com", "Middle", "Mia Familia")
    email3 = Email("exampMike@XXL.com", "Last", "Ride it, My Pony")

    email1.add_email(email1)
    email1.add_email(email2)
    email1.add_email(email3)
    
    return email1.get_email()


def read_email(i,inbox):
    """
    read_emails prints out the information of a chosen email.
    Parameters: i : int (decides which email from the inbox), 
                inbox : list (the list of emails)  
    """
    print("\n\n_________________________________________________________\n")
    print("From :\t\t" + inbox[i].address)
    print("Subject :\t" + inbox[i].subject)
    print("Email:\n\n" + inbox[i].content)
    print("\n_________________________________________________________")
    print("\n\tThis email has now been marked as read!")
    print("_________________________________________________________\n\n")

    inbox[i].mark_as_read()


def list_emails(inbox):
    """
    list_emails prints the subject lines of all the emails in an inbox
    Parameters: inbox : list (A list of emails)
    """

    print("\nYour Emails:")

    for i, inner_list in enumerate(inbox):
        print(f"{i+1} : \'{inbox[i].subject}\' from {inbox[i].address}")


def check_integer(item): 
    """
    check_integer tries to change an input to an int, if it can't it will
    ask for input until it can
    Parameters: item : str
    Returns the item as an int   
    """
    while type(item) != int:
        try:
            item = int(item)
        except:  
            item = input("That is not an integer , please input again.\n")
    return item


def check_in_range(item, upper_value, lower_value):
    """
    check_in_range checks if an int is within a given range and will ask
    for a new input until it falls within the range.
    Parameters: item : int , upper_value : int/float (the highest item can be)
                lower_value : int/float (the smallest item can be)
    returns item as an int 
    """
    while (check_integer(item) > upper_value or check_integer(item) < 
           lower_value):
        
        item = input(f"Please input an integer between {upper_value} and "
                     + f"{lower_value}.\n")
        
    return int(item)


inbox = populate_inbox()

while True:

    menu = input("""\n\nPlease choose an action from the following.
1. Read an email
2. View unread emails
3. Quit application: \n""")
    

    if menu == "1":
        """
        If the user wishes to read an email, they will be presented with the 
        subject lines and asked which email they wish to read. Then, the 
        chosen email will be shown to them and marked as read
        """
        list_emails(inbox)
        choice = input("Please input which email you wish to read:\n")
        choice = check_in_range(choice, len(inbox), 1)
        index = choice - 1
        read_email(index, inbox)


    elif menu == "2":
        """
        The user wishes to view the unread emails. If there are none they
        will be notified of this. If there are unread emails they will be 
        shown the subject lines the unread emails by looping through the
        emails in inbox and printing out those with has_been_read == False
        """
        print("\n\n_____________________________________________________\n")

        unread_emails = []

        for i, inner_list in enumerate(inbox):

            if inbox[i].has_been_read == False:
                    unread_emails.append(inbox[i])


        if len(unread_emails) == 0: 
            print("There are no unread emails!")

        else: 
            print("Unread Emails:")

            list_emails(unread_emails)

        
        print("_____________________________________________________\n\n")
        
    elif menu == "3":
        print ("Goodbye!")
        exit()

    elif menu == '4':

        while menu == '4': 
            address = input("\nRecipient email address:\n")
            subject_line = input("\nSubject line:\n")
            content = input("\nEmail content:\n")
        
        send_email = Email(address, subject_line, content)

    else: 
        print("This is not a valid input, please input '1', '2' or '3'")






