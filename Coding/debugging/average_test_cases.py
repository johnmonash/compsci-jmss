def average(the_list):
    the_sum = 0
    for i in the_list:
        the_sum += i
    return the_sum/len(the_list)


print(average([3,4,5]))