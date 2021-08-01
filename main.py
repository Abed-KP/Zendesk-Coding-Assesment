import requests
import ApiErrors
import json

all_tickets_url = 'https://zccstudents5231.zendesk.com/api/v2/tickets?page[size]=25'
single_ticket_url = 'https://zccstudents5231.zendesk.com/api/v2/tickets/'
username = 'abed98kp@gmail.com'
password = 'codingproject123'
response = requests.get('https://zccstudents5231.zendesk.com/api/v2/tickets', auth=(username, password))
num_of_tickets = response.json().get('count')


def main():
    print('\n' + "Welcome to the Greatest Ticket Viewer on all the Inter-Webs! (Verified by Us)" + '\n')
    start()


def start():
    user_Response = input(
        '\n' "○ Press 1 to Enter the Main Menu" '\n'
        "○ Press 2 or type 'exit' to Exit \n ")

    if user_Response == str(1):
        mainMenu()

    elif user_Response == str(2) or user_Response.lower() == "exit":
        print(
            'Thank you for stopping by today, and Remember' '\n' "We are the Greatest Ticket Viewer on all the Inter-Webs! (Verified by Us ♥☻♥).")
        exit()

    else:
        "Please enter a valid response."
        start()


def mainMenu():
    while True:
        user_Response = input('\n' "◘ Main Menu" '\n'
                              "○ Press 1 to get all Tickets." '\n'
                              "○ Press 2 to get a single ticket." '\n'
                              "○ Press 3 or type 'exit' to Exit." '\n')

        if user_Response == str(1):
            getAllTickets(all_tickets_url, username, password, 1, True)

        elif user_Response == str(2):

            ticket_id = input('\n' "Please Enter the associated ID for the ticket you wish to view - Valid [1-" + str(
                num_of_tickets) + "]." '\n')
            while int(ticket_id) < 1 or int(ticket_id) > num_of_tickets:  # Convert to INT
                print("The ticket ID you entered is not valid" '\n')
                ticket_id = input('\n' "Please enter the id for the ticket you wish to view - Valid [1-" + str(
                    num_of_tickets) + "]." '\n')
            response = requests.get(single_ticket_url + str(ticket_id) + '.json', auth=(username, password))
            if (response.status_code != 200):
                print("OOPS! Looks like you got a " + str(response.status_code) + " error. That usually means")
                print(ApiErrors.errorCodes.get(int(response.status_code)))
                continue
            ticket = response.json()
            print(getSingleTicket(ticket))

        elif user_Response == str(3) or user_Response.lower() == 'exit':
            print(
                'Thank you for stopping by today, and Remember' '\n' "We are the Greatest Ticket Viewer on all the Inter-Webs! (Verified by Us ♥☻♥).")
            exit()

        else:
            print('\n'"Please enter a valid response.")


def getAllTickets(currentURL, user, pwd, page_number, flag_for_parse):
    print('\n')
    response = requests.get(currentURL, auth=(user, pwd))
    if (response.status_code != 200):
        print("OOPS! Looks like you got a " + str(response.status_code) + " error. That usually means:")
        print(ApiErrors.errorCodes.get(int(response.status_code)))
        return
    tickets = response.json()

    if flag_for_parse: parseTicketInfo(tickets.get('tickets'))

    user_Response = input(
        "○ Press n or type 'next' for next page." '\n'
        "○ Press p or type 'prev for previous page." '\n'
        "○ Press 3 to go back to the back Main Menu. '\n' ")

    if (user_Response == 'n' or user_Response.lower() == 'next') and tickets.get('meta').get('has_more') == True:
        getAllTickets(tickets.get('links').get('next'), user, pwd, page_number + 1, True)

    elif (user_Response == 'n' or user_Response == 'next') and tickets.get('meta').get('has_more') == False:
        print("There are no more pages." '\n')
        getAllTickets(currentURL, user, pwd, page_number, False)

    elif (user_Response == 'p' or user_Response.lower() == 'prev') and page_number > 1:
        getAllTickets(tickets.get('links').get('prev'), user, pwd, page_number - 1, True)

    elif (user_Response == 'p' or user_Response.lower() == 'prev') and page_number == 1:
        print("You are currently on the first page")
        getAllTickets(currentURL, user, pwd, page_number, False)

    elif user_Response == str(3):
        mainMenu()

    else:
        print("Please enter a valid response.")
        getAllTickets(currentURL, user, pwd)


def getSingleTicket(ticket):
    ticket_info = " "
    ticket_info += "Ticket ID: " + str(ticket.get('ticket').get('id')) + '\n'
    ticket_info += "Subject: " + str(ticket.get('ticket').get('subject')) + '\n'
    ticket_info += "Description: " + str(ticket.get('ticket').get('description')) + '\n'
    ticket_info += "Status: " + str(ticket.get('ticket').get('status')) + '\n'
    ticket_info += "priority: " + str(ticket.get('ticket').get('priority')) + '\n'
    ticket_info += "Created On: " + str(ticket.get('ticket').get('created_at')) + '\n'
    ticket_info += "Last Updated: " + str(ticket.get('ticket').get('updated_at')) + '\n'
    return ticket_info


def parseTicketInfo(tickets_list):
    for ticket in tickets_list:
        print("Ticket ID: " + str(ticket.get('id')))
        print("Subject: " + str(ticket.get('subject')))
        print("Description: " + str(ticket.get('description')))
        print("Status: " + str(ticket.get('status')))
        print("priority: " + str(ticket.get('priority')))
        print("Created On: " + str(ticket.get('created_at')))
        print("Last Updated: " + str(ticket.get('updated_at')))
        print('\n')


if __name__ == "__main__":
    main()
