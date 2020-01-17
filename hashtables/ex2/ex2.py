#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# each ticket such that the starting location is the key and the destination is the value.
# i.source = key
# i.destination = value

#  ith location in the route can be found by checking the hash table for the i-1th location.

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    index = 0
    # for every ticket
    for i in tickets:
        # if i.source = "NONE":

        # insert ticket to hashtable
        # hash_table_insert(hashtable, i.source, i.destination)

        if i.source == "NONE":
        #     hash_table_retrieve(hashtable, i.source)
            # print(hash_table_retrieve(hashtable, i.source))
            # route[index] (hash_table_retrieve(hashtable, i.source))
            route[index] = i.destination
            index += 1
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
print(reconstruct_trip(tickets, 3))