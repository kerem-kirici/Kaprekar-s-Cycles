from collections import defaultdict


def cycle(number, number_of_digits):
    difference = None
    array = []
    step = 0

    while difference not in array:
        if difference != None:
            step += 1
            array.append(difference)
            string_number = str(difference)
        else:
            string_number = str(number)

        large_integer = int("".join(sorted(string_number, reverse=True)))

        small_integer = int("".join(sorted(string_number)))

        if len(string_number) != number_of_digits:
            large_integer *= 10

        difference = large_integer-small_integer

    return array[array.index(difference):], step

def check_num_of_digit(number_of_digits):
    array = []
    list_of_sets = []
    max_steps = 0

    for i in range(10**(number_of_digits-1), 10**number_of_digits):
        if i % int("1"*number_of_digits):
            answer, step = cycle(i, number_of_digits)
            max_steps = max(step, max_steps)
            set_answer = set(answer)
            if set_answer not in list_of_sets:
                array.append(str(answer + [answer[0]]).replace(",", "").replace("]", " ...]"))
                list_of_sets.append(set_answer)

    return array, max_steps


def main():
    number = int(input("How many digit numbers you want to look for?\n"))
    answer, max_steps = check_num_of_digit(number)
    print("%d digit kaprekar cycle(s):" % number, *answer, "\nMaximum required number of steps:", max_steps, "\n")

if __name__ == '__main__':
    main()