# -*- coding: utf-8 -*-

import click

import measure.measure


@click.command()
@click.argument('value')
def main(value):
    measure.measure.record(value)


if __name__ == "__main__":
    main()
