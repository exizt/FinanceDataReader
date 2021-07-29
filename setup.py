from setuptools import setup, find_packages

setup(name='FinanceDataReader-forked',
      version='0.9.30',
      packages=find_packages(),
      install_requires=[
            'pandas>=0.19.2',
            'requests>=2.3.0',
            'requests-file',
            'lxml',
            'tqdm',
            'beautifulsoup4'
      ])
