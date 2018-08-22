def for_loop_list():
    i = 0
    beat_list = ['John', 'Paul', 'George', 'Ringo']
    for b_str in beat_list:
        i = str(i + 1)
        print(b_str, sep=i)

for_loop_list()