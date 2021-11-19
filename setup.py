from setuptools import find_packages, setup
setup(
    name='decypher',
    packages=find_packages(include=['decypher']),
    version='0.1.0',
    description='A library with useful decyphering functions',
    # long_description=README,
    author='Arthur Allilaire',
    license='MIT',
    install_requires=['matplotlib', 'pyenchant'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
# python setup.py pytest --> runs all tests in the tests folder