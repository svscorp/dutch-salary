#!/usr/bin/python -tt
__author__ = 'Ilia Shakitko'

import argparse

holiday_allowance = 0.08

interval_difference = [19645, 13718, 22628, 0]
interval_taxation = [0.37, 0.42, 0.42, 0.52]

b = [0, 19646, 33364, 55992]

p = argparse.ArgumentParser(description='Salary calculator. Displays monthly salary (gross, net) based on gross input.')
p.add_argument('--salary', '-s', default=None, type=int, help="Your gross yearly salary")
p.add_argument('--rule', '-r', default=False, type=bool, help="Consider 30%% ruling in calculation")

args = p.parse_args()


def main():
    gross = args.salary

    allowance_multiplier = (1 + holiday_allowance)
    gross_storage = gross/allowance_multiplier

    allowance_storage = gross - gross_storage
    net_storage = 0

    for i in range(len(interval_taxation)):
        gross_storage -= interval_difference[i]
        if i == len(interval_taxation)-1:
            net_storage += interval_difference[i]*(1-interval_taxation[i])
            break
        elif gross_storage < 0:
            net_storage += (interval_difference[i] + gross_storage)*(1-interval_taxation[i])
            break
        else:
            net_storage += interval_difference[i]*(1-interval_taxation[i])

    print('Yearly gross salary with holiday allowance: %d' % gross)
    print('Yearly gross salary without holiday allowance: %d\n' % (gross - allowance_storage))
    print('Yearly nett salary: %d\n' % net_storage)
    print('Monthly gross salary: %d' % (gross / 12 / allowance_multiplier))
    print('Monthly nett salary: %d\n' % (net_storage / 12))
    print('Holiday allowance %d %%: %d' % (holiday_allowance * 100, allowance_storage))


if __name__ == '__main__':
    main()
