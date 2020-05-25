#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import logging
import shutil

from PDFknife import __version__, find_available_engine
from PDFknife import reverse

def main():
    # TODO add option for engine
    parser = argparse.ArgumentParser(description='Reverse pdf',
                                     epilog='')
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-d', '--debug', action='store_true',
                        default=False, help='Run in debug mode')
    parser.add_argument('pdf', metavar='PDF', help='Filename')
    parser.add_argument('-o', help='output', required=False, default=None)
    args = parser.parse_args()

    # Logger level
    if args.debug:
        llevel = logging.DEBUG
    else:
        llevel = logging.INFO
    logger = logging.getLogger()
    logger.setLevel(llevel)


    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(llevel)
    logger.addHandler(steam_handler)

    logger.debug(f'Script arguments: {args}')

    available_engines = find_available_engine(engines=('pdftk', 'pdfjam'))
    logger.debug(f'Available engine: {available_engines}')

    reverse(args.pdf, output=args.o, engine=available_engines[0])


if __name__ == '__main__':
    main()
