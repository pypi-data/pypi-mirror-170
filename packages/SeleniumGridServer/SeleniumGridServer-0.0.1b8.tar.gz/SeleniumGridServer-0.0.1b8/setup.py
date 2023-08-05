from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='SeleniumGridServer',
    version='0.0.1b8',
    description='ChokChaisak',
    long_description=readme(),
    url='https://test.pypi.org/user/ChokChaisak/',
    author='ChokChaisak',
    author_email='ChokChaisak@gmail.com',
    license='ChokChaisak',
    install_requires=[
        'matplotlib',
        'numpy',
        'webdrivermanager>=0.10.0',
        'install-jdk>=0.3.0',
    ],
    keywords='SeleniumGridServer',
    packages=['SeleniumGridServer'],
    package_dir={
    'SeleniumGridServer': 'src/SeleniumGridServer',
    },
    package_data={
    'SeleniumGridServer': ['*'],
    },
)