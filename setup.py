#!/usr/bin/env python

import pkg_resources
import setuptools
import pathlib
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name         = 'PDFknife',
    version      = '0.2.5',
    url          = "https://github.com/sciunto-org/PDFknife",
    author       = "Francois Boulogne",
    license      = "BSD",
    author_email = "devel@sciunto.org",
    description  = "Command line tools to manipulate PDF files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages     = setuptools.find_packages(exclude=['doc', 'benchmarks']),
    scripts      = ['bin/pdfknife-A5.py',
                    'bin/pdfknife-cut.py',
                    'bin/pdfknife-even.py',
                    'bin/pdfknife-extract.py',
                    'bin/pdfknife-merge.py',
                    'bin/pdfknife-recto.py',
                    'bin/pdfknife-reverse.py',
                    'bin/pdfknife-split.py',
                    'bin/pdfknife-shrink.py',
                    'bin/pdfknife-tearpages.py',
                    'bin/pdfknife-trim.py',
                    ],
    install_requires=install_requires,
)
