from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'prettyplot', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='prettyplot',
    version=version['__version__'],
    description=('Framework for quick and pretty plotting.'),
    long_description=long_description,
    author='Mariia Redchuk',
    author_email='mariia.redchuk@gmail.com',
    url='https://github.com/sagitta42/prettyplot',
    license='MPL-2.0',
    packages=['prettyplot'],
#   yes dependencies in this example
   install_requires=[
       'matplotlib'#==3.3.2',
   ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
