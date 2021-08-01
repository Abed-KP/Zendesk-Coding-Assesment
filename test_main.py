import io
import unittest
import main
import requests


class TestMain(unittest.TestCase):

    def test_getSingleTicekt(self):
        response = requests.get(main.single_ticket_url + '1' + '.json', auth=(main.username, main.password))
        ticket = response.json()
        ticket_info = " "
        ticket_info += "Ticket ID: " + str(ticket.get('ticket').get('id')) + '\n'
        ticket_info += "Subject: " + str(ticket.get('ticket').get('subject')) + '\n'
        ticket_info += "Description: " + str(ticket.get('ticket').get('description')) + '\n'
        ticket_info += "Status: " + str(ticket.get('ticket').get('status')) + '\n'
        ticket_info += "priority: " + str(ticket.get('ticket').get('priority')) + '\n'
        ticket_info += "Created On: " + str(ticket.get('ticket').get('created_at')) + '\n'
        ticket_info += "Last Updated: " + str(ticket.get('ticket').get('updated_at')) + '\n'
        self.assertEquals(ticket_info,main.getSingleTicket(ticket))

        response = requests.get(main.single_ticket_url + '2' + '.json', auth=(main.username, main.password))
        ticket = response.json()
        ticket_info = " "
        ticket_info += "Ticket ID: " + str(ticket.get('ticket').get('id')) + '\n'
        ticket_info += "Subject: " + str(ticket.get('ticket').get('subject')) + '\n'
        ticket_info += "Description: " + str(ticket.get('ticket').get('description')) + '\n'
        ticket_info += "Status: " + str(ticket.get('ticket').get('status')) + '\n'
        ticket_info += "priority: " + str(ticket.get('ticket').get('priority')) + '\n'
        ticket_info += "Created On: " + str(ticket.get('ticket').get('created_at')) + '\n'
        ticket_info += "Last Updated: " + str(ticket.get('ticket').get('updated_at')) + '\n'
        self.assertEquals(ticket_info, main.getSingleTicket(ticket))

        response = requests.get(main.single_ticket_url + '3' + '.json', auth=(main.username, main.password))
        ticket = response.json()
        ticket_info = " "
        ticket_info += "Ticket ID: " + str(ticket.get('ticket').get('id')) + '\n'
        ticket_info += "Subject: " + str(ticket.get('ticket').get('subject')) + '\n'
        ticket_info += "Description: " + str(ticket.get('ticket').get('description')) + '\n'
        ticket_info += "Status: " + str(ticket.get('ticket').get('status')) + '\n'
        ticket_info += "priority: " + str(ticket.get('ticket').get('priority')) + '\n'
        ticket_info += "Created On: " + str(ticket.get('ticket').get('created_at')) + '\n'
        ticket_info += "Last Updated: " + str(ticket.get('ticket').get('updated_at')) + '\n'
        self.assertEquals(ticket_info, main.getSingleTicket(ticket))


if __name__ == '__main__':
    unittest.main





