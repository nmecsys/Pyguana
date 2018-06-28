from setuptools import setup


setup(name='pyguana',
      version='0.1.5',
      description='The pyguana provides a python wrapper to the Iguana API.',
      long_description=open('README.rst').read(),
      url='http://github.com/nmecsys/pyguana',
      author='Jonatha Costa','Fernando Teixeira',
      author_email='jonatha.costa@fgv.br','fernandoteixeira@bancobbm.com.br',
      license='BSD',
      packages=['pyguana'],
	  install_requires=['requests', 'pandas','json'],
      zip_safe=False)
