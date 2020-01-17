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
    # for every ticket
    for i in tickets:
        # insert ticket to hashtable
        hash_table_insert(hash_table, i.source, i.destination)

    return route
