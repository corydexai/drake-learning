def recursive_print_dict(dictionary, offset=''):
    for key in dictionary.keys():
        print (offset + key)
        if type(dictionary[key]) == dict:
            recursive_print_dict(dictionary[key], offset+'   ')
