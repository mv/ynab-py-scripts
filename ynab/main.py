#!/usr/bin/env python3
""" YNAB: creting CSV files to be imported into YNAB 4 Classic

Usage:
  ynab <filename> [options]
  ynab <filename> [<filename>...] [-o | -i | -s | -b ] [-v | --verbose]
  ynab --version
  ynab -h | --help

Options:
  -o --ofx                     Type: ofx file (default).
  -i --inter-credit-card-csv   Type: Banco Inter - Credit Card CSV
  -s --santander               Type: Santander
  -b --banco-do-brasil         Type: BB
  -v --verbose                 Verbose
  --version                    Show version.

"""

from docopt import docopt
import sys

import util
import ynab

print('=' * 60)
print('argv: ', sys.argv)
print('=' * 60)

if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    print(args)
    print('=' * 60)
