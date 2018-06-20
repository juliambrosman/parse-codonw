import io
from os.path import join, dirname
from setuptools import setup


setup(
    name='codonw_parser',
    version=0.0,
    url='https://github.com/jmargbrosman/parse_codonw',
    license='',
    author='Julia Brown',
    author_email='julia@bigelow.org',
    description='parse codonw output',
    long_description=__doc__,
    install_requires=['pandas',
                     'click'],
    py_modules=['codonw_parser'],
    entry_points='''
        [console_scripts]
        codonw-parser=codonw_parser:codonw_to_table
    '''
)
