# 1. Real-World Python Dictionary Applications
# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
 }
# restaurant_menu.append({"Beverages": "Margarita": 9.99, "Fountain drink": 3:99})
# print(restaurant_menu)
restaurant_menu["Starters"]["Beverages"]= {"Margarita: 9.99, Fountain drink: 3:99"}
print(restaurant_menu)

# Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)


# Remove "Bruschetta" from "Starters".
item =restaurant_menu["Starters"].pop("Bruschetta")
print(item)
print(restaurant_menu)

# 2. Python Programming Challenges for Customer Service Data Handling
# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
 }



def open_ticket(service_tickets):
    ticket_id = input("Enter the service ticket you would like to add:?")
    if not ticket_id in service_tickets:
      service_tickets[ticket_id]= {}
    customer_name = input("What is the customer name?:")
    if not customer_name in service_tickets [ticket_id]:
        service_tickets[ticket_id][customer_name]=[]
    issue = input("What is the issue?:")
    service_tickets[ticket_id][customer_name].append(issue)


def view_ticket(service_tickets):
    response = input("Would you like to view all tickets in que or status? Enter que or status.").lower()
    if response == "view":
        print("Tickets display here:")
        for ticket_id in customer_name in service_tickets:
            print(ticket_id)
    elif response == "status":
        print("Here is your ticket status:")
        for customer_name, issue in customer_name.keys():
            print(f"- {customer_name} status: "+",".join(issue))
        else:
            print("please enter valid response")

def update_ticket(service_tickets):
    print("Would you like to update ticket status?")
    status= input("Please enter ticket id: ")
    if status in service_tickets:
       if service_tickets[status] == "Open":
         service_tickets[status] == "Closed"
         print("Ticket status has now been changed." )
    elif service_tickets[status] == "Closed":
         service_tickets[status] == "Open"
         print ("Ticket status has now been changes." )
    else:
        print("Please enter a valid ticket number")


while True:
  response = input("Would you like to open/update/vew/quit ticket?").lower()
  if response == "open":
    open_ticket(service_tickets)
    print(f"service_tickets")
  elif response == "view":
    view_ticket(service_tickets )
  elif response == "update":
    update_ticket(service_tickets)
    print("Here is your updated ticket:")
    for ticket in open_ticket :
     print(ticket)
  elif response == "quit":
    for ticket in service_tickets:
     print(ticket)
    for open_ticket in service_tickets:
     print(open_ticket)
    break
  else:
    print("Please enter a valid response")  





