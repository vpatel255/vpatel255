#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # create_dictionary will return a dictionary with keys and values combined from the provided lists
    result = {}
    i = 0
    while i < len(keys) and i < len(values):
        result[keys[i]] = values[i]
        i += 1
    return result

def shared_values(dict1, dict2):
    # shared_values will return a set containing values found in both dictionaries
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    return set1.intersection(set2)

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)


import lab4c
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

york = lab4c.create_dictionary(list_keys, list_values)
print(york)
# Will print: {'Address': '70 The Pond Rd',
#              'City': 'Toronto',
#              'Country': 'Canada',
#              'Postal Code': 'M3J3M6',
#              'Province': 'ON'}

common = lab4c.shared_values(dict_york, dict_newnham)
print(common)
# Will print: {'Canada', 'ON', 'Toronto'}

