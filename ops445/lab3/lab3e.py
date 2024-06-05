#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.

my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Does not accept any arguments
    # Returns all of items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Does not accept any arguments
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global object my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global object my_list
    return [my_list[1], my_list[2]]

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())


import lab3e

print(lab3e.give_list())                # Should print [100, 200, 300, 'six hundred']
print(lab3e.give_first_item())          # Should print 100
print(lab3e.give_first_and_last_item()) # Should print [100, 'six hundred']
print(lab3e.give_second_and_third_item()) # Should print [200, 300]

