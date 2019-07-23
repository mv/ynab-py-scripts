#!/usr/bin/env python3
#

from ofxparse import OfxParser

from lib.nubank_credit_card import DATE_FORMAT as DATE_FORMAT
import lib.ynab


with open('nubank-2019-06.ofx') as file:
    ofx = OfxParser.parse(file)

my_data = []
for tr in ofx.account.statement.transactions:
    my_data.append({'dt':tr.date, 'memo':tr.memo, 'amount':tr.amount})

lib.ynab.ynab_output( my_data )

