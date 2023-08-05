from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.32'
DESCRIPTION = "No more sleepless nights due to a nested dict, json, list or whatsoever"

# Setting up
setup(
    name="flatten_any_dict_iterable_or_whatsoever",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/flatten_any_dict_iterable_or_whatsoever',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=[],
    keywords=['Tagsflatten', 'pandas', 'dict', 'list', 'numpy', 'tuple', 'Tagsiter', 'nested', 'iterable', 'listsoflists', 'flattenjson'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=[],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*