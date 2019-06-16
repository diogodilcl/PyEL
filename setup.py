import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='PyEL',
    version='0.0.1',
    author='Diogo Dil',
    author_email='diogodicl@gmail.com',
    license='Apache License 2.0',
    description='This project aims to facilitate the use of decorators',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/diogodilcl/PyEL',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
    ],
)