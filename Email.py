#******** Email.py **************************
# Keanan Hinchliffe 
"""
A program which creates the class Email and uses it to allow users to read, 
delete and write emails. 

"""

#******** Class Definitions *****************
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


#******** Function Definitions **************
def check_yes_no(answer):
    """
    check_yes_no(answer)

    Checks if the inputted string is either a yes or a no and asks for an
    input until it is then returns the result.

    Parameters:     answer : str
                        A string which should be yes or no.

    Returns:        answer : str
                        Either 'yes' or 'no'.       
    """
    while answer.lower() !='yes' and answer.lower() != 'no':
        answer = input('\nPlease only put in \'yes\' or \'no\':\n')

    answer = answer.lower()
    return answer


def populate_inbox(): 
    """
    populate_inbox creates 3 Email objects and adds them to a list
    returns list of emails.

    Parameters :

    Returns :      inbox : list
                        A list of Email objects. 
    
    """
    email1 = Email("examp1@email.com","First", "Here we go!")
    email2 = Email ("2examp@2furious.com", "Middle", "Mia Familia")
    email3 = Email("exampMike@XXL.com", "Last", "Ride it, My Pony")

    email1.add_email(email1)
    email1.add_email(email2)
    email1.add_email(email3)

    inbox = email1.get_email()
    
    return inbox


def delete_email(folder_index, folder):
    """
    delete_email asks the user if they wish to delete the email they just
    read. If the user does wish to delete the email, then the email will be 
    removed from the folder. 

    Parameters:     folder_index : int
                        The index of the email inside the folder list.

                    folder : list
                        The list of which emails will be deleted from. 
    
    Returns :
    """

    print(dashes + "\n")

    delete_choice = input("Would you like to delete this Email now that" + 
    " it has been read?\n")

    if check_yes_no(delete_choice) == "yes":

        del folder[folder_index]

        print("\n\nThe email has been deleted from your inbox!")

    print(dashes)


    


def read_email(folder_index, folder, in_or_out):
    """
    read_emails prints out the information of a chosen email. If the email 
    is from an incoming folder then it will get marked as read, and show the 
    sender's email address.

    Parameters:     folder_index : int 
                        The index of the email inside the folder list.
    
                    folder : list 
                        A list of emails.
                    
                    in_or_out : str
                        Either 'in' or 'out' depending on whether the email 
                        comes from the inbox or outbox. 
             
    Returns:        
    """
    print("\n\n" + dashes + "\n")
    if in_or_out == "in":
        print("From :\t\t" + folder[folder_index].address)
    else:
        print("To :\t\t" + folder[folder_index].address)
    print("Subject :\t" + folder[folder_index].subject)
    print("Email:\n\n" + folder[folder_index].content)
    print("\n" + dashes)
    
    if in_or_out == "in":
        folder[folder_index].mark_as_read()

        print("\n\tThis email has now been marked as read!")
        print(dashes + "\n\n")

        
def list_emails(folder):
    """
    list_emails prints the subjects and senders of all the emails in an inbox.

    Parameters:     folder : list 
                        A list of emails.
    
    Returns:
    """

    for i, inner_list in enumerate(folder):
        print(f"{i+1} : \'{folder[i].subject}\' from {folder[i].address}")


def check_integer(item): 
    """
    check_integer tries to change an input to an int, if it can't it will
    ask for input until it can.
    Parameters:     item : str
                        A string which may be a number.
    Returns:         item : int
                        A user chosen integer.
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

    Parameters:     item : str
                        A string which should be a number. 
                    upper_value : int/float 
                        The highest value which item can be. 
                    lower_value : int/float 
                        The lowest value which item can be. 

    Returns:        item : int
                        A user chosen int between upper_value and lower_value.
    """
    while (check_integer(item) > upper_value or check_integer(item) < 
           lower_value):
        
        item = input(f"Please input an integer between {upper_value} and "
                     + f"{lower_value}.\n")
        
    return int(item)


