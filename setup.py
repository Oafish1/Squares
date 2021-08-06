from setuptools import find_packages, setup

with open('squares/_version.py') as version_file:
    exec(version_file.read())

setup(
    name='squares-rng',
    version=__version__,
    packages=['squares'],
    description='A simple counter-based pseudo random number generator implementation based on arXiv:2004.06278',
    test_suite='tests',
    install_requires=[]
)
