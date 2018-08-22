"""
Chapter 05 - Sandbox file

"""

temp_list = [79, 79, 80, 68, 79, 68, 80]

temp_list.append(85)

temp_list = temp_list + [85]

[78, 79, 80] == [78, 79, 80]

beat_list = ['John', 'Paul', 'George', 'Pete']

beat_list2 = beat_list[:]
beat_list.sort()
beat_list == beat_list2
# op from the above is:
# False

beat_list2 = beat_list[:] # Copy elements.


beat_list2 = beat_list # Make an alias.
beat_list.append('Brian')
beat_list2 == beat_list # Equal?

# op from the above is:
# True

beat_list = ['John', 'Paul', 'George', 'Ringo']
for b_str in beat_list:
    print(b_str)

# op for the above:
# John
# Paul
# Ringo
# George

beat_list = ['John', 'Paul', 'George', 'Ringo']
for b_str in beat_list:
    print(b_str, end=' ')

# op for the above:
# John Paul George Ringo



# def for_loop_list():
#     i = 0
#     beat_list = ['John', 'Paul', 'George', 'Ringo']
#     for b_str in beat_list:
#         i = str(i + 1)
#         print(b_str, sep=i)

# for_loop_list()

