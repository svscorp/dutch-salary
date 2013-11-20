#!/usr/bin/python -tt
__author__ = 'Ilia Shakitko'

gross = 10000
holiday_allowance = 0.08

salary_ = [19645, 13718, 22628, 0]
aa = [0.37, 0.42, 0.42, 0.52]

b = [0, 19646, 33364, 55992]




def main():
  allowance_multiplier = (1 + holiday_allowance)
  gross_storage = gross/allowance_multiplier

  allowance_storage = gross - gross_storage;
  nettStorage = 0

  for i in range(len(aa)):
    gross_storage -= a[i]
    if i == len(aa)-1:
      nettStorage += a[i]*(1-aa[i])
      break
    elif gross_storage < 0:
      nettStorage += (a[i] + gross_storage)*(1-aa[i])
      break
    else:
      nettStorage += a[i]*(1-aa[i])

  print 'Yearly gross salary with holiday allowance: %d' % gross
  print 'Yearly gross salary without holiday allowance: %d\n' % (gross-allowance_storage)
  print 'Yearly nett salary: %d\n' % nettStorage
  print 'Monthly gross salary: %d' % (gross/12/allowance_multiplier)
  print 'Monthly nett salary: %d\n' % (nettStorage/12)
  print 'Holiday allowance %d %%: %d' % (holiday_allowance*100, allowance_storage)


if __name__ == '__main__':
  main()
