from setuptools import setup


setup(name='pyguana',
      version='0.1',
      description='The pyguana provides a python wrapper to the Iguana API.',
      long_description=open('README.rst').read(),
      url='http://github.com/nmecsys/pyguana',
      author='Fernando Teixeira',
      author_email='fernando.teixeira@fgv.br',
      license='BSD',
      packages=['pyguana'],
	  install_requires=['requests', 'pandas'],
      zip_safe=False)
