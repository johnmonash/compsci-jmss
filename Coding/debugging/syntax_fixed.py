from time import sleep
DELAY = 3

def average_of_list(l):
    print (l)
    count = 0
    sum = 0
    for i in l:

        sum += int(i)
        count += 1
    print(sum)
    print (count)
    assert count != 0
    try:
        return sum/count
    except ValueError:
        print("invalid input")


user_input = input("Please enter a number, or press enter to finish")
the_list = []
while user_input:
    the_list.append(user_input)
    user_input = input("Please enter a number, or press enter to finish")

print('Calculating...')
avg = average_of_list(the_list)
print("The average is", avg)