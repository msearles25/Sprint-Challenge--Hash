#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    d = {}
    route = []
    nextLocation = "NONE"
    
    for ticket in tickets:   

        if ticket.source not in d:
            d[ticket.source] = ticket.destination

    while len(route) < length:

        for ticket in d:

            if ticket == nextLocation and d[ticket] not in route:
                route.append(d[ticket])
                nextLocation = d[ticket]

            else:
                continue

    return route

ticket_2 = Ticket("ORD", "LAX")
ticket_1 = Ticket("NONE", "ORD")
ticket_3 = Ticket("LAX", "NONE")

tickets = [ ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)
