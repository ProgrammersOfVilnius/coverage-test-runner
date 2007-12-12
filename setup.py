from distutils.core import setup

setup(name='CoverageTestRunner',
      version='1.0',
      description='fail Python program unit tests unless they test everything',
      long_description='''\
CoverageTestRunner runs unit tests implemented using the unittest module
in the Python standard library. It runs them using coverage.py and fails
the test if all statements are not covered.
''',
      author='Lars Wirzenius',
      author_email='liw@iki.fi',
      url='http://braawi.org/coveragetestrunner.html',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
      ],
      license='GNU General Public License, version 2 or later',
      py_modules=['CoverageTestRunner'],
     )
