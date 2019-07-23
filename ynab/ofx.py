#

from ofxparse import OfxParser

import os
import ynab


def ofx(list_of_files):
    '''
    ofx:
       parse the list of ofx files
    '''

    for f in list_of_files:
        print('ofx: processing [{}]'.format(f))
        ofx_parse(f)


def ofx_parse(file):
    '''
    ofx_parse:
       parse one single ofx file
    '''

    with open(file) as f:
        ofx = OfxParser.parse(f)

    # Filter out my transaction data
    my_ynab_data = []
    for tr in ofx.account.statement.transactions:
        my_ynab_data.append({'dt':tr.date, 'memo':tr.memo, 'amount':tr.amount})

    # my data in YNAB format
    csv = ynab.ynab_output( my_ynab_data )

    filename, ext = os.path.splitext(file)
    with open(filename + '.ynab.csv', 'w') as f:
        f.write(csv)


print('Imported: ', __file__)
