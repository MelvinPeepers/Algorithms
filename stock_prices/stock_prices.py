#!/usr/bin/python

import argparse


def find_max_profit(prices):  # first pass
    length = len(prices)
    prices.sort()
    print(prices)
    profit = prices[length-1] - prices[1]
    return profit


# prices = [1050, 270, 1540, 3800, 2]
prices = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
print(find_max_profit(prices))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
