#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # itterate over arr elements
    for i in range(length):
        # key = difference between limit and current weight
        key = limit - weights[i]
        # current weight in storage
        storage = hash_table_retrieve(ht, key)

        # if nothing in storage, insert
        if storage is None:
            hash_table_insert(ht, weights[i], i)
        else:
            return (i, storage)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_2 = [4, 4]