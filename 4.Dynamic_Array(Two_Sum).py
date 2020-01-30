def calculate_the_pair_of_the_target(array_list, T):
    if len(array_list) < 2:
        return print("No way, the array is too short, It even can't be called array!")

    counted = set()
    output_set = set()

    for num in array_list:
        the_num_you_want_to_find = T - num

        if the_num_you_want_to_find not in counted:
            counted.add(num)

        else:
            output_set.add((min(num, the_num_you_want_to_find), max(num, the_num_you_want_to_find)))

    print('\n'.join(map(str, list(output_set))))


calculate_the_pair_of_the_target([2, 7, 3, 6, 11, 15], 9)