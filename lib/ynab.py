#!/usr/bin/env python3
#
import re

# replacements
repl = [
    { 'pattern': r'"'                  , 'replace': r''   },
    { 'pattern': r'IOF de[ ]?(.*)'     , 'replace': r'\1' },
    { 'pattern': r'(.*)\d+\/\d+(.*)'   , 'replace': r'\1 \2' },
    { 'pattern': r'(Maria Zamlutti).*' , 'replace': r'Mercado' },
    { 'pattern': r'.*(Perola).*'       , 'replace': r'Mercado' },
    { 'pattern': r'.*(Padaria).*'      , 'replace': r'Mercado' },
    { 'pattern': r'.*(Supermercado).*' , 'replace': r'Mercado' },
    { 'pattern': r'.*(Carrefour).*'    , 'replace': r'Mercado' },
    { 'pattern': r'.*(P.o de A.ucar).*', 'replace': r'Mercado' },
    { 'pattern': r'.*(Hirota).*'       , 'replace': r'Mercado' },
    { 'pattern': r'.*(Mambo).*'        , 'replace': r'Mercado' },
    { 'pattern': r'.*(Restaurante).*'  , 'replace': r'Restaurante'},
    { 'pattern': r'.*(Taxi).*'         , 'replace': r'Taxi'   },
    { 'pattern': r'(99[*]?[ ]?Taxi).*' , 'replace': r'99Taxi' },
    { 'pattern': r'(Uber).*'           , 'replace': r'Uber'   },
    { 'pattern': r'(Cobasi).*'         , 'replace': r'Cobasi'  },
    { 'pattern': r'(Kalunga).*'        , 'replace': r'Kalunga' },
    { 'pattern': r'(Renner).*'         , 'replace': r'Renner'  },
    { 'pattern': r'.*(Droga).*'        , 'replace': r'Farmacia' },
    { 'pattern': r'.*(Farma).*'        , 'replace': r'Farmacia' },
    { 'pattern': r'(P Estation).*'     , 'replace': r'AutoPosto' },
]

def payee_replace( payee ):
    new_payee = payee
    for i,regex in enumerate(repl):
        new_payee = re.sub(regex['pattern'], regex['replace'], new_payee, flags=re.I )
        # print(f'regex: {i} - {payee} | {new_payee}')

    return(new_payee)


def ynab_output( tr_data, dt_format='%Y/%m/%d', layout=None ):

    print('Date,Payee,Category,Memo,Outflow,Inflow')

    for tr in tr_data:
        payee = payee_replace(tr['memo'])

        # putting "quotes" before so I can align with spaces on the outside
        dt = f'"{tr["dt"]:{dt_format}}"'
        memo = f'"{tr["memo"].title()}"'
        payee = f'"{payee}"'
        amount = f'"{float(tr["amount"]):.2f}"'

        # Aligned CSV
        print(f'{dt}, {payee:<30}, "", {memo:<40}, "", {amount:>10}')
