# ynab-py-scripts

[![license][license-badge]](https://help.github.com/en/articles/licensing-a-repository)

My custom scripts to import `ofx and csv` files into [Classical YNAB](https://classic.youneedabudget.com/).

## Usage

### OFX files

OFX files are easy:

```sh
    $ bin/ofx  my-file-statement.ofx
```

A new file `my-file-statement.ynab.csv` will be generated locally, ready to be imported into YNAB.

### CSV files

In my experience, some banks will provide specific statement files in CSV format.
Each CSV will have a specific layout. Current layouts I currently use:

- [Brasil] - Banco Inter: credit card invoice.


To generate a valid YNAB file:

```sh
    $ bin/csv --inter my-file-statement.csv
```


## Details

YNAB Classic input CSV file must have the follow layout:

```csv
Date,Payee,Category,Memo,Outflow,Inflow
```


[LICENSE]: ./LICENSE
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg
