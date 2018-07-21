from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='restdbserver',
    version='0.1.0',  # Required
    description='A REST Server DB Thin Wrapper',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',
    url='https://github.com/bitwyre/database-server',
    author='Bitwyre Technologies LLC',
    author_email='dendi@bitwyre.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Financial Services :: Payment Systems',
        'License :: OSI Approved :: BSD-3 License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='thin wrapper to Stripe, BitGO API',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['pymongo', 'stripe'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'clearing=clearing:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/bitwyre/clearing/issues',
        'Funding': 'https://icls.cc',
        'Say Thanks!': 'http://bitwyre.com',
        'Source': 'https://github.com/bitwyre/clearing/',
    },
)
