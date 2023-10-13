def print_sorted_dictionary(a_dictionary):
    sorts_keys = sorted(a_dictionary.keys())
    
    for key in sorts_keys:
        print("{}: {}".format(key, a_dictionary[key]))
