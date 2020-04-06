"""Config for PyPI."""

from setuptools import find_packages
from setuptools import setup

import eddas

setup(
    author='Clément Besnier',
    author_email='clemsciences@aol.com',
    description='Old Norse Eddas',
    include_package_data=True,
    keywords=['nlp', 'old norse', "philology"],
    license='MIT',
    long_description='',
    name='eddas',
    packages=find_packages(),
    url='https://github.com/clemsciences/old_norse_texts_heimskringla',
    version='1.3.3',
    zip_safe=True, install_requires=['bs4', 'cltk', 'nltk']
    # test_suite='cltk.tests.test_cltk',
)
