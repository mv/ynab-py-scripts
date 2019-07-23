#!/usr/bin/env python3
#

from ofxparse import OfxParser

DATE_FORMAT='%Y/%m/%d'
with open('nubank-2019-06.ofx') as file:
    ofx = OfxParser.parse(file)

my_data = []
print('Date,Payee,Category,Memo,Outflow,Inflow')
for tr in ofx.account.statement.transactions:

    # putting "quotes" before so I can align with spaces on the outside
    dt = f'"{tr.date:{DATE_FORMAT}}"'
    memo = f'"{tr.memo}"'
    amount = f'"{float(tr.amount):.2f}"'

    # Aligned CSV
    print(f'{dt}, {memo:<40}, "", {memo:<40}, "", {amount:>10}')

