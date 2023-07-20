from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.bdist_egg import bdist_egg
from setuptools.command.egg_info import egg_info
from setuptools.command.build_py import build_py

from subprocess import check_call
import sys
import os


setup(name='checklist',
      version='0.0.11',
      description='Beyond Accuracy: Behavioral Testing of NLP Models with CheckList',
      url='http://github.com/marcotcr/checklist',
      author='Marco Tulio Ribeiro',
      author_email='marcotcr@gmail.com',
      license='MIT',
      packages= find_packages(exclude=['js', 'node_modules', 'tests']),
      install_requires=[
        'numpy>=1.18',
        'spacy>=2.2',
        'munch>=2.5',
        'dill>=0.3.1',
        'ipywidgets>=7.5',
        'transformers>=2.8',
        'patternfork-nosql',
        'iso-639'
      ],
      package_data={'viewer':['static/*'], "data": ["*"], 'checklist': ['data/*', 'data/lexicons/*', 'viewer/static/*']},
      #include_package_data=True,
      zip_safe=False
)
