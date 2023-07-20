from setuptools import setup

setup(
    name='currency_rates',
    version='0.1.0',
    py_modules=['main'],
    install_requires=['click'],
    entry_points="""
        [console_scripts]
        currency_rates=main:currency_rates
    """
)
