# Goal: Find the Elf with the maximum calories: How many calories are they carrying?

"""
BestCase = WorstCase = O(N) where N is the size of the list
"""

with open('input1.txt') as infile:
    lst = infile.read().split('\n')
    cals = 0
    summation = 0
    for number in lst:
        try:
            summation += int(number)
        except ValueError:
            if summation > cals:
                cals = summation
            summation = 0
    print(cals)

# Goal: Find the Calories of the total 3 elves:

with open('input1.txt') as infile:
    lst = infile.read().split('\n')
    cals = [0] * 3
    summation = 0
    for number in lst:
        try:
            summation += int(number)
        except ValueError:
            if summation > min(cals):
                cals.remove(min(cals))
                cals.append(summation)
            summation = 0
    print(sum(cals))

# Implementing as a singular function:


def get_cals(file_name: str, single_max: bool = True):
    """
    This function returns either a single max calories or the sum of the 3 max calories. By default, it's single.
    """
    with open(file_name) as infile:
        lst = infile.read().split('\n')
        if single_max:
            cals = 0
        else:
            cals = [0] * 3
        summation = 0
        for number in lst:
            try:
                summation += int(number)
            except ValueError:
                if single_max and summation > cals:
                    cals = summation
                elif not single_max and summation > min(cals):
                    cals.remove(min(cals))
                    cals.append(summation)
                summation = 0
        if not single_max:
            cals = sum(cals)
        return cals


if __name__ == "__main__":
    print(get_cals('input1.txt'))
