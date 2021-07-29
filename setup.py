from setuptools import setup, find_packages

setup(name='FinanceDataReader-forked',
      version='0.9.30',
      packages=find_packages(),
      install_requires=[
            'pandas',
            'requests',
            'requests-file',
            'lxml',
            'tqdm'
      ])
