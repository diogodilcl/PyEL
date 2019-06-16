import io

import setuptools

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

setuptools.setup(
    name='PyEL',
    version='0.0.1',
    author='Diogo Dil',
    author_email='diogodicl@gmail.com',
    license='Apache License 2.0',
    description='This project aims to facilitate the execution of codes before and after a method using decorator',
    long_description=readme,
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.1.*,!=3.2.*,!=3.3.*',
    url='https://github.com/diogodilcl/PyEL',
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
