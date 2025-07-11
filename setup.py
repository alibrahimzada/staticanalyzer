from setuptools import setup


setup(name='staticfg',
      version='0.9.6',
      url='https://github.com/coetaur0/staticfg',
      license='Apache 2',
      author='Aurelien Coet',
      author_email='aurelien.coet19@gmail.com',
      description='Control flow graph generator for Python3 programs',
      packages=['python', 'java', 'javascript', 'rust', 'go', 'c'],
      test_suite='tests',
      install_requires=[
        'astor',
        'graphviz',
      ])
