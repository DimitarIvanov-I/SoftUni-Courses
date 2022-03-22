import sys


def equal_distribution(data):

    minimum_wealth = int(input())

    for part in range(len(data)):
        maximum_wealth = max(population)
        index = data.index(maximum_wealth)

        if minimum_wealth > data[part]:
            diff = minimum_wealth - data[part]
            data[index] -= diff
            data[part] += diff
        if data[index] < minimum_wealth:
            print("No equal distribution possible")
            sys.exit()

    print(data)


population = list(map(int, input().split(', ')))
equal_distribution(population)