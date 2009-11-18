from distutils.core import setup

setup(name='CoverageTestRunner',
      version='1.2',
      description='fail Python program unit tests unless they test everything',
      long_description='''\
CoverageTestRunner runs unit tests implemented using the unittest module
in the Python standard library. It runs them using coverage.py and fails
the test if all statements are not covered.
''',
      author='Lars Wirzenius',
      author_email='liw@liw.fi',
      url='http://braawi.org/coveragetestrunner.html',
      license='GNU General Public License, version 2 or later',
      py_modules=['CoverageTestRunner'],
     )
