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
        hash_table_insert(hashtable, i.source, i.destination)

        # start at key "NONE"
        if i.source == "NONE":
        #     hash_table_retrieve(hashtable, i.source)
            # print(hash_table_retrieve(hashtable, i.source))
            # route[index] (hash_table_retrieve(hashtable, i.source))

            # destination = value at index
            route[index] = i.destination
            # print(route[index])
            index += 1

    # traverse over the length
    while index < length:
        # print(hash_table_retrieve(hashtable, route[index])) = TypeError: 'NoneType' object is not iterable
        
        # print(route[index-1])
        # retrieve key at i-th location
        route[index] = hash_table_retrieve(hashtable, route[index-1])
        index += 1
    return route
