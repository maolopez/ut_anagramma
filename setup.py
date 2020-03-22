from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='ut_anagramma',
    version='0.2.0',
    description='an internet-facing web service accepting a single word and deriving all possible anagrams.',
    long_description=readme,
    author='Maurizio Lopez',
    author_email='maurizio.school@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['flask', 'more_itertools', 'numpy' ],
    entry_points={'console_scripts': ['ut_anagramma=ut_anagramma.main:adder_page',]}
)