def choose_email(folder):
    """
    choose_email will present all the emails from a folder of emails using 
    the list_emails function. Then it will ask the user which email they wish
    to read and then return the index of the chosen email inside the folder. 

    Parameters:     folder : list
                        A list of emails.
    
    Returns:        folder_index : int
                        The index of the chosen email inside folder.  
    """
    list_emails(folder)
    print(dashes)
    choice = input("\nPlease input which email you wish to read:\n")
    choice = check_in_range(choice, len(folder), 1)
    print(dashes)
    folder_index = choice - 1
    
    return folder_index





#********* Main Code *************************

inbox = populate_inbox()
outbox = []

# dashes will be used to make the output more readable.
dashes = "_" * 63

while True:

    print("\n\n" + dashes + "\n")

    menu = input("""Please choose an action from the following:
1. Read an email from your inbox
2. View unread emails 
3. Send an email
4. Read an email from your outbox
5. Quit application\n""" + dashes + "\n\n")

    print(dashes)
    

    if menu == "1":
        """
        If the user wishes to read an email, they will be presented with the 
        subject lines and asked which email they wish to read. Then, the 
        chosen email will be shown to them and marked as read
        """
        print("\n\n" + dashes)

        if len(inbox) != 0: 

            print("\nInbox:\n")
            inbox_index  = choose_email(inbox)
            read_email(inbox_index, inbox, "in")

            delete_email(inbox_index, inbox)

        else:
            print("\nYou have no emails in your inbox!")
            print(dashes)

        

    elif menu == "2":
        """
        The user wishes to view the unread emails. If there are none they
        will be notified of this. If there are unread emails they will be 
        shown the subject lines the unread emails by looping through the
        emails in inbox and printing out those with has_been_read == False
        """

        unread_emails = []

        for i, inner_list in enumerate(inbox):

            if inbox[i].has_been_read == False:
                    unread_emails.append(inbox[i])
        
        print("\n\n" + dashes +"\n")

        if len(unread_emails) == 0: 
            print("There are no unread emails!")
            print(dashes)

        else: 
            print("Unread Emails:")

            unread_index = choose_email(unread_emails)
            read_email(unread_index, unread_emails, "in")

            # In order to delete from the inbox we must first find their 
            # chosen email in the inbox. 
            inbox_index = inbox.index(unread_emails[unread_index])
            delete_email(inbox_index, inbox)


    elif menu == "3":
        """
        The user wishes to send an email. The recipient email address, subject
        line and the contents of the email which is then checked with the user, 
        if the information is correct the email is added to the outbox, if not
        the information is asked for again."""

        while True: 

            print("\n" + dashes)
            address = input("\nRecipient email address:\n")
            subject_line = input("\nSubject line:\n")
            content = input("\nEmail content:\n")
            print(dashes)

            send_email = Email(address, subject_line, content)
            
            print("\n\n" + dashes + "\n")
            print("To :\t\t" + send_email.address)
            print("Subject :\t" + send_email.subject)
            print("Email:\n\n" + send_email.content)
            print(dashes)
            
            print(dashes)
            is_correct = input("\nIs the above information correct?\n")

            if check_yes_no(is_correct) == "yes":
                outbox.append(send_email)
                print("\nYour email has now been added to your Outbox!")
                print(dashes)
                break
            
            else:
                print("\nWe will now ask you to put in the correct "+ 
                      "information.")
                print(dashes)
                continue


    elif menu == "4":
        
        if len(outbox) != 0 : 
            
            print("\n\n" + dashes)
            print("\nOutbox:\n")
            outbox_index = choose_email(outbox)
            read_email(outbox_index, outbox, "out")
        
        else: 
            print("\n" + dashes + "\n\nYou have no outgoing emails yet!")
            print(dashes)


    elif menu == "5":
        print ("Goodbye!")
        exit()


    else: 
        print("This is not a valid input, please only input a valid option.")


