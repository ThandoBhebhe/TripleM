import math
# TODO: create method called median that takes a list and returns the median a a number DONE
# TODO: create method called mode that takes a list and returns the mode a a number DONE
# TODO: create method called mean that takes a list and returns the mean a a number DONE

# read from file
with open('data.txt', 'r') as dataFile:
    listOfNumbers = [int(number) for number in dataFile.readline().split(' ')]
    listOfNumbers.sort()
    # print(listOfNumbers)


# compute the mode
def mode(list_of_numbers):
    number_dictionary = {}
    initial_value = 1
    max_value = 0
    for number in list_of_numbers:

        if number not in number_dictionary:
            number_dictionary[number] = initial_value
        else:
            number_dictionary.update({number: initial_value+1})
            values = number_dictionary.values()
            max_value = max(values)

    key_list = list(number_dictionary.keys())
    value_list = list(number_dictionary.values())
    max_value_index = value_list.index(max_value)

    return key_list[max_value_index]


# compute the mean
def median(list_of_numbers):
    the_median = len(list_of_numbers) / 2
    actual_median = math.floor(the_median)

    if actual_median % 2 == 0:

        num1 = list_of_numbers[int(len(list_of_numbers) / 2 - 1)]
        num2 = list_of_numbers[int(len(list_of_numbers) / 2)]
        the_sum = num1 + num2

        return the_sum / 2
    else:
        return list_of_numbers[actual_median]


# compute the median
def mean(list_of_numbers):
    the_sum = 0;
    for number in list_of_numbers:
        the_sum += number

    the_mean = the_sum / len(list_of_numbers)
    return the_mean


def main():
    print(' ')
    print('Median: ' + str(median(listOfNumbers)))
    print('Mode: ' + str(mode(listOfNumbers)))
    print('Mean: ' + str(mean(listOfNumbers)))


if __name__ == '__main__':
    main()
