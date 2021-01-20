# You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.


def possibleSums(coins, quantity):
    possible_sums = {0}
    for c, q in zip(coins, quantity):
        possible_sums = {x + c * i for x in possible_sums for i in range(q + 1)}
        print(possible_sums)

    return len(possible_sums) - 1


coins = [10, 50, 100]
quantity = [1, 2, 1]
possibleSums(coins, quantity)
