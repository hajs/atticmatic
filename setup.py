from setuptools import setup, find_packages

setup(
    name='atticmatic',
    version='0.0.1',
    description='A wrapper script for Attic backup software',
    author='Dan Helfman',
    author_email='witten@torsion.org',
    packages=find_packages(),
    entry_points={'console_scripts': ['atticmatic = atticmatic.command:main']},
    tests_require=(
        'flexmock',
        'nose',
    )
)
