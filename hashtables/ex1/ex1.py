#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # store weights in hash table
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    
    # find the correct pair
    for i in range(length):
        key = limit - weights[i]
        pair = hash_table_retrieve(ht, key)
        if pair is not None:
            if pair >= i:
                return (pair, i)
            else:
                return (i, pair)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
