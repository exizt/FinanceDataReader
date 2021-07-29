from setuptools import setup, find_packages

setup(name='FinanceDataReader-forked',
      version='0.1',
      packages=find_packages(),
      install_requires=[
            'pandas',
            'tqdm',
            'requests-file',
            'lxml',
            'beautifulsoup4'
      ])
